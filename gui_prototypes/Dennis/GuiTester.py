from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import (QApplication, QBoxLayout, QCheckBox, QComboBox,
        QDial, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QScrollBar,
        QSlider, QSpinBox, QStackedWidget, QWidget)
import sys

class GuiController(QObject):

    def __init__(self, algorithm):
        self.app = QApplication(sys.argv)
        self.window = Window()
        self.window.show()
        sys.exit(self.app.exec_())

        self.signals = None
        self.window = Window()
        self.horizontal_sliders = self.window.horizontalSliders

        for item in algorithm.integer_sliders:
            slider = self.horizontalSliders.add_slider(item.default, item.lower, item.upper)
            slot = item.set_value
            signal = pyqtSignal()
            slider.connect(signal)
            slider.s


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.horizontalSliders = SlidersGroup()

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.horizontalSliders)

        layout = QHBoxLayout()
        layout.addWidget(self.stackedWidget)
        self.setLayout(layout)

        self.setWindowTitle("Sliders")


class SlidersGroup(QGroupBox):

    valueChanged = pyqtSignal(int)

    def __init__(self, title, parent=None):
        super(SlidersGroup, self).__init__(title, parent)
        slidersLayout = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(slidersLayout)

    def add_slider(self, default, lower, upper):
        slider = QSlider(Qt.Horizontal)
        slider.setFocusPolicy(Qt.StrongFocus)
        slider.setTickPosition(QSlider.TicksBothSides)
        slider.setRange(lower, upper)
        slider.setValue(default)
        slider.setTickInterval(10)
        slider.setSingleStep(1)
        self.slidersLayout.addWidget(slider)
        return slider


