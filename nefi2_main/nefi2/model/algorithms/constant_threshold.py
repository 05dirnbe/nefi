# -*- coding: utf-8 -*-

__algorithm__ = 'Constant Threshold'
__belongs2__ = 'Segmentation'


import _alg

def constant_threshold():
    pass

def process(image):
    _alg.Algorithm.process(image, __belongs2__, constant_threshold)


if __name__ == '__main__':
    pass
