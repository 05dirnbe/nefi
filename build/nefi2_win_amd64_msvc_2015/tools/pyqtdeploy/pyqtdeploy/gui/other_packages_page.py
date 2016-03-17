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


import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QGroupBox, QHBoxLayout, QMessageBox, QTreeWidget,
        QTreeWidgetItem, QWidget)

from ..project import QrcPackage
from .filename_editor_delegate import FilenameEditorDelegate
from .qrc_package_editor import QrcPackageEditor


class OtherPackagesPage(QWidget):
    """ The GUI for the other packages page of a project. """

    # The page's label.
    label = "Other Packages"

    @property
    def project(self):
        """ The project property getter. """

        return self._project

    @project.setter
    def project(self, value):
        """ The project property setter. """

        if self._project != value:
            self._project = value
            self._package_delegate.set_project(value)
            self._update_page()

    def __init__(self):
        """ Initialise the page. """

        super().__init__()

        self._project = None

        # Create the page's GUI.
        layout = QHBoxLayout()

        self._package_selector = QTreeWidget(
                whatsThis="This shows a list of directories containing "
                        "additional Python packages which can be scanned when "
                        "selected. Double-click on a directory to edit or "
                        "remove it. Double-click below the last directory in "
                        "order to add a new one.")
        self._package_selector.setHeaderLabel("Packages Directory")
        self._package_selector.setEditTriggers(
                QTreeWidget.DoubleClicked|QTreeWidget.SelectedClicked|
                QTreeWidget.EditKeyPressed)
        self._package_selector.setRootIsDecorated(False)
        self._package_selector.currentItemChanged.connect(
                self._package_selector_changed)
        self._package_selector.itemChanged.connect(self._package_dir_changed)

        self._package_delegate = FilenameEditorDelegate("Packages Directory",
                directory=True)

        self._package_selector.setItemDelegateForColumn(0,
                self._package_delegate)

        layout.addWidget(self._package_selector)

        self._package_edit = _PackageDirectoryEditor()
        self._package_edit.package_changed.connect(self._package_changed)

        package_edit_gb = QGroupBox(self._package_edit.title)
        package_edit_gb.setLayout(self._package_edit)
        layout.addWidget(package_edit_gb)

        self.setLayout(layout)

    def _update_page(self):
        """ Update the page using the current project. """

        project = self.project

        self._package_selector.clear()

        for package in project.other_packages:
            self._add_package_dir(package)

        self._add_package_dir()

    def _add_package_dir(self, package=None):
        """ Add a QTreeWidgetItem that holds a package directory. """

        if package is None:
            package = QrcPackage()
            name = ''
        else:
            name = package.name

        itm = QTreeWidgetItem([name])
        itm.setData(0, Qt.UserRole, package)
        itm.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled|Qt.ItemNeverHasChildren|Qt.ItemIsEditable)

        self._package_selector.addTopLevelItem(itm)

    def _package_selector_changed(self, new, old):
        """ Invoked when the user selects a package directory. """

        if new is not None:
            self._package_edit.configure(new.data(0, Qt.UserRole),
                    self.project)

    def _package_dir_changed(self, itm, column):
        """ Invoked when the user edits a package directory name. """

        project = self.project

        selector = self._package_selector

        new_dir = itm.data(0, Qt.DisplayRole).strip()
        itm_index = selector.indexOfTopLevelItem(itm)

        if new_dir != '':
            itm.data(0, Qt.UserRole).name = project.path_to_user(new_dir)

            # See if we have added a new one.
            if itm_index == selector.topLevelItemCount() - 1:
                self._add_package_dir()
        else:
            # It is empty so remove it.
            selector.takeTopLevelItem(itm_index)

        # Save the new packages.
        project.other_packages = [
                selector.topLevelItem(i).data(0, Qt.UserRole)
                        for i in range(selector.topLevelItemCount() - 1)]

        self.project.modified = True

    def _package_changed(self):
        """ Invoked when the user edits a package contents. """

        self.project.modified = True


class _PackageDirectoryEditor(QrcPackageEditor):
    """ A memory filesystem package editor for a package directory. """

    # The editor title.
    title = "Packages Directory Contents"

    def __init__(self):
        """ Initialise the editor. """

        super().__init__(
                scan_whats_this="Scan the currently selected packages "
                        "directory.",
                whats_this="This shows the contents of the scanned packages "
                        "directory. Check those directories and files that "
                        "should be included in the application.")

    def get_root_dir(self):
        """ Get the name of the packages directory. """

        project = self.project
        package = self.package

        if package.name == '':
            QMessageBox.warning(self.parentWidget(), self.title,
                        "The name of the package directory has not been set.")
            return ''

        return project.path_from_user(package.name)

    def filter(self, name):
        """ Reimplemented to filter out any PyQt related stuff. """

        if name in ('libsip.a', 'sip.so', 'sip.lib', 'sip.pyd', 'PyQt5', 'PyQt4'):
            return True

        return super().filter(name)
