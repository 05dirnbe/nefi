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

from PyQt5.QtCore import QFileInfo, QPoint, QSettings, QSize
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import (QFileDialog, QMainWindow, QMessageBox, QTabWidget,
        QWhatsThis)

from ..project import Project
from ..user_exception import UserException
from ..version import PYQTDEPLOY_RELEASE

from .application_page import ApplicationPage
from .build_page import BuildPage
from .exception_handlers import handle_user_exception
from .locations_page import LocationsPage
from .other_extension_modules_page import OtherExtensionModulesPage
from .other_packages_page import OtherPackagesPage
from .pyqt_page import PyQtPage
from .qmake_page import QMakePage
from .standard_library_page import StandardLibraryPage


class ProjectGUI(QMainWindow):
    """ The GUI for a project. """

    # The filter string to use with file dialogs.
    file_dialog_filter = "Projects (*.pdy)"

    def __init__(self, project):
        """ Initialise the GUI for a project. """

        super().__init__()

        self._create_menus()
        self._create_central_widget()
        self._load_settings()

        self._set_project(project)

    @classmethod
    def load(cls, filename):
        """ Create a project from the given file.  Return None if there was an
        error.
        """

        return cls._load_project(filename) if QFileInfo(filename).exists() else Project(filename)

    def closeEvent(self, event):
        """ Handle a close event. """

        if self._current_project_done():
            self._save_settings()
            event.accept()
        else:
            event.ignore()

    def _set_project(self, project):
        """ Set the GUI's project. """

        self._project = project

        self._project.modified_changed.connect(self.setWindowModified)
        self._project.name_changed.connect(self._name_changed)

        self._name_changed(self._project.name)

        tabs = self.centralWidget()

        for p in range(tabs.count()):
            page = tabs.widget(p)
            page.project = self._project

    def _name_changed(self, name):
        """ Invoked when the project's name changes. """

        title = os.path.basename(name) if name != '' else "Unnamed"
        self.setWindowTitle(title + '[*]')

        self._save_action.setEnabled(name != '')

    def _create_menus(self):
        """ Create the menus. """

        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction("&New", self._new_project, QKeySequence.New)
        file_menu.addAction("&Open...", self._open_project, QKeySequence.Open)
        self._save_action = file_menu.addAction("&Save", self._save_project,
                QKeySequence.Save)
        file_menu.addAction("Save &As...", self._save_as_project,
                QKeySequence.SaveAs)
        file_menu.addSeparator()
        file_menu.addAction("E&xit", self.close, QKeySequence.Quit)

        menu_bar.addSeparator()

        help_menu = menu_bar.addMenu("&Help")
        help_menu.addAction("About pyqtdeploy...", self._about)
        help_menu.addAction(QWhatsThis.createAction(help_menu))

    def _create_central_widget(self):
        """ Create the central widget. """

        tabs = QTabWidget()

        application_page = ApplicationPage()
        tabs.addTab(application_page, application_page.label)

        qmake_page = QMakePage()
        tabs.addTab(qmake_page, qmake_page.label)

        pyqt_page = PyQtPage()
        tabs.addTab(pyqt_page, pyqt_page.label)

        standard_library_page = StandardLibraryPage()
        tabs.addTab(standard_library_page, standard_library_page.label)

        other_packages_page = OtherPackagesPage()
        tabs.addTab(other_packages_page, other_packages_page.label)

        other_extension_modules_page = OtherExtensionModulesPage()
        tabs.addTab(other_extension_modules_page,
                other_extension_modules_page.label)

        locations_page = LocationsPage()
        tabs.addTab(locations_page, locations_page.label)

        build_page = BuildPage()
        tabs.addTab(build_page, build_page.label)

        application_page.pyqt_version_changed.connect(
                pyqt_page.set_pyqt_version)

        application_page.python_target_version_changed.connect(
                standard_library_page.python_target_version_changed)

        self.setCentralWidget(tabs)

    def _about(self):
        """ Tell the user about the application. """

        QMessageBox.about(self, "About pyqtdeploy",
"""This is pyqtdeploy v%s

pyqtdeploy is a tool for deploying PyQt4 and PyQt5 applications written using Python v2.7 or later or Python v3.3 or later to desktop and mobile devices.
""" % PYQTDEPLOY_RELEASE)

    def _new_project(self):
        """ Create a new, unnamed project. """

        if self._current_project_done():
            self._set_project(Project())

    def _open_project(self):
        """ Open an existing project. """

        if self._current_project_done():
            filename, _ = QFileDialog.getOpenFileName(self, "Open",
                    filter=self.file_dialog_filter)

            if filename != '':
                project = self._load_project(filename, self)
                if project is not None:
                    self._set_project(project)

    def _save_project(self):
        """ Save the project and return True if it was saved. """

        try:
            self._project.save()
        except UserException as e:
            handle_user_exception(e, "Save", self)
            return False

        return True

    def _save_as_project(self):
        """ Save the project under a new name and return True if it was saved.
        """

        filename, _ = QFileDialog.getSaveFileName(self, "Save As",
                    filter=self.file_dialog_filter)

        if filename == '':
            return False

        try:
            self._project.save_as(filename)
        except UserException as e:
            handle_user_exception(e, "Save", self)
            return False

        return True

    @staticmethod
    def _load_project(filename, parent=None):
        """ Create a project from the given file.  Return None if there was an
        error.
        """

        try:
            project = Project.load(filename)
        except UserException as e:
            handle_user_exception(e, "Open", parent)
            project = None

        return project

    def _current_project_done(self):
        """ Return True if the user has finished with any current project. """

        if self._project.modified:
            msg_box = QMessageBox(QMessageBox.Question, "Save",
                    "The project has been modified.",
                    QMessageBox.Save|QMessageBox.Discard|QMessageBox.Cancel,
                    parent=self)

            msg_box.setDefaultButton(QMessageBox.Save)
            msg_box.setInformativeText("Do you want to save your changes?")

            ans = msg_box.exec()

            if ans == QMessageBox.Cancel:
                return False

            if ans == QMessageBox.Save:
                return self._save_project() if self._project.name != "" else self._save_as_project()

        return True

    def _load_settings(self):
        """ Load the user specific settings. """

        settings = QSettings()

        self.resize(settings.value('size', QSize(860, 400)))
        self.move(settings.value('pos', QPoint(200, 200)))

    def _save_settings(self):
        """ Save the user specific settings. """

        settings = QSettings()

        settings.setValue('size', self.size())
        settings.setValue('pos', self.pos())
