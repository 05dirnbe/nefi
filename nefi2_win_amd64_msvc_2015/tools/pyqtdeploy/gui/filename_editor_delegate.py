# Copyright (c) 2014, Riverbank Computing Limited
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
from PyQt5.QtWidgets import QStyledItemDelegate

from .filename_editor import FilenameEditor


class FilenameEditorDelegate(QStyledItemDelegate):
    """ A delegate to handle the editing of file and directory names in a view.
    """

    def __init__(self, caption, directory=False, **kwds):
        """ Initialise the delegate. """

        super().__init__()

        self._project = None
        self._caption = caption
        self._directory = directory
        self._kwds = kwds

    def set_project(self, project):
        """ Set the project. """

        self._project = project

    def createEditor(self, parent, option, index):
        """ Reimplemented to create the delegated editor. """

        editor = FilenameEditor(self._caption, directory=self._directory,
                parent=parent, **self._kwds)
        editor.set_project(self._project)

        def commit_and_close():
            self.commitData.emit(editor)
            self.closeEditor.emit(editor)

        editor.autoCommit.connect(commit_and_close)

        # Prevent the selected value showing through.
        editor.setAutoFillBackground(True)

        return editor

    def setEditorData(self, editor, index):
        """ Reimplemented to set the delegated editor's value. """

        data = index.data(Qt.EditRole)
        if data is None:
            data = ''

        editor.setText(data)

    def setModelData(self, editor, model, index):
        """ Reimplemented to set the model's value. """

        model.setData(index, editor.text(), Qt.EditRole)
