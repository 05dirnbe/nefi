#!/usr/bin/env python3
"""
Tutorial Algorithm
Reduce image size using predefined ratio value.
"""
from nefi2.model.algorithms._alg import Algorithm, IntegerSlider
import cv2


class AlgBody(Algorithm):
    """OpenCV image size reduction implementation"""
    def __init__(self):
        Algorithm.__init__(self)
        self.name = "Image Reduce"
        self.parent = "Preprocessing"
        self.ratio = IntegerSlider("Reduction %", 1, 100, 1, 50)
        self.integer_sliders.append(self.ratio)

    def process(self, args):
        """
        Args
            |*img* (ndarray): image array

        """
        ratio = 1 - (self.ratio.value / 100)
        smaller = cv2.resize(args[0], (0, 0), fx=ratio, fy=ratio,
                             interpolation=cv2.INTER_AREA)
        self.result['img'] = smaller


if __name__ == '__main__':
    pass
