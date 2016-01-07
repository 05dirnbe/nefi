# -*- coding: utf-8 -*-
"""
This class represents the algorithm Canny edge
"""
__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}

import cv2
from nefi2.model.algorithms._alg import *


class AlgBody(Algorithm):
    """Guo Hall algorithm implementation"""

    def __init__(self):
        """
        Canny object constructor
        Instance vars:
            self.name -- name of the algorithm
            self.parent -- name of the appropriated category
            self.threshold1 -- first threshold for the hysteresis procedure
            self.threshold2 -- second threshold for the hysteresis procedure
        """
        self.name = "Canny graph detector"
        self.parent = "Graph detection"
        self.threshold1 = IntegerSlider("threshold1", 1, 100, 1, 1)
        self.integer_sliders.append(self.threshold1)
        self.threshold2 = IntegerSlider("threshold2", 1, 100, 1, 1)
        self.integer_sliders.append(self.threshold2)

    def process(self, image):
        """
        Use the Canny algorithm from the opencv package to the current image.
        The function finds edges in the input image image and marks them in
        the output map edges using the Canny algorithm. The smallest value
        between threshold1 and threshold2 is used for edge linking
        Args:
            image: image instance

        """
        skeleton = cv2.Canny(image, self.threshold1.value,
                             self.threshold2.value)
