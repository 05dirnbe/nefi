# -*- coding: utf-8 -*-

import _meth


__meth_name__ = 'Graph detection'


def get_name():
    """
    Return method name that will be displayed in UI.
    Args:
        __algorithm__ -- algorithm's name to be displayed in UI
    """
    return __meth_name__


def new(methmap):
    """
    Create a new Method instance.
    Args:
        methmap -- a simple dict mapping: algorithm --> method
    """
    return _meth.Method(get_name(), methmap)


if __name__ == '__main__':
    pass
