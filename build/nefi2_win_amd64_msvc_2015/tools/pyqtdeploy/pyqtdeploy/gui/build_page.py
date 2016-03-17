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
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QAbstractSlider, QCheckBox, QGridLayout,
        QGroupBox, QLabel, QMessageBox, QPlainTextEdit, QPushButton, QSpinBox,
        QVBoxLayout, QWidget)

from ..builder import Builder
from ..message_handler import MessageHandler
from ..user_exception import UserException

from .exception_handlers import handle_user_exception


class BuildPage(QWidget):
    """ The GUI for the build page of a project. """

    # The page's label.
    label = "Build"

    def __init__(self):
        """ Initialise the page. """

        super().__init__()

        self.project = None

        # Create the page's GUI.
        layout = QGridLayout()

        self._log_viewer = QPlainTextEdit(
                whatsThis="This displays the messages generated when building "
                        "the application.",
                readOnly=True)
        layout.addWidget(self._log_viewer, 0, 0, 5, 1)

        build = QPushButton("Build",
                whatsThis="Build the application and optionally run "
                        "<tt>qmake</tt>, <tt>make</tt> and the application "
                        "itself.",
                clicked=self._build)
        layout.addWidget(build, 0, 1)

        optimisation = QGroupBox("Optimisations")
        optimisation_layout = QVBoxLayout()

        self._opt1_button = QCheckBox("No asserts",
                whatsThis="The compiled Python code will not contain any "
                        "<tt>assert</tt> statements.",
                checked=True, stateChanged=self._opt1_changed)
        optimisation_layout.addWidget(self._opt1_button)
        self._opt2_button = QCheckBox("No docstrings",
                whatsThis="The compiled Python code will not contain any "
                        "docstrings.",
                checked=True, stateChanged=self._opt2_changed)
        optimisation_layout.addWidget(self._opt2_button)

        optimisation.setLayout(optimisation_layout)
        layout.addWidget(optimisation, 1, 1)

        options = QGroupBox("Build Options")
        options_layout = QGridLayout()

        self._clean_button = QCheckBox("Clean before building",
                whatsThis="The build directory will be deleted and recreated "
                        "before starting a new build.",
                checked=True)
        options_layout.addWidget(self._clean_button, 0, 0, 1, 2)
        self._verbose_button = QCheckBox("Verbose output",
                whatsThis="Additional messages will be displayed during the "
                        "build process.")
        options_layout.addWidget(self._verbose_button, 1, 0, 1, 2)
        options_layout.addWidget(QLabel("Resource files"), 2, 0)
        self._resources_edit = QSpinBox(
                whatsThis="The number of Qt <tt>.qrc</tt> files that will be "
                        "generated. Increasing this number reduces the size "
                        "of each file meaning <tt>rcc</tt> requires less "
                        "memory.",
                minimum=1)
        options_layout.addWidget(self._resources_edit, 2, 1)

        options.setLayout(options_layout)
        layout.addWidget(options, 2, 1)

        steps = QGroupBox("Additional Build Steps")
        steps_layout = QVBoxLayout()

        self._run_qmake_button = QCheckBox("Run qmake",
                whatsThis="Run <tt>qmake</tt> after successfully generating "
                        "the application code.",
                stateChanged=self._run_qmake_changed)
        steps_layout.addWidget(self._run_qmake_button)
        self._run_make_button = QCheckBox("Run make",
                whatsThis="Run <tt>make</tt> after successfully running "
                        "<tt>qmake</tt>.",
                stateChanged=self._run_make_changed)
        steps_layout.addWidget(self._run_make_button)
        self._run_application_button = QCheckBox("Run application",
                whatsThis="Run the application after successfully running "
                        "<tt>make</tt>.",
                stateChanged=self._run_application_changed)
        steps_layout.addWidget(self._run_application_button)

        steps.setLayout(steps_layout)
        layout.addWidget(steps, 3, 1)

        layout.setRowStretch(4, 1)

        self.setLayout(layout)

    def _build(self, _):
        """ Invoked when the user clicks the build button. """

        project = self.project

        # Check the prerequisites.  Note that we don't disable the button if
        # these are missing because (as they are spread across the GUI) the
        # user would have difficulty knowing what needed fixing.
        if project.python_target_include_dir == '':
            self._missing_prereq("target Python include directory")
            return

        if project.python_target_library == '':
            self._missing_prereq("target Python library")
            return

        logger = LoggingMessageHandler(bool(self._verbose_button.checkState()),
                self._log_viewer)
        builder = Builder(project, logger)

        logger.clear()
        logger.status_message("Generating code...")

        if self._opt2_button.checkState():
            opt = 2
        elif self._opt1_button.checkState():
            opt = 1
        else:
            opt = 0

        nr_resources = self._resources_edit.value()

        try:
            builder.build(opt, nr_resources,
                    clean=bool(self._clean_button.checkState()))
        except UserException as e:
            logger.user_exception(e)
            handle_user_exception(e, self.label, self)
            return

        logger.status_message("Code generation succeeded.")

        if self._run_qmake_button.checkState() != Qt.Unchecked:
            qmake = os.path.expandvars(project.qmake)

            if qmake == '':
                QMessageBox.warning(self, self.label,
                    "qmake cannot be run because its name has not been set.")
            else:
                logger.status_message("Running qmake...")

                try:
                    builder.run([qmake], "qmake failed.", in_build_dir=True)
                except UserException as e:
                    logger.user_exception(e)
                    handle_user_exception(e, self.label, self)
                    return

                logger.status_message("qmake succeeded.")

        if self._run_make_button.checkState() != Qt.Unchecked:
            make = 'nmake' if sys.platform == 'win32' else 'make'

            logger.status_message("Running {0}...".format(make))

            try:
                builder.run([make], "{0} failed.".format(make),
                        in_build_dir=True)
            except UserException as e:
                logger.user_exception(e)
                handle_user_exception(e, self.label, self)
                return

            logger.status_message("{0} succeeded.".format(make))

        if self._run_application_button.checkState() != Qt.Unchecked:
            build_dir = project.path_from_user(project.build_dir)
            exe_name = project.get_executable_basename()

            if sys.platform == 'win32':
                application = build_dir + '/Release/' + exe_name + '.exe'
            elif sys.platform == 'darwin' and project.application_is_bundle:
                application = '/'.join([build_dir, exe_name + '.app',
                        'Contents', 'MacOS', exe_name])
            else:
                application = build_dir + '/' + exe_name

            logger.status_message("Running {0}...".format(exe_name))

            try:
                builder.run([application], "{0} failed.".format(application))
            except UserException as e:
                logger.user_exception(e)
                handle_user_exception(e, self.label, self)
                return

            logger.status_message("{0} succeeded.".format(exe_name))

    def _missing_prereq(self, missing):
        """ Tell the user about a missing prerequisite. """

        QMessageBox.warning(self, self.label,
                "The project cannot be built because the name of the {0} has "
                        "not been set.".format(missing))

    def _opt1_changed(self, state):
        """ Invoked when the user clicks on the no asserts button. """

        if state == Qt.Unchecked:
            self._opt2_button.setCheckState(Qt.Unchecked)

    def _opt2_changed(self, state):
        """ Invoked when the user clicks on the no docstrings button. """

        if state == Qt.Checked:
            self._opt1_button.setCheckState(Qt.Checked)

    def _run_qmake_changed(self, state):
        """ Invoked when the user clicks on the run qmake button. """

        if state == Qt.Unchecked:
            self._run_make_button.setCheckState(Qt.Unchecked)

    def _run_make_changed(self, state):
        """ Invoked when the user clicks on the run make button. """

        if state == Qt.Unchecked:
            self._run_application_button.setCheckState(Qt.Unchecked)
        else:
            self._run_qmake_button.setCheckState(Qt.Checked)

    def _run_application_changed(self, state):
        """ Invoked when the user clicks on the run application button. """

        if state != Qt.Unchecked:
            self._run_make_button.setCheckState(Qt.Checked)


