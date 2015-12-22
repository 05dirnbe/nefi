# -*- coding: utf-8 -*-
"""
This class represents the algorithm Fast nl Means Denoising from the opencv package
"""
__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}

from _alg import Algorithm, FloatSlider, IntegerSlider


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
        self.filterStrength = FloatSlider(self,"filter strength",0,0,100)
        self.templateWindowSize = IntegerSlider(self,"template window size",0,0,100)
        self.searchWindowSize = IntegerSlider(self,"search window size",0,0,200)

    def process(self, image):
        """
        Use the Fast nl Means Denoising algorithm from the opencv package to the current image
        Args:
            image: image instance

        """
        self.result = cv2.fastNlMeansDenoising(image,self.filterStrength,self.templateWindowSize,self.searchWindowSize)


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
