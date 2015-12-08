# -*- coding: utf-8 -*-

import _step


__meth_name__ = 'Preprocessing'


def get_name():
    """
    Return method name that will be displayed in UI.
    Args:
        __algorithm__ -- algorithm's name to be displayed in UI
    """
    return __meth_name__


def new(stepmap):
    """
    Create a new Method instance.
    Args:
        stepmap -- a simple dict mapping: algorithm --> method
    """
    return _step.Step(get_name(), stepmap)


if __name__ == '__main__':
    pass
