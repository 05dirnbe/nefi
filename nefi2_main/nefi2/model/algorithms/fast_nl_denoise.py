# -*- coding: utf-8 -*-

__algorithm__ = 'Fast nl Means Denoising'
__belongs2__ = 'Preprocessing'


import _alg

def fast_nl_denoise():
    pass

def process(image):
    _alg.Algorithm.process(image, __belongs2__, fast_nl_denoise)


if __name__ == '__main__':
    pass
