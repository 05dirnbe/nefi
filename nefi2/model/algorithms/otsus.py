#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
(from opencv docs)
Otsu's binarization automatically calculates a threshold value from image
histogram for a bimodal image. (For images which are not bimodal, binarization
won’t be accurate.)
For this, cv2.threshold() function is used with an extra flag, cv2.THRESH_OTSU.
For threshold value, simply pass zero. Then the algorithm finds the optimal
threshold value and returns you as the second output. If Otsu thresholding is
not used, the optimal threshold is same as the threshold value you used.
"""
import cv2
from _alg import Algorithm


__author__ = {"Pavel Shkadzko": "p.shkadzko@gmail.com"}


class AlgBody(Algorithm):
    """
    Otsu's threshold implementation.
    """
    def __init__(self):
        """
        Instance vars:
            | *name* : name of the algorithm
            | *parent* : name of the appropriate category

        """
        Algorithm.__init__(self)
        self.name = "Otsu's Threshold"
        self.parent = "Segmentation"

    def process(self, args):
        """
        Otsu's thresholding as described in opencv docs.

        Args:
            | *args* : a list of arguments, e.g. image ndarray

        """
        gray_img = cv2.cvtColor(args[0], cv2.COLOR_RGB2GRAY)
        self.result['img'] = cv2.threshold(gray_img, 0, 255,
                                           cv2.THRESH_BINARY +
                                           cv2.THRESH_OTSU)[1]


if __name__ == '__main__':
    pass
