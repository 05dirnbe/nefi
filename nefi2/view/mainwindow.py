from PyQt5.QtWidgets import QWidget, QHBoxLayout, QMainWindow, QLabel
from PyQt5.uic.properties import QtGui
from settings import Settings
from pipeline_order import *
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
    def __init__(self, pipeline):
        super(WindowTemplate, self).__init__()
        self.MainWindow = Ui_MainWindow()
        self.MainWindow.setupUi(self)

        self.Settings = Settings(pipeline)
        self.MainWindow.Settings_layout.addWidget(self.Settings)

        self.PipelinOrder = Ui_Pipeline_order()
        self.PipelinOrder.setupUi(self)
        #self.PipelineOrder = PiplineOrder()
        #self.MainWindow.Pipeline_Order_layout.addWidget(self.PipelineOrder)


class PiplineOrder(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Set up the user interface from Designer.
        self.PipelinOrder = Ui_Pipeline_order()
        self.PipelinOrder.setupUi(self)
        self.label = QLabel()
        self.label.setText("bla")
