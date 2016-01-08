# -*- coding: utf-8 -*-
import cv2
from _alg import *

"""
This class represents the algorithm Bilateral Filter from the opencv package
"""

__authors__ = {
    "Andreas Firczynski": "andreasfir91@googlemail.com",
    "Dennis Groß": "gdennis91@googlemail.com",
    "Sebastian Schattner": "s9sescat@stud.uni-saarland.de"}


class AlgBody(Algorithm):

    """
    Bilateral Filter algorithm implementation
    """

    def __init__(self):
        """Bilateral Filter object constructor
            Instance vars:
                | *name* : name of the algorithm
                | *parent* : name of the appropriated category
                | *diameter* : diameter of each pixel neighborhood that is used during filtering.
                        If it is non-positive, it is computed from sigmaSpace.
                | *sigma_color* : filter sigma in the color space. The more large the value,
                        the farther colors within the pixel neighborhood will be mixed together
                | *sigma_space* : filter sigma in the coordinate space. A larger value of the parameter means
                        that farther pixels will influence each other as long as their colors are close enough
                | *channel1* : checkbox if the first color channel will be computed
                | *channel2* : checkbox if the second color channel will be computed
                | *channel3* : checkbox if the third color channel will be computed

        """
        Algorithm.__init__(self)
        self.name = "Bilateral Filter"
        self.parent = "Preprocessing"
        self.diameter = IntegerSlider("diameter", 1, 20, 1, 1)
        self.sigma_color = FloatSlider("sigmaColor", 0.0, 255.0, 0.1, 30.0)
        self.sigma_space = FloatSlider("sigmaSpace", 0.0, 255.0, 0.1, 30.0)
        self.channel1 = CheckBox("channel1", True)
        self.channel2 = CheckBox("channel2", True)
        self.channel3 = CheckBox("channel3", True)
        self.integer_sliders.append(self.diameter)
        self.float_sliders.append(self.sigma_color)
        self.float_sliders.append(self.sigma_space)
        self.checkboxes.append(self.channel1)
        self.checkboxes.append(self.channel2)
        self.checkboxes.append(self.channel3)

    def process(self, image):
        """
        Use the Bilateral Filter algorithm from the opencv package to the selected color channels of the current image

        Args:
            | *image* : image instance
        """
        channels = cv2.split(image)
        if self.channel1.value:
            channels[0] = cv2.bilateralFilter(channels[0], self.diameter.value*2+1, self.sigma_color.value,
                                              self.sigma_space.value)
        if self.channel2.value:
            channels[1] = cv2.bilateralFilter(channels[1], self.diameter.value*2+1, self.sigma_color.value,
                                              self.sigma_space.value)
        if self.channel3.value:
            channels[2] = cv2.bilateralFilter(channels[2], self.diameter.value*2+1, self.sigma_color.value,
                                              self.sigma_space.value)
        self.result = cv2.merge(channels)
if __name__ == '__main__':
    pass
