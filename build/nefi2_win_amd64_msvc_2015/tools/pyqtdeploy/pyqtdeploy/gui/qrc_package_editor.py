# Copyright (c) 2015, Riverbank Computing Limited
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


import fnmatch

from PyQt5.QtCore import pyqtSignal, QDir, Qt
from PyQt5.QtWidgets import (QGridLayout, QMessageBox, QPushButton,
        QTreeWidget, QTreeWidgetItem, QTreeWidgetItemIterator)

from ..project import QrcDirectory, QrcFile


class QrcPackageEditor(QGridLayout):
    """ A resource file system package editor.  Note that this is a QLayout and
    not a QWidget.
    """

    # Emitted when the package has changed.
    package_changed = pyqtSignal()

    def __init__(self, show_root=False, scan="Scan", scan_whats_this='', whats_this=''):
        """ Initialise the editor. """

        super().__init__()

        self.package = None
        self.project = None

        self._show_root = show_root

        self._package_edit = QTreeWidget(whatsThis=whats_this)
        self._package_edit.header().hide()
        self._package_edit.itemChanged.connect(self._package_changed)
        self.addWidget(self._package_edit, 0, 0, 3, 1)

        self._scan_button = QPushButton(scan, whatsThis=scan_whats_this,
                clicked=self._scan, enabled=False)
        self.addWidget(self._scan_button, 0, 1)

        self._remove_button = QPushButton("Remove all",
                whatsThis="Remove all of the scanned directories and files.",
                clicked=self._remove_all, enabled=False)
        self.addWidget(self._remove_button, 0, 2)

        self._include_button = QPushButton("Include all",
                whatsThis="Select all of the scanned directories and files.",
                clicked=self._include_all, enabled=False)
        self.addWidget(self._include_button, 1, 1)

        self._exclude_button = QPushButton("Exclude all",
                whatsThis="Deselect all of the scanned directories and files.",
                clicked=self._exclude_all, enabled=False)
        self.addWidget(self._exclude_button, 1, 2)

        self._exclusions_edit = QTreeWidget(
                whatsThis="Any directory or file that matches any of the "
                        "these patterns will be automatically ignored when "
                        "scanning. Double-click on a pattern to edit or remove "
                        "it. Double-click below the last pattern in order to "
                        "add a new one.")
        self._exclusions_edit.setHeaderLabel("Exclusions")
        self._exclusions_edit.setEditTriggers(
                QTreeWidget.DoubleClicked|QTreeWidget.SelectedClicked|
                        QTreeWidget.EditKeyPressed)
        self._exclusions_edit.setRootIsDecorated(False)
        self._exclusions_edit.itemChanged.connect(self._exclusion_changed)

        self.addWidget(self._exclusions_edit, 2, 1, 1, 2)

    def configure(self, package, project):
        """ Configure the editor with the contents of the given package and
        project.
        """

        # Save the configuration.
        self.package = package
        self.project = project

        # Set the package itself.
        self._visualise()

        # Set the exclusions.
        self._exclusions_edit.clear()

        for exclude in package.exclusions:
            self._add_exclusion_item(exclude)

        # Add one to be edited to create a new entry.
        self._add_exclusion_item()

        self._scan_button.setEnabled(package is not None)

    def get_root_dir(self):
        """ Return the root directory to scan, or '' if there was an error or
        the user cancelled.
        """

        raise NotImplementedError

    def filter(self, name):
        """ See if a scanned name should be discarded. """

        # Include everything by default.
        return False

    def required(self, name):
        """ See if a scanned name is required. """

        # Nothing is required by default.
        return False

    def _add_exclusion_item(self, exclude=''):
        """ Add a QTreeWidgetItem that holds an exclusion. """

        itm = QTreeWidgetItem([exclude])

        itm.setFlags(
                Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsEnabled|
                        Qt.ItemNeverHasChildren)

        self._exclusions_edit.addTopLevelItem(itm)

    def _exclusion_changed(self, itm, column):
        """ Invoked when an exclusion has changed. """

        exc_edit = self._exclusions_edit

        new_exc = itm.data(0, Qt.DisplayRole).strip()
        itm_index = exc_edit.indexOfTopLevelItem(itm)

        if new_exc != '':
            # See if we have added a new one.
            if itm_index == exc_edit.topLevelItemCount() - 1:
                self._add_exclusion_item()
        else:
            # It is empty so remove it.
            exc_edit.takeTopLevelItem(itm_index)

        # Save the new exclusions.
        self.package.exclusions = [
                exc_edit.topLevelItem(i).data(0, Qt.DisplayRole).strip()
                        for i in range(exc_edit.topLevelItemCount() - 1)]

        self.package_changed.emit()

    def _get_items(self):
        """ Return an iterator over the tree widget items. """

        it = QTreeWidgetItemIterator(self._package_edit)

        if self._show_root:
            it += 1

        itm = it.value()
        while itm is not None:
            yield itm
            it += 1
            itm = it.value()

    def _include_all(self, _):
        """ Invoked when the user clicks on the include all button. """

        for itm in self._get_items():
            itm.setCheckState(0, Qt.Checked)

    def _exclude_all(self, _):
        """ Invoked when the user clicks on the exclude all button. """

        for itm in self._get_items():
            if not itm.isDisabled():
                itm.setCheckState(0, Qt.Unchecked)
                itm.setExpanded(False)

    def _remove_all(self, _):
        """ Invoked when the use clicks on the remove all button. """

        blocked = self._package_edit.blockSignals(True)
        self._package_edit.clear()
        self._package_edit.blockSignals(blocked)

        self._enable_buttons()

        # This is a bit of a hack but is currently the only way to completely
        # remove the application package.
        if self._show_root:
            self.package.name = ''

        del self.package.contents[:]
        self.package_changed.emit()

    def _enable_buttons(self):
        """ Set the enabled state of those buttons that require content. """

        enable = (len(list(self._get_items())) != 0)

        self._remove_button.setEnabled(enable)
        self._include_button.setEnabled(enable)
        self._exclude_button.setEnabled(enable)

    def _scan(self, _):
        """ Invoked when the user clicks on the scan button. """

        project = self.project
        package = self.package

        # Get the root directory to scan.
        root = self.get_root_dir()
        if root == '':
            return

        # Save the included state of any existing contents so that they can be
        # restored after the scan.
        old_state = {}

        for itm in self._get_items():
            rel_path = [itm.data(0, Qt.DisplayRole)]

            parent = itm.parent()
            while parent is not None:
                rel_path.append(parent.data(0, Qt.DisplayRole))
                parent = parent.parent()

            rel_path.reverse()

            if self._show_root:
                rel_path = rel_path[1:]

            old_state['/'.join(rel_path)] = (itm.checkState(0) == Qt.Checked)

        # Walk the package.
        root_dir = QDir(root)
        if not root_dir.exists():
            QMessageBox.warning(self.parentWidget(), "Scan Directory",
                    "{0} is not a valid directory.".format(
                            QDir.toNativeSeparators(root)))
            return

        self._add_to_container(package, root_dir, [], old_state)
        self._visualise()

        self.package_changed.emit()

    def _add_to_container(self, container, content_dir, dir_stack, old_state):
        """ Add the files and directories of a package or sub-package to a
        container.
        """

        dir_contents = content_dir.entryInfoList(
                QDir.Files|QDir.Dirs|QDir.NoDotAndDotDot)

        # Make sure any filter is applied in a predictable order.
        dir_contents.sort(key=lambda fi: fi.fileName().lower()[1:] if fi.fileName().startswith('_') else fi.fileName().lower())

        dir_stack.append(content_dir.dirName())
        contents = []

        for content in dir_contents:
            name = content.fileName()

            # Apply any exclusions.
            for exc in self.package.exclusions:
                if fnmatch.fnmatch(name, exc):
                    name = None
                    break

            if name is None:
                continue

            # Apply any filter.
            if len(dir_stack) > 1:
                module_path = dir_stack[1:]
                module_path.append(name)
                path_name = '/'.join(module_path)
            else:
                path_name = name

            if self.filter(path_name):
                continue

            # See if we already know the included state.
            included = old_state.get(path_name, False)

            # Add the content.
            if content.isDir():
                qrc = QrcDirectory(name, included)

                self._add_to_container(qrc, QDir(content.canonicalFilePath()),
                        dir_stack, old_state)
            elif content.isFile():
                qrc = QrcFile(name, included)
            else:
                continue

            contents.append(qrc)

        container.contents = contents
        dir_stack.pop()

    def _visualise(self):
        """ Update the GUI with the package content. """

        blocked = self._package_edit.blockSignals(True)

        self._package_edit.clear()

        if self.package.name is not None:
            if self._show_root:
                parent = QTreeWidgetItem([':/' + self.package.name])
                self._package_edit.addTopLevelItem(parent)
                parent.setExpanded(True)
            else:
                parent = self._package_edit

            self._visualise_contents(self.package.contents, parent)

        self._package_edit.blockSignals(blocked)

        self._enable_buttons()

    def _visualise_contents(self, contents, parent):
        """ Visualise the contents for a parent. """

        p = parent
        while p is not None and isinstance(p, QTreeWidgetItem):
            p = p.parent()

        for content in contents:
            itm = QTreeWidgetItem(parent, [content.name])

            itm.setCheckState(0,
                    Qt.Checked if content.included else Qt.Unchecked)

            itm.setData(0, Qt.UserRole, content)

            if isinstance(content, QrcDirectory):
                self._visualise_contents(content.contents, itm)

    def _package_changed(self, itm, column):
        """ Invoked when part of the package changes. """

        if itm.checkState(0) == Qt.Checked:
            itm.data(0, Qt.UserRole).included = True
            itm.setExpanded(True)
        else:
            self._exclude(itm)
            itm.setExpanded(False)

        self.package_changed.emit()

    def _exclude(self, itm):
        """ Exclude an item and any children it may have. """

        for idx in range(itm.childCount()):
            self._exclude(itm.child(idx))

        itm.data(0, Qt.UserRole).included = False
        itm.setCheckState(0, Qt.Unchecked)
