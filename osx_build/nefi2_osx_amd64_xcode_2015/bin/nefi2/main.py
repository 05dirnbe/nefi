#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The main nefi2 startup script.
It loads extension loader and initializes UI.
It also enables console batch processing mode.
"""
from nefi2.model.ext_loader import ExtensionLoader
from nefi2.model.pipeline import Pipeline
from nefi2.view.main_controller import MainView

import sys
import argparse
import ctypes
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
import qdarkstyle


__authors__ = {"Pavel Shkadzko": "p.shkadzko@gmail.com",
               "Dennig Groß": "gdennis91@googlemail.com",
               "Philipp Reichert": "prei@me.com"}

class start:

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
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        app.setQuitOnLastWindowClosed(True)
        app.setWindowIcon(QtGui.QIcon("./icons/nefi2.ico"))
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
