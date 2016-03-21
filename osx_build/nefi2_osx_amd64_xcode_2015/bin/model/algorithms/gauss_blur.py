#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
from _alg import Algorithm, IntegerSlider, FloatSlider, CheckBox


__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com",
               "Sebastian Schattner": "s9sescat@stud.uni-saarland.de"}


class AlgBody(Algorithm):
    """
    Gaussian Blur algorithm implementation.
    """
    def __init__(self):
        """
        Instance vars:
            | *name* : name of the algorithm
            | *parent* : name of the appropriate category
            | *kernelsize* : blurring kernel size that will be used as slider
              for the UI. Consider that a value n is treated as 2*n+1 to
              guarantee an odd box filter. For example the value 1 gives
              a neighbourhood of size 3x3.
            | *sigmaX* : gaussian kernel standard deviation in X direction
            | *channel1* : checkbox if computing the first color channel
            | *channel2* : checkbox if computing the second color channel
            | *channel3* : checkbox if computing the third color channel

        """
        Algorithm.__init__(self)
        self.name = "Gauss Blur"
        self.parent = "Preprocessing"
        self.kernelsize = IntegerSlider("kernelsize", 1, 20, 1, 1)
        self.sigmaX = FloatSlider("sigmaX", 1.0, 100.0, 0.1, 1.0)
        self.channel1 = CheckBox("channel1", True)
        self.channel2 = CheckBox("channel2", True)
        self.channel3 = CheckBox("channel3", True)
        self.integer_sliders.append(self.kernelsize)
        self.float_sliders.append(self.sigmaX)
        self.checkboxes.append(self.channel1)
        self.checkboxes.append(self.channel2)
        self.checkboxes.append(self.channel3)

    def process(self, args):
        """
        Use the Gaussian Blur algorithm from the opencv package to the current
        image.

        Args:
            | *args* : a list of arguments, e.g. image ndarray

        """
        if (len(args[0].shape) == 2):
            self.result['img'] = cv2.GaussianBlur(args[0],
                                               (self.kernelsize.value*2+1,
                                                self.kernelsize.value*2+1),
                                                self.sigmaX.value)
        else:
            channels = cv2.split(args[0])
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
            self.result['img'] = cv2.merge(channels)


if __name__ == '__main__':
    pass
