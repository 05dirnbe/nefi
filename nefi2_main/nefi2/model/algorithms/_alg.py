# -*- coding: utf-8 -*-
"""
This class represents an image processing algorithm interface.
This class abstracts the interface implementation from a user.
"""

class Algorithm:
    def __init__(self, name, belongs_to, process_func):
        self.name = name
        self.belongs = belongs_to
        self.func = process_func

    def process(self, image):
        """Replace this stub with actual implementation."""
        print '> Algorithm: %s processing "%s" with "%s"' % (self.belongs, image)
        return 'NUMPY.NDARRAY'

    def belongs(self):
        """
        Define method membership.
        """
        return self.belongs

    def get_name(self):
        """
        Return algorithm name that will be displayed in UI.
        """
        return self.name


if __name__ == '__main__':
    pass
