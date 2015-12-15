# -*- coding: utf-8 -*-

import _step


__step_name__ = 'Preprocessing'


def get_name():
    """
    Return method name that will be displayed in UI.
    Args:
        __algorithm__ -- algorithm's name to be displayed in UI
    """
    return __step_name__


def new(imported_algs):
    """
    Create a new Method instance.
    Args:
        imported_algs -- a list of imported algorithm files
    """
    return _step.Step(get_name(), imported_algs)


if __name__ == '__main__':
    pass
