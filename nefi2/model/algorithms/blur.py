# -*- coding: utf-8 -*-
"""
This class represents the algorithm Blur from the opencv package
"""
__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com",
               "Dennis Groß": "gdennis91@googlemail.com"}

import cv2
from nefi2.model.algorithms._alg import *


class AlgBody(Algorithm):
    """Blur algorithm implementation"""

    def report_pip(self):
        """
        Todo: implement
        Returns:

        """
        pass

    def __init__(self):
        """
        Blur object constructor
        Instance vars:
            self.name -- name of the algorithm
            self.parent -- name of the appropriated category
            self.kernelsize -- blurring kernel size that will be used as slider for the UI
        """
        self.name = "Blur"
        self.parent = "Preprocessing"
        self.kernelsize = IntegerSlider("kernelsize",1,1,20)
        self.integer_sliders.append(self.kernelsize)

    def process(self, image):
        """
        Use the Blur algorithm from the opencv package to the current image
        Args:
            image: image instance

        """
        self.image_result = cv2.blur(image,(self.kernelsize.value*2+1,self.kernelsize.value*2+1))


if __name__ == '__main__':
    pass
