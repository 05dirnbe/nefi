# -*- coding: utf-8 -*-

__algorithm__ = 'Blur'
__belongs2__ = 'Preprocessing'


def apply(image, settings):
    """Replace this stub with actual implementation."""
    print '> Algorithm: "blur" processing "%s" with "%s"' % (image, settings)
    return 0


def belongs():
    """Define method membership."""
    return __belongs2__


def get_name():
    """Return algorithm name that will be displayed in UI."""
    return __algorithm__


if __name__ == '__main__':
    pass
