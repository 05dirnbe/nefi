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
from PyQt5.QtWidgets import QFormLayout, QWidgetItem


class BetterForm(QFormLayout):
    """ This is an improved QFormLayout.  On OS/X it behaves like other
    platforms and gives extra space to the field widget (going against the OS/X
    guidelines).  It also provides the ability to align the fields of multiple
    forms arranged vertically.
    """

    def __init__(self):
        """ Initialise the layout. """

        super().__init__()

        self.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)

    @classmethod
    def align_forms(cls, *forms):
        """ Align a set of forms. """

        # Find the widest label.
        max_width = 0

        for form in forms:
            # Force the layout to be calculated.
            form.update()
            form.activate()

            for label in cls._get_labels(form):
                width = label.width()
                if max_width < width:
                    max_width = width

        for form in forms:
            alignment = form.labelAlignment() | Qt.AlignVCenter

            for label in cls._get_labels(form):
                label.setMinimumWidth(max_width)
                label.setAlignment(alignment)

    @staticmethod
    def _get_labels(form):
        """ A generator returning the labels of a form. """

        for row in range(form.rowCount()):
            itm = form.itemAt(row, QFormLayout.LabelRole)
            if isinstance(itm, QWidgetItem):
                yield itm.widget()
