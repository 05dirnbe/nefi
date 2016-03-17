# -*- coding: utf-8 -*-
import cv2
from nefi2.model.algorithms._alg import *

"""
This class represents the algorithm Otsus Threshold from the opencv package
"""

__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}


class AlgBody(Algorithm):

    """
    Otsus Threshold algorithm implementation
    """

    def __init__(self):
        """Otsus threshold object constructor
            Instance vars:
                | *name* : name of the algorithm
                | *parent* : name of the appropriated category

        """
        Algorithm.__init__(self)
        self.name = "Otsus Threshold"
        self.parent = "Segmentation"


    def process(self, image):
        """
        Use the Otsus Threshold algorithm from the opencv package
        to the selected color channels of the current image

        Args:
            | *image* : image instance
        """


if __name__ == '__main__':
    pass
