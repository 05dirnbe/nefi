# -*- coding: utf-8 -*-
"""
This class represents the algorithm Fast nl Means Denoising from the opencv package
"""
__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}

from nefi2.model.algorithms._alg import *


class AlgBody(Algorithm):
    """Fast nl Means Denoising algorithm implementation"""

    def report_pip(self):
        """
        Todo: implement
        Returns:

        """
        pass

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
        self.filterStrength = FloatSlider("filter strength", 0, 0, 100)
        self.float_sliders.append(self.filterStrength)
        self.templateWindowSize = IntegerSlider("template window size", 0, 0, 100)
        self.integer_sliders.append(self.templateWindowSize)
        self.searchWindowSize = IntegerSlider("search window size", 0, 0, 200)
        self.integer_sliders.append(self.searchWindowSize)

    def process(self, image):
        """
        Use the Fast nl Means Denoising algorithm from the opencv package to the current image
        Args:
            image: image instance

        """
        self.image_result = cv2.fastNlMeansDenoising(image,self.filterStrength,self.templateWindowSize,self.searchWindowSize)

if __name__ == '__main__':
    pass
