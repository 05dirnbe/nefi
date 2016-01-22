#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
from _alg import *

__authors__ = {"Sebastian Schattner": "s9sescat@stud.uni-saarland.de"}


class AlgBody(Algorithm):
    """Fast nl Means Denoising Colored algorithm implementation."""

    def __init__(self):
        Algorithm.__init__(self)
        self.name = "Fast nl Means Denoising Colored"
        self.parent = "Preprocessing"
        self.f_strength = FloatSlider("filter strength", 1.0, 100.0, 0.1, 1.0)
        self.f_col = FloatSlider("filter strength color", 1.0, 100.0, 0.1, 1.0)
        self.template_size = IntegerSlider("template window size", 1, 20, 1, 3)
        self.search_size = IntegerSlider("search window size", 1, 20, 1, 10)
        self.integer_sliders.append(self.template_size)
        self.integer_sliders.append(self.search_size)
        self.float_sliders.append(self.f_strength)
        self.float_sliders.append(self.f_col)

    def process(self, args):
        ts = self.template_size.value*2+1
        ss = self.search_size.value*2+1
        result = cv2.fastNlMeansDenoisingColored(src=args[0],
                                                 h=self.f_strength.value,
                                                 hColor=self.f_col.value,
                                                 templateWindowSize=ts,
                                                 searchWindowSize=ss)
        self.result['img'] = result


if __name__ == '__main__':
    pass
