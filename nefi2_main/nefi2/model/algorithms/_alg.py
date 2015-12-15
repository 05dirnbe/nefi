# -*- coding: utf-8 -*-
"""
This class represents an interface of an image processing algorithm.
The class abstracts algorithm interface from user so he can fully focus on his
algorithm implementation.
"""


__author__ = "p.shkadzko@gmail.com"


class Algorithm:
    def __init__(self):
        """
        Algorithm class
        Instance vars:
            self.modified -- True if Algorithm settings were modified
            self.belongs -- A step name to which current algorithm belongs
        """
        self.modified = False

        # for debugging only
        #print '> Algorithm: I am "%s" algorithm' % self.name

    def belongs(self):
        """Return a step name to which current algorithm belongs."""
        return self.parent

    def process(self, image):
        """
        A user must override this method in order to comply with the interface.
        Params:
            image -- a path to image file
        """
        raise NotImplementedError

    def get_name(self):
        return self.name

    def set_modified(self):
        """Set True if method settings were modified."""
        #print '> Algorithm: "%s" was modified.' % (self.name)
        self.modified = True

    def get_modified(self):
        return self.modified

    def report_pip(self):
        pass


if __name__ == '__main__':
    pass
