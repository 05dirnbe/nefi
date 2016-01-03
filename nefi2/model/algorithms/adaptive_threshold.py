# -*- coding: utf-8 -*-

from nefi2.model.algorithms._alg import *


class AlgBody(Algorithm):
    """Adaptive Threshold algorithm implementation"""

    def report_pip(self):
        pass

    def __init__(self):
        Algorithm.__init__(self)
        self.name = "Adaptive Threshold"
        self.parent = "Segmentation"

    def process(self, image):
        pass


if __name__ == '__main__':
    pass
