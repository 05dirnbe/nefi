from PyQt5.QtWidgets import QWidget, QHBoxLayout, QMainWindow
from PyQt5.uic.properties import QtGui
from settings import Settings
from templateQt5 import *



class Window(QWidget):
    def __init__(self, pipeline):
        super(Window, self).__init__()

        self.Settings = Settings(pipeline)

        layout = QHBoxLayout()
        layout.addWidget(self.Settings)
        self.setLayout(layout)

        self.setWindowTitle("NEFI 2.0")


class WindowTemplate(QMainWindow):
    def __init__(self, parent=None):
        super(WindowTemplate, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
