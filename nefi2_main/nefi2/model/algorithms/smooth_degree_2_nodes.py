# -*- coding: utf-8 -*-

__algorithm__ = 'Smooth degree 2 nodes'
__belongs2__ = 'Graph filtering'


import _alg

def smooth_degree_2_nodes():
    pass

def process(image):
    _alg.Algorithm.process(image, __belongs2__, smooth_degree_2_nodes)


if __name__ == '__main__':
    pass
