# -*- coding: utf-8 -*-
"""
This is nefi's main view. Currently we deployed all controls of the
GUI in the MainView.ui. Static changes to the GUI should always been
done by the Qt designer since this reduces the amount of code dramatically.
To draw the complete UI the controllers are invoked and the draw_ui function is
called
"""
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import qdarkstyle
from settings import *
# cus widgets
import PyQt5.QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets

__authors__ = {"Dennis Groß": "gdennis91@googlemail.com"}

base, form = uic.loadUiType("MainView.ui")


class Foo(QObject):
    # Define a new signal called 'trigger' that has no arguments.
    trigger = pyqtSignal()

    def connect_and_emit_trigger(self):
        # Connect the trigger signal to a slot.
        self.trigger.connect(self.handle_trigger)

        # Emit the signal.
        self.trigger.emit()

    def handle_trigger(self):
        # Show that the slot has been called.

        print("trigger signal received")


class MainView(base, form):
    def __init__(self, parent=None):
        super(base, self).__init__(parent)
        self.setupUi(self)
        self.draw_ui()

    def draw_ui(self):
        """
        This function is concerned with drawing all non static elements  into the
        GUI.
        """

        foo = Foo()
        foo.connect_and_emit_trigger()

        self.set_pip_title("A. Junius2")

        self.set_preset(["A.Junius", "test", "test", "test"])

        pixmap_icon = QtGui.QPixmap("add_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.add_btn.setIcon(q_icon)

        pixmap_icon = QtGui.QPixmap("delete_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.delete_btn.setIcon(q_icon)

        pixmap_icon = QtGui.QPixmap("save_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.save_btn.setIcon(q_icon)

        pixmap_icon = QtGui.QPixmap("new_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.new_btn.setIcon(q_icon)

        self.add_pip_entry("seg_fav_scaled.png", "Preprocessing - adaptive trehsold watershed")
        self.add_pip_entry("seg_fav_scaled.png", "Preprocessing - adaptive trehsold watershed")
        self.add_pip_entry("seg_fav_scaled.png", "Preprocessing - adaptive trehsold watershed")
        self.add_pip_entry("seg_fav_scaled.png", "Preprocessing - adaptive trehsold watershed")
        self.add_pip_entry("seg_fav_scaled.png", "Preprocessing - adaptive trehsold watershed")
        self.add_pip_entry("seg_fav_scaled.png", "Preprocessing - adaptive trehsold watershed")
        self.add_pip_entry("seg_fav_scaled.png", "Preprocessing - adaptive trehsold watershed")
        self.add_pip_entry("seg_fav_scaled.png", "Preprocessing - adaptive trehsold watershed")

        self.add_cat_image("seg_fav.jpeg", "Preprocessing")
        self.add_cat_image("wing.jpeg", "Preprocessing")
        self.add_cat_image("wing.jpeg", "Preprocessing")
        self.add_cat_image("wing.jpeg", "Preprocessing")
        self.add_cat_image("wing.jpeg", "Preprocessing")
        self.add_cat_image("wing.jpeg", "Preprocessing")
        self.add_cat_image("wing.jpeg", "Preprocessing")

        self.main_image_label.setPixmap(QtGui.QPixmap("wing.jpeg"))

        self.setting_widget_vbox_layout.addWidget(ComboBoxWidget("type", ["Please Select",
                                                                          "Preprocessing",
                                                                          "Segmentation",
                                                                          "Graph Detection",
                                                                          "Graph Filtering"]))
        self.setting_widget_vbox_layout.addWidget(ComboBoxWidget("algorithm", ["Please Select",
                                                                               "Otsus",
                                                                               "Guo Hall",
                                                                               "Adaptive Treshold"]))
        self.setting_widget_vbox_layout.addWidget(SliderWidget("slider1", 0, 10, 1, 4, False))
        self.setting_widget_vbox_layout.addWidget(SliderWidget("slider1", 0, 10, 2, 4, False))
        self.setting_widget_vbox_layout.addWidget(SliderWidget("slider1", 0, 10, 1, 4, True))
        self.setting_widget_vbox_layout.addWidget(CheckBoxWidget("checkbox1", True))

    def set_preset(self, options):
        """
        Inserts the options for the preset pipelines. Those are the
        default pipelines.json offered by the nefi project. The default
        jsons are located in the ../assets/json/ folder.

        Args:
            | *options*: a string list with the options.
            | *combobox_ref*:  a reference to the combobox object.
        """
        for item in options:
            self.fav_pips_combo_box.addItem(item)

    def set_pip_title(self, title):
        """
        Sets the title of the current selected pipeline in the ui.

        Args:
            | *title*: the title of the pipeline
            | *label_ref*: the reference to the label.
        """
        self.current_pip_label.setText("Current Pipeline " + title)

    def add_pip_entry(self, icon_url, label):
        """
        this methods creates an entry in the pipeline with a given
        icon and label. On the right side will be a button to delete
        the entry.

        Args:
            | *icon_url*: the url to the pip entry icon
            | *label*: the name of the cat for this entry
            | *parent_vbox_layout*: the parent layout to draw it in
        """
        pip_main_main_widget = QtWidgets.QWidget()
        pip_main_layout = QtWidgets.QHBoxLayout()
        pip_main_main_widget.setLayout(pip_main_layout)

        pixmap = QtGui.QPixmap(icon_url)
        pixmap_scaled_keeping_aspec = pixmap.scaled(30, 30, QtCore.Qt.KeepAspectRatio)
        pixmap_label = QtWidgets.QLabel()
        pixmap_label.setPixmap(pixmap_scaled_keeping_aspec)

        string_label = QtWidgets.QLabel()
        string_label.setText(label)
        string_label.setFixedWidth(210)

        btn = QtWidgets.QPushButton()
        btn.setFixedSize(20, 20)
        pixmap_icon = QtGui.QPixmap("delete_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        btn.setIcon(q_icon)

        pip_main_layout.addWidget(pixmap_label)
        pip_main_layout.addWidget(string_label, Qt.AlignLeft)
        pip_main_layout.addWidget(btn)

        self.pip_widget_vbox_layout.addWidget(pip_main_main_widget)

    def add_cat_image(self, url, image_label):
        """
        Creates an image item in the immediate results group
        (left side of the ui). The image will be displayed inside vertical
        layout inside a fresh widget along with its label.

        Args:
            | *url*: the url to the image
            | *image_label*: the name of the image cat e.g. preprocessing

        """
        # create top level widget and set its layout vertical
        image_vbox_layout = QtWidgets.QVBoxLayout()
        image_widget = LeftCustomWidget()
        image_widget.setLayout(image_vbox_layout)

        # create a pixmap and draw it into a widget with a label
        pixmap = QtGui.QPixmap(url)
        pixmap_scaled_keeping_aspec = pixmap.scaled(290, 200, QtCore.Qt.KeepAspectRatio)
        pixmap_widget = QtWidgets.QWidget()

        pixmap_label = QtWidgets.QLabel(pixmap_widget)
        pixmap_label.setPixmap(pixmap_scaled_keeping_aspec)

        image_widget.set_image_label(self.main_image_label)
        image_widget.set_pixmap(pixmap)

        # create label for the image_label
        label = QtWidgets.QLabel()
        label.setText(image_label)

        # add image and label to the image_widget
        image_vbox_layout.addWidget(label)
        image_vbox_layout.addWidget(pixmap_label)

        # add the image widget to the parents vertical layout
        self.left_scroll_results_vbox_layout.addWidget(image_widget)

    def reset_settings(self):
        """
        deletes all settings widgets.
        """
        for child in self.setting_widget_vbox_layout.children():
            self.setting_widget_vbox_layout.removeWidget(child)

    def set_settings(self, widgets):
        """
        Adds all widgets to for the activated algorithm.
        Args:
            widgets: the widgets to add
        """
        for widget in widgets:
            self.setting_widget_vbox_layout.addWidget(widget)


class PipelineEntry:
    def __init__(self):
        self._algorithm = None
        self._category = None
        self.settings_widgets = []

    def set_algorithm(self, algorithm):
        if algorithm is not None:
            self._algorithm = algorithm
            for int_slider in self._algorithm.integer_sliders:
                slider = SliderWidget(
                    int_slider.lower,
                    int_slider.upper,
                    int_slider.step_size,
                    int_slider.default
                ).textfield.valueChanged.connect()
                slider.valueChanged.connect()
                self.settings_widgets.append(slider)

    def set_category(self, category):
        if category is not None:
            self._category = category


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
    """
    This Widget is used for the entry's in the pipeline of thr right
    GUI panel.
    """
    def __init__(self, parent=None):
        PyQt5.QtWidgets.QWidget.__init__(self, parent)
        self.main_image_label = parent
        self.pixmap = None

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.main_image_label.setPixmap(QtGui.QPixmap(self.pixmap))


class ComboBoxWidget(PyQt5.QtWidgets.QGroupBox):
    """
    This is the combobox widget as it is shown in the settings
    panel of the GUI. It gets initialized with a name and a list
    of string options. Those options refer to a list of strings which can
    be selected in the combobox later.
    With self.valueChanged on can connect a pyqt slot with the
    combobox pyqtSignal.
    """

    def __init__(self, name, options):
        super(ComboBoxWidget, self).__init__()
        self.valueChanged = pyqtSignal()

        # ComboBox itself
        self.combobox = QtWidgets.QComboBox()
        self.combobox.orientationCombo = PyQt5.QtWidgets.QComboBox()
        self.combobox.orientationCombo.addItems(options)

        # Label
        self.label = PyQt5.QtWidgets.QLabel()
        self.label.setText(name + ": ")

        self.SingleCheckBoxLayout = PyQt5.QtWidgets.QGridLayout()
        self.SingleCheckBoxLayout.setAlignment(Qt.AlignLeft)
        self.SingleCheckBoxLayout.addWidget(self.label, 0, 0)
        self.SingleCheckBoxLayout.addWidget(self.combobox, 0, 1)
        self.setLayout(self.SingleCheckBoxLayout)


class CheckBoxWidget(PyQt5.QtWidgets.QGroupBox):
    """
    Thi sis the checkbox widget as it is shown in the GUI.
    The name is the displayed in fron of the checkbox in the GUI and
    the default value is of type boolean.
    With self.valueChanged on can connect a pyqt slot with the
    checkbox pyqtSignal.
    """

    def __init__(self, name, default):
        super(CheckBoxWidget, self).__init__()
        self.valueChanged = pyqtSignal()

        # CheckBox itself
        self.checkbox = PyQt5.QtWidgets.QCheckBox()
        self.checkbox.setEnabled(default)

        # Label
        self.label = PyQt5.QtWidgets.QLabel()
        self.label.setText(name + ": ")

        self.SingleCheckBoxLayout = PyQt5.QtWidgets.QGridLayout()
        self.SingleCheckBoxLayout.setAlignment(Qt.AlignLeft)
        self.SingleCheckBoxLayout.addWidget(self.label, 0, 0)
        self.SingleCheckBoxLayout.addWidget(self.checkbox, 0, 1)
        self.setLayout(self.SingleCheckBoxLayout)


class IntegerSliderWidget(PyQt5.QtWidgets.QGroupBox):
    """
    This is a combined widget for integer slider in the GUI. It
    contains several input fields and a slider itself. By setting
    the constructor value, the complete widget is connected in itself.
    The name will be displayed in front of the widget. lower and upper
    refer to the sliders range, step_size tells the distance of each step
    and default is the preset value in the GUI.
    With self.valueChanged on can connect a pyqt slot with the
    integer slider pyqtSignal.
    """

    def __init__(self, name, lower, upper, step_size, default):
        super(SliderWidget, self).__init__()
        self.valueChanged = pyqtSignal()
        self.lower = lower
        self.upper = upper
        self.step_size = step_size
        self.default = default
        self.name = name
        self.internal_steps = abs(upper - lower / step_size)
        self.slider = create_horizontal_slider(0, self.internal_steps, 1, self.to_internal_coordinate(default)).slider

        textfield = PyQt5.QtWidgets.QSpinBox()
        textfield.setRange(lower, upper)
        textfield.setSingleStep(step_size)
        textfield.setValue(default)

        label = PyQt5.QtWidgets.QLabel()
        label.setText(name + ": ")

        single_slider_layout = PyQt5.QtWidgets.QBoxLayout(PyQt5.QtWidgets.QBoxLayout.LeftToRight)
        single_slider_layout.addWidget(self.label)
        single_slider_layout.addWidget(self.slider)
        single_slider_layout.addWidget(self.textfield)
        self.setLayout(self.SingleSlidersLayout)

        # connect the slots and signals
        textfield.valueChanged.connect(self.textfield_value_changed)
        self.slider.valueChanged.connect(self.slider_value_changed)

    @pyqtSlot(int)
    def textfield_value_changed(self, value):
        """
        This is a pyqt slot used to set the textfield value
        Args:
            | *value*: The new value for the textfield
        """
        self.slider.setValue((self.internal_steps / (self.upper - self.lower)) * (value - self.lower))

    @pyqtSlot(int)
    def slider_value_changed(self, value):
        """
        This is a pyqt slot used to set the slider value
        Args:
            | *value*: The new value for the slider
        """
        self.textfield.setValue(self.lower + (value * (self.upper - self.lower)) / self.internal_steps)


class FloatSliderWidget(PyQt5.QtWidgets.QGroupBox):
    """
    This is a combined widget for float slider in the GUI. It
    contains several input fields and a slider itself. By setting
    the constructor value, the complete widget is connected in itself.
    The name will be displayed in front of the widget. lower and upper
    refer to the sliders range, step_size tells the distance of each step
    and default is the preset value in the GUI.
    With self.valueChanged on can connect a pyqt slot with the
    float slider pyqtSignal.
    """

    def __init__(self, name, lower, upper, step_size, default):
        super(SliderWidget, self).__init__()
        self.valueChanged = pyqtSignal()
        self.lower = lower
        self.upper = upper
        self.step_size = step_size
        self.default = default
        self.name = name
        self.internal_steps = abs(upper - lower / step_size)
        self.slider = create_horizontal_slider(0, self.internal_steps, 1, self.to_internal_coordinate(default)).slider

        textfield = PyQt5.QtWidgets.QDoubleSpinBox()
        textfield.setRange(lower, upper)
        textfield.setSingleStep(step_size)
        textfield.setValue(default)

        label = PyQt5.QtWidgets.QLabel()
        label.setText(name + ": ")

        single_slider_layout = PyQt5.QtWidgets.QBoxLayout(PyQt5.QtWidgets.QBoxLayout.LeftToRight)
        single_slider_layout.addWidget(self.label)
        single_slider_layout.addWidget(self.slider)
        single_slider_layout.addWidget(self.textfield)
        self.setLayout(self.SingleSlidersLayout)

        textfield.valueChanged.connect(self.textfield_value_changed)
        self.slider.valueChanged.connect(self.slider_value_changed)

    @pyqtSlot(float)
    def textfield_value_changed(self, value):
        """
        This is a pyqt slot used to set the textfield value
        Args:
            | *value*: The new value for the textfield
        """
        self.slider.setValue((self.internal_steps / (self.upper - self.lower)) * (value - self.lower))

    @pyqtSlot(float)
    def slider_value_changed(self, value):
        """
        This is a pyqt slot used to set the slider value
        Args:
            | *value*: The new value for the slider
        """
        self.textfield.setValue(self.lower + (value * (self.upper - self.lower)) / self.internal_steps)


@staticmethod
def create_horizontal_slider(lower, upper, step_size, default):
    """
    This method is used by FloatSliderWidget and IntegerSliderWidget to
    create a horizontal slider with the given input arguments.
    Args:
        lower: lower bound of the slider
        upper: upper bound of the slider
        step_size: the size of each slider step
        default: the default value of this slider
    """
    slider = PyQt5.QtWidgets.QSlider(Qt.Horizontal)
    slider.setFocusPolicy(Qt.StrongFocus)
    slider.setTickPosition(PyQt5.QtWidgets.QSlider.TicksBothSides)
    slider.setTickInterval(step_size)
    slider.setRange(lower, upper)
    slider.setSingleStep(step_size)
    slider.setValue(default)
    slider.setPageStep(step_size)
    return slider


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    wnd2 = MainView()
    wnd2.show()

    sys.exit(app.exec_())
