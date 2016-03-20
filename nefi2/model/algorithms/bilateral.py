#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from model.algorithms._alg import *
import cv2


__authors__ = {
    "Andreas Firczynski": "andreasfir91@googlemail.com",
    "Dennis Groß": "gdennis91@googlemail.com",
    "Sebastian Schattner": "s9sescat@stud.uni-saarland.de"}


class AlgBody(Algorithm):
    """
    Bilateral Filter algorithm implementation
    """
    def __init__(self):
        """
        Instance vars:
            | *name* : name of the algorithm
            | *parent* : name of the appropriate category
            | *diameter* : diameter of each pixel neighborhood that is used
             during filtering. If it is non-positive, it is computed from
             sigmaSpace. Consider that a value n is treated as 2*n+1 to
              guarantee an odd box filter. For example the value 1 gives
              a neighbourhood of size 3x3.
            | *sigma_color* : filter sigma in the color space. The larger
             the value, the further the colors within a pixel neighborhood
             will be mixed together
            | *sigma_space* : filter sigma in the coordinate space. A
             larger value of the parameter means that distant pixels will
             influence each other as long as their colors are close enough
            | *channel1* : checkbox if computing the first color channel
            | *channel2* : checkbox if computing the second color channel
            | *channel3* : checkbox if computing the third color channel

        """
        Algorithm.__init__(self)
        self.name = "Bilateral"
        self.parent = "Preprocessing"
        self.diameter = IntegerSlider("diameter", 1, 20, 1, 1)
        self.sigma_color = FloatSlider("sigmaColor", 0.0, 255.0, 0.1, 30.0)
        self.sigma_space = FloatSlider("sigmaSpace", 0.0, 255.0, 0.1, 30.0)
        self.channel1 = CheckBox("channel1", True)
        self.channel2 = CheckBox("channel2", True)
        self.channel3 = CheckBox("channel3", True)
        self.integer_sliders.append(self.diameter)
        self.float_sliders.append(self.sigma_color)
        self.float_sliders.append(self.sigma_space)
        self.checkboxes.append(self.channel1)
        self.checkboxes.append(self.channel2)
        self.checkboxes.append(self.channel3)

    def process(self, args):
        """
        Use the Bilateral Filter algorithm from the opencv package to the
        selected color channels of the current image.

        Args:
            | *image* : image instance

        """
        def bilateral(chnls):
            """
            Bilateral cv2 filter function

            Args:
                *chnls* (ndarray) -- image array

            Returns:
                result of cv2.bilateralFilter

            """
            return cv2.bilateralFilter(chnls, self.diameter.value*2+1,
                                              self.sigma_color.value,
                                              self.sigma_space.value)

        if (len(args[0].shape) == 2):
           self.result['img'] = cv2.bilateralFilter(args[0], self.diameter.value*2+1,
                                              self.sigma_color.value,
                                              self.sigma_space.value)
        else:
            channels = cv2.split(args[0])
            if all([self.channel1.value, self.channel2.value, self.channel3.value]):
                self.result['img'] = bilateral(args[0])
            else:
                if self.channel1.value:
                    channels[0] = bilateral(channels[0])
                if self.channel2.value:
                    channels[1] = bilateral(channels[1])
                if self.channel3.value:
                    channels[2] = bilateral(channels[2])
                self.result['img'] = cv2.merge(channels)


if __name__ == '__main__':
    pass
