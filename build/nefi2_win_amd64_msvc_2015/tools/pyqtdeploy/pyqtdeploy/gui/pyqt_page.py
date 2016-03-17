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


from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from PyQt5.QtWidgets import (QCheckBox, QGridLayout, QGroupBox, QStackedWidget,
        QVBoxLayout, QWidget)

from ..metadata import pyqt4_metadata, pyqt5_metadata


class PyQtPage(QStackedWidget):
    """ The GUI for the PyQt configuration page of a project. """

    # The page's label.
    label = "PyQt Modules"

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

        # Create the stacked pages for each PyQt version.
        self._pyqt5_page = _PyQtVersionPage(pyqt5_metadata)
        self.addWidget(self._pyqt5_page)

        self._pyqt4_page = _PyQtVersionPage(pyqt4_metadata)
        self.addWidget(self._pyqt4_page)

    @pyqtSlot(bool)
    def set_pyqt_version(self, is_pyqt5):
        """ Configure the page according to the PyQt version. """

        page = self._pyqt5_page if is_pyqt5 else self._pyqt4_page
        page.update_project()
        self.setCurrentWidget(page)

    def _update_page(self):
        """ Update the page using the current project. """

        project = self._project

        self._pyqt5_page.project = project
        self._pyqt4_page.project = project

        if project.application_is_pyqt5:
            self._pyqt5_page.configure()
            self._pyqt4_page.clear()

            self.setCurrentWidget(self._pyqt5_page)
        else:
            self._pyqt5_page.clear()
            self._pyqt4_page.configure()

            self.setCurrentWidget(self._pyqt4_page)


class _PyQtVersionPage(QWidget):
    """ The GUI for a PyQt version specific configuration page. """

    def __init__(self, metadata):
        """ Initialise the page. """

        super().__init__()

        self._metadata = metadata
        self._buttons = {}
        self.project = None

        # Create the page's GUI.
        layout = QVBoxLayout()

        self._create_buttons(layout, "Imported Modules", 'base')
        self._create_buttons(layout, "Internal OpenGL Modules", 'opengl')
        self._create_buttons(layout, "Add-on Modules", 'addon')
        layout.addStretch()

        self.setLayout(layout)

    def update_project(self):
        """ Update the project to contain the currently selected modules. """

        modules = self.project.pyqt_modules

        modules[:] = [name for name, b in self._buttons.items()
                if b.explicitly_required]

    def configure(self):
        """ Update the page according to modules specified in the project. """

        modules = self.project.pyqt_modules

        for name, b in self._buttons.items():
            b.explicitly_required = (name in modules)

        self._set_implicit_requirements()

    def clear(self):
        """ Deselect all modules. """

        for b in self._buttons.values():
            b.explictly_required = False

        self._set_implicit_requirements()

    def _create_buttons(self, layout, title, group):
        """ Add a button for each module in a group to a layout. """

        imports = grid = None
        row = column = 0

        for module_name in sorted(self._metadata.keys()):
            if self._metadata[module_name].group != group:
                continue

            if imports is None:
                imports = QGroupBox(title)
                grid = QGridLayout()

            b = ModuleButton(module_name)
            b.explicitly_required_changed.connect(self._module_toggled)

            self._buttons[module_name] = b
            grid.addWidget(b, row, column)

            column += 1
            if column == 5:
                row += 1
                column = 0

        if imports is not None:
            imports.setLayout(grid)
            layout.addWidget(imports)

    def _module_toggled(self, module, required):
        """ Invoked when a module button is toggled. """

        self._set_implicit_requirements()

        if required:
            self.project.pyqt_modules.append(module)
        else:
            self.project.pyqt_modules.remove(module)

        self.project.modified = True

    def _set_implicit_requirements(self):
        """ Set the implicit requirement for each module button. """

        for b in self._buttons.values():
            b.implicitly_required = False

        for name, b in self._buttons.items():
            if b.explicitly_required:
                self._set_button_dependencies(name)

    def _set_button_dependencies(self, module_name):
        """ Set the implicit requirements for the dependencies of a button. """

        for dep in self._metadata[module_name].deps:
            self._buttons[dep].implicitly_required = True

            # Handle sub-dependencies.
            self._set_button_dependencies(dep)


class ModuleButton(QCheckBox):
    """ A button for a module allowing for it to be explicitly included or
    implicitly included because it is a dependency.
    """

    # Emitted if the user changes the explicitly required state of the module.
    explicitly_required_changed = pyqtSignal(str, bool)

    def __init__(self, text):
        """ Initialise the button. """

        super().__init__(text)

        self.setWhatsThis(
                "Check this if the application explicitly imports the "
                "<tt>{0}</tt> module. It will be partially checked (and "
                "automatically included) if another module requires "
                "it.".format(text))
        self.setTristate(True)

        self._explicit = False
        self._implicit = False

    def nextCheckState(self):
        """ Reimplemented to update the state after the user clicks the button.
        """

        self._explicit = not self._explicit
        self._update_state()

        self.explicitly_required_changed.emit(self.text(), self._explicit)

    @property
    def explicitly_required(self):
        """ The explicitly_required property getter. """

        return self._explicit

    @explicitly_required.setter
    def explicitly_required(self, required):
        """ The explicitly_required property setter. """

        self._explicit = required
        self._update_state()

    @property
    def implicitly_required(self):
        """ The implicitly_required property getter. """

        return self._implicit

    @implicitly_required.setter
    def implicitly_required(self, required):
        """ The implicitly_required property setter. """

        self._implicit = required
        self._update_state()

    def _update_state(self):
        """ Update the state of the button after a change. """

        if self._explicit:
            state = Qt.Checked
        elif self._implicit:
            state = Qt.PartiallyChecked
        else:
            state = Qt.Unchecked

        self.setCheckState(state)
