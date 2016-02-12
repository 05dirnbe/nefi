from PyQt5.QtCore import QObject, pyqtSlot, Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QStackedWidget, QSlider, QBoxLayout, QHBoxLayout, QLabel, \
    QSpinBox, QDoubleSpinBox, QCheckBox, QFormLayout, QGridLayout, QComboBox

"""
class GroupOfSliders(QGroupBox):
    def __init__(self, algorithm):
        super(GroupOfSliders, self).__init__()

        GroupOfSliderssLayout = QBoxLayout(QBoxLayout.TopToBottom)
        GroupOfSliders.setFixedHeight(self, 300)

        for slider in algorithm.integer_sliders:
            GroupOfSliderssLayout.addWidget(
                SliderWidget(slider.name, slider.lower, slider.upper, slider.step_size, slider.default,
                             False))

        for slider in algorithm.float_sliders:
            GroupOfSliderssLayout.addWidget(
                SliderWidget(slider.name, slider.lower, slider.upper, slider.step_size, slider.default,
                             True))

        for checkbox in algorithm.checkboxes:
            GroupOfSliderssLayout.addWidget(
                CheckBoxWidget(checkbox.name, checkbox.default))

        for dropdown in algorithm.drop_downs:
            GroupOfSliderssLayout.addWidget(
                ComboBoxWidget(dropdown.name, dropdown.options))

        self.setLayout(GroupOfSliderssLayout)
"""

class IntegerTextfield(QSpinBox):
    def __init__(self, lower, upper, step_size, default):
        super(IntegerTextfield, self).__init__()

        # Textfield
        self.textfield = QSpinBox()

        self.textfield.setRange(lower, upper)
        self.textfield.setSingleStep(step_size)
        self.textfield.setValue(default)
        self.textfield.setFixedWidth(75)


class DoubleTextfield(QDoubleSpinBox):
    def __init__(self, lower, upper, step_size, default):
        super(DoubleTextfield, self).__init__()

        # Textfield
        self.textfield = QDoubleSpinBox()

        self.textfield.setRange(lower, upper)
        self.textfield.setSingleStep(step_size)
        self.textfield.setValue(default)
        self.textfield.setFixedWidth(75)


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


class CheckBox(QCheckBox):
    def __init__(self, default):
        super(CheckBox, self).__init__()

        self.checkbox = QCheckBox()
        self.checkbox.setEnabled(default)


class ComboBox(QComboBox):
    def __init__(self, options):
        super(ComboBox, self).__init__()

        self.orientationCombo = QComboBox()
        self.orientationCombo.addItems(options)


class ComboBoxWidget(QGroupBox):
    valueChanged = pyqtSignal()

    def __init__(self, name, options):
        super(ComboBoxWidget, self).__init__()

        # ComboBox itself
        self.combobox = ComboBox(options).orientationCombo

        # Label
        self.label = QLabel()
        self.label.setText(name + ": ")

        self.SingleCheckBoxLayout = QGridLayout()
        self.SingleCheckBoxLayout.setAlignment(Qt.AlignLeft)
        self.SingleCheckBoxLayout.addWidget(self.label, 0, 0)
        self.SingleCheckBoxLayout.addWidget(self.combobox, 0, 1)
        self.setLayout(self.SingleCheckBoxLayout)


class CheckBoxWidget(QGroupBox):
    valueChanged = pyqtSignal()

    def __init__(self, name, default):
        super(CheckBoxWidget, self).__init__()

        # CheckBox itself
        self.checkbox = CheckBox(default).checkbox

        # Label
        self.label = QLabel()
        self.label.setText(name + ": ")

        self.SingleCheckBoxLayout = QGridLayout()
        self.SingleCheckBoxLayout.setAlignment(Qt.AlignLeft)
        self.SingleCheckBoxLayout.addWidget(self.label, 0, 0)
        self.SingleCheckBoxLayout.addWidget(self.checkbox, 0, 1)
        self.setLayout(self.SingleCheckBoxLayout)


class SliderWidget(QGroupBox):
    valueChanged = pyqtSignal()

    def __init__(self, name, lower, upper, step_size, default, float_flag):
        super(SliderWidget, self).__init__()

        self.internal_steps = abs(upper - lower) / step_size

        def to_internal_coordinate(self, value):
            return (self.internal_steps / (upper - lower)) * (value - lower)

        def to_external_coordinate(self, value):
            return lower + (value * (upper - lower)) / self.internal_steps

        # Slider itself
        self.slider = \
            Slider(0, self.internal_steps, 1, to_internal_coordinate(self, default)) \
            .slider

        # Textfield
        if float_flag:
            self.textfield = \
                DoubleTextfield(lower, upper, step_size, default) \
                .textfield
        else:
            self.textfield = \
                IntegerTextfield(lower, upper, step_size, default)\
                .textfield

        # Label
        self.label = QLabel()
        self.label.setText(name + ": ")

        # Connect Textfield with Slider
        def textfield_value_changed(value):
            self.slider.setValue(to_internal_coordinate(self, value))

        def slider_value_changed(value):
            self.textfield.setValue(to_external_coordinate(self, value))

        self.textfield.valueChanged.connect(textfield_value_changed)
        self.slider.valueChanged.connect(slider_value_changed)

        self.SingleSlidersLayout = QBoxLayout(QBoxLayout.LeftToRight)
        self.SingleSlidersLayout.addWidget(self.label)
        self.SingleSlidersLayout.addWidget(self.slider)
        self.SingleSlidersLayout.addWidget(self.textfield)
        self.setLayout(self.SingleSlidersLayout)
        self.setFixedHeight(50)
        self.setFlat(True)


"""class Settings(QWidget):

    Creates a widget with all the sliders and checkboxes for all available algorithms.


    def __init__(self, pipeline):


        Args:
            pipeline (object): 

        super(Settings, self).__init__()

        layout = QBoxLayout(QBoxLayout.TopToBottom)

        self.stackedWidgetAlgorithmsSelect = QStackedWidget()
        self.stackedWidgetAlgorithmsSettings = QStackedWidget()
        self.orientationComboCategories = QComboBox()
        self.orientationComboAlgorithms = dict()
        # print("here")


        for category in pipeline.available_cats:

            print(category)
            self.orientationComboCategories.addItem(category.get_name())
            tmp1 = QComboBox()

            for algorithm in category.available_algs[category.get_name()]:
                tmp1.addItem(algorithm.get_name())
                self.orientationComboAlgorithms[category.get_name()] = tmp1
                self.stackedWidgetAlgorithmsSettings.addWidget(GroupOfSliders(algorithm))

            self.stackedWidgetAlgorithmsSelect.addWidget(tmp1)

        layout.addWidget(self.orientationComboCategories)
        layout.addWidget(self.stackedWidgetAlgorithmsSelect)
        layout.addWidget(self.stackedWidgetAlgorithmsSettings)

        self.orientationComboCategories.activated.connect(self.stackedWidgetAlgorithmsSelect.setCurrentIndex)
        # self.orientationComboCategories.activated.connect(self.stackedWidgetAlgorithmsSettings.setCurrentIndex)
        # self.stackedWidgetAlgorithmsSelect.currentWidget().activated.connect(
        #        self.stackedWidgetAlgorithmsSettings.setCurrentIndex)

        self.setLayout(layout)

"""