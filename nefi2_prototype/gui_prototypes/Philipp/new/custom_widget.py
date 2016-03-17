# -*- coding: utf-8 -*-
"""
This python file contains all custom widgets which are used in Nefi's
GUI implementation. The widgets shown here are heavily used by the controllers.
The main reason for extending the QtWidget class is to override functions to
trigger on events.
"""
import PyQt5.QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets

__authors__ = {"Dennis Groß": "gdennis91@googlemail.com"}


class LeftCustomWidget(QtWidgets.QWidget):
    """
    this widget is used in the left panel of the GUI. All indermediate
    result images are packed into a LeftCustomWidget and appended to the
    according vbox_layout of the Mainview.ui
    """
    def __init__(self, parent=None):
        PyQt5.QtWidgets.QWidget.__init__(self, parent)
        self.main_image_label = parent
        self.pixmap = None

    def set_image_label(self, image_label):
        """
        puts the image label at its place

        Args:
            | *image_label*: the string label of the image e.g. "preprocessing"
        """
        self.main_image_label = image_label

    def set_pixmap(self, pixmap):
        """
        puts the image pixmap on its place

        Args:
            | *pixmap*: the url to the intermediate result
        """
        self.pixmap = pixmap

    def mousePressEvent(self, event):
        """
        this events sets the self.pixmap from this custom widget
        into the middle panel of the GUI. Or more general: by clicking
        on this widget the users wants to see this picture in the big display
        area of the middle.

        Args:
            | *event*: the mouse press event
        """
        if event.button() == QtCore.Qt.LeftButton:
            self.main_image_label.setPixmap(QtGui.QPixmap(self.pixmap))


class PipCustomWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        PyQt5.QtWidgets.QWidget.__init__(self, parent)
        self.main_image_label = parent
        self.pixmap = None

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.main_image_label.setPixmap(QtGui.QPixmap(self.pixmap))


class IntegerTextfield(PyQt5.QtWidgets.QSpinBox):
    def __init__(self, lower, upper, step_size, default):
        super(IntegerTextfield, self).__init__()

        # Textfield
        self.textfield = PyQt5.QtWidgets.QSpinBox()

        self.textfield.setRange(lower, upper)
        self.textfield.setSingleStep(step_size)
        self.textfield.setValue(default)


class DoubleTextfield(PyQt5.QtWidgets.QDoubleSpinBox):
    def __init__(self, lower, upper, step_size, default):
        super(DoubleTextfield, self).__init__()

        # Textfield
        self.textfield = PyQt5.QtWidgets.QDoubleSpinBox()

        self.textfield.setRange(lower, upper)
        self.textfield.setSingleStep(step_size)
        self.textfield.setValue(default)


class Slider(PyQt5.QtWidgets.QSlider):
    def __init__(self, lower, upper, step_size, default):
        super(Slider, self).__init__()

        self.slider = PyQt5.QtWidgets.QSlider(Qt.Horizontal)

        self.slider.setFocusPolicy(Qt.StrongFocus)
        self.slider.setTickPosition(PyQt5.QtWidgets.QSlider.TicksBothSides)
        self.slider.setTickInterval(step_size)

        self.slider.setRange(lower, upper)
        self.slider.setSingleStep(step_size)
        self.slider.setValue(default)
        self.slider.setPageStep(step_size)


class CheckBox(PyQt5.QtWidgets.QCheckBox):
    def __init__(self, default):
        super(CheckBox, self).__init__()

        self.checkbox = PyQt5.QtWidgets.QCheckBox()
        self.checkbox.setEnabled(default)


class ComboBox(PyQt5.QtWidgets.QComboBox):
    def __init__(self, options):
        super(ComboBox, self).__init__()

        self.orientationCombo = PyQt5.QtWidgets.QComboBox()
        self.orientationCombo.addItems(options)


class ComboBoxWidget(PyQt5.QtWidgets.QGroupBox):
    valueChanged = pyqtSignal()

    def __init__(self, name, options):
        super(ComboBoxWidget, self).__init__()

        # ComboBox itself
        self.combobox = ComboBox(options).orientationCombo

        # Label
        self.label = PyQt5.QtWidgets.QLabel()
        self.label.setText(name + ": ")

        self.SingleCheckBoxLayout = PyQt5.QtWidgets.QGridLayout()
        self.SingleCheckBoxLayout.setAlignment(Qt.AlignLeft)
        self.SingleCheckBoxLayout.addWidget(self.label, 0, 0)
        self.SingleCheckBoxLayout.addWidget(self.combobox, 0, 1)
        self.setLayout(self.SingleCheckBoxLayout)


class CheckBoxWidget(PyQt5.QtWidgets.QGroupBox):
    valueChanged = pyqtSignal()

    def __init__(self, name, default):
        super(CheckBoxWidget, self).__init__()

        # CheckBox itself
        self.checkbox = CheckBox(default).checkbox

        # Label
        self.label = PyQt5.QtWidgets.QLabel()
        self.label.setText(name + ": ")

        self.SingleCheckBoxLayout = PyQt5.QtWidgets.QGridLayout()
        self.SingleCheckBoxLayout.setAlignment(Qt.AlignLeft)
        self.SingleCheckBoxLayout.addWidget(self.label, 0, 0)
        self.SingleCheckBoxLayout.addWidget(self.checkbox, 0, 1)
        self.setLayout(self.SingleCheckBoxLayout)


class SliderWidget(PyQt5.QtWidgets.QGroupBox):
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
        self.label = PyQt5.QtWidgets.QLabel()
        self.label.setText(name + ": ")

        # Connect Textfield with Slider
        def textfield_value_changed(value):
            self.slider.setValue(to_internal_coordinate(self, value))

        def slider_value_changed(value):
            self.textfield.setValue(to_external_coordinate(self, value))

        self.textfield.valueChanged.connect(textfield_value_changed)
        self.slider.valueChanged.connect(slider_value_changed)

        self.SingleSlidersLayout = PyQt5.QtWidgets.QBoxLayout(PyQt5.QtWidgets.QBoxLayout.LeftToRight)
        self.SingleSlidersLayout.addWidget(self.label)
        self.SingleSlidersLayout.addWidget(self.slider)
        self.SingleSlidersLayout.addWidget(self.textfield)
        self.setLayout(self.SingleSlidersLayout)
