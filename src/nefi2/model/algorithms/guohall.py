# -*- coding: utf-8 -*-

__algorithm__ = 'Guo Hall graph detector'
__belongs2__ = 'Graph detection'


def apply(image, settings):
    """Replace this stub with actual implementation."""
    print '> Algorithm: "blur" processing "%s" with "%s"' % (image, settings)
    sign(image, settings)
    return 'GRAPH'


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


if __name__ == '__main__':
    pass
