# -*- coding: utf-8 -*-
import cv2
from nefi2.model.algorithms._alg import *
"""
This class represents the algorithm Fast nl Means Denoising from the opencv package
"""
__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com",
               "Sebastian Schattner": "s9sescat@stud.uni-saarland.de"}


class AlgBody(Algorithm):
    """
    Fast nl Means Denoising algorithm implementation
    """

    def __init__(self):
        """
        Fast nl Means Denoising object constructor
            Instance vars:
                | *name* : name of the algorithm
                | *parent* : name of the appropriated category
                | *filterStrength* : Parameter regulating filter strength. A larger value of the parameter means
                    that more noise and also more image details will be removed
                | *templateWindowSize* : size in pixels of the template patch that is used to compute weights
                | *searchWindowSize* : size in pixels of the window that is used to compute weighted average for given pixel.
                    A larger value of the parameter means a larger denoising time
        """
        Algorithm.__init__(self)
        self.name = "Fast nl Means Denoising"
        self.parent = "Preprocessing"
        self.filter_strength = FloatSlider("filter strength", 1.0, 100.0, 0.1, 1.0)
        self.template_window_size = IntegerSlider("template window size", 1, 20, 1, 3)
        self.search_window_size = IntegerSlider("search window size", 1, 20, 1, 10)
        self.channel1 = CheckBox("channel1", True)
        self.channel2 = CheckBox("channel2", True)
        self.channel3 = CheckBox("channel3", True)
        self.integer_sliders.append(self.template_window_size)
        self.integer_sliders.append(self.search_window_size)
        self.float_sliders.append(self.filter_strength)
        self.checkboxes.append(self.channel1)
        self.checkboxes.append(self.channel2)
        self.checkboxes.append(self.channel3)

    def process(self, image):
        """
        Use the Fast nl Means Denoising algorithm from the opencv package to the current image

        Args:
            | *image* : image instance

        """
        channels = cv2.split(image)
        if self.channel1.value:
            channels[0] = cv2.fastNlMeansDenoising(channels[0],
                                                   self.filterStrength.value,
                                                   self.templateWindowSize.value*2+1,
                                                   self.searchWindowSize.value*2+1)
        if self.channel2.value:
            channels[1] = cv2.fastNlMeansDenoising(channels[1],
                                                   self.filterStrength.value,
                                                   self.templateWindowSize.value*2+1,
                                                   self.searchWindowSize.value*2+1)
        if self.channel3.value:
            channels[2] = cv2.fastNlMeansDenoising(channels[2],
                                                   self.filterStrength.value,
                                                   self.templateWindowSize.value*2+1,
                                                   self.searchWindowSize.value*2+1)
        self.result = cv2.merge(channels)
if __name__ == '__main__':
    pass
