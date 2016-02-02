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
import numpy as np
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
        processed_img = cv2.threshold(gray_img, 0, 255,
                                      cv2.THRESH_BINARY_INV +
                                      cv2.THRESH_OTSU)[1]
        zero_img_arr = np.zeros_like(args[0])
        zero_img_arr[processed_img == 255] = [255] * 3
        self.result['img'] = zero_img_arr

if __name__ == '__main__':
    pass
