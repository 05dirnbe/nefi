import sys

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import (QApplication, QBoxLayout, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QSlider, QSpinBox, QStackedWidget, QWidget)

from gui_prototypes.Philipp import algorithm_test


class GuiController:
    def __init__(self, algorithm):
        self.app = QApplication(sys.argv)

        self.window = Window(algorithm.get_name() + ":")
        self.algorithm_sliders = SlidersGroup(algorithm.get_name())

        layout = QHBoxLayout()
        layout.addWidget(self.controlsGroup)
        layout.addWidget(self.stackedWidget)
        self.setLayout(layout)

        for item in algorithm.integer_sliders:
            slider = self.algorithm_sliders.add_slider_box(item.name, item.default, item.lower, item.upper)
            # textfield = self.horizontal_sliders.add_textfield(item.default, item.lower, item.upper)

        self.window.show()
        sys.exit(self.app.exec_())
        print
        "test"


class Window(QWidget):
    def __init__(self, title):
        super(Window, self).__init__()

        self.horizontalSliders = SlidersGroup(title)

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.horizontalSliders)

        layout = QHBoxLayout()
        layout.addWidget(self.stackedWidget)
        self.setLayout(layout)

        self.setWindowTitle("Algorithm Settings: ")


class SlidersGroup(QGroupBox):
    valueChanged = pyqtSignal(int)

    def __init__(self, title, parent=None):
        super(SlidersGroup, self).__init__(title, parent)
        self.slidersLayout = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(self.slidersLayout)

    # SliderBox describes a group of a slider, a textfield and a title
    def add_slider_box(self, name, default, lower, upper):

        """

        Args:
            name:
            default:
            lower:
            upper:

        Returns:
            object:

        """

        slider_box = QGroupBox(name)
        slider_box_layout = QGridLayout()

        # Slider itself
        slider = QSlider(Qt.Horizontal)
        slider.setFocusPolicy(Qt.StrongFocus)
        slider.setTickPosition(QSlider.TicksBothSides)
        slider.setRange(lower, upper)
        slider.setValue(default)
        #slider.setTickInterval(10)
        slider.setSingleStep(upper-lower)

        # Textfield
        textfield = QSpinBox()
        textfield.setRange(lower, upper)
        textfield.setSingleStep(1)
        textfield.setValue(default)

        # Label
        title = QLabel("" + name + ": ")

        # Connect Textfield with Slider
        textfield.valueChanged.connect(slider.setValue)
        slider.valueChanged.connect(textfield.setValue)

        # Arrange Title, Slider and Textfield on the Box
        slider_box_layout.addWidget(title, 0, 0)
        slider_box_layout.addWidget(slider, 0, 1)
        slider_box_layout.addWidget(textfield, 0, 2)
        slider_box.setLayout(slider_box_layout)

        return slider_box


MyAlgorithm = algorithm_test.MyAlgorithm
Slider1 = algorithm_test.Slider1
Slider2 = algorithm_test.Slider2
Slider3 = algorithm_test.Slider3
CheckBox1 = algorithm_test.CheckBox1

Controller = GuiController(MyAlgorithm)
