#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
from _alg import Algorithm, FloatSlider, IntegerSlider

__authors__ = {"Sebastian Schattner": "s9sescat@stud.uni-saarland.de"}


class AlgBody(Algorithm):
    """Fast nl Means Denoising Colored algorithm implementation."""

    def __init__(self):
        """
        Instance vars:
            | *name* : name of the algorithm
            | *parent* : name of the appropriate category
            | *f_strength* : Parameter regulating filter strength.
              A larger value of the parameter means that more noise and also
              more image details will be removed
            | *f_col* : The same as h but for color components. For most images
                value equals 10 will be enough to remove colored noise and do
                not distort colors
            | *template_size* : size in pixels of the template patch that
              is used to compute weights. Consider that a value n is treated
              as 2*n+1 to guarantee an odd box filter. For example the value 1
              gives a neighbourhood of size 3x3.
            | *search_size* : size in pixels of the window that is used
              to compute weighted average for given pixel.
              A larger value of the parameter means a larger denoising time.
              Consider that a value n is treated as 2*n+1 to
              guarantee an odd box filter. For example the value 1 gives
              a neighbourhood of size 3x3.

        """
        Algorithm.__init__(self)
        self.name = "FM Denoise Color"
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
        if (len(args[0].shape) == 2):
            self.result['img'] = cv2.fastNlMeansDenoising(args[0],
                                            self.f_strength.value,
                                            self.template_size.value*2+1,
                                            self.search_size.value*2+1)
        else:
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
