# -*- coding: utf-8 -*-

from _alg import Algorithm


class Body(Algorithm):
    """Guided Watershed with deletion and erosion algorithm implementation"""
    def __init__(self):
        self.name = "Guided Watershed with distance transform"
        self.parent = "Segmentation"

    def process(self, image):
        pass


if __name__ == '__main__':
    pass


