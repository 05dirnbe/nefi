# -*- coding: utf-8 -*-


import numpy as np
from blur import *
import cv2
import unittest

class TestBlur(unittest.TestCase):

  def test_instantiation(self):
    obj = AlgBody()
    self.assertEqual(len(obj.integer_sliders), 1)
    self.assertEqual(obj.name, "Blur")
    self.assertEqual(obj.parent, "Preprocessing")
    self.assertEqual(obj.integer_sliders[0].name, "kernelsize")
    self.assertEqual(obj.integer_sliders[0].lower, 1)
    self.assertEqual(obj.integer_sliders[0].upper, 20)
    self.assertEqual(obj.integer_sliders[0].step_size, 1)
    self.assertEqual(obj.integer_sliders[0].value, 1)

    self.assertEqual(len(obj.checkboxes), 3)
    self.assertEqual(obj.checkboxes[0].name, "channel1")
    self.assertEqual(obj.checkboxes[0].value, True)
    self.assertEqual(obj.checkboxes[1].name, "channel2")
    self.assertEqual(obj.checkboxes[0].value, True)
    self.assertEqual(obj.checkboxes[2].name, "channel3")
    self.assertEqual(obj.checkboxes[0].value, True)

  def test_slider_setter(self):
    obj = AlgBody()
    obj.integer_sliders[0].set_value(5)
    self.assertEqual(obj.integer_sliders[0].value, 5)
    self.assertEqual(obj.kernelsize.value, 5)
    obj.integer_sliders[0].set_value(10)
    self.assertEqual(obj.integer_sliders[0].value, 10)
    self.assertEqual(obj.kernelsize.value, 10)

    obj.checkboxes[0].set_value(False)
    obj.checkboxes[1].set_value(False)
    obj.checkboxes[2].set_value(False)
    self.assertEqual(obj.checkboxes[0].value, False)
    self.assertEqual(obj.checkboxes[0].value, False)
    self.assertEqual(obj.checkboxes[0].value, False)
    obj.checkboxes[0].set_value(True)
    obj.checkboxes[1].set_value(True)
    obj.checkboxes[2].set_value(True)
    self.assertEqual(obj.checkboxes[0].value, True)
    self.assertEqual(obj.checkboxes[0].value, True)
    self.assertEqual(obj.checkboxes[0].value, True)

  def test_process_whole_channels(self):
    obj1 = AlgBody()
    obj2 = AlgBody()
    obj2.integer_sliders[0].set_value(5)
    test_image = cv2.imread("NEFI1_Images/p_polycephalum.jpg")
    ref_image1 = cv2.blur(test_image, (3, 3))
    ref_image2 = cv2.blur(test_image, (11, 11))
    input = [test_image]
    obj1.process(input)
    obj2.process(input)
    h,w,d = obj1.result["img"].shape
    for i in range(h):
        for j in range(w):
            for k in range(d):
                test_val1 = obj1.result["img"].item(i,j,k)
                test_val2 = obj2.result["img"].item(i,j,k)
                ref_val1 = ref_image1.item(i,j,k)
                ref_val2 = ref_image2.item(i,j,k)
                diff_ksize3 = abs(test_val1-ref_val1)
                diff_ksize11 = abs(test_val2-ref_val2)
                self.assertEqual(diff_ksize3,0)
                self.assertEqual(diff_ksize11,0)

  def test_greyscale(self):
    obj1 = AlgBody()
    obj2 = AlgBody()
    obj2.integer_sliders[0].set_value(5)
    test_img = cv2.imread("NEFI1_Images/p_polycephalum.jpg")
    test_image = cv2.cvtColor(test_img, cv2.COLOR_RGB2GRAY)
    ref_image1 = cv2.blur(test_image, (3, 3))
    ref_image2 = cv2.blur(test_image, (11, 11))
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
                diff_ksize3 = abs(test_val1-ref_val1)
                diff_ksize11 = abs(test_val2-ref_val2)
                self.assertEqual(diff_ksize3,0)
                self.assertEqual(diff_ksize11,0)

  def test_process_separate_channels(self):
    obj1 = AlgBody()
    obj2 = AlgBody()
    obj3 = AlgBody()
    obj4 = AlgBody()

    obj1.checkboxes[0].set_value(False)
    obj1.checkboxes[1].set_value(False)
    obj1.checkboxes[2].set_value(False)

    obj2.checkboxes[0].set_value(True)
    obj2.checkboxes[1].set_value(False)
    obj2.checkboxes[2].set_value(False)

    obj3.checkboxes[0].set_value(False)
    obj3.checkboxes[1].set_value(True)
    obj3.checkboxes[2].set_value(False)

    obj4.checkboxes[0].set_value(False)
    obj4.checkboxes[1].set_value(False)
    obj4.checkboxes[2].set_value(True)

    test_image = cv2.imread("NEFI1_Images/p_polycephalum.jpg")
    input = [test_image]
    ref_image1 = cv2.blur(test_image, (3, 3))

    channels_original = cv2.split(test_image)
    channels_ref = cv2.split(ref_image1)

    obj1.process(input)
    obj2.process(input)
    obj3.process(input)
    obj4.process(input)

    channels_obj1 = cv2.split(obj1.result["img"])
    channels_obj2 = cv2.split(obj2.result["img"])
    channels_obj3 = cv2.split(obj3.result["img"])
    channels_obj4 = cv2.split(obj4.result["img"])

    h, w, d = test_image.shape
    for i in range(h):
        for j in range(w):
          test_val_original_c1 = channels_original[0].item(i,j)
          test_val_original_c2 = channels_original[1].item(i,j)
          test_val_original_c3 = channels_original[2].item(i,j)

          test_val_ref_c1 = channels_ref[0].item(i,j)
          test_val_ref_c2 = channels_ref[1].item(i,j)
          test_val_ref_c3 = channels_ref[2].item(i,j)

          test_val_o1_c1 = channels_obj1[0].item(i,j)
          test_val_o1_c2 = channels_obj1[1].item(i,j)
          test_val_o1_c3 = channels_obj1[2].item(i,j)

          test_val_o2_c1 = channels_obj2[0].item(i,j)
          test_val_o2_c2 = channels_obj2[1].item(i,j)
          test_val_o2_c3 = channels_obj2[2].item(i,j)

          test_val_o3_c1 = channels_obj3[0].item(i,j)
          test_val_o3_c2 = channels_obj3[1].item(i,j)
          test_val_o3_c3 = channels_obj3[2].item(i,j)

          test_val_o4_c1 = channels_obj4[0].item(i,j)
          test_val_o4_c2 = channels_obj4[1].item(i,j)
          test_val_o4_c3 = channels_obj4[2].item(i,j)

          diff_o1_c1 = test_val_o1_c1 - test_val_original_c1
          diff_o1_c2 = test_val_o1_c2 - test_val_original_c2
          diff_o1_c3 = test_val_o1_c3 - test_val_original_c3

          diff_o2_c1 = test_val_o2_c1 - test_val_ref_c1
          diff_o2_c2 = test_val_o2_c2 - test_val_original_c2
          diff_o2_c3 = test_val_o2_c3 - test_val_original_c3

          diff_o3_c1 = test_val_o3_c1 - test_val_original_c1
          diff_o3_c2 = test_val_o3_c2 - test_val_ref_c2
          diff_o3_c3 = test_val_o3_c3 - test_val_original_c3

          diff_o4_c1 = test_val_o4_c1 - test_val_original_c1
          diff_o4_c2 = test_val_o4_c2 - test_val_original_c2
          diff_o4_c3 = test_val_o4_c3 - test_val_ref_c3

          self.assertEqual(diff_o1_c1,0)
          self.assertEqual(diff_o1_c2,0)
          self.assertEqual(diff_o1_c3,0)

          self.assertEqual(diff_o2_c1,0)
          self.assertEqual(diff_o2_c2,0)
          self.assertEqual(diff_o2_c3,0)

          self.assertEqual(diff_o3_c1,0)
          self.assertEqual(diff_o3_c2,0)
          self.assertEqual(diff_o3_c3,0)

          self.assertEqual(diff_o4_c1,0)
          self.assertEqual(diff_o4_c2,0)
          self.assertEqual(diff_o4_c3,0)

if __name__ == '__main__':
    unittest.main()