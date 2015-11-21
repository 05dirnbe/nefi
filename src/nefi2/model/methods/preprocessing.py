# -*- coding: utf-8 -*-

import _meth


__meth_name__ = 'Preprocessing'


def get_name():
    return __meth_name__


def new(methmap):
    return _meth.Method(get_name(), methmap)


if __name__ == '__main__':
    pass
