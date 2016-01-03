# -*- coding: utf-8 -*-

from _alg import Algorithm


class AlgBody(Algorithm):
    """Keep only largest connected component algorithm implementation"""
    def __init__(self):
        Algorithm.__init__(self)
        self.name = "Keep only largest connected component"
        self.parent = "Graph filtering"

    def process(self, image):
        pass


if __name__ == '__main__':
    pass


