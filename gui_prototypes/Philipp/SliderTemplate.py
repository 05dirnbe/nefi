from PyQt5.QtCore import QObject, pyqtSlot, Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QStackedWidget, QSlider, QBoxLayout, QHBoxLayout, QLabel, \
    QSpinBox

import algorithm_test


class GroupOfSliders(QGroupBox):
    def __init__(self, algorithm):
        super(GroupOfSliders, self).__init__()

        GroupOfSliderssLayout = QBoxLayout(QBoxLayout.TopToBottom)

        for slider in algorithm.integer_sliders:
            GroupOfSliderssLayout.addWidget(SingleSlider(slider.name, slider.default, slider.lower, slider.upper))

        self.setLayout(GroupOfSliderssLayout)


class SingleSlider(QGroupBox):
    valueChanged = pyqtSignal()

    def __init__(self, name, default, lower, upper):
        super(SingleSlider, self).__init__()

        # Slider itself
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setFocusPolicy(Qt.StrongFocus)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setRange(lower, upper)
        self.slider.setValue(default)
        # ?slider.setTickInterval(10)?
        self.slider.setSingleStep(upper - lower)

        # Textfield
        self.textfield = QSpinBox()
        self.textfield.setRange(lower, upper)
        self.textfield.setSingleStep(1)
        self.textfield.setValue(default)

        # Label
        self.label = QLabel()
        self.label.setText(name + ": ")

        # Connect Textfield with Slider
        self.textfield.valueChanged.connect(self.slider.setValue)
        self.slider.valueChanged.connect(self.textfield.setValue)

        self.SingleSlidersLayout = QBoxLayout(QBoxLayout.LeftToRight)
        self.SingleSlidersLayout.addWidget(self.label)
        self.SingleSlidersLayout.addWidget(self.slider)
        self.SingleSlidersLayout.addWidget(self.textfield)
        self.setLayout(self.SingleSlidersLayout)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(GroupOfSliders(MyAlgorithm))

        layout = QHBoxLayout()
        layout.addWidget(self.stackedWidget)
        self.setLayout(layout)

        self.setWindowTitle(MyAlgorithm.get_name() + " Settings")


if __name__ == '__main__':
    import sys

    algorithms = []
    MyAlgorithm = algorithm_test.MyAlgorithm
    algorithms.append(MyAlgorithm)

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
