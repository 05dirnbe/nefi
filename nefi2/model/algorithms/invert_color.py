# -*- coding: utf-8 -*-

__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}

from _alg import Algorithm


class AlgBody(Algorithm):
    """Invert Color algorithm implementation"""
    def __init__(self):
        self.name = "Invert Color"
        self.parent = "Preprocessing"

    def process(self, image):
        """
        Invert the image
        Args:
            image: image instance

        Returns: inverted image

        """
        return (255-image)


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




