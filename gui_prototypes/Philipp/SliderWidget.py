from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget, QGroupBox, QBoxLayout, QGridLayout, QSlider, QSpinBox, \
    QLabel, QStackedWidget

import algorithm_test


class GuiElement(QGroupBox):
    def __init__(self, algorithm):
        super(GuiElement, self).__init__()

        self.algorithm_sliders = algorithm.integer_sliders
        self.settings = SettingsGroup(algorithm.get_name())

        i = 0

        for item in algorithm.integer_sliders:
            self.settings.add_slider_box(item.name, item.default, item.lower, item.upper, i)
            i += 1
            # textfield = self.horizontal_sliders.add_textfield(item.default, item.lower, item.upper)


# A group of sliders for different algorithm settings
class SettingsGroup(QWidget):
    valueChanged = pyqtSignal(int)

    def __init__(self, title):
        super(SettingsGroup, self).__init__()
        self.settingsLayout = QGroupBox(title)

    # Add a single slider with a textfield and a title
    def add_slider_box(self, name, default, lower, upper, row):
        """

        Args:
            row:
            name:
            default:
            lower:
            upper:

        Returns:
            object:

        """

        slider_box = QGridLayout()

        # Slider itself
        slider = QSlider(Qt.Horizontal)
        slider.setFocusPolicy(Qt.StrongFocus)
        slider.setTickPosition(QSlider.TicksBothSides)
        slider.setRange(lower, upper)
        slider.setValue(default)
        # ?slider.setTickInterval(10)?
        slider.setSingleStep(upper - lower)

        # Textfield
        textfield = QSpinBox()
        textfield.setRange(lower, upper)
        textfield.setSingleStep(1)
        textfield.setValue(default)

        # Label

        label = QLabel()
        label.setText(name + ": ")

        # Connect Textfield with Slider
        textfield.valueChanged.connect(slider.setValue)
        slider.valueChanged.connect(textfield.setValue)

        # Arrange Title, Slider and Textfield on the Box
        slider_box.addWidget(label, row, 0)
        slider_box.addWidget(slider, row, 1)
        slider_box.addWidget(textfield, row, 2)

        self.settingsLayout.setLayout(slider_box)


class Window(QWidget):
    def __init__(self, all_algorithms):
        super(Window, self).__init__()

        self.stackedWidget = QStackedWidget()
        for item in algorithms:
            widget = GuiElement(item)
            self.stackedWidget.addWidget(widget)

        layout = QHBoxLayout()
        layout.addWidget(self.stackedWidget)
        self.setLayout(layout)

        self.setWindowTitle("Algorithm Settings")


if __name__ == '__main__':
    import sys

    algorithms = []
    MyAlgorithm = algorithm_test.MyAlgorithm
    algorithms.append(MyAlgorithm)

    app = QApplication(sys.argv)
    window = Window(algorithms)
    window.show()
    sys.exit(app.exec_())
