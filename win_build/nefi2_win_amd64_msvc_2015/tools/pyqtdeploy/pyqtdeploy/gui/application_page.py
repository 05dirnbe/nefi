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


from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import (QButtonGroup, QCheckBox, QComboBox, QFileDialog,
        QGridLayout, QGroupBox, QHBoxLayout, QLineEdit, QRadioButton, QWidget)

from ..metadata import (get_supported_python_version,
        get_supported_python_version_index, get_supported_python_versions)
from .better_form import BetterForm
from .filename_editor import FilenameEditor
from .qrc_package_editor import QrcPackageEditor


class ApplicationPage(QWidget):
    """ The GUI for the application page of a project. """

    # The page's label.
    label = "Application Source"

    # Emitted when the user changes the PyQt version.
    pyqt_version_changed = pyqtSignal(bool)

    # Emitted when the user changes the Python target version.
    python_target_version_changed = pyqtSignal()

    @property
    def project(self):
        """ The project property getter. """

        return self._project

    @project.setter
    def project(self, value):
        """ The project property setter. """

        if self._project != value:
            self._project = value
            self._script_edit.set_project(value)
            self._package_edit.set_project(value)
            self._update_page()

    def __init__(self):
        """ Initialise the page. """

        super().__init__()

        self._project = None

        # Create the page's GUI.
        layout = QGridLayout()

        form = BetterForm()

        self._name_edit = QLineEdit(
                placeholderText="Application name",
                whatsThis="The name of the application. It will default to "
                        "the base name of the application script without any "
                        "extension.",
                textEdited=self._name_changed)
        form.addRow("Name", self._name_edit)

        self._script_edit = FilenameEditor("Application Script",
                placeholderText="Application script",
                whatsThis="The name of the application's optional main script "
                        "file.",
                textEdited=self._script_changed)
        form.addRow("Main script file", self._script_edit)

        self._entry_point_edit = QLineEdit(
                placeholderText="Entry point in application package",
                whatsThis="The name of the optional entry point in the "
                        "application's package.",
                textEdited=self._entry_point_changed)
        form.addRow("Entry point", self._entry_point_edit)

        self._sys_path_edit = QLineEdit(
                placeholderText="Additional sys.path directories",
                whatsThis="A space separated list of additional directories, "
                        "ZIP files and eggs to add to <tt>sys.path</tt>. Only "
                        "set this if you want to allow external packages to "
                        "be imported.",
                textEdited=self._sys_path_changed)
        form.addRow("sys.path", self._sys_path_edit)

        layout.addLayout(form, 0, 0)

        options_layout = BetterForm()

        self._py_version_edit = QComboBox(
                whatsThis="Select the target Python version.")
        self._py_version_edit.addItems(get_supported_python_versions())
        self._py_version_edit.currentIndexChanged.connect(
                self._py_version_changed)
        options_layout.addRow("Target Python version", self._py_version_edit)

        self._pyqt_version_edit = QComboBox(
                whatsThis="Select the PyQt version.")
        self._pyqt_version_edit.addItems(["PyQt4", "PyQt5"])
        self._pyqt_version_edit.currentIndexChanged.connect(
                self._pyqt_version_changed)
        options_layout.addRow("Target PyQt version", self._pyqt_version_edit)

        self._console_edit = QCheckBox("Use console (Windows)",
                whatsThis="Enable console output for Windows applications. "
                        "Console output will be enabled automatically if no "
                        "graphical PyQt modules are used.",
                stateChanged=self._console_changed)
        options_layout.addRow(self._console_edit)

        self._bundle_edit = QCheckBox("Application bundle (OS X)",
                whatsThis="Build an application bundle on OS X. If it is not "
                        "checked then the application will be built as a "
                        "simple executable.",
                stateChanged=self._bundle_changed)
        options_layout.addRow(self._bundle_edit)

        layout.addLayout(options_layout, 0, 1)

        self._package_edit = _ApplicationPackageEditor()
        self._package_edit.package_changed.connect(self._package_changed)
        package_edit_gb = QGroupBox(self._package_edit.title)
        package_edit_gb.setLayout(self._package_edit)
        layout.addWidget(package_edit_gb, 1, 0, 1, 2)
        layout.setRowStretch(1, 1)

        self.setLayout(layout)

    def _update_page(self):
        """ Update the page using the current project. """

        project = self.project

        self._name_edit.setText(project.application_name)
        self._script_edit.setText(project.application_script)
        self._entry_point_edit.setText(project.application_entry_point)
        self._sys_path_edit.setText(project.sys_path)
        self._package_edit.configure(project.application_package, project)

        blocked = self._py_version_edit.blockSignals(True)
        self._py_version_edit.setCurrentIndex(
                get_supported_python_version_index(
                        project.python_target_version))
        self._py_version_edit.blockSignals(blocked)

        blocked = self._pyqt_version_edit.blockSignals(True)
        self._pyqt_version_edit.setCurrentIndex(
                1 if project.application_is_pyqt5 else 0)
        self._pyqt_version_edit.blockSignals(blocked)

        blocked = self._console_edit.blockSignals(True)
        self._console_edit.setCheckState(
                Qt.Checked if project.application_is_console else Qt.Unchecked)
        self._console_edit.blockSignals(blocked)

        blocked = self._bundle_edit.blockSignals(True)
        self._bundle_edit.setCheckState(
                Qt.Checked if project.application_is_bundle else Qt.Unchecked)
        self._bundle_edit.blockSignals(blocked)

    def _py_version_changed(self, idx):
        """ Invoked when the user changes the Python version number. """

        self.project.python_target_version = get_supported_python_version(idx)
        self.project.modified = True

        self.python_target_version_changed.emit()

    def _pyqt_version_changed(self, idx):
        """ Invoked when the user changes the PyQt version number. """

        pyqt5 = (idx == 1)
        self.project.application_is_pyqt5 = pyqt5
        self.project.modified = True

        self.pyqt_version_changed.emit(pyqt5)

    def _console_changed(self, state):
        """ Invoked when the user changes the console state. """

        self.project.application_is_console = (state == Qt.Checked)
        self.project.modified = True

    def _bundle_changed(self, state):
        """ Invoked when the user changes the bundle state. """

        self.project.application_is_bundle = (state == Qt.Checked)
        self.project.modified = True

    def _name_changed(self, value):
        """ Invoked when the user edits the application name. """

        self.project.application_name = value
        self.project.modified = True

    def _script_changed(self, value):
        """ Invoked when the user edits the application script name. """

        self.project.application_script = value
        self.project.modified = True

    def _entry_point_changed(self, value):
        """ Invoked when the user edits the entry point. """

        self.project.application_entry_point = value
        self.project.modified = True

    def _sys_path_changed(self, value):
        """ Invoked when the user edits the sys.path directories. """

        self.project.sys_path = value.strip()
        self.project.modified = True

    def _package_changed(self):
        """ Invoked when the user edits the application package. """

        self.project.modified = True


class _ApplicationPackageEditor(QrcPackageEditor):
    """ A memory filesystem package editor for the application package. """

    # The editor title.
    title = "Application Package Directory"

    def __init__(self):
        """ Initialise the editor. """

        super().__init__(show_root=True, scan="Scan...",
                scan_whats_this="Display a dialog from which you can select "
                        "the application package directory.",
                whats_this="This shows the scanned application package "
                        "directory and its contents. Check those directories "
                        "and files that should be included in the "
                        "application.")

        self._project = None

    def get_root_dir(self):
        """ Get the name of the application directory. """

        project = self._project
        application_package = project.application_package

        default = application_package.name
        if default is not None:
            default = project.path_from_user(default)

        root = QFileDialog.getExistingDirectory(self.parentWidget(),
                self.title, default)

        if root != '':
            application_package.name = project.path_to_user(root)

        return root

    def set_project(self, project):
        """ Set the project. """

        self._project = project
