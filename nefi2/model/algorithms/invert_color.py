# -*- coding: utf-8 -*-
"""
This class represents the algorithm Invert Color
"""
__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}

from _alg import Algorithm


class AlgBody(Algorithm):
    """Invert Color algorithm implementation"""
    def __init__(self):
        """
        Invert Color object constructor
        Instance vars:
            self.name -- name of the algorithm
            self.parent -- name of the appropriated category
        """
        self.name = "Invert Color"
        self.parent = "Preprocessing"

    def process(self, image):
        """
        Invert the current image
        Args:
            image: image instance

        """
        self.result =  (255-image)


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




