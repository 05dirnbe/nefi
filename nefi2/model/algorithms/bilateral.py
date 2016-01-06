# -*- coding: utf-8 -*-
"""
This class represents the algorithm Bilateral Filter from the opencv package
"""
__authors__ = {
    "Andreas Firczynski": "andreasfir91@googlemail.com",
    "Dennis Groß": "gdennis91@googlemail.com"
}

import cv2
from nefi2.model.algorithms._alg import *


class AlgBody(Algorithm):
    """Bilateral Filter algorithm implementation"""

    def report_pip(self):
        """
        Todo: implement
        Returns:

        """
        pass

    def __init__(self):
        """
        Bilateral Filter object constructor
        Instance vars:
            self.name -- name of the algorithm
            self.parent -- name of the appropriated category
            self.diameter -- diameter of each pixel neighborhood that is used during filtering.
                            if it is non-positive, it is computed from sigmaSpace.
            self.sigmaColor -- filter sigma in the color space. The more large the value, the farther colors within
                            the pixel neighborhood will be mixed together
            self.sigmaSpace -- filter sigma in the coordinate space. A larger value of the parameter means
                            that farther pixels will influence each other as long as their colors are close enough
        """
        self.name = "Bilateral Filter"
        self.parent = "Preprocessing"
        self.diameter = IntegerSlider("diameter", 1, 1, 200)
        self.integer_sliders.append(self.diameter)
        self.sigmaColor = FloatSlider("sigmaColor", 0, 0, 255)
        self.float_sliders.append(self.sigmaColor)
        self.sigmaSpace = FloatSlider("sigmaSpace", 0, 0, 200)
        self.float_sliders.append(self.sigmaSpace)

    def process(self, image):
        """
        Use the Bilateral Filter algorithm from the opencv package to the current image
        Args:
            image: image instance

        """
        self.image_result = cv2.bilateralFilter(image, self.diameter, self.sigmaColor, self.sigmaSpace)


if __name__ == '__main__':
    pass
