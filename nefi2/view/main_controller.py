# -*- coding: utf-8 -*-
"""
This is nefi's main view. Currently we deployed all controls of the
GUI in the MainView.ui. Static changes to the GUI should always been
done by the Qt designer since this reduces the amount of code dramatically.
To draw the complete UI the controllers are invoked and the draw_ui function is
called
"""
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys, os, sys
import qdarkstyle
from PyQt5.QtGui import QIcon
# cus widgets
import PyQt5.QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QBoxLayout, QGroupBox, QSpinBox, QDoubleSpinBox, QSlider, QLabel, QWidget

__authors__ = {"Dennis Groß": "gdennis91@googlemail.com",
               "Philipp Reichert": "prei@me.com"}

base, form = uic.loadUiType("./view/MainView.ui")


class MainView(base, form):
    def __init__(self, pipeline, parent=None):

        super(base, self).__init__(parent)
        self.setupUi(self)
        self.pipeline = pipeline
        self.pip_widgets = []
        self.default_pips = []

        self.draw_ui()
        self.connect_ui()

    def register_observers(self):
        pass

    def connect_ui(self):
        """
        This function connects the ui using signals from the
        ui elements and its method counterparts.
        """
        self.input_btn.clicked.connect(self.set_input_url)
        self.save_btn.clicked.connect(self.save_pipeline)
        self.load_favorite_pipelines()
        self.fav_pips_combo_box.activated.connect(self.select_default_pip)
        self.run_btn.clicked.connect(self.run)
        self.delete_btn.clicked.connect(self.trash_pipeline)

    def draw_ui(self):
        """
        This function draws all additional UI elements. If you want the
        application to display any additional things like a button you can
        either add it in the QtDesigner or declare it here.
        """

        #self.add_pip_entry()

        """
        This function is concerned with drawing all non static elements  into the
        GUI.
        """
        """self.set_pip_title("A. Junius2")

        self.set_preset(["A.Junius", "test", "test", "test"])


        self.add_pip_entry("../assets/images/P.png", "Preprocessing - adaptive trehsold watershed")
        self.add_pip_entry("../assets/images/P.png", "Preprocessing - adaptive trehsold watershed")
        self.add_pip_entry("../assets/images/P.png", "Preprocessing - adaptive trehsold watershed")
        self.add_pip_entry("../assets/images/P.png", "Preprocessing - adaptive trehsold watershed")
        self.add_pip_entry("../assets/images/P.png", "Preprocessing - adaptive trehsold watershed")
        self.add_pip_entry("../assets/images/P.png", "Preprocessing - adaptive trehsold watershed")
        self.add_pip_entry("../assets/images/P.png", "Preprocessing - adaptive trehsold watershed")
        self.add_cat_image("../assets/images/seg_fav.jpeg", "Preprocessing")
        self.add_cat_image("../assets/images/wing.jpeg", "Preprocessing")
        self.add_cat_image("../assets/images/wing.jpeg", "Preprocessing")
        self.add_cat_image("../assets/images/wing.jpeg", "Preprocessing")
        self.add_cat_image("../assets/images/wing.jpeg", "Preprocessing")
        self.add_cat_image("../assets/images/wing.jpeg", "Preprocessing")
        self.add_cat_image("../assets/images/wing.jpeg", "Preprocessing")

        self.main_image_label.setPixmap(QtGui.QPixmap("wing.jpeg"))

        category_combo_box = ComboBoxWidget("type")
        category_combo_box.add_item("Preprocessing", "../assets/images/P.png")
        category_combo_box.add_item("Segmentation", "../assets/images/S.png")
        category_combo_box.add_item("Graph Detection", "../assets/images/D.png")
        category_combo_box.add_item("Graph Filtering", "../assets/images/F.png")

        alg_combo_box = ComboBoxWidget("algorithm")
        alg_combo_box.add_item("Otsus")
        alg_combo_box.add_item("Guo Hall")
        alg_combo_box.add_item("Adaptive Treshold")

        slider_1 = SliderWidget("slider1das", 0, 10, 1, 4, True)
        slider_2 = SliderWidget("slider1", 0, 10, 2, 4, False)
        slider_3 = SliderWidget("sliderböadsad", 0, 10, 1, 4, True)
        slider_4 = SliderWidget("sliderböadsad", 0, 10, 1, 4, True)
        slider_5 = SliderWidget("sliderböadsad", 0, 10, 1, 4, True)
        checkbox_1 = CheckBoxWidget("checkbox1", True)

        self.setting_widget_vbox_layout.addWidget(category_combo_box)
        self.setting_widget_vbox_layout.addWidget(alg_combo_box)
        self.setting_widget_vbox_layout.addWidget(slider_1)
        self.setting_widget_vbox_layout.addWidget(slider_2)
        self.setting_widget_vbox_layout.addWidget(slider_3)
        self.setting_widget_vbox_layout.addWidget(slider_4)
        self.setting_widget_vbox_layout.addWidget(slider_5)
        self.setting_widget_vbox_layout.addWidget(checkbox_1)
        self.setting_widget_vbox_layout.setAlignment(Qt.AlignTop)"""

    def set_pip_title(self, title):
        """
        Sets the title of the current selected pipeline in the ui.

        Args:
            | *title*: the title of the pipeline
            | *label_ref*: the reference to the label.
        """
        self.current_pip_label.setText(title)

    def load_dark_theme(self, application):
        """
        This function is called to load the white theme with
        all its icons for the buttons and the css file.
        Args:
            application: the cureent app instance
        """
        # load buttons
        pixmap_icon = QtGui.QPixmap("./assets/images/add_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.add_btn.setIcon(q_icon)

        pixmap_icon = QtGui.QPixmap("./assets/images/trash_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.delete_btn.setIcon(q_icon)

        pixmap_icon = QtGui.QPixmap("./assets/images/diskette_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.save_btn.setIcon(q_icon)

        pixmap_icon = QtGui.QPixmap("./assets/images/up-arrow_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.input_btn.setIcon(q_icon)

        pixmap_icon = QtGui.QPixmap("./assets/images/folder_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.output_btn.setIcon(q_icon)

    @pyqtSlot(int)
    def select_default_pip(self, index):
        """
        This is the slot for the Pipeline combobox in the ui
        Args:
            index: index of the option currently selected
        """

        # delete current pipeline

        self.trash_pipeline()

        # get url and name
        name, url = self.default_pips[index - 1]

        # parse the json in the model
        self.pipeline.load_pipeline_json(url)

        # set the title
        self.set_pip_title(name)

        # create the widgets
        for i in range(0, len(self.pipeline.executed_cats)):
            alg_widgets = self.load_widgets_from_cat(i, True)
            self.add_pip_entry(i)

            """for widget in alg_widgets:
                self.setting_widget_vbox_layout.addWidget(widget)"""

    def create_pipeline(self):
        pass

    def trash_pipeline(self):
        """
        This method clears the complete pipeline while users clicked the trash
        button.
        """
        # remove all entries in the pipeline list
        print("trash")

        while self.pip_widget_vbox_layout.count():
            child = self.pip_widget_vbox_layout.takeAt(0)
            child.widget().deleteLater()

        # remove the pipeline name
        self.set_pip_title("")

        # remove all entries int the executed_cats of the model pipeline
        for i in self.pipeline.executed_cats:
            del i

        # remove all widgets
        for i in self.pip_widgets:
            del i

    @pyqtSlot()
    def run(self):
        """
        This method runs the the pipeline by calling the process methode
        in pipeline
        """
        self.pipeline.process()

    @pyqtSlot()
    def set_input_url(self):
        """
        This method sets the url for the input image in the pipeline.
        """
        url = QtWidgets.QFileDialog.getOpenFileNames()
        print(url)
        self.custom_line_edit.setText(url[0][0])
        self.pipeline.set_input(url[0][0])

    # todo
    @pyqtSlot()
    def set_output_url(self, url):
        """
        This method sets the url for the output folder in the pipeline.
        Args:
            url: the url to the output folder a user selected in the ui
        """
        self.pipeline.set_output_dir(url)

    def load_favorite_pipelines(self):
        """
        Scans the directory for default pipelines to display all available items
        """
        self.fav_pips_combo_box.addItem("Please Select")

        # scan the directory for default pipelines
        for file in os.listdir("./_default_pipelines"):
            if file.endswith(".json"):
                name = file.split(".")[0]
                url = os.path.abspath("./_default_pipelines" + "/" + file)
                self.default_pips.append([name, url])
                self.fav_pips_combo_box.addItem(name)

    @pyqtSlot()
    def save_pipeline(self):
        """
        Saves the pipeline as a json at the users file system.
        """
        url = str(QtWidgets.QFileDialog.getSaveFileName()[0])

        split_list = url.split("/")
        name = split_list[len(split_list) - 1].split(".")[0]
        del split_list[len(split_list) - 1]
        url = url.replace(name, "")
        self.pipeline.save_pipeline_json(name, url)

    @pyqtSlot(int)
    def remove_pip_entry(self, position):
        """
        Removes the pip entry at the given position in the ui
        Args:
            position: position at which the pip entry gets removed
        """
        # todo check
        # remove at ui
        self.pip_widget_vbox_layout.itemAt(position).widget().setParent(None)

        # remove it settings widgets
        del self.pip_widgets[position]

        # remove in model
        del self.pipeline.executed_cats[position]

    def change_pip_entry_type(self, position, type):
        """
        Changes the type of the pipeline entry. The ui pipeline will then display
        the correct category icon as well as a combobox to select the algorithm type.
        Args:
            position: position of the pipeline entry
            type: the string type of the pipeline entry
        """
        # set in ui
        icon = ""

        # todo not hardcod
        if type == "Preprocessing":
            icon = "./assets/images/P.png"
        elif type == "Segmentation":
            icon = "./assets/images/S.png"
        elif type == "Graph Detection":
            icon = "./assets/images/D.png"
        elif type == "Graph Filtering":
            icon = "./assets/images/F.png"

        pixmap = QtGui.QPixmap(icon)
        pixmap_scaled_keeping_aspec = pixmap.scaled(30, 30, QtCore.Qt.KeepAspectRatio)
        pixmap_label = QtWidgets.QLabel()
        pixmap_label.setPixmap(pixmap_scaled_keeping_aspec)

        string_label = QtWidgets.QLabel()
        string_label.setText(type)
        string_label.setFixedWidth(210)

        # todo settings at the location

        # set in model
        self.pipeline.change_category(type, position)

    def change_pip_entry_alg(self, position, algorithm):
        """
        Changes the selected algorithm of the pipeline entry at the position.
        Afterwards create all widgets for this algorithm instance
        Args:
            position: the position of the pipeline entry
            algorithm: the selected algorithm for this category
        """
        # set in model
        self.pipeline.change_algorithm(algorithm, position)

        # create widgets
        widget_list = self.pip_widgets[position]

        for item in self.load_widgets_from_cat(position, False):
            widget_list.append(item)
            self.setting_widget_vbox_layout.addWidget(item)

    def load_widgets_from_cat(self, position, from_json):
        """
        Extracts all widgets from a single algorithm and returns a list
        of widgets.
        Args:
            alg: the alg instance we extract from

        Returns: a list widgets for this particular alg.

        """

        alg = self.pipeline.executed_cats[position].active_algorithm
        widget_list = []

        if from_json:
            type_widget = ComboBoxWidget("type", [])
            type_widget.add_item("Preprocessing", "./assets/images/P.png")
            type_widget.add_item("Segmentation", "./assets/images/S.png")
            type_widget.add_item("Graph Detection", "./assets/images/D.png")
            type_widget.add_item("Graph Filtering", "./assets/images/F.png")
            widget_list.append(type_widget)

            widget_list.append(ComboBoxWidget("selected alg", self.pipeline.get_algorithm_list(position)))

            widget_list.append(CheckBoxWidget("store result", alg.store_image, alg.set_store_image))

        # create integer sliders
        for slider in alg.integer_sliders:
            slid = SliderWidget(slider.name, slider.lower, slider.upper, slider.step_size, slider.value,
                                slider.set_value, False)
            widget_list.append(slid)

        # create float sliders
        for slider in alg.float_sliders:
            slid = SliderWidget(slider.name, slider.lower, slider.upper, slider.step_size, slider.value,
                                slider.set_value, True)
            widget_list.append(slid)

        # create checkboxes
        for checkbox in alg.checkboxes:
            check = CheckBoxWidget(checkbox.name, checkbox.value, checkbox.set_value)
            widget_list.append(check)

        # create dropdowns
        for combobox in alg.drop_downs:
            combo = ComboBoxWidget(combobox.name, combobox.options, combobox.set_value, combobox.default)
            widget_list.append(combo)

        return widget_list

    def add_pip_entry(self, cat_position=None):
        """
        Creates an blank entry in the ui pipeline since the user still needs to specify
        a type and an algorithm of the category.
        """
        # create an widget that displays the pip entry in the ui
        pip_main_widget = QtWidgets.QWidget()
        pip_main_layout = QtWidgets.QHBoxLayout()
        pip_main_widget.setLayout(pip_main_layout)

        if cat_position is not None:
            cat = self.pipeline.executed_cats[cat_position]
            label = cat.get_name()
            icon = cat.get_icon()

        pixmap = QtGui.QPixmap(icon)
        pixmap_scaled_keeping_aspec = pixmap.scaled(30, 30, QtCore.Qt.KeepAspectRatio)
        pixmap_label = QtWidgets.QLabel()
        pixmap_label.setPixmap(pixmap_scaled_keeping_aspec)

        string_label = QtWidgets.QLabel()
        string_label.setText(label)
        string_label.setFixedWidth(210)

        btn = QtWidgets.QPushButton()
        btn.setFixedSize(20, 20)

        pixmap_icon = QtGui.QPixmap("./assets/images/delete_x_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        btn.setIcon(q_icon)

        #btn.clicked.connect(self.remove_pip_entry(len(self.pip_widget_vbox_layout))) ????

        pip_main_layout.addWidget(pixmap_label)
        pip_main_layout.addWidget(string_label, Qt.AlignLeft)
        pip_main_layout.addWidget(btn)

        self.pip_widget_vbox_layout.addWidget(pip_main_widget)

        # create an dictionary entry at the position of the pip_widget_dictionary
        # todo ordering
        self.pip_widgets.append(
            [ComboBoxWidget("type", ["Preprocessing", "Segmentation", "Graph Detection", "Graph Filtering"])])

        if cat_position is not None:
            name = self.pipeline.executed_cats[cat_position].name
            widgets = self.load_widgets_from_cat(cat_position, True)
            self.pip_widgets.append([name, widgets])
        else:
            # create blank in the model pipeline at the last position
            self.pipeline.new_category(self.pipeline.executed_cats.count() - 1)

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

    def set_settings(self, position):
        """
        Adds all widgets to for the activated algorithm for a specific pip entry.
        Args:
            position: the position in widget list where we can find the widgets
        """
        self.reset_settings()

        for widget in self.pip_widgets[position]:
            self.setting_widget_vbox_layout.addWidget(widget)


class LeftCustomWidget(QWidget):
    """
    this widget is used in the left panel of the GUI. All intermediate
    result images are packed into a LeftCustomWidget and appended to the
    according vbox_layout of the Mainview.ui
    """

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
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
    panel of the GUI. It gets initialized with a name
    With self.valueChanged on can connect a pyqt slot with the
    combobox pyqtSignal.
    """

    def __init__(self, name, options, slot=None, default=None):
        super(ComboBoxWidget, self).__init__()
        self.valueChanged = pyqtSignal()

        # ComboBox itself
        self.combobox = QtWidgets.QComboBox()
        self.combobox.orientationCombo = PyQt5.QtWidgets.QComboBox()
        self.combobox.setFixedWidth(220)

        # Label
        self.label = PyQt5.QtWidgets.QLabel()
        self.label.setText(name + ": ")

        self.SingleCheckBoxLayout = QBoxLayout(QBoxLayout.LeftToRight)
        self.SingleCheckBoxLayout.addWidget(self.label)
        self.SingleCheckBoxLayout.addWidget(self.combobox, Qt.AlignRight)
        self.setLayout(self.SingleCheckBoxLayout)
        self.setFixedHeight(70)
        self.setFlat(True)

        # options
        for i in options:
            self.add_item(i)

        if default is not None:
            self.combobox.setCurrentIndex(self.items.keys().index(default))

        if slot is not None:
            self.combobox.activated().connect(slot)

    def add_item(self, option, image=None):
        """

        Args:
            | *option*: A string option refers to an entry which can be selected in the combobox later.
            | *image*: An optional icon that can be shown combobox.
        """
        if image is None:
            self.combobox.addItem(option)
        else:
            self.combobox.addItem(QIcon(image), option)


class CheckBoxWidget(PyQt5.QtWidgets.QGroupBox):
    """
    Thi sis the checkbox widget as it is shown in the GUI.
    The name is the displayed in fron of the checkbox in the GUI and
    the default value is of type boolean.
    With self.valueChanged on can connect a pyqt slot with the
    checkbox pyqtSignal.
    """

    def __init__(self, name, default, slot):
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
        self.setFixedHeight(70)
        self.setFlat(True)

        self.checkbox.stateChanged.connect(slot)


class SliderWidget(QGroupBox):
    """
    This is a combined widget for a slider in the GUI. It
    contains several input fields and a slider itself. By setting
    the constructor value, the complete widget is connected in itself.
    The name will be displayed in front of the widget. lower and upper
    refer to the sliders range, step_size tells the distance of each step
    and default is the preset value in the GUI.
    The float_flag determines whether the slider should represent float values or not.
    Set float_flag to true if you want to store float values.
    With self.valueChanged on can connect a pyqt slot with the
    float slider pyqtSignal.
    A SliderWidget is built by a Slider, a QLabel and either a DoubleTextfield or an IntegerTextfield.
    """

    def __init__(self, name, lower, upper, step_size, default, slot, float_flag):
        super(SliderWidget, self).__init__()
        self.valueChanged = pyqtSignal()
        self.internal_steps = abs(upper - lower) / step_size

        def to_internal_coordinate(value):
            return (self.internal_steps / (upper - lower)) * (value - lower)

        def to_external_coordinate(value):
            return lower + (value * (upper - lower)) / self.internal_steps

        # Slider itself
        self.slider = \
            Slider(0, self.internal_steps, 1, to_internal_coordinate(default)).slider

        # Textfield
        if float_flag:
            self.textfield = \
                DoubleTextfield(lower, upper, step_size, default).textfield
        else:
            self.textfield = \
                IntegerTextfield(lower, upper, step_size, default).textfield

        # Label
        self.label = QLabel()
        self.label.setText(name + ": ")

        # Connect Textfield with Slider
        def textfield_value_changed(value):
            self.slider.setValue(to_internal_coordinate(value))

        def slider_value_changed(value):
            self.textfield.setValue(to_external_coordinate(value))

        self.textfield.valueChanged.connect(textfield_value_changed)
        self.slider.valueChanged.connect(slider_value_changed)

        self.SingleSlidersLayout = QBoxLayout(QBoxLayout.LeftToRight)
        self.SingleSlidersLayout.addWidget(self.label)
        self.SingleSlidersLayout.addWidget(self.slider)
        self.SingleSlidersLayout.addWidget(self.textfield)
        self.setLayout(self.SingleSlidersLayout)
        self.setFixedHeight(70)
        self.setFlat(True)

        self.textfield.valueChanged.connect(slot)
        self.slider.valueChanged.connect(slot)


class IntegerTextfield(QSpinBox):
    """
    A customized QSpinBox that is used by the SliderWidget to allow users to enter integer values.
    """

    def __init__(self, lower, upper, step_size, default):
        super(IntegerTextfield, self).__init__()

        # Textfield
        self.textfield = QSpinBox()

        self.textfield.setRange(lower, upper)
        self.textfield.setSingleStep(step_size)
        self.textfield.setValue(default)
        self.textfield.setFixedWidth(75)


class DoubleTextfield(QDoubleSpinBox):
    """
    A customized QDoubleSpinBox that is used by the SliderWidget to allow users to enter float values.
    """

    def __init__(self, lower, upper, step_size, default):
        super(DoubleTextfield, self).__init__()

        # Textfield
        self.textfield = QDoubleSpinBox()

        self.textfield.setRange(lower, upper)
        self.textfield.setSingleStep(step_size)
        self.textfield.setValue(default)
        self.textfield.setFixedWidth(75)


class Slider(QSlider):
    """
    A customized QSlider that is used by the SliderWidget to allow users to change a certain setting.
    """

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


if __name__ == '__main__':
    pass
