#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The main nefi2 startup script.
It loads extension loader and initializes UI.
It also enables console batch processing mode.
"""
__authors__ = {"Pavel Shkadzko": "p.shkadzko@gmail.com"}


import argparse
import os
from model.ext_loader import ExtensionLoader
from model.pipeline import Pipeline
import sys
sys.path.insert(0, os.path.join(os.curdir, 'model'))
sys.path.insert(0, os.path.join(os.curdir, 'model', 'categories'))
sys.path.insert(0, os.path.join(os.curdir, 'model', 'algorithms'))


def gui_mode():
    """Start NEFI2 GUI"""
    pass


def batch_mode():
    """Process images in console"""
    pass


def main(args):
    """
    Load all available categories and algorithms into the pipeline.
    Params:
        args -- a Namespace object of supplied command-line arguments
    """
    extloader = ExtensionLoader()
    pipeline = Pipeline(extloader.cats_container)
    if len(vars(args)) > 3:
        batch_mode()
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
                     default=os.getcwd(),
                     help='Specify a directory with images '
                          'for batch processing. If not specified, current '
                          'directory is used.',
                     required=False)
    prs.add_argument('-f', '--file',
                     help='Specify an image file to process.',
                     required=False)
    prs.add_argument('-o', '--out',
                     default=os.getcwd(),
                     help='Specify output directory. If not specified current '
                          'directory is used.',
                     required=False)
    arguments = prs.parse_args()
    main(arguments)
