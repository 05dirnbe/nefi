# -*- coding: utf-8 -*-
"""
Actual algorithm implementation.

:license: BSD
"""

import cv2


__algorithm__ = 'Color enhancement'
__belongs2__ = 'Preprocessing'
__settings__ = 'Left percentage, Right percentage'


def process(image, settings):
    # Do something before running the algorithm.
    print '> Algorithm: %s processing "%s" with "%s"' % (__algorithm__, image, settings)
    sign(image, settings)
    return 'NUMPY.NDARRAY'


def belongs():
    """
    Define method membership.
    Args:
        __belongs2__ -- method's name that owns the algorithm
    """
    return __belongs2__


def get_name():
    """
    Return algorithm name that will be displayed in UI.
    Args:
        __algorithm__ -- algorithm's name to be displayed in UI
    """
    return __algorithm__


def sign(image, settings):
    """
    Save the name of the current algorithm and settings used to process the
    image in the Image class.
    Args:
        image -- Image instance
        settings -- dict of settings used by the algorithm
    """
    image.sign(__algorithm__, settings)


######################## UNDER CONSTRUCTION! ##################################
def apply2(func, image='', settings=''):
    """A simple decorator for algorithm function.
        Args:
            func -- a function of algorithm implementation.
            image -- Image instance.
            settings -- a dict of settings provided to the algorithm.
        Returns:
            wrapfun -- a wrapper function for func.
    """
    def wrapfun():
        # Do something before running the algorithm.
        print '> Algorithm: %s processing "%s" with "%s"' % (__algorithm__, image, settings)
        sign(image, settings)
        # Run the algorithm
        func(image, settings)
    return wrapfun
    # return 'NUMPY.NDARRAY'


@apply2
def color_enhancement(src, left_percentage, right_percentage):
    """
    STUB

    :author: Tim
    """
    channels = cv2.split(src)
    for channel in channels:
        vmin = 0
        vmax = 255
        hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
        cdf = hist.cumsum()
        for i, e in enumerate(cdf):
            if e > channel.size * (left_percentage / 100):
                if i != 0:
                    vmin = i - 1
                break
        for i, e in enumerate(cdf):
            if e > channel.size * (1 - (right_percentage / 100)):
                vmax = i
                break
        if vmax != vmin:
            channel[channel < vmin] = vmin
            channel[channel > vmax] = vmax
            channel -= vmin
            channel *= 255.0 / (vmax-vmin)
    return cv2.merge(channels)


if __name__ == '__main__':
    pass
