#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Thinning is the operation that takes a binary image and contracts the
foreground until only single-pixel wide lines remain. It is also known as
skeletonization.

The algorithm below was taken from NEFI1. It uses thinning C module written by
`Adrian Neumann <https://bitbucket.org/adrian_n/thinning>`_.
The code was adapted for NEFI2.
"""
from nefi2.model.algorithms._alg import Algorithm
import cv2
import networkx as nx
import numpy as np
import thinning
from thinning import guo_hall_thinning
import sys
import traceback
from collections import defaultdict
from itertools import chain


__author__ = {"Adrian Neumann": "", "Pavel Shkadzko": "p.shkadzko@gmail.com"}


class AlgBody(Algorithm):
    """
    Guo Hall Thinning implementation.
    """
    def __init__(self):
        """
        Instance vars:
            | *name* : name of the algorithm
            | *parent* : name of the appropriate category

        """
        Algorithm.__init__(self)
        self.name = "Guo Hall Thinning"
        self.parent = "Thinning"

    def process(self, args):
        """
        Guo Hall Thinning.

        Args:
            | *args* : a list of arguments, e.g. image ndarray

        """
        # create a skeleton
        skeleton = guo_hall_thinning(args[0].copy())
        #skeleton = cv2.cvtColor(skeleton, cv2.COLOR_GRAY2BGR)
        self.result['skeleton'] = skeleton
        self.result['img'] = args[0]

if __name__ == '__main__':
    pass
