# -*- coding: utf-8 -*-
import cv2 as cv

__algorithm__ = 'Otsus Threshold'
__belongs2__ = 'Segmentation'


import _alg

def otsus():
    pass

def process(image):
    _alg.Algorithm.process(image, __belongs2__, otsus)

if __name__ == '__main__':
    pass
