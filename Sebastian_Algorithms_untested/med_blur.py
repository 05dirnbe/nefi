# -*- coding: utf-8 -*-
import cv2
from nefi2.model.algorithms._alg import *
"""
This class represents the algorithm Median Blur from the opencv package
"""
__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com",
               "Sebastian Schattner": "s9sescat@stud.uni-saarland.de"}


class AlgBody(Algorithm):
    """Median Blur algorithm implementation"""
    def __init__(self):
        """
        Gaussian Blur object constructor
        Instance vars:
            self.name -- name of the algorithm
            self.parent -- name of the appropriated category
            self.kernelsize -- blurring kernel size that will be used as slider for the UI
        """
        Algorithm.__init__(self)
        self.name = "Median Blur"
        self.parent = "Preprocessing"
        self.kernelsize = IntegerSlider(self, "kernelsize", 1, 20, 1, 1)
        self.channel1 = CheckBox(self, "channel1", True)
        self.channel2 = CheckBox(self, "channel2", True)
        self.channel3 = CheckBox(self, "channel3", True)
        self.integer_sliders.append(self.kernelsize)
        self.checkboxes.append(self.channel1)
        self.checkboxes.append(self.channel2)
        self.checkboxes.append(self.channel3)

    def process(self, image):
        """
        Use the Median Blur algorithm from the opencv package to the current image
        Args:
            image: image instance

        """
        channels = cv2.split(image)
        if self.channel1.value:
            channels[0] = cv2.medianBlur(channels[0], self.kernelsize.value*2+1)
        if self.channel2.value:
            channels[1] = cv2.medianBlur(channels[1], self.kernelsize.value*2+1)
        if self.channel3.value:
            channels[2] = cv2.medianBlur(channels[2], self.kernelsize.value*2+1)
        self.result = cv2.merge(channels)

if __name__ == '__main__':
    pass



