
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
