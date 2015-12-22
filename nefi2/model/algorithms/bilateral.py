# -*- coding: utf-8 -*-
"""
This class represents the algorithm Bilateral filter from the opencv package
"""
__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}

import cv2
from _alg import Algorithm, IntegerSlider, FloatSlider


class AlgBody(Algorithm):
    """Bilateral Filter algorithm implementation"""
    def __init__(self):
        """
        Bilateral filter object constructor
        Instance vars:
            self.name -- name of the algorithm
            self.parent -- name of the appropriated category
            self.diameter -- diameter of each pixel neighborhood that is used during filtering.
                            if it is non-positive, it is computed from sigmaSpace.
            self.sigmaColor -- filter sigma in the color space. The more large the value, the farther colors within
                            the pixel neighborhood will be mixed together
            self.sigmaSpace -- filter sigma in the coordinate space. A larger value of the parameter means
                            that farther pixels will influence each other as long as their colors are close enough
        """
        self.name = "Bilateral Filter"
        self.parent = "Preprocessing"
        self.diameter = IntegerSlider(self,"diameter",1,1,200)
        self.sigmaColor = FloatSlider(self,"sigmaColor",0,0,255)
        self.sigmaSpace = FloatSlider(self,"sigmaSpace",0,0,200)

    def process(self, image):
        """
        Use the bilateral filter from the opencv package to the current image
        Args:
            image: image instance

        """
        self.result = cv2.bilateralFilter(image,self.diameter,self.sigmaColor,self.sigmaSpace)


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
        pass
        #image.sign(self.name, settings)

if __name__ == '__main__':
    pass
