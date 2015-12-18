from PyQt5.QtCore import QObject, pyqtSlot, Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QStackedWidget, QSlider, QBoxLayout, QHBoxLayout, QLabel, \
    QSpinBox, QDoubleSpinBox

import algorithm_test


class GroupOfSliders(QGroupBox):
    def __init__(self, algorithm):
        super(GroupOfSliders, self).__init__()

        GroupOfSliderssLayout = QBoxLayout(QBoxLayout.TopToBottom)

        for slider in algorithm.integer_sliders:
            GroupOfSliderssLayout.addWidget(
                    SingleIntegerSlider(slider.name, slider.lower, slider.upper, slider.step_size, slider.default,
                                        False))

        self.setLayout(GroupOfSliderssLayout)


class IntegerTextfield(QSpinBox):
    def __init__(self, lower, upper, step_size, default):
        super(IntegerTextfield, self).__init__()

        # Textfield
        self.textfield = QSpinBox()

        self.textfield.setRange(lower, upper)
        self.textfield.setSingleStep(step_size)
        self.textfield.setValue(2)


class DoubleTextfield(QDoubleSpinBox):
    def __init__(self, lower, upper, step_size, default):
        super(DoubleTextfield, self).__init__()

        # Textfield
        self.textfield = QDoubleSpinBox()

        self.textfield.setRange(lower, upper)
        self.textfield.setSingleStep(step_size)
        self.textfield.setValue(default)


class Slider(QSlider):
    def __init__(self, lower, upper, step_size, default):
        super(Slider, self).__init__()

        self.slider = QSlider(Qt.Horizontal)

        self.slider.setFocusPolicy(Qt.StrongFocus)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setTickInterval(step_size)

        self.slider.setRange(lower, upper)
        self.slider.setSingleStep(step_size)
        self.slider.setValue(default)
        self.slider.setPageStep(step_size)


class SingleIntegerSlider(QGroupBox):
    valueChanged = pyqtSignal()

    def __init__(self, name, lower, upper, step_size, default, float_flag):
        super(SingleIntegerSlider, self).__init__()

        self.internal_lower = 0
        self.internal_upper = (upper - lower) / step_size
        self.offset = lower
        self.factor = (self.internal_upper - self.offset) / upper

        def ExternalCoordinate2InternalCoordinate(self, value):
            return self.factor * value + self.offset

        def InternalCoordinate2ExternalCoordinate(self, value):
            return (value - self.offset) / self.factor

        # Slider itself
        self.slider = Slider(self.internal_lower, self.internal_upper, 1,
                             ExternalCoordinate2InternalCoordinate(self, default)).slider

        # Textfield
        if float_flag:
            self.textfield = DoubleTextfield(lower, upper, step_size,
                                             ExternalCoordinate2InternalCoordinate(self, default)).textfield
        else:
            self.textfield = IntegerTextfield(lower, upper, step_size,
                                              ExternalCoordinate2InternalCoordinate(self, default)).textfield

        # Label
        self.label = QLabel()
        self.label.setText(name + ": ")

        # Connect Textfield with Slider
        def textfield_value_changed(value):
            self.slider.setValue(ExternalCoordinate2InternalCoordinate(self, value))

        def slider_value_changed(value):
            self.textfield.setValue(InternalCoordinate2ExternalCoordinate(self, value))

        self.textfield.valueChanged.connect(textfield_value_changed)
        self.slider.valueChanged.connect(slider_value_changed)

        # self.textfield.setValue(2)

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
