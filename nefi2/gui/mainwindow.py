import sys
from PyQt5.QtWidgets import QWidget, QStackedWidget, QApplication, QComboBox, QHBoxLayout

from gui.settings import Settings


class Window(QWidget):
    def __init__(self, pipeline):
        super(Window, self).__init__()

        self.Settings = Settings(pipeline)

        layout = QHBoxLayout()
        layout.addWidget(self.Settings)
        self.setLayout(layout)

        self.setWindowTitle("NEFI 2.0")
