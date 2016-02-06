# -*- coding: utf-8 -*-


from constant_threshold import *
from ImageSegmentationCollection import *
import cv2
import unittest

class TestConstantThreshold(unittest.TestCase):

  def test_instantiation(self):
    obj = AlgBody()
    self.assertEqual(len(obj.integer_sliders), 1)
    self.assertEqual(obj.name, "Constant Threshold")
    self.assertEqual(obj.parent, "Segmentation")
    self.assertEqual(obj.integer_sliders[0].name, "Threshold")
    self.assertEqual(obj.integer_sliders[0].lower, 1)
    self.assertEqual(obj.integer_sliders[0].upper, 254)
    self.assertEqual(obj.integer_sliders[0].step_size, 1)
    self.assertEqual(obj.integer_sliders[0].value, 127)

  def test_slider_setter(self):
    obj = AlgBody()
    obj.integer_sliders[0].set_value(1)
    self.assertEqual(obj.integer_sliders[0].value, 1)
    self.assertEqual(obj.threshold.value, 1)
    obj.integer_sliders[0].set_value(254)
    self.assertEqual(obj.integer_sliders[0].value, 254)
    self.assertEqual(obj.threshold.value, 254)

  def test_segmentation(self):
    obj1 = AlgBody()
    obj2 = AlgBody()
    obj2.integer_sliders[0].set_value(203)

    test_image = cv2.imread("NEFI1_Images/p_polycephalum.jpg")
    ref_image1 = constant_threshold(src=test_image,threshold_value=127)
    ref_image2 = constant_threshold(src=test_image,threshold_value=203)
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