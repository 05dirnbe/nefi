# -*- coding: utf-8 -*-


import numpy as np
from adaptive import *
from ImageSegmentationCollection import *
import cv2
import unittest

class TestAdaptiveThreshold(unittest.TestCase):

  def test_instantiation(self):
    obj = AlgBody()
    self.assertEqual(len(obj.integer_sliders), 2)
    self.assertEqual(obj.name, "Adaptive Threshold")
    self.assertEqual(obj.parent, "Segmentation")
    self.assertEqual(obj.integer_sliders[0].name, "Threshold Blocksize")
    self.assertEqual(obj.integer_sliders[0].lower, 1)
    self.assertEqual(obj.integer_sliders[0].upper, 20)
    self.assertEqual(obj.integer_sliders[0].step_size, 1)
    self.assertEqual(obj.integer_sliders[0].value, 5)
    self.assertEqual(obj.integer_sliders[1].name, "Threshold Constant")
    self.assertEqual(obj.integer_sliders[1].lower, -10)
    self.assertEqual(obj.integer_sliders[1].upper, 10)
    self.assertEqual(obj.integer_sliders[1].step_size, 1)
    self.assertEqual(obj.integer_sliders[1].value, 2)

  def test_slider_setter(self):
    obj = AlgBody()
    obj.integer_sliders[0].set_value(1)
    self.assertEqual(obj.integer_sliders[0].value, 1)
    self.assertEqual(obj.blocksize.value, 1)
    obj.integer_sliders[0].set_value(10)
    self.assertEqual(obj.integer_sliders[0].value, 10)
    self.assertEqual(obj.blocksize.value, 10)

    obj.integer_sliders[1].set_value(-10)
    self.assertEqual(obj.integer_sliders[1].value, -10)
    self.assertEqual(obj.constant.value, -10)
    obj.integer_sliders[1].set_value(10)
    self.assertEqual(obj.integer_sliders[1].value, 10)
    self.assertEqual(obj.constant.value, 10)

  def test_segmentation(self):
    obj1 = AlgBody()
    obj2 = AlgBody()
    obj2.integer_sliders[0].set_value(10)
    obj2.integer_sliders[1].set_value(8)

    test_image = cv2.imread("NEFI1_Images/p_polycephalum.jpg")
    ref_image1 = adaptive_threshold(src=test_image,constant=2,block_size=11)
    ref_image2 = adaptive_threshold(src=test_image,constant=8,block_size=21)
    ref_image1 = cv2.cvtColor(ref_image1, cv2.COLOR_BGR2GRAY)
    ref_image2 = cv2.cvtColor(ref_image2, cv2.COLOR_RGB2GRAY)

    input = [test_image]
    obj1.process(input)
    obj2.process(input)
    h,w = obj1.result["img"].shape
    for i in range(h):
        for j in range(w):
            test_val1 = obj1.result["img"].item(i,j)
            test_val2 = obj2.result["img"].item(i,j)
            ref_val1 = ref_image1.item(i,j)
            ref_val2 = ref_image2.item(i,j)
            diff_ob1 = abs(test_val1-ref_val1)
            diff_obj2 = abs(test_val2-ref_val2)
            self.assertEqual(diff_ob1,0)
            self.assertEqual(diff_obj2,0)


if __name__ == '__main__':
    unittest.main()