class LoggingMessageHandler(MessageHandler):
    """ A message handler that captures user messages and displays them in a
    widget.
    """

    def __init__(self, verbose, viewer):
        """ Initialise the object. """

        super().__init__(quiet=False, verbose=verbose)

        self._viewer = viewer

        self._default_format = self._viewer.currentCharFormat()

        self._error_format = self._viewer.currentCharFormat()
        self._error_format.setForeground(QColor('#7f0000'))

        self._status_format = self._viewer.currentCharFormat()
        self._status_format.setForeground(QColor('#007f00'))

    def clear(self):
        """ Clear the viewer. """

        self._viewer.setPlainText('')

    def status_message(self, message):
        """ Add a status message to the viewer. """

        self._append_text(message, self._status_format)

    def user_exception(self, e):
        """ Add a user exception to the viewer. """

        self._append_text(e.text, self._error_format)

        if self.verbose and e.detail != '':
            self._append_text(e.detail, self._error_format)

    def message(self, message):
        """ Reimplemented to handle progress messages. """

        self._append_text(message, self._default_format)

    def _append_text(self, text, char_format):
        """ Append text to the viewer using a specific character format. """

        viewer = self._viewer

        viewer.setCurrentCharFormat(char_format)
        viewer.appendPlainText(text)
        viewer.setCurrentCharFormat(self._default_format)

        # Make sure the new text is visible.
        viewer.verticalScrollBar().triggerAction(
                QAbstractSlider.SliderToMaximum)
