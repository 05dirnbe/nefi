# -*- coding: utf-8 -*-

__algorithm__ = 'Blur'
__belongs2__ = 'Preprocessing'


import _alg

def blur():
    pass

def process(image):
    _alg.Algorithm.process(image, __belongs2__, blur)


if __name__ == '__main__':
    pass
