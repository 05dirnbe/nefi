# -*- coding: utf-8 -*-
"""
This is nefi's main view. Currently we deployed all controls of the
GUI in the MainView.ui. Static changes to the GUI should always been
done by the Qt designer since this reduces the amount of code dramatically.
To draw the complete UI the controllers are invoked and the draw_ui function is
called
"""
from PyQt5 import QtCore, QtGui, QtWidgets, uic, Qt
import sys
import qdarkstyle
from settings import *

__authors__ = {"Dennis Groß": "gdennis91@googlemail.com"}

base, form = uic.loadUiType("MainView.ui")


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
        self.set_pip_title("A. Junius2", self.current_pip_label)

        self.set_preset(["A.Junius", "test", "test", "test"], self.fav_pips_combo_box)

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

        self.add_pip_entry("seg_fav_scaled.png", "Preprocessing - adaptive trehsold watershed",
                           self.pip_widget_vbox_layout)
        self.add_pip_entry("seg_fav_scaled.png", "Preprocessing - adaptive trehsold watershed",
                           self.pip_widget_vbox_layout)
        self.add_pip_entry("seg_fav_scaled.png", "Preprocessing - adaptive trehsold watershed",
                           self.pip_widget_vbox_layout)
        self.add_pip_entry("seg_fav_scaled.png", "Preprocessing - adaptive trehsold watershed",
                           self.pip_widget_vbox_layout)
        self.add_pip_entry("seg_fav_scaled.png", "Preprocessing - adaptive trehsold watershed",
                           self.pip_widget_vbox_layout)
        self.add_pip_entry("seg_fav_scaled.png", "Preprocessing - adaptive trehsold watershed",
                           self.pip_widget_vbox_layout)
        self.add_pip_entry("seg_fav_scaled.png", "Preprocessing - adaptive trehsold watershed",
                           self.pip_widget_vbox_layout)
        self.add_pip_entry("seg_fav_scaled.png", "Preprocessing - adaptive trehsold watershed",
                           self.pip_widget_vbox_layout)

        self.add_cat_image("wing.jpeg", "Preprocessing", self.left_scroll_results_vbox_layout)
        self.add_cat_image("wing.jpeg", "Preprocessing", self.left_scroll_results_vbox_layout)
        self.add_cat_image("wing.jpeg", "Preprocessing", self.left_scroll_results_vbox_layout)
        self.add_cat_image("wing.jpeg", "Preprocessing", self.left_scroll_results_vbox_layout)
        self.add_cat_image("wing.jpeg", "Preprocessing", self.left_scroll_results_vbox_layout)
        self.add_cat_image("wing.jpeg", "Preprocessing", self.left_scroll_results_vbox_layout)
        self.add_cat_image("wing.jpeg", "Preprocessing", self.left_scroll_results_vbox_layout)

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

    @staticmethod
    def set_preset(options, combobox_ref):
        """
        Inserts the options for the preset pipelines. Those are the
        default pipelines.json offered by the nefi project. The default
        jsons are located in the ../assets/json/ folder.

        Args:
            | *options*: a string list with the options.
            | 'combobox_ref*:  a reference to the combobox object.
        """
        for item in options:
            combobox_ref.addItem(item)

    @staticmethod
    def set_pip_title(title, label_ref):
        """
        Sets the title of the current selected pipeline in the ui.

        Args:
            | *title*: the title of the pipeline
            | *label_ref*: the reference to the label.
        """
        label_ref.setText("Current Pipeline " + title)

    @staticmethod
    def add_pip_entry(icon_url, label, parent_vbox_layout):
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

        parent_vbox_layout.addWidget(pip_main_main_widget)

    @staticmethod
    def add_cat_image(url, image_label, parent_vbox_layout):
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
        image_widget = QtWidgets.QWidget()
        image_widget.setLayout(image_vbox_layout)

        # create a pixmap and draw it into a widget with a label
        pixmap = QtGui.QPixmap(url)
        pixmap_scaled_keeping_aspec = pixmap.scaled(290, 200, QtCore.Qt.KeepAspectRatio)
        pixmap_widget = QtWidgets.QWidget()
        pixmap_label = QtWidgets.QLabel(pixmap_widget)
        pixmap_label.setPixmap(pixmap_scaled_keeping_aspec)

        # create label for the image_label
        label = QtWidgets.QLabel()
        label.setText(image_label)

        # add image and label to the image_widget
        image_vbox_layout.addWidget(label)
        image_vbox_layout.addWidget(pixmap_label)

        # add the image widget to the parents vertical layout
        parent_vbox_layout.addWidget(image_widget)


class LeftImageCustomWidget(QtWidgets.QWidget):
    def __init__(self, main_image_label):
        self.main_image_label = main_image_label

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.main_image_label.setPixmap(QtGui.QPixmap(self.pixmap))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    wnd2 = MainView()
    # wnd2.setWindowState(Qt.WindowFullScreen)
    wnd2.show()

    sys.exit(app.exec_())
