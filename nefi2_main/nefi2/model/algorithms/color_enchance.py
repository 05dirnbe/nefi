# -*- coding: utf-8 -*-

from _alg import Algorithm


class Body(Algorithm):
    """Color enhancement algorithm implementation"""
    def __init__(self):
        self.name = "Color enhancement"
        self.parent = "Preprocessing"

    def process(self, image):
        pass


if __name__ == '__main__':
    pass
