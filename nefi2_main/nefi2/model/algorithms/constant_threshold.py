# -*- coding: utf-8 -*-

from _alg import Algorithm


class Body(Algorithm):
    """Constant Threshold algorithm implementation"""
    def __init__(self):
        self.name = "Constant Threshold"
        self.parent = "Segmentation"

    def process(self, image):
        pass


if __name__ == '__main__':
    pass
