#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The main nefi2 startup script.
It loads extension loader and initializes UI.
It also enables console batch processing mode.
"""
import os

from nefi2.model.ext_loader import ExtensionLoader
from nefi2.model.pipeline import Pipeline
from nefi2.view.main_controller import MainView

import sys
import argparse
import ctypes
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication
import qdarkstyle

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

__authors__ = {"Pavel Shkadzko": "p.shkadzko@gmail.com",
               "Dennig Groß": "gdennis91@googlemail.com",
               "Philipp Reichert": "prei@me.com"}

class Main:

    @staticmethod
    def gui_mode():
        """
        Start NEFI2 GUI
        """
        myappid = 'nefi2.0' # arbitrary string
        if sys.platform == 'win32' or sys.platform == 'win64':
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)
        app = QApplication(sys.argv)
        app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        app.setQuitOnLastWindowClosed(True)
        app.setWindowIcon(QtGui.QIcon(os.path.join('icons', 'nefi2.ico')))
        wnd = MainView(pipeline)
        wnd.load_dark_theme(app)
        wnd.show()
        sys.exit(app.exec_())

    @staticmethod
    def batch_mode(args):
        """
        Process images in console mode

        Args:
            | *args* (dict) : argument dict returned by ArgumentParser

        """
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)
        # processing args values
        if args.pipeline:
            # load the specified pipeline file
            # default url
            pipeline.load_pipeline_json(args.pipeline)
        if args.dir:
            # load the images from the specified source dir
            pipeline.set_input(args.dir)
        elif args.file:
            # load a single image
            pipeline.set_input(args.file)
        if args.out:
            pipeline.set_output_dir(args.out)
        pipeline.process_batch()


if __name__ == '__main__':
    pass
