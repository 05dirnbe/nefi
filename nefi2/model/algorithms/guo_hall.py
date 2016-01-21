#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Custom Guo Hall thinning algorithm
https://pypi.python.org/pypi/thinning
"""
import cv2
import thinning
from _alg import *


__author__ = {"Pavel Shkadzko": "p.shkadzko@gmail.com"}


class AlgBody(Algorithm):
    """
    Guo Hall thinning implementation.
    """
    def __init__(self):
        """
        Instance vars:
            | *name* : name of the algorithm
            | *parent* : name of the appropriate category
            
        """
        Algorithm.__init__(self)
        self.name = "Guo Hall Thinning"
        self.parent = "Graph Detection"

    def process(self, image):
        """
        Guo Hall thinning.

        Args:
            | *image* : image instance

        """
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self.result = thinning.guo_hall_thinning(gray_img)


if __name__ == '__main__':
    pass
