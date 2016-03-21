#!/usr/bin/env python3
from nefi2 import main
import argparse
import os
import sys
os.chdir(os.path.dirname(os.path.realpath(__file__)))


def runner(args):
    """
    Load all available categories and algorithms into the pipeline.

    Args:
        | *args* : a Namespace object of supplied command-line arguments
    """
    if args.dir or args.file:
        main.batch_mode(args)
    else:
        main.gui_mode()


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
    prs.add_argument('-o', '--out',
                     help='Specify output directory.',
                     required=False)
    arguments = prs.parse_args()
    runner(arguments)
