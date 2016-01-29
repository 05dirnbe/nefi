#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The main nefi2 startup script.
It loads extension loader and initializes UI.
It also enables console batch processing mode.
"""
import sys
import argparse

from PyQt5.QtWidgets import QApplication
from model.ext_loader import ExtensionLoader
from model.pipeline import Pipeline
from view.mainwindow import Window

__authors__ = {"Pavel Shkadzko": "p.shkadzko@gmail.com"}


def gui_mode():
    """
    Start NEFI2 GUI
    """
    extloader = ExtensionLoader()
    pipeline = Pipeline(extloader.cats_container)

    #app = QApplication(sys.argv)
    #window = Window(pipeline)
    #window.show()
    #sys.exit(app.exec_())


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
        # pipeline.load_pipeline()
        pass
    if args.dir:
        # load the images from the specified source dir
        pipeline.set_input_dir(args.dir)
    if args.out:
        pipeline.set_output_dir(args.out)
    pipeline.get_image(args.file)

    ############################ DEBUGGING ####################################
    # just testing, safe to remove
    print("########## TESTING ##########")
    print('DEFAULT PIPELINE:', [(c.name, c.active_algorithm.name) for c in pipeline.executed_cats])
    for cat in pipeline.executed_cats:
        if cat.name == 'Preprocessing':
            cat.set_active_algorithm('Invert Color')
    # pipeline.delete_category('Graph detection')
    # pipeline.delete_category('Graph filtering')
    print('CURRENT PIPELINE:', [(c.name, c.active_algorithm.name) for c in pipeline.executed_cats])
    pipeline.process()
    print("########## FINISHED ##########")
    ############################ DEBUGGING ####################################


def main(args):
    """
    Load all available categories and algorithms into the pipeline.

    Args:
        | *args* : a Namespace object of supplied command-line arguments
    """
    if args.dir or args.file:
        batch_mode(args)
    else:
        gui_mode()


if __name__ == '__main__':
    prs = argparse.ArgumentParser(description="""NEFI2 is a tool created to
    extract networks from images. Given a suitable 2D image of a network as
    input, NEFI2 outputs a mathematical representation of the structure of the
    depicted network as a weighted undirected planar graph.""")
    prs.add_argument('-p', '--pipeline',
                     help='Specify a saved pipeline xml file.',
                     required=False)
    prs.add_argument('-d', '--dir',
                     help='Specify a directory with images '
                          'for batch processing.',
                     required=False)
    prs.add_argument('-f', '--file',
                     help='Specify an image file to process.',
                     required=False)
    prs.add_argument('-p', '--pipeline',
                     help='Specify a saved pipeline.',
                     required=False)
    prs.add_argument('-o', '--out',
                     help='Specify output directory.',
                     required=False)
    arguments = prs.parse_args()
    main(arguments)
