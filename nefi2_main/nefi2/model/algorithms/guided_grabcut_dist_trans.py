# -*- coding: utf-8 -*-

__algorithm__ = 'Guided Grabcut with distance transform'
__belongs2__ = 'Segmentation'


import _alg

def guided_grabcut_dist_trans():
    pass

def process(image):
    _alg.Algorithm.process(image, __belongs2__, guided_grabcut_dist_trans)

if __name__ == '__main__':
    pass
