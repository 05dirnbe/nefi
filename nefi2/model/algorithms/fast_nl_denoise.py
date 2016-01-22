#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This class represents the algorithm Fast nl Means Denoising from the opencv
package.
"""
import cv2
from _alg import *


__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com",
               "Sebastian Schattner": "s9sescat@stud.uni-saarland.de"}


class AlgBody(Algorithm):
    """
    Fast nl Means Denoising algorithm implementation.
    """

    def __init__(self):
        """
        Fast nl Means Denoising object constructor.

        Instance vars:
            | *name* : name of the algorithm
            | *parent* : name of the appropriate category
            | *filterStrength* : Parameter regulating filter strength.
              A larger value of the parameter means that more noise and also
              more image details will be removed
            | *templateWindowSize* : size in pixels of the template patch that
              is used to compute weights
            | *searchWindowSize* : size in pixels of the window that is used
              to compute weighted average for given pixel.
              A larger value of the parameter means a larger denoising time

        """
        Algorithm.__init__(self)
        self.name = "Fast nl Means Denoising"
        self.parent = "Preprocessing"
        self.f_strength = FloatSlider("filter strength", 1.0, 100.0, 0.1, 1.0)
        self.template_size = IntegerSlider("template window size", 1, 20, 1, 3)
        self.search_size = IntegerSlider("search window size", 1, 20, 1, 10)
        self.channel1 = CheckBox("channel1", True)
        self.channel2 = CheckBox("channel2", True)
        self.channel3 = CheckBox("channel3", True)
        self.integer_sliders.append(self.template_size)
        self.integer_sliders.append(self.search_size)
        self.float_sliders.append(self.f_strength)
        self.checkboxes.append(self.channel1)
        self.checkboxes.append(self.channel2)
        self.checkboxes.append(self.channel3)

    def process(self, args):
        """
        Use the Fast nl Means Denoising algorithm from the opencv package to
        the current image.

        Args:
            | *args* : a list of arguments, e.g. image ndarray

        """
        channels = cv2.split(args[0])
        if self.channel1.value:
            val = cv2.fastNlMeansDenoising(channels[0],
                                           self.filterStrength.value,
                                           self.templateWindowSize.value*2+1,
                                           self.searchWindowSize.value*2+1)
            channels[0] = val
        if self.channel2.value:
            val = cv2.fastNlMeansDenoising(channels[1],
                                           self.filterStrength.value,
                                           self.templateWindowSize.value*2+1,
                                           self.searchWindowSize.value*2+1)
            channels[1] = val
        if self.channel3.value:
            val = cv2.fastNlMeansDenoising(channels[2],
                                           self.filterStrength.value,
                                           self.templateWindowSize.value*2+1,
                                           self.searchWindowSize.value*2+1)
            channels[2] = val
        self.result['img'] = cv2.merge(channels)


if __name__ == '__main__':
    pass
