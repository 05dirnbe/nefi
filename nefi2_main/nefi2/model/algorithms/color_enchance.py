# -*- coding: utf-8 -*-
"""
Actual algorithm implementation.

:license: BSD
"""

import cv2


__algorithm__ = 'Color enhancement'
__belongs2__ = 'Preprocessing'
__settings__ = 'Left percentage, Right percentage'


import _alg

def bilateral():
    pass

def process(image):
    _alg.Algorithm.process(image, __belongs2__, bilateral)


if __name__ == '__main__':
    pass
