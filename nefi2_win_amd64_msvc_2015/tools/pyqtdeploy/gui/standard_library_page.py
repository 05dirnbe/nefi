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


from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import (QCheckBox, QGroupBox, QSplitter, QTreeView,
        QTreeWidget, QTreeWidgetItem, QTreeWidgetItemIterator, QVBoxLayout,
        QWidget)

from ..metadata import (external_libraries_metadata, get_python_metadata,
        PLATFORM_SCOPES)
from ..project import ExternalLibrary


class StandardLibraryPage(QSplitter):
    """ The GUI for the standard library page of a project. """

    # The page's label.
    label = "Standard Library"

    @property
    def project(self):
        """ The project property getter. """

        return self._project

    @project.setter
    def project(self, value):
        """ The project property setter. """

        if self._project != value:
            self._project = value

            self._update_page()

    def __init__(self):
        """ Initialise the page. """

        super().__init__()

        self._project = None

        # Create the page's GUI.
        stdlib_pane = QWidget()
        stdlib_layout = QVBoxLayout()

        self._stdlib_edit = QTreeWidget(
                whatsThis="This shows the packages and modules in the target "
                        "Python version's standard library. Check those "
                        "packages and modules that are explicitly imported by "
                        "the application. A module will be partially checked "
                        "(and automatically included) if another module "
                        "requires it.")
        self._stdlib_edit.setHeaderLabels(["Package"])
        self._stdlib_edit.itemChanged.connect(self._module_changed)

        stdlib_layout.addWidget(self._stdlib_edit)

        stdlib_pane.setLayout(stdlib_layout)
        self.addWidget(stdlib_pane)

        extlib_pane = QWidget()
        extlib_layout = QVBoxLayout()

        plat_gb = QGroupBox("Use standard Python shared library")
        plat_gb_layout = QVBoxLayout()
        self._platform_buttons = []

        for scope, plat, subscopes in PLATFORM_SCOPES:
            plat_cb = QCheckBox(plat,
                    whatsThis="Enable the use of the standard Python shared "
                            "library on {0} rather than a statically compiled "
                            "library.".format(plat),
                    stateChanged=self._platforms_changed)
            plat_cb._scope = scope
            plat_gb_layout.addWidget(plat_cb)
            self._platform_buttons.append(plat_cb)

        plat_gb.setLayout(plat_gb_layout)
        extlib_layout.addWidget(plat_gb)

        self._ssl_edit = QCheckBox("Enable optional SSL support",
                whatsThis="Enable SSL for the standard library modules "
                        "that have optional support for it.",
                stateChanged=self._ssl_changed)
        extlib_layout.addWidget(self._ssl_edit)

        self._extlib_edit = QTreeView(
                whatsThis="This is the list of external libraries that must "
                        "be linked with the application. A library will only "
                        "be enabled if a module in the standard library uses "
                        "it. Double-click in the <b>DEFINES</b>, "
                        "<b>INCLUDEPATH</b> and <b>LIBS</b> columns to modify "
                        "the corresponding <tt>qmake</tt> variable as "
                        "required. Values may be prefixed by a platform "
                        "specific <tt>qmake</tt> scope.")
        self._extlib_edit.setRootIsDecorated(False)
        self._extlib_edit.setEditTriggers(
                QTreeView.DoubleClicked|QTreeView.SelectedClicked|
                QTreeView.EditKeyPressed)

        model = QStandardItemModel(self._extlib_edit)
        model.setHorizontalHeaderLabels(
                ("External Library", 'DEFINES', 'INCLUDEPATH', 'LIBS'))
        model.itemChanged.connect(self._extlib_changed)

        for extlib in external_libraries_metadata:
            name_itm = QStandardItem(extlib.user_name)

            extlib._items = (name_itm, QStandardItem(), QStandardItem(),
                    QStandardItem())

            model.appendRow(extlib._items)

        self._extlib_edit.setModel(model)

        for col in range(3):
            self._extlib_edit.resizeColumnToContents(col)

        extlib_layout.addWidget(self._extlib_edit)

        self._ignore_extlib_changes = False

        extlib_pane.setLayout(extlib_layout)
        self.addWidget(extlib_pane)

    @pyqtSlot()
    def python_target_version_changed(self):
        """ Configure the page after the Python target version has changed. """

        self._update_page()
 
    def _update_page(self):
        """ Update the page using the current project. """

        project = self.project

        for plat in self._platform_buttons:
            blocked = plat.blockSignals(True)
            plat.setCheckState(
                    Qt.Checked if plat._scope in project.python_use_platform
                            else Qt.Unchecked)
            plat.blockSignals(blocked)

        blocked = self._ssl_edit.blockSignals(True)
        self._ssl_edit.setCheckState(
                Qt.Checked if project.python_ssl else Qt.Unchecked)
        self._ssl_edit.blockSignals(blocked)

        self._update_extlib_editor()
        self._update_stdlib_editor()

    def _update_stdlib_editor(self):
        """ Update the standard library module editor. """

        project = self.project
        editor = self._stdlib_edit

        metadata = get_python_metadata(project.python_target_version)

        blocked = editor.blockSignals(True)

        editor.clear()

        def add_module(name, module, parent):
            itm = QTreeWidgetItem(parent, name.split('.')[-1:])
            itm.setFlags(Qt.ItemIsEnabled|Qt.ItemIsUserCheckable)
            itm._name = name

            # Handle any sub-modules.
            if module.modules is not None:
                for submodule_name in module.modules:
                    # We assume that a missing sub-module is because it is not
                    # in the current version rather than bad meta-data.
                    submodule = metadata.get(submodule_name)
                    if submodule is not None:
                        add_module(submodule_name, submodule, itm)

        for name, module in metadata.items():
            if not module.internal and '.' not in name:
                add_module(name, module, editor)

        editor.sortItems(0, Qt.AscendingOrder)

        editor.blockSignals(blocked)

        self._set_dependencies()

    def _set_dependencies(self):
        """ Set the dependency information. """

        project = self.project
        editor = self._stdlib_edit

        required_modules, required_libraries = project.get_stdlib_requirements()

        blocked = editor.blockSignals(True)

        it = QTreeWidgetItemIterator(editor)
        itm = it.value()
        while itm is not None:
            external = required_modules.get(itm._name)
            expanded = False
            if external is None:
                state = Qt.Unchecked
            elif external:
                state = Qt.Checked
                expanded = True
            else:
                state = Qt.PartiallyChecked

            itm.setCheckState(0, state)

            # Make sure every explicitly checked item is visible.
            if expanded:
                parent = itm.parent()
                while parent is not None:
                    parent.setExpanded(True)
                    parent = parent.parent()

            it += 1
            itm = it.value()

        editor.blockSignals(blocked)

        model = self._extlib_edit.model()

        # Note that we can't simply block the model's signals as this would
        # interfere with the model/view interactions.
        self._ignore_extlib_changes = True

        for extlib in external_libraries_metadata:
            if extlib.name in required_libraries:
                for idx, itm in enumerate(extlib._items):
                    itm.setFlags(
                            Qt.ItemIsEnabled|Qt.ItemIsEditable if idx != 0
                                    else Qt.ItemIsEnabled)
            else:
                for itm in extlib._items:
                    itm.setFlags(Qt.NoItemFlags)

        self._ignore_extlib_changes = False

    def _update_extlib_editor(self):
        """ Update the external library editor. """

        project = self.project
        model = self._extlib_edit.model()

        blocked = model.blockSignals(True)

        for extlib in external_libraries_metadata:
            _, defs, incp, libs = extlib._items

            for prj_extlib in project.external_libraries:
                if prj_extlib.name == extlib.name:
                    defs.setText(prj_extlib.defines)
                    incp.setText(prj_extlib.includepath)
                    libs.setText(prj_extlib.libs)
                    break
            else:
                defs.setText('')
                incp.setText('')
                libs.setText(extlib.libs)

        model.blockSignals(blocked)

    def _ssl_changed(self, state):
        """ Invoked when the SSL support changes. """

        project = self.project

        project.python_ssl = (state == Qt.Checked)
        self._set_dependencies()

        project.modified = True

    def _platforms_changed(self, state):
        """ Invoked when the platforms change. """

        project = self._project

        project.python_use_platform = []

        for plat in self._platform_buttons:
            if plat.checkState() == Qt.Checked:
                project.python_use_platform.append(plat._scope)

        project.modified = True

    def _module_changed(self, itm, col):
        """ Invoked when a standard library module has changed. """

        project = self._project
        name = itm._name

        if name in project.standard_library:
            project.standard_library.remove(name)
        else:
            project.standard_library.append(name)

        self._set_dependencies()

        project.modified = True

    def _extlib_changed(self, itm):
        """ Invoked when an external library has changed. """

        if self._ignore_extlib_changes:
            return

        self._ignore_extlib_changes = True

        project = self.project

        idx = self._extlib_edit.model().indexFromItem(itm)
        extlib = external_libraries_metadata[idx.row()]
        col = idx.column()

        # Get the project entry, creating it if necessary.
        for prj_extlib in project.external_libraries:
            if prj_extlib.name == extlib.name:
                break
        else:
            prj_extlib = ExternalLibrary(extlib.name, '', '', extlib.libs)
            project.external_libraries.append(prj_extlib)

        # Update the project.
        text = itm.text().strip()

        if col == 1:
            prj_extlib.defines = text
        elif col == 2:
            prj_extlib.includepath = text
        elif col == 3:
            if text == '':
                text = extlib.libs
                itm.setText(text)

            prj_extlib.libs = text

        # If the project entry corresponds to the default then remove it.
        if prj_extlib.defines == '' and prj_extlib.includepath == '' and prj_extlib.libs == extlib.libs:
            project.external_libraries.remove(prj_extlib)

        project.modified = True

        self._ignore_extlib_changes = False
