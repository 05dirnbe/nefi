#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This class represents the algorithm Gaussian Blur from the opencv package.
"""
import cv2
from _alg import *


__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com",
               "Sebastian Schattner": "s9sescat@stud.uni-saarland.de"}


class AlgBody(Algorithm):
    """
    Gaussian Blur algorithm implementation.
    """
    def __init__(self):
        """
        Gaussian Blur object constructor.

        Instance vars:
            | *name* : name of the algorithm
            | *parent* : name of the appropriated category
            | *kernelsize* : blurring kernel size that will be used as slider
              for the UI
            | *sigmaX* : gaussian kernel standard deviation in X direction

        """
        Algorithm.__init__(self)
        self.name = "Gaussian Blur"
        self.parent = "Preprocessing"
        self.kernelsize = IntegerSlider("kernelsize",1,20,1,1)
        self.sigmaX = FloatSlider("sigmaX",1.0,100.0,0.1,1.0)
        self.channel1 = CheckBox("channel1", True)
        self.channel2 = CheckBox("channel2", True)
        self.channel3 = CheckBox("channel3", True)
        self.integer_sliders.append(self.kernelsize)
        self.float_sliders.append(self.sigmaX)
        self.checkboxes.append(self.channel1)
        self.checkboxes.append(self.channel2)
        self.checkboxes.append(self.channel3)

    def process(self, image):
        """
        Use the Gaussian Blur algorithm from the opencv package to the current
        image.

        Args:
            | *image* : image instance

        """
        channels = cv2.split(image)
        if self.channel1.value:
            channels[0] = cv2.GaussianBlur(channels[0],
                                           (self.kernelsize.value*2+1,
                                            self.kernelsize.value*2+1),
                                            self.sigmaX.value)
        if self.channel2.value:
            channels[1] = cv2.GaussianBlur(channels[1],
                                           (self.kernelsize.value*2+1,
                                            self.kernelsize.value*2+1),
                                            self.sigmaX.value)
        if self.channel3.value:
            channels[2] = cv2.GaussianBlur(channels[2],
                                           (self.kernelsize.value*2+1,
                                            self.kernelsize.value*2+1),
                                            self.sigmaX.value)
        self.result = cv2.merge(channels)


if __name__ == '__main__':
    pass
