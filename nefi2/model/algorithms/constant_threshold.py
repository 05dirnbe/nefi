#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This class represents the algorithm threshold from the opencv package
"""
import cv2
from _alg import Algorithm, IntegerSlider


__author__ = {
    "Sebastian Schattner": "s9sescat@stud.uni-saarland.de"
}

THRESHOLD_FG_COLOR = 255


class AlgBody(Algorithm):
    """
    Adaptive threshold implementation.
    """
    def __init__(self):
        """
        Instance vars:
            | *name* : name of the algorithm
            | *parent* : name of the appropriate category
            | *threshold* : threshold [1-254]

        """
        Algorithm.__init__(self)
        self.name = "Constant Threshold"
        self.parent = "Segmentation"
        self.threshold = IntegerSlider("Threshold", 1, 254, 1, 127)
        self.integer_sliders.append(self.threshold)

    def process(self, args):
        """
        Constant thresholding as described in opencv docs.

        Args:
            | *args* : a list of arguments, e.g. image ndarray

        """
        gray_img = cv2.cvtColor(args[0], cv2.COLOR_RGB2GRAY)
        self.result["img"] = cv2.threshold(gray_img,
                                           self.threshold.value,
                                           THRESHOLD_FG_COLOR,
                                           cv2.THRESH_BINARY_INV)[1]

if __name__ == '__main__':
    pass