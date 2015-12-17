# -*- coding: utf-8 -*-

from _alg import Algorithm


class AlgBody(Algorithm):
    """Guided Grabcut with distance transform algorithm implementation"""
    def __init__(self):
        self.name = "Guided Grabcut with distance transform"
        self.parent = "Segmentation"

    def process(self, image):
        pass


if __name__ == '__main__':
    pass

