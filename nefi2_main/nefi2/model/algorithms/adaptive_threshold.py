# -*- coding: utf-8 -*-

__algorithm__ = 'Adaptive Threshold'
__belongs2__ = 'Segmentation'


import _alg

def adaptive_algorithm():
    pass

def process(image):
    _alg.Algorithm.process(image, __belongs2__, adaptive_algorithm)


if __name__ == '__main__':
    pass
