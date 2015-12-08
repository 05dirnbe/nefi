# -*- coding: utf-8 -*-

__algorithm__ = 'Guided Grabcut with deletion and erosion'
__belongs2__ = 'Segmentation'


import _alg

def guided_grabcut_delerosion():
    pass

def process(image):
    _alg.Algorithm.process(image, __belongs2__, guided_grabcut_delerosion)


if __name__ == '__main__':
    pass
