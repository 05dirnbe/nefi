# -*- coding: utf-8 -*-

__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}

from nefi2.model.algorithms._alg import *


class AlgBody(Algorithm):
    """Fast nl Means Denoising Colored algorithm implementation"""

    def report_pip(self):
        """
        Todo: implement
        Returns:

        """
        pass

    def __init__(self):
        Algorithm.__init__(self)
        self.name = "Fast nl Means Denoising Colored"
        self.parent = "Preprocessing"

    def process(self, image):
        pass


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
            settings: dict of settings used by thealgorithm

        Returns:

        """
        pass
        #image.sign(self.name, settings)

if __name__ == '__main__':
    pass
