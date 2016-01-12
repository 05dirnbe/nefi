# -*- coding: utf-8 -*-
import cv2
from nefi2.model.algorithms._alg import *

"""
This class represents the algorithm Threshold from the opencv package
"""

__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}


class AlgBody(Algorithm):

    """
    Threshold algorithm implementation
    """

    def __init__(self):
        """Threshold object constructor
            Instance vars:
                | *name* : name of the algorithm
                | *parent* : name of the appropriated category
                | *threshold* : value of threshold. Any value that is greater
                than the threshold value is set to 255 and any value less than
                is set to 0 (by using cv2.TRESH_BINARY)
                | *maxvalue* : maximum value that can be assigned to the output


        """
        Algorithm.__init__(self)
        self.name = "Threshold"
        self.parent = "Segmentation"
        self.threshold = IntegerSlider("threshold value", 1, 50, 1, 1)
        self.maxvalue = IntegerSlider("maxvalue", 1, 255, 1, 1)
        self.integer_sliders.append(self.threshold)
        self.integer_sliders.append(self.maxvalue)


    def process(self, image):
        """
        Use the Threshold algorithm from the opencv package
        to the selected color channels of the current image

        Args:
            image:
            | *image* : image instance
        """
        retval, tres = cv2.threshold(image, self.threshold,
                                     self.maxvalue, cv2.THRESH_BINARY)
        self.result = tres


if __name__ == '__main__':
    pass
