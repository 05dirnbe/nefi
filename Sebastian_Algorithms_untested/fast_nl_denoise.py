# -*- coding: utf-8 -*-
"""
This class represents the algorithm Fast nl Means Denoising from the opencv package
"""
__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com",
               "Sebastian Schattner": "s9sescat@stud.uni-saarland.de"}

import cv2
from nefi2.model.algorithms._alg import *


class AlgBody(Algorithm):
    """Fast nl Means Denoising algorithm implementation"""

    def __init__(self):
        """
        Fast nl Means Denoising object constructor
        Instance vars:
            self.name -- name of the algorithm
            self.parent -- name of the appropriated category
            self.filterStrength -- Parameter regulating filter strength. A larger value of the parameter means
                                that more noise and also more image details will be removed
            self.templateWindowSize -- size in pixels of the template patch that is used to compute weights
            self.searchWindowSize -- size in pixels of the window that is used to compute weighted average for
                                given pixel. A larger value of the parameter means a larger denoising time
        """
        self.name = "Fast nl Means Denoising"
        self.parent = "Preprocessing"
        self.filter_strength = FloatSlider(self,"filter strength",1.0,100.0,0.1,1.0)
        self.template_window_size = IntegerSlider(self,"template window size",1,20,1,3)
        self.search_window_size = IntegerSlider(self,"search window size",1,20,1,10)
        self.channel1 = CheckBox(self, "channel1", True)
        self.channel2 = CheckBox(self, "channel2", True)
        self.channel3 = CheckBox(self, "channel3", True)
        self.integer_sliders.append(self.template_window_size)
        self.integer_sliders.append(self.search_window_size)
        self.float_sliders.append(self.filter_strength)
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
        Use the Fast nl Means Denoising algorithm from the opencv package to the current image
        Args:
            image: image instance

        """
        self.channels = cv2.split(image)
        if self.channel1:
            self.channels[0] =cv2.fastNlMeansDenoising(self.channels[0],self.filterStrength,self.templateWindowSize*2+1,self.searchWindowSize*2+1)
        if self.channel2:
            self.channels[1] =cv2.fastNlMeansDenoising(self.channels[1],self.filterStrength,self.templateWindowSize*2+1,self.searchWindowSize*2+1)
        if self.channel3:
            self.channels[2] =cv2.fastNlMeansDenoising(self.channels[2],self.filterStrength,self.templateWindowSize*2+1,self.searchWindowSize*2+1)
        self.result = cv2.merge(self.channels)
if __name__ == '__main__':
    pass
