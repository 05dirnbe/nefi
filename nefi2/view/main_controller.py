#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is nefi's main view. Currently we deployed all controls of the
GUI in the MainView.ui. Static changes to the GUI should always been
done by the Qt designer since this reduces the amount of code dramatically.
To draw the complete UI the controllers are invoked and the draw_ui function is
called
"""
from nefi2.model.pipeline import *
from nefi2.model.algorithms import _utility
import copy
import time
import os
import traceback

import sys
import zope.event.classhandler
import PyQt5
import webbrowser

from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QKeySequence
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QEvent, QSize, QFile, QTextStream, QIODevice
from PyQt5.QtWidgets import QBoxLayout, QSpinBox, QDoubleSpinBox, QSlider, QLabel, QWidget, QHBoxLayout, \
    QVBoxLayout, QStackedWidget, QComboBox, QSizePolicy, QToolButton, QMenu, QAction, QMessageBox, QApplication, \
    QScrollArea, QFrame, QGridLayout, QSplitter, QCheckBox, QSpacerItem

__authors__ = {"Dennis Groß": "gdennis91@googlemail.com",
               "Philipp Reichert": "prei@me.com"}

try:
    mainview_path = os.path.join('nefi2', 'view', 'MainView.ui')
    base, form = uic.loadUiType(mainview_path)
except (FileNotFoundError):
    raise NameError(os.listdir(os.curdir))


class MainView(base, form):
    scrollsignal = pyqtSignal()

    def __init__(self, pipeline, parent=None):

        super(base, self).__init__(parent)
        self.setupUi(self)

        self.pipeline = pipeline
        self.pip_widgets = []
        self.default_pips = []
        self.active_pip_label = ""
        self.active_immediate_results_group_layout = None
        self.left_panel_resize_flag = True
        self.right_panel_resize_flag = True

        # Current corresponding cat object shown by main view
        self.current_cat = None

        # Cache pipeline entries to use them for settings history.
        self.pipeline_cache = []

        self.autofit = True
        self.autoclear = False
        self.autoscroll = True
        self.resultsonly = False
        self.comparemode = False
        self.MidCustomWidget = MidCustomWidget(self.mid_panel, self.autofit)

        self.q_icon_up = QtGui.QIcon()
        self.q_icon_down = QtGui.QIcon()
        self.q_icon_plus = QtGui.QIcon()
        self.q_icon_plus_grey = QtGui.QIcon()
        self.q_icon_delete = QtGui.QIcon()

        self.thread = ProcessWorker(self.pipeline)
        self.printer = QPrinter()

        self.createActions()
        self.createMenus()
        self.draw_ui()
        self.connect_ui()

    def createMenus(self):
        self.fileMenu = QMenu("&File", self)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.printAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.openPiplineAct)
        self.fileMenu.addAction(self.savePiplineAct)
        self.fileMenu.addSeparator()
        #self.fileMenu.addAction(self.saveGraphAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.runAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.viewMenu = QMenu("&View", self)
        self.viewMenu.addAction(self.zoomInAct)
        self.viewMenu.addAction(self.zoomOutAct)
        self.viewMenu.addAction(self.normalSizeAct)
        self.viewMenu.addSeparator()
        self.viewMenu.addAction(self.fitToWindowAct)
        self.viewMenu.addAction(self.autoScrollAct)
        self.viewMenu.addAction(self.autoClearAct)
        self.viewMenu.addAction(self.resultsOnlyAct)
        self.viewMenu.addAction(self.edgeTransparencyAct)
        self.viewMenu.addSeparator()
        self.viewMenu.addAction(self.fullScreenAct)

        self.helpMenu = QMenu("&Help", self)
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutUsedSoftwareAct)
        self.helpMenu.addAction(self.docsAct)

        self.menuBar().addMenu(self.fileMenu)
        self.menuBar().addMenu(self.viewMenu)
        self.menuBar().addMenu(self.helpMenu)

    def about(self):

        try:
            html_file = os.path.join(os.getcwd(), 'about.html')
            f = QFile(html_file)
            f.open(QIODevice.ReadOnly)
            reader = QTextStream(f)
            reader.setCodec("UTF-8")
            text = reader.readAll()
        except FileNotFoundError:
            print("about.html could not be opened")
            return

        QMessageBox.about(self, "About NEFI 2", text)

    def usedSoftware(self):
        try:
            html_file = os.path.join(os.getcwd(), 'about_software.html')
            f = QFile(html_file)
            f.open(QIODevice.ReadOnly)
            reader = QTextStream(f)
            reader.setCodec("UTF-8")
            text = reader.readAll()
        except FileNotFoundError:
            print("about.html could not be opened")
            return

        QMessageBox.about(self, "About Software", text)

    def open_docs(self):
        index = os.path.join(os.getcwd(), 'nefi2', 'doc', 'documentation',
                             '_build', 'html', 'index.html')
        webbrowser.open('file://' + index)

    def print_(self):

        if self.MidCustomWidget.getCurrentImage() is None:
            return

        dialog = QPrintDialog(self.printer, self)
        if dialog.exec_():
            painter = QPainter(self.printer)
            rect = painter.viewport()
            size = self.MidCustomWidget.getCurrentImage().size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.MidCustomWidget.getCurrentImage().rect())
            painter.drawPixmap(0, 0, self.MidCustomWidget.getCurrentImage())

    def createActions(self):
        self.openAct = QAction("&Open Image", self, shortcut="Ctrl+O",
                               triggered=self.set_input_url)

        self.saveAct = QAction("&Save Image", self, shortcut="Ctrl+S",
                               triggered=self.save_output_picture)

        self.printAct = QAction("&Print Image", self, shortcut="Ctrl+P",
                                enabled=True, triggered=self.print_)

        self.openPiplineAct = QAction("&Open Pipeline", self, shortcut="Ctrl+K",
                                      enabled=True, triggered=self.open_pip_json)

        self.savePiplineAct = QAction("&Save Pipeline", self, shortcut="Ctrl+J",
                                      enabled=True, triggered=self.save_pip_json)

        self.saveGraphAct = QAction("&Save Graph", self, shortcut="Ctrl+G",
                                    enabled=True, triggered=self.save_graph)

        self.exitAct = QAction("E&xit", self, shortcut="Ctrl+Q",
                               triggered=self.close)

        self.runAct = QAction("&Run Pipeline", self, shortcut="Shift+Return",
                              triggered=self.run)

        self.zoomInAct = QAction("Zoom &In (25%)", self, shortcut="Ctrl++",
                                 enabled=True, triggered=self.MidCustomWidget.zoom_in_)

        self.zoomOutAct = QAction("Zoom &Out (25%)", self, shortcut="Ctrl+-",
                                  enabled=True, triggered=self.MidCustomWidget.zoom_out_)

        self.normalSizeAct = QAction("&Normal Size", self, shortcut="Ctrl+D",
                                     enabled=True, triggered=self.MidCustomWidget.resize_original)

        self.fitToWindowAct = QAction("&Fit To Window", self, enabled=True,
                                      checkable=True, checked=True, shortcut="Ctrl+F",
                                      triggered=self.MidCustomWidget.toggleAutofit)
        self.fitToWindowAct.setChecked(True)

        self.autoScrollAct = QAction("&Auto Scroll Results", self, enabled=True,
                                     checkable=True, checked=True, shortcut="Ctrl+B",
                                     triggered=self.set_autoscroll)
        self.autoScrollAct.setChecked(True)

        self.autoClearAct = QAction("&Auto Clear Results", self, enabled=True,
                                    checkable=True, checked=False, shortcut="Ctrl+N",
                                    triggered=self.set_autoclear)

        self.resultsOnlyAct = QAction("&Show Last Result Only", self, enabled=True,
                                      checkable=True, checked=False, shortcut="Ctrl+M",
                                      triggered=self.set_resultsonly)

        self.edgeTransparencyAct = QAction("&Edge Transparency", self, enabled=True,
                                           checkable=True, checked=False, shortcut="Ctrl+T",
                                           triggered=self.toggleEdgeTransparency)
        self.edgeTransparencyAct.setChecked(False)

        self.fullScreenAct = QAction("&Fullscreen Mode", self, enabled=True,
                                     checkable=True, checked=False, shortcut="F11",
                                     triggered=self.toggleFullscreen)
        self.fullScreenAct.setChecked(False)

        self.aboutAct = QAction("&About NEFI", self, triggered=self.about)

        self.aboutUsedSoftwareAct = QAction("About &Used Software", self,
                                            triggered=self.usedSoftware)

        self.docsAct = QAction("&Documentation", self, triggered=self.open_docs)

    def load_dark_theme(self, application):
        """
        This function is called to load the white theme with
        all its icons for the buttons and the css file.
        Args:
            application: the cureent app instance
        """
        # load buttons
        iconpath = os.path.join('nefi2', 'icons', 'close.png')
        pixmap_icon = QtGui.QPixmap(iconpath)
        q_icon = QtGui.QIcon(pixmap_icon)
        self.clear_immediate_btn.setIcon(q_icon)

        iconpath = os.path.join('nefi2', 'icons', 'folder_white.png')
        pixmap_icon = QtGui.QPixmap(iconpath)
        q_icon = QtGui.QIcon(pixmap_icon)
        self.open_pip_btn.setIcon(q_icon)

        iconpath = os.path.join('nefi2', 'icons', 'man.png')
        pixmap_icon = QtGui.QPixmap(iconpath)
        q_icon = QtGui.QIcon(pixmap_icon)
        self.run_btn.setIcon(q_icon)

        iconpath = os.path.join('nefi2', 'icons', 'trash_white.png')
        pixmap_icon = QtGui.QPixmap(iconpath)
        self.q_icon_trash = QtGui.QIcon(pixmap_icon)
        self.delete_btn.setIcon(self.q_icon_trash)

        iconpath = os.path.join('nefi2', 'icons', 'diskette_white.png')
        pixmap_icon = QtGui.QPixmap(iconpath)
        q_icon = QtGui.QIcon(pixmap_icon)
        self.save_btn.setIcon(q_icon)

        iconpath = os.path.join('nefi2', 'icons', 'folder_white.png')
        pixmap_icon = QtGui.QPixmap(iconpath)
        q_icon = QtGui.QIcon(pixmap_icon)
        self.input_btn.setIcon(q_icon)

        iconpath = os.path.join('nefi2', 'icons', 'folder_white.png')
        pixmap_icon = QtGui.QPixmap(iconpath)
        q_icon = QtGui.QIcon(pixmap_icon)
        self.output_btn.setIcon(q_icon)

        iconpath = os.path.join('nefi2', 'icons', 'plus.png')
        pixmap_icon = QtGui.QPixmap(iconpath)
        q_icon = QtGui.QIcon(pixmap_icon)
        self.zoom_in.setIcon(q_icon)

        iconpath = os.path.join('nefi2', 'icons', 'minus.png')
        pixmap_icon = QtGui.QPixmap(iconpath)
        q_icon = QtGui.QIcon(pixmap_icon)
        self.zoom_out.setIcon(q_icon)

        iconpath = os.path.join('nefi2', 'icons', 'resize.png')
        q_icon = QtGui.QIcon(iconpath)
        self.resize.setIcon(q_icon)

        iconpath = os.path.join('nefi2', 'icons', 'up.png')
        pixmap_up = QtGui.QPixmap(iconpath)
        iconpath = os.path.join('nefi2', 'icons', 'down.png')
        pixmap_down = QtGui.QPixmap(iconpath)
        self.q_icon_up = QtGui.QIcon(pixmap_up)
        self.q_icon_down = QtGui.QIcon(pixmap_down)

        iconpath = os.path.join('nefi2', 'icons', 'plus.png')
        pixmap_plus = QtGui.QPixmap(iconpath)
        self.q_icon_plus = QtGui.QIcon(pixmap_plus)
        self.enable_plus()

        iconpath = os.path.join('nefi2', 'icons', 'plus_grey.png')
        pixmap_plus_grey = QtGui.QPixmap(iconpath)
        self.q_icon_plus_grey = QtGui.QIcon(pixmap_plus_grey)

        iconpath = os.path.join('nefi2', 'icons', 'delete_x_white.png')
        pixmap_icon_delete = QtGui.QPixmap(iconpath)
        self.q_icon_delete = QtGui.QIcon(pixmap_icon_delete)

    def draw_ui(self):
        """
        This function draws all additional UI elements. If you want the
        application to display any additional things like a button you can
        either add it in the QtDesigner or declare it here.
        """
        self.setWindowTitle("NEFI 2.0")
        icon = QIcon(os.path.join('nefi2', 'icons', 'nefi2.png'))
        self.setWindowIcon(icon)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.ComboxCategories = QComboBox()
        self.stackedWidgetComboxesAlgorithms = QStackedWidget()
        self.select_cat_alg_vbox_layout.addWidget(self.ComboxCategories)
        self.select_cat_alg_vbox_layout.addWidget(self.stackedWidgetComboxesAlgorithms)
        self.ComboxCategories.hide()
        self.pip_widget_vbox_layout.setAlignment(Qt.AlignTop)
        self.select_cat_alg_vbox_layout.setAlignment(Qt.AlignTop)
        self.left_scroll_results_vbox_layout.setAlignment(Qt.AlignTop)

        self.progress_label = QLabel(self)
        self.progress_label.setGeometry(self.width() / 2 - 200, self.height() / 2 - 20, 400, 20)
        self.progress_label.hide()

        self.progressbar = QtWidgets.QProgressBar(self)
        self.progressbar.setGeometry(self.width() / 2 - 200, self.height() / 2, 400, 30)
        self.progressbar.hide()
        self.mid_panel_layout.addWidget(self.MidCustomWidget)
        self.mid_panel_layout.setContentsMargins(0, 0, 0, 0)

        self.splitterWidget = QWidget()
        self.splitterWidgetLayout = QGridLayout()
        self.splitterWidgetLayout.setContentsMargins(7, 0, 0, 0)
        self.splitterWidget.setLayout(self.splitterWidgetLayout)

        self.splitter = QSplitter()
        self.splitterLayout = QHBoxLayout()
        self.splitterLayout.setSpacing(0)
        self.splitterLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter.setLayout(self.splitterLayout)

        self.splitterFrame = QFrame()
        self.splitterFrame.setFixedHeight(2)
        self.splitterFrame.setFrameShape(QFrame.HLine)
        self.splitterFrame.setFrameShadow(QFrame.Sunken)

        self.splitter.setHandleWidth(0)
        self.splitter.handleWidth()
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setChildrenCollapsible(False)
        # self.pip_collapsable.setStyleSheet("border:0;")
        self.settings_collapsable.setStyleSheet("border:0;")
        self.splitter.addWidget(self.pip_collapsable)
        self.splitterLayout.addWidget(self.splitterFrame)
        self.splitter.addWidget(self.settings_collapsable)

        self.splitterWidgetLayout.addWidget(self.splitter)

        self.verticalLayout_9.addWidget(self.splitterWidget, Qt.AlignHCenter)

        # self.setStyleSheet("QScrollBar:horizontal {max-height: 15px;}" "QScrollBar:vertical {max-width: 15px;}")

        # self.mid_panel.setStyleSheet("border:0;")
        # self.right_panel.setStyleSheet("border:0;")

    def connect_ui(self):
        """
        This function connects the ui using signals from the
        ui elements and its method counterparts.
        """
        # connect pyqt slots with signals
        self.input_btn.clicked.connect(self.set_input_url)
        self.output_btn.clicked.connect(self.set_output_url)
        self.load_favorite_pipelines()
        self.fav_pips_combo_box.activated.connect(self.select_default_pip)
        self.run_btn.clicked.connect(self.run)
        self.delete_btn.clicked.connect(self.trash_pipeline)
        self.add_btn.clicked.connect(lambda: self.add_pipe_entry())
        self.resize.clicked.connect(lambda: self.MidCustomWidget.resize_default(True))
        self.zoom_in.clicked.connect(self.MidCustomWidget.zoom_in_)
        self.zoom_out.clicked.connect(self.MidCustomWidget.zoom_out_)
        self.pip_scroll.verticalScrollBar().rangeChanged.connect(self.scroll_down_pip)
        self.clear_immediate_btn.clicked.connect(self.clear_immediate_results)
        self.thread.progess_changed.connect(self.update_progress)
        self.thread.immediate_results_changed[object, QCheckBox, QToolButton].connect(
            lambda x=object, y=QCheckBox, z=QToolButton: self.update_add_immediate_result(x, y, z))
        self.thread.finished.connect(self.process_finish)
        self.open_pip_btn.clicked.connect(self.open_pip_json)
        self.save_btn.clicked.connect(self.save_pip_json)
        self.auto_clear.toggled.connect(self.set_autoclear)
        self.auto_scroll.toggled.connect(self.set_autoscroll)
        self.thread.finished.connect(self.delay)
        self.scrollsignal.connect(self.scroll_down_left)
        self.results_only.toggled.connect(self.set_resultsonly)
        self.compare_mode.toggled.connect(self.set_comparemode)
        self.btn_resize_left_panel.clicked.connect(self.resize_left_panel)
        self.btn_resize_right_panel.clicked.connect(self.resize_right_panel)
        # not implemented yes
        self.compare_mode.hide()
        self.results_only.hide()
        self.auto_clear.hide()
        self.auto_scroll.hide()

        # connect zope.events
        zope.event.classhandler.handler(ProgressEvent, self.thread.update_progress)
        zope.event.classhandler.handler(CacheAddEvent, self.thread.update_add_immediate_result)
        zope.event.classhandler.handler(CacheRemoveEvent, self.update_remove_immediate_result)
        zope.event.classhandler.handler(CacheInputEvent, self.update_input)

    def back_connect_settings(self, cat, pixmap):

        try:
            pip_entry = self.get_pip_entry(cat)
        except (ValueError):
            print("Pipeline entry has already been deleted.")
            return

        # Show image while settings is selected
        # *TODO* Use pip_entry.findChild(PyQt5.QtWidgets.QLabel, name) instead
        labels = pip_entry.findChildren(PyQt5.QtWidgets.QLabel)

        pixmap_label = labels[0]
        string_label = labels[1]

        def set_image():
            self.MidCustomWidget.setCurrentImage(pixmap)
            #self.MidCustomWidget.resetImageSize()
            self.MidCustomWidget.setPixmap(pixmap)
            self.mid_panel.setTitle(
                str(cat.get_name() + " " + cat.active_algorithm.name) + " - Pipeline Position " + str(
                    self.pipeline.get_index(cat) + 1))

        pixmap_label.trigger.connect(set_image)
        string_label.trigger.connect(set_image)

    @pyqtSlot()
    def get_current_image(self, image, cat=None):
        self.MidCustomWidget.setCurrentImage(image)
        #self.MidCustomWidget.resize_default()

        self.current_cat = cat
        print("Current cat " + str(self.current_cat))

        try:
            pip_entry = self.get_pip_entry(cat)
            settings_widget = self.get_settings_widget(cat)
        except (ValueError):
            self.reset_pip_backgroundcolor()
            self.reset_pip_backgroundcolor()
            self.stackedWidget_Settings.hide()
            self.remove_cat_alg_dropdown()
            self.settings_collapsable.setTitle("Settings")
            return

        # Set background color while widget is selected.
        pip_entry.setStyleSheet("background-color:DarkSlateGrey;")

        # Reset background color for all other pipeline entries
        self.reset_pip_backgroundcolor(pip_entry)

        self.stackedWidget_Settings.show()
        self.stackedWidget_Settings.setCurrentIndex(self.pipeline.get_index(cat))
        self.settings_collapsable.setTitle(cat.active_algorithm.get_name() + " Settings")

        # Create drop down for cats and algs
        self.remove_cat_alg_dropdown()
        self.create_cat_alg_dropdown(self.pipeline.get_index(cat), pip_entry, settings_widget)

        self.set_cat_alg_dropdown(cat, cat.active_algorithm)

    def resizeEvent(self, event=None):
        if self.MidCustomWidget.auto_fit:
            self.progressbar.setGeometry(self.width() / 2 - 200, self.height() / 2, 400, 30)
            self.progress_label.setGeometry(self.width() / 2 - 200, self.height() / 2 - 20, 400, 20)
            self.MidCustomWidget.resize_default()

    def set_autoclear(self):
        self.autoclear = not self.autoclear

    def set_autoscroll(self):
        self.autoscroll = not self.autoscroll

    def set_resultsonly(self):
        self.resultsonly = not self.resultsonly

    def set_comparemode(self):
        self.comparemode = not self.comparemode

    def toggleEdgeTransparency(self):
        _utility.EDGETRANSPARENCY = not _utility.EDGETRANSPARENCY

    def toggleFullscreen(self):
        self.resize_left_panel()
        self.resize_right_panel()

    """
    def keyPressEvent(self, key):
        if key.modifiers() & Qt.ControlModifier:
            self.left_scroll.verticalScrollBar().blockSignals(True)

    def keyReleaseEvent(self, key):
        if Qt.ControlModifier:
            self.left_scroll.verticalScrollBar().blockSignals(False)

    def mousePressEvent(self, key):
        self.left_scroll.verticalScrollBar().blockSignals(True)

    def mouseReleaseEvent(self, key):
        self.left_scroll.verticalScrollBar().blockSignals(False)
    """

    def delay(self):

        from threading import Timer

        def send():
            self.scrollsignal.emit()

        t = Timer(0.01, send)
        t.start()

    def scroll_down_left(self):
        if self.autoscroll:
            self.left_scroll.verticalScrollBar().setSliderPosition(self.left_scroll.verticalScrollBar().maximum() + 100)

    def scroll_down_pip(self):
        self.pip_scroll.verticalScrollBar().setSliderPosition(self.pip_scroll.verticalScrollBar().maximum() + 100)

    def disable_plus(self):
        self.add_btn.setEnabled(False)
        self.add_btn.setIcon(self.q_icon_plus_grey)

    def enable_plus(self):
        self.add_btn.setEnabled(True)
        self.add_btn.setIcon(self.q_icon_plus)

    def disable_pip(self):
        pass

    def enable_pip(self):
        pass

    def resize_left_panel(self):
        self.left_panel_resize_flag = not self.left_panel_resize_flag

        if (self.left_panel_resize_flag):
            self.left_panel.setFixedWidth(350)
            self.btn_resize_left_panel.setText("<")
        else:
            self.left_panel.setFixedWidth(0)
            self.btn_resize_left_panel.setText(">")

    def resize_right_panel(self):
        self.right_panel_resize_flag = not self.right_panel_resize_flag

        if (self.right_panel_resize_flag):
            self.right_panel.setFixedWidth(370)
            self.btn_resize_right_panel.setText(">")
        else:
            self.right_panel.setFixedWidth(0)
            self.btn_resize_right_panel.setText("<")

    def set_pip_title(self, title):
        """
        Sets the title of the current selected pipeline in the ui.

        Args:
            | *title*: the title of the pipeline
            | *label_ref*: the reference to the label.
        """
        self.current_pip_label.setText(title)
        self.active_pip_label = title

    @pyqtSlot()
    def clear_immediate_results(self):
        """
        This method removes all images from the immediate results when
        the user clicked the clear button
        """
        self.clear_left_side_new_run()
        self.pipeline.run_id = 0
        self.pipeline.set_cache()
        self.MidCustomWidget.clearPixmap()


    @pyqtSlot(object)
    def update_progress(self, event):
        """
        This method gets fired by the progress event in the pipeline
        and tells the maincontroller about the actual progress in the
        pipeline
        Args:
            value: the percentage of the progress value
            status_name: the next category being processed
        """
        self.progressbar.setValue(event.value)
        self.progress_label.setText("Calculating " + event.report)

    @pyqtSlot(object)
    def update_remove_immediate_result(self, event):
        """
        This event gets triggered when the pipeline removes something from the
        cache of the model side.
        We remove the accordin widget then also in the ui.
        Args:
            event: the event from the model
        """
        for left_custom in self.left_scroll_results_vbox_layout:
            if left_custom.cat == event.cat:
                del left_custom

    @pyqtSlot(object)
    def update_input(self, event):
        """
        This events tells us that the model loaded a new input image into the cache.
        We also display the new image in the immediate results.
        Args:
            event: the event from the model
        """
        path = event.path

        self.lineEdit.setText(path)
        self.clear_left_side_new_image()

        pixmap = QPixmap(event.path)
        self.MidCustomWidget.setCurrentImage(pixmap)
        self.MidCustomWidget.setPixmap(pixmap)
        settings_widget = None

        widget = LeftCustomWidget(event.path, self.MidCustomWidget, self.mid_panel,
                                  self.left_scroll_results, self.MidCustomWidget.getCurrentImage(),
                                  self.get_current_image, self.pipeline, settings_widget,
                                  self.left_scroll.verticalScrollBar())

        self.left_scroll_results_vbox_layout.addWidget(widget, Qt.AlignTop)

    @pyqtSlot(object)
    def update_add_immediate_result(self, event, checkbox, delete_button):
        """
        This method gets fired when the pipeline computed a fresh
        immediate result.
        Args:
            event: the event from the model
        """

        path = event.path

        pixmap = QPixmap(path)
        self.MidCustomWidget.setCurrentImage(pixmap)
        #self.MidCustomWidget.resetImageSize()
        self.MidCustomWidget.setPixmap(pixmap)
        self.mid_panel.setTitle(
            "Result image - " + str(event.cat.get_name() + " - " + event.cat.active_algorithm.name) + \
            " - Pipeline Position " + str(self.pipeline.get_index(event.cat) + 1))

        self.current_cat = event.cat
        print("Current cat " + str(self.current_cat))

        settings_widget = self.load_settings_widgets_from_pipeline_groupbox(event.cat)

        widget = LeftCustomWidget(path, self.MidCustomWidget, self.mid_panel,
                                  self.left_scroll_results, self.MidCustomWidget.getCurrentImage(),
                                  self.get_current_image,
                                  self.pipeline, settings_widget, self.left_scroll.verticalScrollBar(), event.cat)

        self.active_immediate_results_group_layout.addWidget(widget)
        if self.resultsonly:
            if self.pipeline.get_index(event.cat) is not (len(self.pipeline.executed_cats) - 1):
                widget.hide()

        if self.pipeline.get_index(event.cat) is not (len(self.pipeline.executed_cats) - 1):
            checkbox.toggled.connect(widget.setVisible, Qt.UniqueConnection)

        delete_button.clicked.connect(widget.deleteLater, Qt.UniqueConnection)

        try:
            self.back_connect_settings(event.cat, pixmap)
        except:
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)

    @pyqtSlot()
    def run(self):
        """
        This method runs the the pipeline by calling the process methode
        in pipeline
        """
        signal = pyqtSignal()

        # Check if we have a legal pipeline configuration
        msg, cat = self.pipeline.sanity_check()
        if cat:
            widget = self.get_pip_entry(cat)
            widget.setStyleSheet("background-color:red;")
            widget.setToolTip(msg)
            return

        # Clear left side pictures for auto delete option
        if self.autoclear:
            self.clear_immediate_results()

        # set a timestamp for the current run
        # so the user can distinct between them
        if len(self.pipeline.executed_cats) != 0:

            title = QWidget()

            title.setFixedWidth(315)
            title.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
            titelLayout = QVBoxLayout()
            titelLayout.setAlignment(Qt.AlignLeft)
            titelLayout.setContentsMargins(0, 0, 0, 0)
            titelLayout.setSpacing(7)
            title.setLayout(titelLayout)

            self.active_immediate_results_group_layout = titelLayout

            timestampLayout = QHBoxLayout()
            timestampwidget = QWidget()
            timestampwidget.setLayout(timestampLayout)

            timestamp = QLabel()
            self.pipeline.run_id += 1
            self.pipeline.set_timestamp()
            timestamp.setText(
                self.active_pip_label + " " + str(self.pipeline.get_timestamp()) + ", #" + str(self.pipeline.run_id))
            timestamp.setStyleSheet("font:Candara; font-size: 11pt;")
            timestamp.setContentsMargins(0, 7, 0, 7)

            delete_btn_run = QToolButton()
            delete_btn_run.setIcon(self.q_icon_trash)
            delete_btn_run.setToolTip("Delete this pipeline run.")

            timestampLayout.addWidget(timestamp)
            timestampLayout.addWidget(delete_btn_run, Qt.AlignRight)

            show_pipeline = QCheckBox()
            show_pipeline.setToolTip("Show/Hide intermediate results")

            if self.resultsonly:
                show_pipeline.setChecked(False)
            else:
                show_pipeline.setChecked(True)
            show_pipeline.setText("Intermediate Results")

            show_pipeline.setContentsMargins(0, 0, 0, 0)

            line = QFrame()
            line.setFrameShape(QFrame.HLine)
            line.setFrameShadow(QFrame.Sunken)
            line.setFixedWidth(295)

            titelLayout.addWidget(line)
            titelLayout.addWidget(timestampwidget, Qt.AlignLeft)
            titelLayout.addWidget(show_pipeline, Qt.AlignLeft)
            self.left_scroll_results_vbox_layout.addWidget(title)
            self.right_panel.setEnabled(False)
            self.progress_label.show()
            self.progressbar.show()
            self.thread.setCheckbox(show_pipeline)
            self.thread.setDeleteBtn(delete_btn_run)

            delete_btn_run.clicked.connect(timestamp.deleteLater, Qt.UniqueConnection)
            delete_btn_run.clicked.connect(title.deleteLater, Qt.UniqueConnection)
            delete_btn_run.clicked.connect(show_pipeline.deleteLater, Qt.UniqueConnection)

        try:
            if not self.thread.isRunning():
                self.thread.start()
        except Exception as e:
            print("Process thread crashed")
            traceback.print_exc()

    @pyqtSlot()
    def process_finish(self):
        self.right_panel.setEnabled(True)
        self.progress_label.hide()
        self.progressbar.hide()

    @pyqtSlot(int)
    def select_default_pip(self, index):
        """
        This is the slot for the Pipeline combobox in the ui
        Args:
            index: index of the option currently selected
        """

        if index < 1:
            self.trash_pipeline()
            return

        # delete current pipeline

        self.trash_pipeline()

        # get url and name
        name, url = self.default_pips[index - 1]

        # parse the json in the model
        try:
            self.pipeline.load_pipeline_json(url)
        except Exception as e:
            print("Failed to load default pip: " + name + " received parser error")
            traceback.print_exc()
            return

        # set the title
        self.set_pip_title(name)

        # Create an entry in the pipeline widget for every step in the pipeline
        for i in range(0, len(self.pipeline.executed_cats)):
            self.add_pipe_entry(i)

    def save_graph(self):

        if not self.current_cat:
            return

        graph = self.pipeline.get_cached_graph_by_cat(self.current_cat, self.current_cat.get_run_id())

        if not graph:
            print("Graph not found.")
            return

        url = str(QtWidgets.QFileDialog.getSaveFileName(self, "Save Graph", '', 'Text file (*.txt)')[0])

        try:
            if url[0] and self.current_cat:
                name = os.path.basename(url)
                print(url)
                print(name)
                print("Try to save current graph. Found cat " + str(self.current_cat))
                print("Found graph " + str(id(graph)) + "  Saving it on file system.")
                shutil.copy(graph, url)
        except Exception as e:
            print("Failed to save graph on file system")
            traceback.print_exc()
            return

    @pyqtSlot()
    def save_pip_json(self):
        """
        This method allows the user to save its pip json on the file system
        while clicking the save_btn
        """
        url = str(QtWidgets.QFileDialog.getSaveFileName(self, "Save Pipeline", '')[0])
        try:
            if url[0]:
                name = os.path.basename(url)
                print(url)
                print(name)
                self.pipeline.save_pipeline_json(name, url)
                self.fav_pips_combo_box.setCurrentIndex(0)
        except Exception as e:
            print("Failed to save pip json on file system")
            traceback.print_exc()
            return

        self.set_pip_title(os.path.basename(url))

    @pyqtSlot()
    def open_pip_json(self):
        """
        This method provides the logic for the open_pip_btn which lets the user load a
        pip json from an abritary location of the file system.
        """
        url = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open Pipeline', '',
                                                     'JSON file (*.json)')
        if url[0]:

            # delete current pipeline
            self.trash_pipeline()

            # parse the json in the model
            try:
                self.pipeline.load_pipeline_json(url[0][0])

            except Exception as e:
                print("Failed to load the json at the location: " + url[0][0])
                traceback.print_exc()
                return

            # set the title
            self.set_pip_title(os.path.basename(url[0][0]))

            # Create an entry in the pipeline widget for every step in the pipeline
            for i in range(0, len(self.pipeline.executed_cats)):
                self.add_pipe_entry(i)

    @pyqtSlot()
    def set_input_url(self):
        """
        This method sets the url for the input image in the pipeline.
        """
        url = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open Image', '',
                                                     'Images (*.jpg *.jpeg *.png *.tif *.tiff)')
        if url[0]:

            # reset current pipeline
            self.reset_pipeline()

            self.clear_left_side_new_image()
            self.pipeline.set_input(url[0][0])
            self.mid_panel.setTitle("Input - Image")
            self.pipeline.run_id = 0
            # reset pipelines run

    @pyqtSlot()
    def save_output_picture(self):
        """
        This method sets the url for the input image in the pipeline.
        """

        print(self.MidCustomWidget.getCurrentImage())

        if self.MidCustomWidget.getCurrentImage() is None:
            return

        url = str(QtWidgets.QFileDialog.getSaveFileName(self, "Save Image", '', 'Image file (*.png)')[0])
        try:
            if url[0]:
                name = os.path.basename(url)
                self.MidCustomWidget.getCurrentImage().save(url)
        except Exception as e:
            print("Failed to save image file on file system")
            traceback.print_exc()
            return

    @pyqtSlot()
    def set_output_url(self):
        """
        This method sets the url for the output folder in the pipeline.
        Args:
            url: the url to the output folder a user selected in the ui
        """
        url = QtWidgets.QFileDialog.getExistingDirectory()
        if url:
            self.custom_line_edit.setText(url)
            self.pipeline.set_output_dir(url)

    def cache_pipeline_entries(self, pipeline):
        for i in range(0, len(pipeline.executed_cats)):
            copied_entry = copy.deepcopy(pipeline.executed_cats[i])
            self.pipeline_cache.append(copied_entry)

    def cache_remove_entry(self, entry):
        self.pipeline_cache.remove(entry)

    def cache_clear(self):
        self.pipeline_cache.clear()

    def load_favorite_pipelines(self):
        """
        Scans the directory for default pipelines to display all available items
        """
        self.fav_pips_combo_box.addItem("Please Select")

        # scan the directory for default pipelines
        default_pip = os.path.join('nefi2', 'default_pipelines')
        for pip in os.listdir(default_pip):
            if pip.endswith(".json"):
                name = pip.split(".")[0]
                url = os.path.join('nefi2', 'default_pipelines', pip)
                self.default_pips.append([name, url])
                self.fav_pips_combo_box.addItem(name)

    def reset_pipeline(self):
        """
        This method reset the current pipeline while users loaded a new image
        """

        for idx, cat in enumerate(self.pipeline.executed_cats):
            cat.active_algorithm.set_modified()

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
        new_pipe_entry_widget.setStyleSheet("background-color:DarkSlateGrey;")

        self.stackedWidget_Settings.show()
        self.stackedWidget_Settings.setCurrentIndex(position)
        self.settings_collapsable.setTitle(new_alg.get_name() + " Settings")

        self.remove_cat_alg_dropdown()
        self.create_cat_alg_dropdown(position, new_pipe_entry_widget, new_settings_widget)
        self.set_cat_alg_dropdown(new_cat, new_alg)
        # print("New Cat found in pipeline: " + str(new_cat))
        # print("New Alg found in pipeline: " + str(new_alg))

    def load_settings_widgets_from_pipeline_groupbox(self, cat):
        """
        Extracts all widgets from a single algorithm and returns a QBoxLayout
        Args:
            alg: the alg instance we extract from

        Returns: a QBoxLayout containing all widgets for this particular alg.

        """

        alg = cat.active_algorithm

        empty_flag = True

        groupOfSliders = QWidget()
        sp = QSizePolicy()
        sp.setVerticalPolicy(QSizePolicy.Preferred)
        groupOfSliderssLayout = QBoxLayout(QBoxLayout.TopToBottom)
        groupOfSliderssLayout.setContentsMargins(0, 0, 0, 0)
        groupOfSliderssLayout.setAlignment(Qt.AlignTop)
        groupOfSliderssLayout.setSpacing(0)

        # create integer sliders
        for slider in alg.integer_sliders:
            empty_flag = False
            groupOfSliderssLayout.addWidget(
                SliderWidget(slider.name, slider.lower, slider.upper, slider.step_size, slider.value,
                             slider.set_value, False, alg), 0, Qt.AlignTop)

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
            label.setFixedHeight(30)
            label.setText("This algorithm has no Settings.")
            label.setFixedHeight(50)
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
            last_cat = self.pipeline.executed_cats[cat_position]
            last_cat_name = last_cat.get_name()

        # Combobox for selecting Category
        self.ComboxCategories.show()
        self.ComboxCategories.setFixedHeight(30)
        self.ComboxCategories.addItem("<Please Select Category>")

        self.stackedWidgetComboxesAlgorithms = QStackedWidget()
        self.stackedWidgetComboxesAlgorithms.setFixedHeight(30)
        self.stackedWidgetComboxesAlgorithms.hide()

        def setCurrentIndexCat(index):
            if self.ComboxCategories.currentIndex() == 0:
                self.stackedWidgetComboxesAlgorithms.hide()
            else:
                self.stackedWidgetComboxesAlgorithms.show()
                self.stackedWidgetComboxesAlgorithms.setCurrentIndex(index - 1)

        for category_name in [cat.name for cat in self.pipeline.get_available_cats()]:
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

            tmp1.activated.connect(setCurrentIndexAlg, Qt.UniqueConnection)

            for algorithm_name in self.pipeline.get_all_algorithm_list(category):
                tmp1.addItem(algorithm_name)

            self.stackedWidgetComboxesAlgorithms.addWidget(tmp1)

        # layout.setMaximumHeight(200)
        layout.addWidget(self.ComboxCategories)
        layout.addWidget(self.stackedWidgetComboxesAlgorithms)

        self.ComboxCategories.activated.connect(setCurrentIndexCat, Qt.UniqueConnection)

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

        self.ComboxCategories = QComboBox()
        self.select_cat_alg_vbox_layout.addWidget(self.ComboxCategories)

        while self.stackedWidgetComboxesAlgorithms.currentWidget() is not None:
            self.stackedWidgetComboxesAlgorithms.removeWidget(self.stackedWidgetComboxesAlgorithms.currentWidget())

        while self.select_cat_alg_vbox_layout.count():
            child = self.select_cat_alg_vbox_layout.takeAt(0)
            child.widget().hide()

    def add_pipe_entry(self, position=None):
        """
            Creates an entry in the ui pipeline with a given position in pipeline.
            It also creates the corresponding settings widget.
            """
        # create an widget that displays the pip entry in the ui and connect the remove button

        pip_main_widget = QWidget()
        pip_main_widget.setFixedWidth(350)
        pip_main_widget.setFixedHeight(50)
        hbox_layout = QHBoxLayout()
        hbox_layout.setAlignment(Qt.AlignLeft)
        hbox_layout.setAlignment(Qt.AlignVCenter)
        hbox_layout.setContentsMargins(7, 0, 16, 0)
        pip_main_widget.setLayout(hbox_layout)

        new_marker = False

        if position is None:
            position = len(self.pipeline.executed_cats)
            cat = self.pipeline.new_category(position)
            label = "<Specify new step to continue>"
            icon = None
            new_marker = True
        else:
            cat = self.pipeline.executed_cats[position]
            alg = cat.active_algorithm
            label = alg.get_name()
            icon = cat.get_icon()
            new_marker = False

        pixmap_label = ClickableQLabel()

        pixmap_label.setFixedHeight(50)
        pixmap_label.setFixedWidth(50)

        pip_up_down = QWidget()
        pip_up_down.setFixedHeight(30)
        pip_up_down.setFixedWidth(30)
        pip_up_down_layout = QVBoxLayout()
        pip_up_down_layout.setAlignment(Qt.AlignLeft)
        pip_up_down.setLayout(pip_up_down_layout)

        pip_up_down.setContentsMargins(-13, -11, 0, 0)

        up_btn = QToolButton()
        up_btn.setStyleSheet("border:0;")
        dw_btn = QToolButton()
        dw_btn.setStyleSheet("border:0;")

        up_btn.setIcon(self.q_icon_up)
        dw_btn.setIcon(self.q_icon_down)

        up_btn.setFixedHeight(20)
        dw_btn.setFixedHeight(20)

        pip_up_down_layout.addWidget(up_btn)
        pip_up_down_layout.addWidget(dw_btn)

        if not new_marker:
            hbox_layout.addWidget(pip_up_down, Qt.AlignVCenter)
            pixmap_icon = QPixmap(icon)
            pixmap_scaled_keeping_aspec = pixmap_icon.scaled(30, 30, QtCore.Qt.KeepAspectRatio)
            pixmap_label.setPixmap(pixmap_scaled_keeping_aspec)

        if not new_marker:
            hbox_layout.addWidget(pixmap_label, Qt.AlignRight)

        string_label = ClickableQLabel()
        string_label.setText(label)
        if not new_marker:
            string_label.setFixedHeight(30)
            string_label.setFixedWidth(200)

        btn = QToolButton()
        btn.setIcon(self.q_icon_delete)
        btn.setIconSize(QtCore.QSize(20, 20))
        btn.setMaximumHeight(30)
        btn.setMinimumHeight(30)
        btn.setMaximumWidth(30)
        btn.setMinimumWidth(30)
        btn.setToolTip("Delete this step from pipeline.")

        hbox_layout.addWidget(string_label, Qt.AlignLeft)
        hbox_layout.addWidget(btn, Qt.AlignRight)

        self.pip_widget_vbox_layout.insertWidget(position, pip_main_widget, Qt.AlignTop)

        # Create the corresponding settings widget and connect it
        self.settings_collapsable.setTitle("Settings")
        self.stackedWidget_Settings.hide()
        settings_main_widget = None
        if not new_marker:
            settings_main_widget = self.load_settings_widgets_from_pipeline_groupbox(cat)
            self.stackedWidget_Settings.insertWidget(position, settings_main_widget)

        def show_settings():

            # Set background color while widget is selected.
            pip_main_widget.setStyleSheet("background-color:DarkSlateGrey;")

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
            try:
                current_position = self.pipeline.get_index(cat)
            except ValueError:
                print("Pipeline entry has already been removed.")
                return

            if current_position == 0 or new_marker:
                pass
            else:
                current_position = self.pipeline.get_index(cat)
                self.swap_pip_entry(current_position - 1, current_position)
                self.reset_pip_backgroundcolor()
                self.get_pip_entry(cat).setStyleSheet("background-color:DarkSlateGrey;")

        def move_down_button_clicked():
            try:
                current_position = self.pipeline.get_index(cat)
            except ValueError:
                print("Pipeline entry has already been removed.")
                return

            if current_position == len(self.pipeline.executed_cats) - 1 or new_marker:
                pass
            else:
                current_position = self.pipeline.get_index(cat)
                if self.pipeline.executed_cats[current_position + 1].get_name() == "blank":
                    pass
                else:
                    self.swap_pip_entry(current_position, current_position + 1)
                    self.reset_pip_backgroundcolor()
                    self.get_pip_entry(cat).setStyleSheet("background-color:DarkSlateGrey;")

        pixmap_label.trigger.connect(show_settings)
        string_label.trigger.connect(show_settings)

        btn.clicked.connect(delete_button_clicked, Qt.UniqueConnection)
        up_btn.clicked.connect(move_up_button_clicked, Qt.UniqueConnection)
        dw_btn.clicked.connect(move_down_button_clicked, Qt.UniqueConnection)

        # show new settings widget for new step
        if new_marker:
            show_settings()
            self.disable_plus()

        return (pip_main_widget, settings_main_widget)

    def reset_pip_backgroundcolor(self, current_pip_main_widget=None):
        for i in range(0, self.pip_widget_vbox_layout.count()):
            child = self.pip_widget_vbox_layout.itemAt(i)
            if child.widget() is current_pip_main_widget:
                pass
            else:
                child.widget().setStyleSheet("background-color:None;")

    def get_pip_entry(self, cat):
        index = self.pipeline.get_index(cat)
        pip_entry = self.pip_widget_vbox_layout.itemAt(index).widget()
        return pip_entry

    def get_settings_widget(self, cat):
        index = self.pipeline.get_index(cat)
        pip_widget = self.stackedWidget_Settings.widget(index)
        return pip_widget

    def swap_pip_entry(self, pos1, pos2):
        """
        Swap two entries in the ui pipeline and the pipeline model
        """

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

        # self.pipeline.executed_cats[pos1] = cat2
        # self.pipeline.executed_cats[pos2] = cat1

        self.pipeline.swap_category(pos1, pos2)

        self.add_pipe_entry(pos1)
        self.add_pipe_entry(pos2)


class QScrollArea_filtered(QScrollArea):
    def __init__(self):
        super(QScrollArea_filtered, self).__init__()

    zoom_in = pyqtSignal()
    zoom_out = pyqtSignal()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Wheel:
            if event.modifiers() & Qt.ControlModifier:
                if event.angleDelta().y() < 0:
                    self.zoom_out.emit()
                else:
                    self.zoom_in.emit()

                return True
        return False


class ClickableQLabel(QLabel):
    trigger = pyqtSignal()

    def __init__(self):
        super(ClickableQLabel, self).__init__()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.trigger.emit()


class MidCustomWidget(QWidget):
    def __init__(self, mid_panel, auto_fit):
        super(MidCustomWidget, self).__init__()

        self.auto_fit = auto_fit
        self.current_image_original = None
        self.current_image_size = 1.0
        self.mid_panel = mid_panel
        self.offset = 0
        self.pixels_x = None
        self.pixels_y = None
        self.scrollX = None
        self.scrollY = None
        self.zoomed = False

        self.imageLabel = QLabel()
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(False)

        self.scrollArea = QScrollArea_filtered()
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidget(self.imageLabel)
        self.scrollArea.setAlignment(Qt.AlignHCenter)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.Layout = QVBoxLayout()
        self.Layout.setContentsMargins(11, 11, 11, 11)
        self.setLayout(self.Layout)
        self.Layout.addWidget(self.scrollArea, Qt.AlignTop)

        self.scrollArea.zoom_in.connect(self.zoom_in_)
        self.scrollArea.zoom_out.connect(self.zoom_out_)
        self.scrollArea.horizontalScrollBar().rangeChanged[int, int].connect(
            lambda min, max: self.handle_scroll_x(min, max, ))
        self.scrollArea.verticalScrollBar().rangeChanged[int, int].connect(
            lambda min, max: self.handle_scroll_y(min, max, ))
        self.scrollArea.horizontalScrollBar().valueChanged.connect(self.saveHBar)
        self.scrollArea.verticalScrollBar().valueChanged.connect(self.saveVBar)

    def saveHBar(self, value):
        self.scrollX = value

    def saveVBar(self, value):
        self.scrollY = value

    def mousePressEvent(self, QMouseEvent):
        self.setCursor(Qt.ClosedHandCursor)
        self.offset = QMouseEvent.pos()

    def mouseReleaseEvent(self, QMouseEvent):
        self.setCursor(Qt.ArrowCursor)

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() & Qt.LeftButton:
            self.move(QMouseEvent.pos() - self.offset)

    """
    def keyPressEvent(self, key):
        if key.modifiers() & Qt.ControlModifier:
            self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def keyReleaseEvent(self, key):
        if Qt.ControlModifier:
            self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    """

    def move(self, offset):

        print("BADDSd")
        self.zoomed = True

        self.scrollArea.verticalScrollBar().setSliderPosition(
            self.scrollArea.verticalScrollBar().value() - offset.y() / 50)
        self.scrollArea.horizontalScrollBar().setSliderPosition(
            self.scrollArea.horizontalScrollBar().value() - offset.x() / 50)

    def setPixmap(self, pixmap):
        self.setCurrentImage(pixmap)

        if self.zoomed:
            self.set_zoom()
            self.set_scroll()
            #print("Reset image zoom and position")
            return

        if self.auto_fit:
            self.resize_default()
        else:
            self.resize_original()

    def clearPixmap(self):
        self.imageLabel.clear()

    def resetImageSize(self):
        self.current_image_size = 1.0

    def setCurrentImage(self, pixmap):
        self.current_image_original = pixmap

    def getCurrentImage(self):
        return self.current_image_original

    def set_zoom(self):
        pixmap = self.current_image_original.scaled(self.current_image_original.width() * self.current_image_size,
                                                    self.current_image_original.width() * self.current_image_size,
                                                    QtCore.Qt.KeepAspectRatio, Qt.FastTransformation)

        self.imageLabel.setGeometry(0, 0, pixmap.width() + 22, pixmap.height() + 22)
        self.imageLabel.setPixmap(pixmap)

    def set_scroll(self):
        if self.scrollX is None:
            return
        if self.scrollY is None:
            return
        self.scrollArea.verticalScrollBar().setValue(self.scrollY)
        self.scrollArea.horizontalScrollBar().setValue(self.scrollX)

    @pyqtSlot()
    def handle_scroll_y(self, min, max):

        if self.pixels_y is None:
            return

        delta = self.scrollArea.verticalScrollBar().maximum() - self.pixels_y
        # print("y delta " + str(delta))

        self.scrollY = self.scrollArea.verticalScrollBar().value() + delta / 2
        self.scrollArea.verticalScrollBar().setValue(self.scrollY)

        self.pixels_y = self.scrollArea.verticalScrollBar().maximum()

    @pyqtSlot()
    def handle_scroll_x(self, min, max):

        if self.pixels_x is None:
            return

        delta = self.scrollArea.horizontalScrollBar().maximum() - self.pixels_x
        # print("x delta " + str(delta))

        self.scrollX = self.scrollArea.horizontalScrollBar().value() + delta / 2
        self.scrollArea.horizontalScrollBar().setValue(self.scrollX)

        self.pixels_x = self.scrollArea.horizontalScrollBar().maximum()

    def zoom_out_(self):
        if not self.current_image_original:
            return
        if self.current_image_size < 0.1:
            return

        self.zoomed = True

        self.pixels_x = self.scrollArea.horizontalScrollBar().maximum()
        self.pixels_y = self.scrollArea.verticalScrollBar().maximum()

        self.current_image_size *= 0.85
        pixmap = self.current_image_original.scaled(self.current_image_original.width() * self.current_image_size,
                                                    self.current_image_original.width() * self.current_image_size,
                                                    QtCore.Qt.KeepAspectRatio, Qt.FastTransformation)

        self.imageLabel.setGeometry(0, 0, pixmap.width() + 22, pixmap.height() + 22)
        self.imageLabel.setPixmap(pixmap)

    def zoom_in_(self):
        if not self.current_image_original:
            return
        if self.current_image_size > 3:
            return

        self.zoomed = True

        self.pixels_x = self.scrollArea.horizontalScrollBar().maximum()
        self.pixels_y = self.scrollArea.verticalScrollBar().maximum()

        self.current_image_size *= 1.25
        pixmap = self.current_image_original.scaled(self.current_image_original.width() * self.current_image_size,
                                                    self.current_image_original.width() * self.current_image_size,
                                                    QtCore.Qt.KeepAspectRatio, Qt.FastTransformation)
        self.imageLabel.setGeometry(0, 0, pixmap.width() + 22, pixmap.height() + 22)
        self.imageLabel.setPixmap(pixmap)

    def resize_original(self):
        if not self.current_image_original:
            return

        self.zoomed = False

        self.current_image_size = 1.0
        self.imageLabel.setGeometry(0, 0, self.current_image_original.width() + 22,
                                    self.current_image_original.height() + 22)
        self.imageLabel.setPixmap(self.current_image_original)

    def resize_default(self, force=None):
        if not self.current_image_original:
            return
        if not self.auto_fit and not force:
            return

        self.zoomed = False

        original_width = self.current_image_original.width()
        if original_width != 0:
            self.current_image_size = self.mid_panel.width() / original_width

        new_pixmap = self.current_image_original.scaled(self.mid_panel.width() - 50, self.mid_panel.height() - 120,
                                                        QtCore.Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.imageLabel.setGeometry(0, 0, new_pixmap.width() + 22, new_pixmap.height() + 22)
        self.imageLabel.setPixmap(new_pixmap)

    def toggleAutofit(self):
        self.auto_fit = not self.auto_fit
        if self.auto_fit:
            self.resize_default()
        else:
            self.resize_original()


class LeftCustomWidget(QWidget):
    """
    this widget is used in the left panel of the GUI. All intermediate
    result images are packed into a LeftCustomWidget and appended to the
    according vbox_layout of the Mainview.ui
    """

    select_image = pyqtSignal()

    def __init__(self, image_path, MidCustomWidget, mid_panel, left_scroll_results, current_image,
                 slot, pipeline, settings_widget, left_slider, cat=None):
        super(LeftCustomWidget, self).__init__()

        self.setStyleSheet("font:Candara; font-size: 8pt;")
        # self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.MidCustomWidget = MidCustomWidget
        self.mid_panel = mid_panel
        self.left_scroll_results = left_scroll_results
        self.cat = cat
        self.pipeline = pipeline
        self.settings_widget = settings_widget
        self.left_slider = left_slider
        self.step = 0

        self.image_label = QLabel()

        if cat is None:
            self.image_name = "Input - Image"
        else:
            self.setToolTip("Click here while holding 'CTRL/CMD' button to see used settings .")
            index = self.pipeline.get_index(self.cat)
            if index is not (len(self.pipeline.executed_cats) - 1):
                self.image_name = str(cat.get_name() + " - " + cat.active_algorithm.name)
            else:
                self.image_label.setStyleSheet("background-color:DarkSlateGrey; font:Candara; font-size: 8pt;")
                self.image_name = "Result image - " + str(cat.get_name() + " - " + cat.active_algorithm.name)
            self.step = self.pipeline.get_index(cat) + 1
        self.slot = slot
        # self.setGeometry(0, 0, 300, 100)

        self.LeftCustomWidgetLayout = QVBoxLayout()
        self.LeftCustomWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftCustomWidgetLayout.setSpacing(11)
        self.setLayout(self.LeftCustomWidgetLayout)
        # self.LeftCustomWidgetLayout.setAlignment(Qt.AlignTop)

        self.image_label.setText(self.image_name)
        self.image_label.setGeometry(0, 0, 150, 30)

        self.pixmap = QPixmap(image_path)
        self.pixmap_scaled_keeping_aspec = self.pixmap.scaledToWidth(315, Qt.SmoothTransformation)

        self.image = QLabel()
        # self.image.setAlignment(Qt.AlignLeft)
        self.image.setGeometry(0, 0, 330, self.pixmap_scaled_keeping_aspec.height())
        self.image.setPixmap(self.pixmap_scaled_keeping_aspec)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.LeftCustomWidgetLayout.addWidget(self.image)
        self.LeftCustomWidgetLayout.addWidget(self.image_label)

        self.setGeometry(0, 0, 315, self.pixmap_scaled_keeping_aspec.height() + 50)

        if cat:
            self.createSettings()
            # self.settings_widget.layout().setContentsMargins(0, 0, 0, 0)
            # self.settings_widget.layout().setSpacing(1)
            self.settings_widget.hide()
            self.LeftCustomWidgetLayout.addWidget(self.settings_widget)

        self.select_image.connect(lambda: self.slot(self.MidCustomWidget.getCurrentImage(), self.cat))

    def mousePressEvent(self, QMouseEvent):
        """
        this events sets the self.pixmap from this custom widget
        into the middle panel of the GUI. Or more general: by clicking
        on this widget the users wants to see this picture in the big display
        area of the middle.

        Args:
            | *event*: the mouse press event
        """
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            try:
                if self.step == 0 or self.cat is None:
                    self.mid_panel.setTitle(self.image_name)
                else:
                    index = self.pipeline.get_index(self.cat)
                    if index is not (len(self.pipeline.executed_cats) - 1):
                        self.mid_panel.setTitle(self.image_name + " - Pipeline Position " + str(index + 1))
                    else:
                        self.setStyleSheet("font:Candara; font-size: 8pt;")
                        self.mid_panel.setTitle(self.image_name + " - Pipeline Position " + str(index + 1))
            except (ValueError):
                self.mid_panel.setTitle(self.image_name + " - Already Removed From Pipeline")

            self.MidCustomWidget.setCurrentImage(self.pixmap)
            self.MidCustomWidget.setPixmap(self.pixmap)

            # Connect the trigger signal to a slot.
            # Emit the signal.
            self.select_image.emit()

            if (QMouseEvent.modifiers() & Qt.ControlModifier):

                if self.settings_widget:
                    if self.settings_widget.isVisible():
                        self.settings_widget.hide()
                    else:
                        self.settings_widget.show()

    def createSettings(self):
        self.settings_widget.setDisabled(True)
        self.settings_widget.setStyleSheet("color:silver;")


class ProcessWorker(QtCore.QThread):
    progess_changed = pyqtSignal(object)
    immediate_results_changed = pyqtSignal(object, QCheckBox, QToolButton)
    finished = pyqtSignal()

    def __init__(self, pipeline):
        QtCore.QThread.__init__(self)
        self.pipeline = pipeline
        self.checkbox = None
        self.deleteBtn = None

    def update_progress(self, event):
        self.progess_changed.emit(event)

    def update_add_immediate_result(self, event):
        self.immediate_results_changed.emit(event, self.checkbox, self.deleteBtn)

    def setCheckbox(self, checkbox):
        self.checkbox = checkbox

    def setDeleteBtn(self, deleteBtn):
        self.deleteBtn = deleteBtn

    def run(self):
        try:
            self.pipeline.process()
        except Exception as e:
            print("Failed to process pipeline")
            traceback.print_exc()

        self.finished.emit()


class PipCustomWidget(QWidget):
    """
    This Widget is used for the entry's in the pipeline of thr right
    GUI panel.
    """

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.MidCustomWidget = parent
        self.pixmap = None

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            qpixmap = QtGui.QPixmap(self.pixmap)
            self.MidCustomWidget.setCurrentImage(qpixmap)
            self.MidCustomWidget.setPixmap(qpixmap, self.mid_panel)


class ComboBoxWidget(QWidget):
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
        self.setFixedHeight(50)

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


class CheckBoxWidget(QWidget):
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
        self.setFixedHeight(50)

        def set_modified():
            alg.set_modified()

        self.checkbox.stateChanged.connect(slot)
        self.checkbox.stateChanged.connect(set_modified)


class SliderWidget(QWidget):
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
        self.setFixedHeight(50)

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
        self.textfield.setFixedWidth(50)


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
        self.textfield.setFixedWidth(50)


class Slider(QSlider):
    """
    A customized QSlider that is used by the SliderWidget to allow users to
    change a certain setting.
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
