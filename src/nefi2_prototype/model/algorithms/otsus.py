# -*- coding: utf-8 -*-
import cv2 as cv

__algorithm__ = 'Otsus Threshold'
__belongs2__ = 'Segmentation'

#Segmentation routines
THRESHOLD_FG_COLOR = 255
THRESHOLD_BG_COLOR = 0

def process(image, settings):
    """Replace this stub with actual implementation."""
    print '> Algorithm: "blur" processing "%s" with "%s"' % (image, settings)
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

def otsus_threshold(image, threshold_value=0, threshold_type=cv.THRESH_OTSU):
    """
    Computes a threshold image of the source image using the otsus threshold value.

    Args:
        Image: An input image which will not be changed

    Returns:
        A threshold image
    """
    grayscale_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    threshold_image = cv.threshold(grayscale_image, threshold_value, THRESHOLD_FG_COLOR, threshold_type)[1]

    return threshold_image

if __name__ == '__main__':
    pass
