# -*- coding: utf-8 -*-
"""
This is nefi's main view. Currently we deployed all controls of the
GUI in the MainView.ui. Static changes to the GUI should always been
done by the Qt designer since this reduces the amount of code dramatically.
To draw the complete UI the controllers are invoked and the draw_ui function is
called
"""
import copy

from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys, os, sys
import qdarkstyle
from PyQt5.QtGui import QIcon, QPixmap
# cus widgets
import PyQt5.QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QObject, QEvent
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QBoxLayout, QGroupBox, QSpinBox, QDoubleSpinBox, QSlider, QLabel, QWidget, QHBoxLayout, \
    QVBoxLayout, \
    QStackedWidget, QComboBox, QSizePolicy, QToolButton

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

        self.current_image_original = None
        self.current_image_size = 1.0

        self.q_icon_up = QtGui.QIcon()
        self.q_icon_down = QtGui.QIcon()
        self.q_icon_plus = QtGui.QIcon()
        self.q_icon_plus_grey = QtGui.QIcon()

    def register_observers(self):
        pass

    @pyqtSlot()
    def get_current_image(self, image):
        self.current_image_original = image
        self.resize_default()

    def connect_ui(self):
        """
        This function connects the ui using signals from the
        ui elements and its method counterparts.
        """
        self.input_btn.clicked.connect(self.set_input_url)
        self.output_btn.clicked.connect(self.set_output_url)
        self.save_btn.clicked.connect(self.save_pipeline)
        self.load_favorite_pipelines()
        self.fav_pips_combo_box.activated.connect(self.select_default_pip)
        self.run_btn.clicked.connect(self.run)
        self.delete_btn.clicked.connect(self.trash_pipeline)
        self.add_btn.clicked.connect(lambda: self.add_pipe_entry())
        self.resize.clicked.connect(self.resize_default)
        self.zoom_in.clicked.connect(self.zoom_in_)
        self.zoom_out.clicked.connect(self.zoom_out_)
        self.pip_scroll.verticalScrollBar().rangeChanged.connect(self.scroll_down_pip)

    def draw_ui(self):
        """
        This function draws all additional UI elements. If you want the
        application to display any additional things like a button you can
        either add it in the QtDesigner or declare it here.
        """

        self.ComboxCategories = QComboBox()
        self.stackedWidgetComboxesAlgorithms = QStackedWidget()
        self.select_cat_alg_vbox_layout.addWidget(self.ComboxCategories)
        self.select_cat_alg_vbox_layout.addWidget(self.stackedWidgetComboxesAlgorithms)
        self.ComboxCategories.hide()
        self.pip_widget_vbox_layout.setAlignment(Qt.AlignTop)
        self.select_cat_alg_vbox_layout.setAlignment(Qt.AlignTop)
        self.left_scroll_results_vbox_layout.setAlignment(Qt.AlignTop)

    def disable_plus(self):
        self.add_btn.setEnabled(False)
        self.add_btn.setIcon(self.q_icon_plus_grey)

    def enable_plus(self):
        self.add_btn.setEnabled(True)
        self.add_btn.setIcon(self.q_icon_plus)

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
        pixmap_icon = QtGui.QPixmap("./assets/images/folder_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.open_pip_btn.setIcon(q_icon)

        pixmap_icon = QtGui.QPixmap("./assets/images/man.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.run_btn.setIcon(q_icon)

        pixmap_icon = QtGui.QPixmap("./assets/images/trash_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.delete_btn.setIcon(q_icon)

        pixmap_icon = QtGui.QPixmap("./assets/images/diskette_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.save_btn.setIcon(q_icon)

        pixmap_icon = QtGui.QPixmap("./assets/images/folder_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.input_btn.setIcon(q_icon)

        pixmap_icon = QtGui.QPixmap("./assets/images/folder_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.output_btn.setIcon(q_icon)

        pixmap_icon = QtGui.QPixmap("./assets/images/plus.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.zoom_in.setIcon(q_icon)

        pixmap_icon = QtGui.QPixmap("./assets/images/minus.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.zoom_out.setIcon(q_icon)

        pixmap_icon = QtGui.QPixmap("./assets/images/resize.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.resize.setIcon(q_icon)

        pixmap_up = QtGui.QPixmap("./assets/images/up.png")
        pixmap_down = QtGui.QPixmap("./assets/images/down.png")
        self.q_icon_up = QtGui.QIcon(pixmap_up)
        self.q_icon_down = QtGui.QIcon(pixmap_down)

        pixmap_plus = QtGui.QPixmap("./assets/images/plus.png")
        self.q_icon_plus = QtGui.QIcon(pixmap_plus)
        self.enable_plus()

        pixmap_plus_grey = QtGui.QPixmap("./assets/images/plus_grey.png")
        self.q_icon_plus_grey = QtGui.QIcon(pixmap_plus_grey)


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
        try:
            self.pipeline.load_pipeline_json(url)
        except Exception as e:
            print("failed to load default pip: " + name + " received parser error")
            return

        # set the title
        self.set_pip_title(name)

        # Create an entry in the pipeline widget for every step in the pipeline
        for i in range(0, len(self.pipeline.executed_cats)):
            self.add_pipe_entry(i)

    @pyqtSlot()
    def run(self):
        """
        This method runs the the pipeline by calling the process methode
        in pipeline
        """
        if len(self.pipeline.executed_cats) == 0:
            return

        self.pipeline.set_cache()
        self.clear_left_side_new_run()
        self.pipeline.process()
        self.show_results()

    @pyqtSlot()
    def set_input_url(self):
        """
        This method sets the url for the input image in the pipeline.
        """
        url = QtWidgets.QFileDialog.getOpenFileNames()
        if url[0]:
            # print(url[0])
            # print(url[0][0])
            self.lineEdit.setText(url[0][0])
            self.pipeline.set_input(url[0][0])

            self.clear_left_side_new_image()

            # Add input image to the main panel
            pixmap = QPixmap(url[0][0])
            self.current_image_original = pixmap
            self.current_image_size = 1.0

            self.resize_default()
            # self.main_image_label.setPixmap(pixmap)

            widget = LeftCustomWidget(url[0][0], "Input - Image", 0, self.main_image_label, self.mid_panel,
                                      self.left_scroll_results, self.current_image_original, self.get_current_image)

            self.left_scroll_results_vbox_layout.addWidget(widget)

    @pyqtSlot()
    def set_output_url(self):
        """
        This method sets the url for the output folder in the pipeline.
        Args:
            url: the url to the output folder a user selected in the ui
        """
        url = QtWidgets.QFileDialog.getExistingDirectory()
        if url:
            # print(url)
            # print(url)
            self.custom_line_edit.setText(url)
            self.pipeline.set_output_dir(url)

    def load_favorite_pipelines(self):
        """
        Scans the directory for default pipelines to display all available items
        """
        self.fav_pips_combo_box.addItem("Please Select")

        # scan the directory for default pipelines
        for file in os.listdir("./default_pipelines"):
            if file.endswith(".json"):
                name = file.split(".")[0]
                url = os.path.abspath("./default_pipelines" + "/" + file)
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

    def trash_pipeline(self):
        """
        This method clears the complete pipeline while users clicked the trash
        button.
        """
        # remove all entries in the pipeline list

        while self.pip_widget_vbox_layout.count():
            child = self.pip_widget_vbox_layout.takeAt(0)
            child.widget().deleteLater()

        while self.stackedWidget_Settings.currentWidget() is not None:
            self.stackedWidget_Settings.removeWidget(self.stackedWidget_Settings.currentWidget())
            self.settings_collapsable.setTitle("")

        # remove the pipeline name
        self.set_pip_title("")

        # remove all entries int the executed_cats of the model pipeline
        del self.pipeline.executed_cats[:]

        # remove all widgets
        del self.pip_widgets[:]

        # remove category algorith dropdown
        self.remove_cat_alg_dropdown()

        # remove all entries from the pipeline model

        del self.pipeline.executed_cats[:]

        self.enable_plus()

    def clear_left_side_new_image(self):
        while self.left_scroll_results_vbox_layout.count():
            child = self.left_scroll_results_vbox_layout.takeAt(0)
            child.widget().deleteLater()

    def clear_left_side_new_run(self):
        while self.left_scroll_results_vbox_layout.count() > 1:
            child = self.left_scroll_results_vbox_layout.takeAt(1)
            child.widget().deleteLater()

    @pyqtSlot(int)
    def remove_pip_entry(self, pipe_entry_widget, settings_widget, cat=None):
        """
        Removes the pip entry at the given position in the ui
        Args:
            pipeline_index (object):
            settings_widget:
            position: position at which the pip entry gets removed
        """

        # remove pipeline entry widget from ui
        self.pip_widget_vbox_layout.removeWidget(pipe_entry_widget)
        pipe_entry_widget.deleteLater()

        # remove it settings widgets from ui
        if settings_widget is not None:
            if self.stackedWidget_Settings.currentWidget() == settings_widget:
                self.stackedWidget_Settings.hide()
                self.remove_cat_alg_dropdown()
                self.settings_collapsable.setTitle("Settings")

            self.stackedWidget_Settings.removeWidget(settings_widget)

        # remove in model
        if cat is not None:

            if cat.get_name() == "blank":
                self.enable_plus()

            self.pipeline.delete_category(self.pipeline.get_index(cat))




    def change_pip_entry_alg(self, position, new_category, new_algorithm, pipe_entry_widget, settings_widget):
        """
        Changes the selected algorithm of the pipeline entry at the position.
        Afterwards create all widgets for this algorithm instance
        Args:
            position: the position of the pipeline entry
            algorithm: the selected algorithm for this category
        """
        # print("Position to be changed:" + str(position))
        # print("Pipeline length: " + str(len(self.pipeline.executed_cats)))

        old_cat = self.pipeline.executed_cats[position]
        old_alg = old_cat.active_algorithm
        # print("Old Cat found in pipeline: " + str(old_cat))
        # print("Old Alg: found in pipeline:" + str(old_alg))

        # print("New Category given:" + str(new_category))
        # print("New Algorithm given:" + str(new_algorithm))

        # set in model
        self.pipeline.change_category(new_category, position)
        self.pipeline.change_algorithm(new_algorithm, position)

        new_cat = self.pipeline.executed_cats[position]
        new_alg = new_cat.active_algorithm

        # change settings widgets
        self.remove_pip_entry(pipe_entry_widget, settings_widget)
        (new_pipe_entry_widget, new_settings_widget) = self.add_pipe_entry(position)
        new_pipe_entry_widget.setStyleSheet("background-color:grey;")

        self.stackedWidget_Settings.show()
        self.stackedWidget_Settings.setCurrentIndex(position)
        self.settings_collapsable.setTitle(new_alg.get_name() + " Settings")

        self.remove_cat_alg_dropdown()
        self.create_cat_alg_dropdown(position, new_pipe_entry_widget, new_settings_widget)
        self.set_cat_alg_dropdown(new_cat, new_alg)


        # print("New Cat found in pipeline: " + str(new_cat))
        # print("New Alg found in pipeline: " + str(new_alg))

    def load_settings_widgets_from_pipeline_groupbox(self, position):
        """
        Extracts all widgets from a single algorithm and returns a QBoxLayout
        Args:
            alg: the alg instance we extract from

        Returns: a QBoxLayout containing all widgets for this particular alg.

        """

        alg = self.pipeline.executed_cats[position].active_algorithm

        empty_flag = True

        groupOfSliders = QWidget()
        sp = QSizePolicy()
        sp.setVerticalPolicy(QSizePolicy.Preferred)
        # groupOfSliders.setSizePolicy(sp)
        groupOfSliderssLayout = QBoxLayout(QBoxLayout.TopToBottom)
        groupOfSliderssLayout.setContentsMargins(0, -0, -0, 0)
        groupOfSliderssLayout.setAlignment(Qt.AlignTop)
        groupOfSliderssLayout.setSpacing(0)

        # create integer sliders
        for slider in alg.integer_sliders:
            empty_flag = False
            groupOfSliderssLayout.addWidget(
                SliderWidget(slider.name, slider.lower, slider.upper, slider.step_size, slider.value,
                             slider.set_value, False, alg))

        # create float sliders
        for slider in alg.float_sliders:
            empty_flag = False
            groupOfSliderssLayout.addWidget(
                SliderWidget(slider.name, slider.lower, slider.upper, slider.step_size, slider.value,
                             slider.set_value, True, alg), 0, Qt.AlignTop)

        # create checkboxes
        for checkbox in alg.checkboxes:
            empty_flag = False
            groupOfSliderssLayout.addWidget(CheckBoxWidget(checkbox.name, checkbox.value, checkbox.set_value, alg), 0,
                                            Qt.AlignTop)

        # create dropdowns
        for combobox in alg.drop_downs:
            empty_flag = False
            groupOfSliderssLayout.addWidget(
                ComboBoxWidget(combobox.name, combobox.options, alg, combobox.set_value, combobox.value), 0,
                Qt.AlignTop)

        if empty_flag:
            label = QLabel()
            label.setText("This algorithm has no Settings.")
            groupOfSliderssLayout.addWidget(label, 0, Qt.AlignHCenter)

        groupOfSliders.setLayout(groupOfSliderssLayout)

        return groupOfSliders

    def create_cat_alg_dropdown(self, cat_position, pipe_entry_widget, settings_widget):

        """
        Args:
            last_cat (object):
        """
        layout = self.select_cat_alg_vbox_layout
        cat = self.pipeline.executed_cats[cat_position]

        last_cat = None
        last_cat_name = None

        # Show only allowed categories in dropdown
        if len(self.pipeline.executed_cats) > 1:
            last_cat = self.pipeline.executed_cats[cat_position - 1]
            last_cat_name = last_cat.get_name()

        # Combobox for selecting Category
        self.ComboxCategories.show()
        self.ComboxCategories.setFixedHeight(30)
        self.ComboxCategories.addItem("<Please Select Category>")

        self.stackedWidgetComboxesAlgorithms = QStackedWidget()
        self.stackedWidgetComboxesAlgorithms.setFixedHeight(30)
        self.stackedWidgetComboxesAlgorithms.hide()

        def setCurrentIndexCat(index):
            # print("Set Cat")
            if self.ComboxCategories.currentIndex() == 0:
                self.stackedWidgetComboxesAlgorithms.hide()
            else:
                self.stackedWidgetComboxesAlgorithms.show()
                self.stackedWidgetComboxesAlgorithms.setCurrentIndex(index - 1)

        # *TODO* CHANGE HERE to last_cat_name
        for category_name in self.pipeline.report_available_cats(last_cat_name):

            # Add Category to combobox
            self.ComboxCategories.addItem(category_name)
            tmp1 = QComboBox()
            tmp1.addItem("<Please Select Algorithm>")
            tmp1.setFixedHeight(30)
            category = self.pipeline.get_category(category_name)

            # self.current_index = -1

            def setCurrentIndexAlg(index):
                if self.ComboxCategories.currentIndex() == 0 or self.stackedWidgetComboxesAlgorithms.currentWidget().currentIndex() == 0:
                    pass
                else:
                    if cat.get_name() == "blank":
                        self.enable_plus()
                    self.change_pip_entry_alg(self.pipeline.get_index(cat), self.ComboxCategories.currentText(),
                                              self.stackedWidgetComboxesAlgorithms.currentWidget().currentText(),
                                              pipe_entry_widget, settings_widget)
                    # self.current_index = index

            tmp1.activated.connect(setCurrentIndexAlg)

            for algorithm_name in self.pipeline.get_all_algorithm_list(category):
                tmp1.addItem(algorithm_name)

            self.stackedWidgetComboxesAlgorithms.addWidget(tmp1)

        layout.addWidget(self.ComboxCategories)
        layout.addWidget(self.stackedWidgetComboxesAlgorithms)

        self.ComboxCategories.activated.connect(setCurrentIndexCat)

    def set_cat_alg_dropdown(self, category, algorithm):

        indexC = self.ComboxCategories.findText(category.get_name())
        self.ComboxCategories.setCurrentIndex(indexC)
        self.stackedWidgetComboxesAlgorithms.show()
        self.stackedWidgetComboxesAlgorithms.setCurrentIndex(indexC - 1)
        indexA = self.stackedWidgetComboxesAlgorithms.currentWidget().findText(algorithm.get_name())
        self.stackedWidgetComboxesAlgorithms.currentWidget().setCurrentIndex(indexA)

    def remove_cat_alg_dropdown(self):

        """

        Returns:
            object:
        """
        self.ComboxCategories.clear()

        while self.stackedWidgetComboxesAlgorithms.currentWidget() is not None:
            self.stackedWidgetComboxesAlgorithms.removeWidget(self.stackedWidgetComboxesAlgorithms.currentWidget())

        while self.select_cat_alg_vbox_layout.count():
            child = self.select_cat_alg_vbox_layout.takeAt(0)
            child.widget().hide()

    def scroll_down_pip(self):
        self.pip_scroll.verticalScrollBar().setSliderPosition(self.pip_scroll.verticalScrollBar().maximum() + 100)
        print("Pos: " + str(self.pip_scroll.verticalScrollBar().sliderPosition()))
        print("Max: " + str(self.pip_scroll.verticalScrollBar().maximum()))

    def add_pipe_entry(self, position=None):
        """
            Creates an entry in the ui pipeline with a given position in pipeline.
            It also creates the corresponding settings widget.
            """
        # create an widget that displays the pip entry in the ui and connect the remove button

        pip_main_widget = QWidget()
        pip_main_widget.setFixedHeight(70)
        pip_main_widget.setFixedWidth(300)
        pip_main_layout = QHBoxLayout()
        pip_main_widget.setLayout(pip_main_layout)

        pip_main_widget.setContentsMargins(-28, 0, 0, 0)

        new_marker = False

        if position is None:
            position = len(self.pipeline.executed_cats)
            cat = self.pipeline.new_category(position)
            label = "<Click to specify new step>"
            icon = None
            new_marker = True
        else:
            cat = self.pipeline.executed_cats[position]
            alg = cat.active_algorithm
            label = alg.get_name()
            icon = cat.get_icon()
            new_marker = False

        pixmap_label = QtWidgets.QLabel()

        if not new_marker:
            pixmap = QPixmap(icon)
            pixmap_scaled_keeping_aspec = pixmap.scaled(30, 30, QtCore.Qt.KeepAspectRatio)
            pixmap_label.setPixmap(pixmap_scaled_keeping_aspec)

        pip_up_down = QWidget()
        pip_up_down.setFixedHeight(70)
        pip_up_down_layout = QVBoxLayout()
        pip_up_down.setLayout(pip_up_down_layout)

        pip_up_down.setContentsMargins(17, -17, 0, 0)

        up_btn = QToolButton()
        dw_btn = QToolButton()

        up_btn.setIcon(self.q_icon_up)
        dw_btn.setIcon(self.q_icon_down)

        up_btn.setFixedHeight(25)
        dw_btn.setFixedHeight(25)

        pip_up_down_layout.addWidget(up_btn)
        pip_up_down_layout.addWidget(dw_btn)

        string_label = QLabel()
        string_label.setText(label)
        string_label.setFixedWidth(210)

        btn = QtWidgets.QPushButton()
        btn.setFixedSize(20, 20)

        pixmap_icon = QtGui.QPixmap("./assets/images/delete_x_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        btn.setIcon(q_icon)

        #pip_main_layout.addWidget(pip_up_down, Qt.AlignVCenter)
        pip_main_layout.addWidget(pixmap_label, Qt.AlignVCenter)
        pip_main_layout.addWidget(string_label, Qt.AlignLeft)
        pip_main_layout.addWidget(btn, Qt.AlignRight)

        self.pip_widget_vbox_layout.insertWidget(position, pip_main_widget)

        # Create the corresponding settings widget and connect it
        self.settings_collapsable.setTitle("Settings")
        self.stackedWidget_Settings.hide()
        settings_main_widget = None
        if not new_marker:
            settings_main_widget = self.load_settings_widgets_from_pipeline_groupbox(position)
            self.stackedWidget_Settings.insertWidget(position, settings_main_widget)

        def show_settings():
            # Set background color while widget is selected. Doesn't work because of theme? *TODO*
            pip_main_widget.setStyleSheet("background-color:grey;")

            # Reset background color for all other pipeline entries
            self.reset_pip_backgroundcolor(pip_main_widget)

            if not new_marker:
                self.stackedWidget_Settings.show()
                self.stackedWidget_Settings.setCurrentIndex(self.pipeline.get_index(cat))
                self.settings_collapsable.setTitle(alg.get_name() + " Settings")
            else:
                self.stackedWidget_Settings.hide()

            # Create drop down for cats and algs
            self.remove_cat_alg_dropdown()
            self.create_cat_alg_dropdown(self.pipeline.get_index(cat), pip_main_widget, settings_main_widget)

            if not new_marker:
                self.set_cat_alg_dropdown(cat, alg)

        # Connect Button to remove step from pipeline
        def delete_button_clicked():
            self.remove_cat_alg_dropdown()
            self.remove_pip_entry(pip_main_widget, settings_main_widget, cat)

        def move_up_button_clicked():
            if position == 0 or new_marker:
                pass
            else:
                current_position = self.pipeline.get_index(cat)
                self.swap_pip_entry(current_position - 1, current_position)

        def move_down_button_clicked():
            if position == len(self.pipeline.executed_cats) - 1 or new_marker:
                pass
            else:
                current_position = self.pipeline.get_index(cat)
                if self.pipeline.executed_cats[current_position + 1].get_name() == "blank":
                    pass
                else:
                    self.swap_pip_entry(current_position, current_position + 1)

        def check_move_up_allowed():
            pass

        def check_move_down_allowed():
            pass

        self.clickable(pixmap_label).connect(show_settings)
        self.clickable(string_label).connect(show_settings)
        btn.clicked.connect(delete_button_clicked)
        up_btn.clicked.connect(move_up_button_clicked)
        dw_btn.clicked.connect(move_down_button_clicked)

        # show new settings widget for new step
        if new_marker:
            show_settings()
            self.disable_plus()

        return (pip_main_widget, settings_main_widget)

    def reset_pip_backgroundcolor(self, current_pip_main_widget):
        for i in range(0, self.pip_widget_vbox_layout.count()):
            child = self.pip_widget_vbox_layout.itemAt(i)
            if child.widget() is current_pip_main_widget:
                pass
            else:
                child.widget().setStyleSheet("background-color:None;")

    def swap_pip_entry(self, pos1, pos2):
        """
        Swap two entries in the ui pipeline and the pipeline model
        """

        # print("Swap position "  +str(pos1) + " and " + str(pos2))

        if pos1 == pos2:
            return
        if pos1 < 0 or pos2 < 0:
            return
        if pos1 > len(self.pipeline.executed_cats) or pos2 > len(self.pipeline.executed_cats):
            return

        # Save pipeline model entries
        cat1 = self.pipeline.executed_cats[pos1]
        cat2 = self.pipeline.executed_cats[pos2]

        # Find pipe_entry_widget

        pipe_entry_widget1 = self.pip_widget_vbox_layout.itemAt(pos1).widget()
        pipe_entry_widget2 = self.pip_widget_vbox_layout.itemAt(pos2).widget()

        # Find settings_widget

        settings_widget1 = self.stackedWidget_Settings.widget(pos1)
        settings_widget2 = self.stackedWidget_Settings.widget(pos2)

        # Remove old entries

        self.remove_pip_entry(pipe_entry_widget1, settings_widget1)
        self.remove_pip_entry(pipe_entry_widget2, settings_widget2)

        # Create new entries

        self.pipeline.executed_cats[pos1] = cat2
        self.pipeline.executed_cats[pos2] = cat1

        self.add_pipe_entry(pos1)
        self.add_pipe_entry(pos2)

    def clickable(self, widget):
        """
        Convert any widget to a clickable widget.
        Source -> https://wiki.python.org/moin/PyQt/Making%20non-clickable%20widgets%20clickable
        """

        class Filter(QObject):

            clicked = pyqtSignal()

            def eventFilter(self, obj, event):

                if obj == widget:
                    if event.type() == QEvent.MouseButtonPress:
                        if obj.rect().contains(event.pos()):
                            self.clicked.emit()
                            # The developer can opt for .emit(obj) to get the object within the slot.
                            return True

                return False

        filter = Filter(widget)
        widget.installEventFilter(filter)
        return filter.clicked

    def show_results(self):
        # print("Length Cache: " + str(len(self.pipeline.cache)))

        j = 1
        print("Cache length: " + str(len(self.pipeline.cache)))

        for i in self.pipeline.cache:
            image_path = i[2]
            image_name = (str(i[0]) + " - " + str(i[1]))
            # print(str(image_name))
            # print(str(image_path))

            widget = LeftCustomWidget(image_path, image_name, j, self.main_image_label, self.mid_panel,
                                      self.left_scroll_results, self.current_image_original, self.get_current_image)

            def set_image(image):
                print(str(image))

            # widget.connect(set_image)
            self.left_scroll_results_vbox_layout.addWidget(widget)
            j += 1

    def zoom_out_(self):
        if not self.current_image_original:
            return
        if self.current_image_size < 0.1:
            return
        self.current_image_size = self.current_image_size * 0.85
        pixmap = self.current_image_original.scaled(self.current_image_original.width() * self.current_image_size,
                                                    self.current_image_original.width() * self.current_image_size,
                                                    QtCore.Qt.KeepAspectRatio)
        self.main_image_label.setPixmap(pixmap)

    def zoom_in_(self):
        if not self.current_image_original:
            return
        if self.current_image_size > 3:
            return
        self.current_image_size = self.current_image_size * 1.25
        pixmap = self.current_image_original.scaled(self.current_image_original.width() * self.current_image_size,
                                                    self.current_image_original.width() * self.current_image_size,
                                                    QtCore.Qt.KeepAspectRatio)
        self.main_image_label.setPixmap(pixmap)

    def resize_default(self):
        if not self.current_image_original:
            return
        print(str(self.current_image_original))
        self.current_image_size = self.mid_panel.width()/self.current_image_original.width()
        print(self.current_image_size)
        pixmap = self.current_image_original.scaled(self.mid_panel.width(), self.mid_panel.width(),
                                                    QtCore.Qt.KeepAspectRatio)
        self.main_image_label.setPixmap(pixmap)


class LeftCustomWidget(QWidget):
    """
    this widget is used in the left panel of the GUI. All intermediate
    result images are packed into a LeftCustomWidget and appended to the
    according vbox_layout of the Mainview.ui
    """

    trigger = pyqtSignal()

    def __init__(self, image_path, image_name, step, main_image_label, mid_panel, left_scroll_results, current_image,
                 slot):
        super(LeftCustomWidget, self).__init__()

        self.main_image_label = main_image_label
        self.mid_panel = mid_panel
        self.left_scroll_results = left_scroll_results
        self.image_name = image_name
        self.step = step
        self.current_image = current_image
        self.slot = slot
        # self.setGeometry(0, 0, 300, 100)

        self.LeftCustomWidgetLayout = QVBoxLayout()
        self.setLayout(self.LeftCustomWidgetLayout)
        self.LeftCustomWidgetLayout.setAlignment(Qt.AlignTop)

        self.image_label = QLabel(image_name)
        self.image_label.setGeometry(0, 0, 150, 30)

        self.pixmap = QPixmap(image_path)
        # self.pixmap_scaled_keeping_aspec = self.pixmap.scaled(300, 100, QtCore.Qt.KeepAspectRatio)
        self.pixmap_scaled_keeping_aspec = self.pixmap.scaledToWidth(330, Qt.SmoothTransformation)

        self.image = QLabel()
        self.image.setGeometry(0, 0, 330, self.pixmap_scaled_keeping_aspec.height())
        self.image.setPixmap(self.pixmap_scaled_keeping_aspec)

        self.LeftCustomWidgetLayout.addWidget(self.image_label)
        self.LeftCustomWidgetLayout.addWidget(self.image)

        self.setGeometry(0, 0, 330, self.image_label.height() + self.image.height())

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
            #self.main_image_label.setPixmap(self.pixmap)
            self.mid_panel.setTitle(self.image_name + " - Pipeline Position " + str(self.step))
            self.current_image = self.pixmap

            # Connect the trigger signal to a slot.
            self.trigger.connect(lambda: self.slot(self.current_image))
            # Emit the signal.
            self.trigger.emit()


class ImageWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setScaledContents(True)

    def hasHeightForWidth(self):
        return self.pixmap() is not None

    def heightForWidth(self, w):
        if self.pixmap():
            return int(w * (self.pixmap().height() / self.pixmap().width()))


class PipCustomWidget(QWidget):
    """
    This Widget is used for the entry's in the pipeline of thr right
    GUI panel.
    """

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.main_image_label = parent
        self.pixmap = None

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.main_image_label.setPixmap(QtGui.QPixmap(self.pixmap))


class ComboBoxWidget(QGroupBox):
    """
    This is the combobox widget as it is shown in the settings
    panel of the GUI. It gets initialized with a name
    With self.valueChanged on can connect a pyqt slot with the
    combobox pyqtSignal.
    """

    def __init__(self, name, options, alg, slot=None, default=None):
        super(ComboBoxWidget, self).__init__()
        self.activated = pyqtSignal()

        # ComboBox itself
        self.combobox = QtWidgets.QComboBox()
        self.combobox.orientationCombo = PyQt5.QtWidgets.QComboBox()
        self.combobox.setFixedWidth(220)

        # Label
        self.label = QtWidgets.QLabel()
        self.label.setText(name + ": ")

        self.SingleCheckBoxLayout = QBoxLayout(QBoxLayout.LeftToRight)
        self.SingleCheckBoxLayout.addWidget(self.label)
        self.SingleCheckBoxLayout.addWidget(self.combobox, Qt.AlignRight)
        self.setLayout(self.SingleCheckBoxLayout)
        self.setFixedHeight(70)
        self.setFlat(True)

        def set_modified():
            alg.set_modified()

        # options
        for i in options:
            self.add_item(i)

        if default is not None:
            index = self.combobox.findText(default)
            if index != -1:
                self.combobox.setCurrentIndex(index)

        if slot is not None:
            self.combobox.currentTextChanged.connect(slot)
            self.combobox.currentTextChanged.connect(set_modified)

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


class CheckBoxWidget(QGroupBox):
    """
    Thi sis the checkbox widget as it is shown in the GUI.
    The name is the displayed in fron of the checkbox in the GUI and
    the default value is of type boolean.
    With self.valueChanged on can connect a pyqt slot with the
    checkbox pyqtSignal.
    """

    def __init__(self, name, default, slot, alg):
        super(CheckBoxWidget, self).__init__()
        self.stateChanged = pyqtSignal()

        # CheckBox itself
        self.checkbox = PyQt5.QtWidgets.QCheckBox()
        self.checkbox.setChecked(default)

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

        def set_modified():
            alg.set_modified()

        self.checkbox.stateChanged.connect(slot)
        self.checkbox.stateChanged.connect(set_modified)


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

    def __init__(self, name, lower, upper, step_size, default, slot, float_flag, alg):
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

        def set_modified():
            alg.set_modified()

        self.textfield.valueChanged.connect(textfield_value_changed)
        self.slider.valueChanged.connect(slider_value_changed)

        self.SingleSlidersLayout = QBoxLayout(QBoxLayout.LeftToRight)
        self.SingleSlidersLayout.addWidget(self.label)
        self.SingleSlidersLayout.addWidget(self.slider)
        self.SingleSlidersLayout.addWidget(self.textfield)
        self.setLayout(self.SingleSlidersLayout)
        self.setFixedHeight(70)
        self.setFlat(True)

        self.textfield.valueChanged.connect(lambda: slot(self.textfield.value()))
        self.textfield.valueChanged.connect(set_modified)
        # self.textfield.setValue(default)


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
