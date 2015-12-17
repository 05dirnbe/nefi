# -*- coding: utf-8 -*-

from _alg import Algorithm


class AlgBody(Algorithm):
    """Blur algorithm implementation"""
    def __init__(self):
        """
        We are not calling super() here because we don't need anything
        from Algorithm, yet.
        """
        self.name = "Blur"
        self.parent = "Preprocessing"

    def process(self, image):
        pass


if __name__ == '__main__':
    pass
