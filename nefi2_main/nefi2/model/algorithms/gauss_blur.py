# -*- coding: utf-8 -*-

__algorithm__ = 'Gaussian Blur'
__belongs2__ = 'Preprocessing'


import _alg

def gauss_blur():
    pass

def process(image):
    _alg.Algorithm.process(image, __belongs2__, gauss_blur)

if __name__ == '__main__':
    pass
