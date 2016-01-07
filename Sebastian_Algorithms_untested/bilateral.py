# -*- coding: utf-8 -*-
"""
This class represents the algorithm Bilateral Filter from the opencv package
"""
__authors__ = {
    "Andreas Firczynski": "andreasfir91@googlemail.com",
    "Dennis Groß": "gdennis91@googlemail.com",
    "Sebastian Schattner": "s9sescat@stud.uni-saarland.de"
}

import cv2
from nefi2.model.algorithms._alg import *


class AlgBody(Algorithm):
    """Bilateral Filter algorithm implementation"""

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
        self.diameter = IntegerSlider(self,"diameter",1,20,1,1)
        self.sigma_color = FloatSlider(self,"sigmaColor",0.0,255.0,0.1,30.0)
        self.sigma_space = FloatSlider(self,"sigmaSpace",0.0,255.0,0.1,30.0)
        self.channel1 = CheckBox(self, "channel1", True)
        self.channel2 = CheckBox(self, "channel2", True)
        self.channel3 = CheckBox(self, "channel3", True)
        self.integer_sliders.append(self.diameter)
        self.float_sliders.append(self.sigma_color)
        self.float_sliders.append(self.sigma_space)
        self.checkboxes.append(self.channel1)
        self.checkboxes.append(self.channel2)
        self.checkboxes.append(self.channel3)

    def report_pip(self):
        """
        Todo: implement
        Returns:

        """
        pass

    def process(self, image):
        """
        Use the Bilateral Filter algorithm from the opencv package to the current image
        Args:
            image: image instance

        """
        self.channels = cv2.split(image)
        if self.channel1:
            self.channels[0] = cv2.bilateralFilter(self.channels[0],self.diameter*2+1,self.sigma_color,self.sigma_space)
        if self.channel2:
            self.channels[1] = cv2.bilateralFilter(self.channels[1],self.diameter*2+1,self.sigma_color,self.sigma_space)
        if self.channel3:
            self.channels[2] = cv2.bilateralFilter(self.channels[2],self.diameter*2+1,self.sigma_color,self.sigma_space)
        self.result = cv2.merge(self.channels)
if __name__ == '__main__':
    pass
