# -*- coding: utf-8 -*-
"""
This class represents the algorithm Blur from the opencv package
"""
__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}

import cv2
from _alg import Algorithm
from gui_prototypes.Philipp.algorithm_1 import IntegerSlider


class AlgBody(Algorithm):
    """Blur algorithm implementation"""
    def __init__(self):
        """
        Blur object constructor
        Instance vars:
            self.name -- name of the algorithm
            self.parent -- name of the appropriated category
            self.kernelsize -- kernelsize that will be used as slider for the UI
        """
        self.name = "Blur"
        self.parent = "Preprocessing"
        self.kernelsize = IntegerSlider(self,"kernelsize",1,1,20)

    def process(self, image):
        """
        Use the opencv package to blur the current image
        Args:
            image: image instance

        Returns: the blured image

        """
        return cv2.blur(image,(self.kernelsize.value*2+1,self.kernelsize.value*2+1))

    def belongs(self):
        """
        Define method membership (category)
        Returns: name of the appropriated category

        """
        return self.parent

    def get_name(self):
        """
        Define algorithm name that will be displayed in UI
        Returns: algorithm name

        """
        return self.name

    def sign(self, image, settings):
        """
        Save the name of the current algorithm and settings used to process
        the image in the image class
        Args:
            image: image instance
            settings: dict of settings used by the algorithm

        Returns:

        """
        image.sign(self.name, settings)

if __name__ == '__main__':
    pass
