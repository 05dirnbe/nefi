# -*- coding: utf-8 -*-
import cv2
from nefi2.model.algorithms._alg import *

"""
This class represents the algorithm Adaptive Threshold from the opencv package
"""

__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}


class AlgBody(Algorithm):
    """
    Adaptive Threshold algorithm implementation
    """

    def __init__(self):
        """Adaptive threshold object constructor
            Instance vars:
                | *name* : name of the algorithm
                | *parent* : name of the appropriated category
                | *maxvalue* : maximum value that can be assigned to the output
                | *blockSize* : value of b
                | *C* : is the constant that is subtracted from the threshold
                value calculated for each pixel
        """
        Algorithm.__init__(self)
        self.name = "Adaptive Threshold"
        self.parent = "Segmentation"
        self.maxvalue = IntegerSlider("maxvalue", 1, 255, 1, 1)
        self.blockSize = IntegerSlider("blockSize", 3, 23, 1, 1)
        self.C = IntegerSlider("C", -10, 10, 1, 1)
        self.integer_sliders.append(self.maxvalue)
        self.integer_sliders.append(self.blockSize)
        self.integer_sliders.append(self.C)

    def process(self, args):
        """
        Use the Adaptive Threshold algorithm from the opencv package
        to the selected color channels of the current image

        Args:
            | *image* : image instance
        """
        image = cv2.cvtColor(args[0], cv2.COLOR_RGB2GRAY)
        # else CV_8UC1 in function adaptiveThreshold
        self.result['img'] = cv2.adaptiveThreshold(image, self.maxvalue,
                                            cv2.ADAPTIVE_THRESH_MEAN_C,
                                            cv2.THRESH_BINARY, self.blockSize,
                                            self.C)


if __name__ == '__main__':
    pass
