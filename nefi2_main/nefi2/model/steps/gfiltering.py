# -*- coding: utf-8 -*-

import _step


__step_name__ = 'Graph filtering'


def get_name():
    """
    Return method name that will be displayed in UI.
    Args:
        __algorithm__ -- algorithm's name to be displayed in UI
    """
    return __step_name__


def new():
    """
    Create a new Method instance.
    Args:
        imported_algs -- a list of imported algorithm files
    """
    return _step.Step(get_name())


if __name__ == '__main__':
    pass
