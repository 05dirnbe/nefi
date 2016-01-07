# -*- coding: utf-8 -*-
"""
This class represents the algorithm Blur from the opencv package
"""
__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com",
               "Dennis Groß": "gdennis91@googlemail.com",
               "Sebastian Schattner": "s9sescat@stud.uni-saarland.de"}

import cv2
from nefi2.model.algorithms._alg import *


class AlgBody(Algorithm):
    """Blur algorithm implementation"""

    def __init__(self):
        """
        Blur object constructor
        Instance vars:
            self.name -- name of the algorithm
            self.parent -- name of the appropriated category
            self.kernelsize -- blurring kernel size that will be used as slider for the UI
        """
        self.name = "Blur"
        self.parent = "Preprocessing"
        self.kernelsize = IntegerSlider(self,"kernelsize",1,20,1,1)
        self.channel1 = CheckBox(self, "channel1", True)
        self.channel2 = CheckBox(self, "channel2", True)
        self.channel3 = CheckBox(self, "channel3", True)
        self.integer_sliders.append(self.kernelsize)
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
        Use the Blur algorithm from the opencv package to the chosen colour channels of the current image
        Args:
            image: image instance

        """
        self.channels = cv2.split(image)
        if self.channel1:
            self.channels[0] =cv2.blur(self.channels[0],(self.kernelsize.value*2+1,self.kernelsize.value*2+1))
        if self.channel2:
            self.channels[1] =cv2.blur(self.channels[1],(self.kernelsize.value*2+1,self.kernelsize.value*2+1))
        if self.channel3:
            self.channels[2] =cv2.blur(self.channels[2],(self.kernelsize.value*2+1,self.kernelsize.value*2+1))
        self.result = cv2.merge(self.channels)

if __name__ == '__main__':
    pass
