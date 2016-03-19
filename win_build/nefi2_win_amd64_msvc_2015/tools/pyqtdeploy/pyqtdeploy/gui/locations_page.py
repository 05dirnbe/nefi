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


from PyQt5.QtWidgets import QGroupBox, QMessageBox, QVBoxLayout, QWidget

from .better_form import BetterForm
from .filename_editor import FilenameEditor


class LocationsPage(QWidget):
    """ The GUI for the locations page of a project. """

    # The page's label.
    label = "Locations"

    @property
    def project(self):
        """ The project property getter. """

        return self._project

    @project.setter
    def project(self, value):
        """ The project property setter. """

        if self._project != value:
            self._project = value
            self._source_edit.set_project(value)
            self._target_inc_edit.set_project(value)
            self._target_lib_edit.set_project(value)
            self._target_stdlib_edit.set_project(value)
            self._build_edit.set_project(value)
            self._update_page()

    def __init__(self):
        """ Initialise the page. """

        super().__init__()

        self._project = None

        # Create the page's GUI.
        py_host_group = QGroupBox("Host Python Locations")
        py_host_layout = BetterForm()

        self._host_interp_edit = FilenameEditor("Host Interpreter",
                placeholderText="Interpreter executable",
                whatsThis="The name of the host interpreter's executable. "
                        "This must be on <tt>PATH</tt> or be an absolute "
                        "pathname.",
                textEdited=self._host_interp_changed)
        py_host_layout.addRow("Interpreter", self._host_interp_edit)

        self._source_edit = FilenameEditor("Source Directory",
                placeholderText="Source directory name",
                whatsThis="The name of the Python source directory.",
                textEdited=self._source_changed, directory=True)
        py_host_layout.addRow("Source directory", self._source_edit)

        py_host_group.setLayout(py_host_layout)

        py_target_group = QGroupBox("Target Python Locations")
        py_target_layout = BetterForm()

        self._target_inc_edit = FilenameEditor("Target Include Directory",
                placeholderText="Include directory name",
                whatsThis="The target interpreter's include directory.",
                textEdited=self._target_inc_changed, directory=True)
        py_target_layout.addRow("Include directory", self._target_inc_edit)

        self._target_lib_edit = FilenameEditor("Python Library",
                placeholderText="Library name",
                whatsThis="The target interpreter's Python library.",
                textEdited=self._target_lib_changed)
        py_target_layout.addRow("Python library", self._target_lib_edit)

        self._target_stdlib_edit = FilenameEditor(
                "Target Standard Library Directory",
                placeholderText="Standard library directory name",
                whatsThis="The target interpreter's standard library "
                        "directory.",
                textEdited=self._target_stdlib_changed, directory=True)
        py_target_layout.addRow("Standard library directory",
                self._target_stdlib_edit)

        py_target_group.setLayout(py_target_layout)

        others_group = QGroupBox("Other Locations")
        others_layout = BetterForm()

        self._build_edit = FilenameEditor("Build Directory",
                placeholderText="Build directory name",
                whatsThis="The name of the build directory. The directory "
                        "will be created automatically if necessary.",
                textEdited=self._build_changed, directory=True)
        others_layout.addRow("Build directory", self._build_edit)

        self._qmake_edit = FilenameEditor("qmake",
                placeholderText="qmake executable",
                whatsThis="The name of the <tt>qmake</tt> executable. This "
                        "must be on <tt>PATH</tt> or be an absolute pathname.",
                textEdited=self._qmake_changed)
        others_layout.addRow("qmake", self._qmake_edit)

        others_group.setLayout(others_layout)

        layout = QVBoxLayout()
        layout.addWidget(py_host_group)
        layout.addWidget(py_target_group)
        layout.addWidget(others_group)
        layout.addStretch()

        self.setLayout(layout)

        BetterForm.align_forms(py_host_layout, py_target_layout, others_layout)

    def _update_page(self):
        """ Update the page using the current project. """

        project = self.project

        self._host_interp_edit.setText(project.python_host_interpreter)
        self._source_edit.setText(project.python_source_dir)
        self._target_inc_edit.setText(project.python_target_include_dir)
        self._target_lib_edit.setText(project.python_target_library)
        self._target_stdlib_edit.setText(project.python_target_stdlib_dir)
        self._build_edit.setText(project.build_dir)
        self._qmake_edit.setText(project.qmake)

    def _host_interp_changed(self, value):
        """ Invoked when the user edits the host interpreter name. """

        self.project.python_host_interpreter = value
        self.project.modified = True

    def _source_changed(self, value):
        """ Invoked when the user edits the source directory name. """

        self.project.python_source_dir = value
        self.project.modified = True

    def _target_inc_changed(self, value):
        """ Invoked when the user edits the target include directory name. """

        self.project.python_target_include_dir = value
        self.project.modified = True

    def _target_lib_changed(self, value):
        """ Invoked when the user edits the target Python library name. """

        self.project.python_target_library = value
        self.project.modified = True

    def _target_stdlib_changed(self, value):
        """ Invoked when the user edits the target standard library directory
        name.
        """

        self.project.python_target_stdlib_dir = value
        self.project.modified = True

    def _build_changed(self, value):
        """ Invoked when the user edits the build directory name. """

        self.project.build_dir = value
        self.project.modified = True

    def _qmake_changed(self, value):
        """ Invoked when the user edits the qmake name. """

        self.project.qmake = value
        self.project.modified = True
