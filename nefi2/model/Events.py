# -*- coding: utf-8 -*-
"""
"""

__authors__ = {"Dennis Groß": "gdennis91@googlemail.com"}

class ProgressEvent(object):
    """
    This event is used to report the progress back to the maincontroller
    """

    def __init__(self, value, report):
        self.value = value
        self.report = report


class CacheEvent(object):
    """
    This event is used to report the maincontroller the new cached image
    """

    def __init__(self, cat, path):
        self.cat = cat
        self.path = path


if __name__ == '__main__':
    pass
