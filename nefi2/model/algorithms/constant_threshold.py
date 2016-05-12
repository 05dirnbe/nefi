#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from nefi2.model.algorithms._alg import Algorithm, IntegerSlider
import cv2


__author__ = {
    "Sebastian Schattner": "s9sescat@stud.uni-saarland.de"
}

THRESHOLD_FG_COLOR = 255


class AlgBody(Algorithm):
    """
    Constant Threshold implementation.
    """
    def __init__(self):
        """
        Instance vars:
            | *name* : name of the algorithm
            | *parent* : name of the appropriate category
            | *threshold* : threshold [1-254]

        """
        Algorithm.__init__(self)
        self.name = "Constant"
        self.parent = "Segmentation"
        self.threshold = IntegerSlider("Threshold", 1, 254, 1, 127)
        self.integer_sliders.append(self.threshold)

    def process(self, args):
        """
        Constant thresholding as described in opencv docs.

        Args:
            | *args* : a list of arguments, e.g. image ndarray

        """
        if (len(args[0].shape) == 3):
            gray_img = cv2.cvtColor(args[0], cv2.COLOR_RGB2GRAY)
        else:
            gray_img = args[0]
        self.result["img"] = cv2.threshold(gray_img,
                                           self.threshold.value,
                                           THRESHOLD_FG_COLOR,
                                           cv2.THRESH_BINARY_INV)[1]

if __name__ == '__main__':
    pass
