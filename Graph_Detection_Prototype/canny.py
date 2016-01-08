# -*- coding: utf-8 -*-

import cv2
from nefi2.model.algorithms._alg import *

"""
This class represents the algorithm Canny edge
"""

__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}

class AlgBody(Algorithm):
    """
    Guo Hall algorithm implementation
    """

    def __init__(self):
        """
        Canny object constructor
            Instance vars:
                | *name* : name of the algorithm
                | *parent* : name of the appropriated category
                | *threshold1* : first threshold for the hysteresis procedure
                | *threshold2* : second threshold for the hysteresis procedure

        """
        self.name = "Canny graph detector"
        self.parent = "Graph detection"
        self.threshold1 = FloatSlider("threshold1", 1.0, 100.0, 1.0, 1.0)
        self.integer_sliders.append(self.threshold1)
        self.threshold2 = FloatSlider("threshold2", 1.0, 100.0, 1.0, 1.0)
        self.integer_sliders.append(self.threshold2)

    def process(self, image):
        """
        Use the Canny algorithm from the opencv package to the current image.
        The function finds edges in the input image image and marks them in
        the output map edges using the Canny algorithm. The smallest value
        between threshold1 and threshold2 is used for edge linking

        Args:
            | *image* : image instance

        """
        skeleton = cv2.Canny(image, self.threshold1.value,
                             self.threshold2.value)
