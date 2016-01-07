# -*- coding: utf-8 -*-
"""
This class represents the algorithm Invert Color
"""
__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com",
               "Sebastian Schattner": "s9sescat@stud.uni-saarland.de"}

import cv2
from nefi2.model.algorithms._alg import *



class AlgBody(Algorithm):
    """Invert Color algorithm implementation"""
    def __init__(self):
        """
        Invert Color object constructor
        Instance vars:
            self.name -- name of the algorithm
            self.parent -- name of the appropriated category
        """
        Algorithm.__init__(self)
        self.name = "Invert Color"
        self.parent = "Preprocessing"
        self.channel1 = CheckBox(self, "channel1", True)
        self.channel2 = CheckBox(self, "channel2", True)
        self.channel3 = CheckBox(self, "channel3", True)
        self.checkboxes.append(self.channel1)
        self.checkboxes.append(self.channel2)
        self.checkboxes.append(self.channel3)

    def process(self, image):
        """
        Invert the current image
        Args:
            image: image instance

        """
        self.channels = cv2.split(image)
        if self.channel1:
            self.channels[0] =(255-self.channels[0])
        if self.channel2:
            self.channels[1] =(255-self.channels[1])
        if self.channel3:
            self.channels[2] =(255-self.channels[2])
        self.result = cv2.merge(self.channels)



if __name__ == '__main__':
    pass




