# -*- coding: utf-8 -*-
import cv2
from nefi2.model.algorithms._alg import *
__authors__ = {"Sebastian Schattner": "s9sescat@stud.uni-saarland.de"}


class AlgBody(Algorithm):
    """Fast nl Means Denoising Colored algorithm implementation"""

    def __init__(self):
        Algorithm.__init__(self)
        self.name = "Fast nl Means Denoising Colored"
        self.parent = "Preprocessing"
        self.filter_strength = FloatSlider("filter strength", 1.0, 100.0, 0.1, 1.0)
        self.filter_strength_color = FloatSlider("filter strength color", 1.0, 100.0, 0.1, 1.0)
        self.template_window_size = IntegerSlider("template window size", 1, 20, 1, 3)
        self.search_window_size = IntegerSlider("search window size", 1, 20, 1, 10)
        self.integer_sliders.append(self.template_window_size)
        self.integer_sliders.append(self.search_window_size)
        self.float_sliders.append(self.filter_strength)
        self.float_sliders.append(self.filter_strength_color)

    def process(self, image):
        self.result = cv2.fastNlMeansDenoisingColored(src=image,
                                                      h=self.filter_strength.value,
                                                      hColor=self.filter_strength_color.value,
                                                      templateWindowSize= self.template_window_size.value*2+1,
                                                      searchWindowSize=self.search_window_size.value*2+1)

if __name__ == '__main__':
    pass
