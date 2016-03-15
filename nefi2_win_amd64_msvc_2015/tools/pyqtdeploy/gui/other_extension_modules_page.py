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


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget

from ..project import ExtensionModule
from .filename_editor_delegate import FilenameEditorDelegate


class OtherExtensionModulesPage(QWidget):
    """ The GUI for the other extension modules page of a project. """

    # The page's label.
    label = "Other Extension Modules"

    @property
    def project(self):
        """ The project property getter. """

        return self._project

    @project.setter
    def project(self, value):
        """ The project property setter. """

        if self._project != value:
            self._project = value
            self._sources_delegate.set_project(value)
            self._includepath_delegate.set_project(value)
            self._update_page()

    def __init__(self):
        """ Initialise the page. """

        super().__init__()

        self._project = None

        # Create the page's GUI.
        layout = QVBoxLayout()

        self._extension_modules_edit = QTreeWidget(
                whatsThis="This shows a list of additional extension modules "
                        "to be compiled or linked with the application. "
                        "<b>Name</b> should be the full (dot separated) "
                        "package name of the extension module. The remaining "
                        "columns correspond to <tt>qmake</tt> variables "
                        "needed to compile or link the extension module. "
                        "Double-click on an entry to edit or remove it. "
                        "Double-click below the last entry in order to add a "
                        "new one. Values may be prefixed by a platform "
                        "specific <tt>qmake</tt> scope.")
        self._extension_modules_edit.setHeaderLabels(
                ["Name", "QT", "CONFIG", "SOURCES", "DEFINES", "INCLUDEPATH",
                        "LIBS"])
        self._extension_modules_edit.setEditTriggers(
                QTreeWidget.DoubleClicked|QTreeWidget.SelectedClicked|
                QTreeWidget.EditKeyPressed)
        self._extension_modules_edit.setRootIsDecorated(False)
        self._extension_modules_edit.itemChanged.connect(
                self._extension_module_changed)

        self._sources_delegate = FilenameEditorDelegate(
                "Extension Module Source")
        self._extension_modules_edit.setItemDelegateForColumn(3,
                self._sources_delegate)

        self._includepath_delegate = FilenameEditorDelegate(
                "Extension Module Include Directory", directory=True)
        self._extension_modules_edit.setItemDelegateForColumn(5,
                self._includepath_delegate)

        layout.addWidget(self._extension_modules_edit)

        self.setLayout(layout)

    def _update_page(self):
        """ Update the page using the current project. """

        project = self.project

        # Set the extension modules.
        self._extension_modules_edit.clear()

        for extension_module in project.other_extension_modules:
            self._add_extension_module_item(extension_module)

        # Add one to be edited to create a new entry.
        self._add_extension_module_item()

    def _add_extension_module_item(self, extension_module=None):
        """ Add a QTreeWidgetItem that holds an extension module. """

        if extension_module is not None:
            name = extension_module.name
            qt = extension_module.qt
            config = extension_module.config
            sources = extension_module.sources
            defines = extension_module.defines
            includepath = extension_module.includepath
            libs = extension_module.libs
        else:
            name = qt = config = sources = defines = includepath = libs = ''

        itm = QTreeWidgetItem(
                [name, qt, config, sources, defines, includepath, libs])

        itm.setFlags(
                Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsEnabled|
                        Qt.ItemNeverHasChildren)

        self._extension_modules_edit.addTopLevelItem(itm)

    def _extension_module_changed(self, itm, value):
        """ Invoked when an extension module has changed. """

        project = self.project
        em_edit = self._extension_modules_edit

        new_name = itm.data(0, Qt.DisplayRole).strip()
        new_qt = itm.data(1, Qt.DisplayRole).strip()
        new_config = itm.data(2, Qt.DisplayRole).strip()
        new_sources = itm.data(3, Qt.DisplayRole).strip()
        new_defines = itm.data(4, Qt.DisplayRole).strip()
        new_includepath = itm.data(5, Qt.DisplayRole).strip()
        new_libs = itm.data(6, Qt.DisplayRole).strip()
        itm_index = em_edit.indexOfTopLevelItem(itm)

        for new in (new_name, new_qt, new_config, new_sources, new_defines, new_includepath, new_libs):
            if new != '':
                # See if we have added a new one.
                if itm_index == em_edit.topLevelItemCount() - 1:
                    self._add_extension_module_item()

                break
        else:
            # It is empty so remove it.
            em_edit.takeTopLevelItem(itm_index)

        # Save the new extension modules.
        project.other_extension_modules = [
                ExtensionModule(
                        em_edit.topLevelItem(i).data(0, Qt.DisplayRole).strip(),
                        em_edit.topLevelItem(i).data(1, Qt.DisplayRole).strip(),
                        em_edit.topLevelItem(i).data(2, Qt.DisplayRole).strip(),
                        em_edit.topLevelItem(i).data(3, Qt.DisplayRole).strip(),
                        em_edit.topLevelItem(i).data(4, Qt.DisplayRole).strip(),
                        em_edit.topLevelItem(i).data(5, Qt.DisplayRole).strip(),
                        em_edit.topLevelItem(i).data(6, Qt.DisplayRole).strip())
                        for i in range(em_edit.topLevelItemCount() - 1)]

        project.modified = True
