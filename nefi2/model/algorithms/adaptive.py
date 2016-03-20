#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
(from opencv docs)
Adaptive Thresholding.
Global threshold value may not be good in all the conditions where image has
different lighting conditions in different areas. In that case, we go for
adaptive thresholding. In this, the algorithm calculate the threshold for a
small regions of the image. So we get different thresholds for different
regions of the same image and it gives us better results for images with
varying illumination.
"""
from model.algorithms._alg import Algorithm, IntegerSlider
import cv2


__author__ = {
    "Andreas Firczynski": "andreasfir91@googlemail.com",
    "Pavel Shkadzko": "p.shkadzko@gmail.com",
    "Sebastian Schattner": "s9sescat@stud.uni-saarland.de"
}


class AlgBody(Algorithm):
    """
    Adaptive Threshold implementation.
    """
    def __init__(self):
        """
        Instance vars:
            | *name* : name of the algorithm
            | *parent* : name of the appropriate category
            | *constant* : threshold constant [-10-10]
            | *blocksize* : threshold blocksize [3-23]

        """
        Algorithm.__init__(self)
        self.name = "Adaptive"
        self.parent = "Segmentation"
        self.blocksize = IntegerSlider("Threshold Blocksize", 1, 20, 1, 5)
        self.constant = IntegerSlider("Threshold Constant", -10, 10, 1, 2)
        self.integer_sliders.append(self.blocksize)
        self.integer_sliders.append(self.constant)

    def process(self, args):
        """
        Adaptive thresholding as described in opencv docs.

        Args:
            | *args* : a list of arguments, e.g. image ndarray

        """
        if (len(args[0].shape) == 3):
            gray_img = cv2.cvtColor(args[0], cv2.COLOR_RGB2GRAY)
        else:
            gray_img = args[0]
        self.result['img'] = cv2.adaptiveThreshold(gray_img, 255,
                                                   cv2.ADAPTIVE_THRESH_MEAN_C,
                                                   cv2.THRESH_BINARY_INV,
                                                   self.blocksize.value*2+1,
                                                   self.constant.value)


if __name__ == '__main__':
    pass
