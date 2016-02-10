# -*- coding: utf-8 -*-


import numpy as np
from otsus import *
from ImageSegmentationCollection import *
import cv2
import unittest

class TestOtsusThreshold(unittest.TestCase):

  def test_instantiation(self):
    obj = AlgBody()
    self.assertEqual(obj.name, "Otsu's Threshold")
    self.assertEqual(obj.parent, "Segmentation")

  def test_segmentation(self):
    obj1 = AlgBody()

    test_image = cv2.imread("NEFI1_Images/p_polycephalum.jpg")
    ref_image1 = otsus_threshold(src=test_image)
    ref_image1 = cv2.cvtColor(ref_image1, cv2.COLOR_BGR2GRAY)

    input = [test_image]
    obj1.process(input)
    h,w = obj1.result["img"].shape
    for i in range(h):
        for j in range(w):
            test_val1 = obj1.result["img"].item(i,j)
            ref_val1 = ref_image1.item(i,j)
            diff_ob1 = abs(test_val1-ref_val1)
            self.assertEqual(diff_ob1,0)


if __name__ == '__main__':
    unittest.main()