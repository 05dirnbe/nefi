# -*- coding: utf-8 -*-

__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}

from nefi2.model.algorithms._alg import *


class AlgBody(Algorithm):
    """Color enhancement algorithm implementation"""

    def report_pip(self):
        """
        Todo: implement
        Returns:

        """
        pass

    def __init__(self):
        Algorithm.__init__(self)
        self.name = "Color enhancement"
        self.parent = "Preprocessing"

    def process(self, image):
        pass

if __name__ == '__main__':
    pass
