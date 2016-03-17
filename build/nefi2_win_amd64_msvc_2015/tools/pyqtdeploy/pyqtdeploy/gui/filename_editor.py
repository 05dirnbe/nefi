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


from PyQt5.QtCore import pyqtSignal, QDir
from PyQt5.QtWidgets import (QFileDialog, QHBoxLayout, QLineEdit, QStyle,
        QToolButton, QWidget)


class FilenameEditor(QWidget):
    """ A simple file name editor suitable to be added to a layout. Filenames
    are relative to the project if possbile.
    """

    # Emitted when the value should be auto-commited.
    autoCommit = pyqtSignal()

    def __init__(self, caption, directory=False, parent=None, **kwds):
        """ Initialise the editor. """

        super().__init__(parent)

        self._project = None
        self._caption = caption
        self._directory = directory

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        self._line_edit = QLineEdit(**kwds)
        layout.addWidget(self._line_edit)
        self.setFocusProxy(self._line_edit)

        icon = self._line_edit.style().standardIcon(
                QStyle.SP_DirIcon if self._directory else QStyle.SP_FileIcon)

        layout.addWidget(
                QToolButton(icon=icon,
                        whatsThis="Display a dialog from which you can select "
                                "a {0}.".format(
                                        "directory" if self._directory else "file"),
                        clicked=self._browse))

        self.setLayout(layout)

    def set_project(self, project):
        """ Set the project. """

        self._project = project

    def setText(self, text):
        """ Set the text of the embedded QLineEdit. """

        self._line_edit.setText(text)

    def text(self):
        """ Get the text of the embedded QLineEdit. """

        return self._line_edit.text()

    def _browse(self, value):
        """ Invoked when the user clicks on the browse button. """

        orig = default = self._line_edit.text()
        if default != '' and self._project is not None:
            default = self._project.path_from_user(default)

        if self._directory:
            name = QFileDialog.getExistingDirectory(self._line_edit,
                    self._caption, default)
        else:
            name, _ = QFileDialog.getOpenFileName(self._line_edit,
                    self._caption, default)

        if name != '':
            if self._project is not None:
                name = self._project.path_to_user(name)

            if name != orig:
                self._line_edit.setText(name)
                self._line_edit.textEdited.emit(name)
                self.autoCommit.emit()
