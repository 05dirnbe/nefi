# -*- coding: utf-8 -*-

"""
This class represents the algorithm Watershed from the opencv package
"""
import cv2
import numpy as np
from nefi2.model.algorithms._alg import *

__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}


class AlgBody(Algorithm):
    """
    Watershed(dilation and erosion) algorithm implementation
    """

    def __init__(self):
        """Watershed object constructor
            Instance vars:
                | *name* : name of the algorithm
                | *parent* : name of the appropriated category
                | *fgiter* : number of erode iterations
                | *bgiter* : number of dilation iterations

        """
        Algorithm.__init__(self)
        self.name = "Guided Watershed with deletion and erosion"
        self.parent = "Segmentation"
        self.fgiter = IntegerSlider("Foreground iterations", 1, 10, 1, 1)
        self.bgiter = IntegerSlider("Background iterations", 1, 10, 1, 1)
        self.integer_sliders.append(self.fgiter)
        self.integer_sliders.append(self.bgiter)

    def process(self, args):
        """
        Use the Watershed algorithm from the opencv package
        to the selected color channels of the current image

        Args:
            | *args* : a list containing image array and Graph object
        """
        image = args[0]
        im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(im_gray, 0, 255,
                                    cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        fg = cv2.erode(thresh, None, iterations=self.fgiter)
        bgt = cv2.dilate(thresh, None, iterations=self.bgiter)
        ret, bg = cv2.threshold(bgt, 1, 128, 1)
        marker = cv2.add(fg, bg)
        marker32 = np.int32(marker)
        cv2.watershed(image, marker32)
        m = cv2.convertScaleAbs(marker32)
        ret, thresh = cv2.threshold(m, 0, 255,
                                    cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        self.result['img'] = cv2.bitwise_and(image, image, mask=thresh)


if __name__ == '__main__':
    pass
