# -*- coding: utf-8 -*-

__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}

import cv2
from _alg import Algorithm
from gui_prototypes.Philipp.algorithm_1 import IntegerSlider


class AlgBody(Algorithm):
    """Gaussian Blur algorithm implementation"""
    def __init__(self):
        self.name = "Gaussian Blur"
        self.parent = "Preprocessing"
        self.kernelsize = IntegerSlider(self,"kernelsize",1,1,20)
        self.sigmaX = IntegerSlider(self,"sigmaX",1,1,100)

    def process(self, image):
        return cv2.GaussianBlur(image,(self.kernelsize.value*2+1,self.kernelsize.value*2+1),self.sigmaX)


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

