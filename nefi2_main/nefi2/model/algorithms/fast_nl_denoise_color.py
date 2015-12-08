# -*- coding: utf-8 -*-

__algorithm__ = 'Fast nl Means Denoising Colored'
__belongs2__ = 'Preprocessing'

import _alg

def fast_nl_denoise_color():
    pass

def process(image):
    _alg.Algorithm.process(image, __belongs2__, fast_nl_denoise_color)


if __name__ == '__main__':
    pass
