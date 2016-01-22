# -*- coding: utf-8 -*-


import numpy as np
from Sebastian_Algorithms_untested.invert_color import *
import cv2
import unittest

class TestBlur(unittest.TestCase):

  def test_instantiation(self):
    obj = AlgBody()
    self.assertEqual(obj.name, "Invert Color")
    self.assertEqual(obj.parent, "Preprocessing")

    self.assertEqual(len(obj.checkboxes), 3)
    self.assertEqual(obj.checkboxes[0].name, "channel1")
    self.assertEqual(obj.checkboxes[0].value, True)
    self.assertEqual(obj.checkboxes[1].name, "channel2")
    self.assertEqual(obj.checkboxes[0].value, True)
    self.assertEqual(obj.checkboxes[2].name, "channel3")
    self.assertEqual(obj.checkboxes[0].value, True)

  def test_slider_setter(self):
    obj = AlgBody()

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
    test_image = cv2.imread("NEFI1_Images/p_polycephalum.jpg")
    obj1.process(test_image)
    obj2.process(obj1.result)
    h,w,d = obj1.result.shape
    for i in range(h):
        for j in range(w):
            for k in range(d):
                test_val1 = obj2.result.item(i,j,k)
                ref_val1 = test_image.item(i,j,k)
                diff = abs(test_val1-ref_val1)
                self.assertEqual(diff,0)

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

    channels_original = cv2.split(test_image)

    obj1.process(test_image)
    obj2.process(test_image)
    obj3.process(test_image)
    obj4.process(test_image)

    channels_obj1 = cv2.split(obj1.result)
    channels_obj2 = cv2.split(obj2.result)
    channels_obj3 = cv2.split(obj3.result)
    channels_obj4 = cv2.split(obj4.result)

    h, w, d = test_image.shape
    for i in range(h):
        for j in range(w):
          test_val_original_c1 = channels_original[0].item(i,j)
          test_val_original_c2 = channels_original[1].item(i,j)
          test_val_original_c3 = channels_original[2].item(i,j)

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

          diff_o2_c1 = 255 - test_val_o2_c1
          diff_o2_c2 = test_val_o2_c2 - test_val_original_c2
          diff_o2_c3 = test_val_o2_c3 - test_val_original_c3

          diff_o3_c1 = test_val_o3_c1 - test_val_original_c1
          diff_o3_c2 = 255 - test_val_o3_c2
          diff_o3_c3 = test_val_o3_c3 - test_val_original_c3

          diff_o4_c1 = test_val_o4_c1 - test_val_original_c1
          diff_o4_c2 = test_val_o4_c2 - test_val_original_c2
          diff_o4_c3 = 255 - test_val_o4_c3

          self.assertEqual(diff_o1_c1,0)
          self.assertEqual(diff_o1_c2,0)
          self.assertEqual(diff_o1_c3,0)

          self.assertEqual(diff_o2_c1,test_val_o1_c1)
          self.assertEqual(diff_o2_c2,0)
          self.assertEqual(diff_o2_c3,0)

          self.assertEqual(diff_o3_c1,0)
          self.assertEqual(diff_o3_c2,test_val_original_c2)
          self.assertEqual(diff_o3_c3,0)

          self.assertEqual(diff_o4_c1,0)
          self.assertEqual(diff_o4_c2,0)
          self.assertEqual(diff_o4_c3,test_val_original_c3)

if __name__ == '__main__':
    unittest.main()