# -*- coding: utf-8 -*-


import numpy as np
from grabcut_distance_transform_otsu import *
import unittest

class TestGrabcutDilationErosionOtsu(unittest.TestCase):

  def test_instantiation(self):
    obj = AlgBody()
    self.assertEqual(len(obj.integer_sliders), 3)
    self.assertEqual(obj.name, "Grabcut - Distance Transform Otsu")
    self.assertEqual(obj.parent, "Segmentation")
    self.assertEqual(obj.integer_sliders[0].name, "Foreground Iteration")
    self.assertEqual(obj.integer_sliders[0].lower, 1)
    self.assertEqual(obj.integer_sliders[0].upper, 10)
    self.assertEqual(obj.integer_sliders[0].step_size, 1)
    self.assertEqual(obj.integer_sliders[0].value, 2)
    self.assertEqual(obj.integer_sliders[1].name, "Background Iteration")
    self.assertEqual(obj.integer_sliders[1].lower, 1)
    self.assertEqual(obj.integer_sliders[1].upper, 10)
    self.assertEqual(obj.integer_sliders[1].step_size, 1)
    self.assertEqual(obj.integer_sliders[1].value, 1)
    self.assertEqual(obj.integer_sliders[2].name, "GrabCut Iteration")
    self.assertEqual(obj.integer_sliders[2].lower, 1)
    self.assertEqual(obj.integer_sliders[2].upper, 10)
    self.assertEqual(obj.integer_sliders[2].step_size, 1)
    self.assertEqual(obj.integer_sliders[2].value, 5)

  def test_slider_setter(self):
    obj = AlgBody()
    obj.integer_sliders[0].set_value(1)
    self.assertEqual(obj.integer_sliders[0].value, 1)
    self.assertEqual(obj.fg_iter.value, 1)
    obj.integer_sliders[0].set_value(10)
    self.assertEqual(obj.integer_sliders[0].value, 10)
    self.assertEqual(obj.fg_iter.value, 10)

    obj.integer_sliders[1].set_value(5)
    self.assertEqual(obj.integer_sliders[1].value, 5)
    self.assertEqual(obj.bg_iter.value, 5)
    obj.integer_sliders[1].set_value(10)
    self.assertEqual(obj.integer_sliders[1].value, 10)
    self.assertEqual(obj.bg_iter.value, 10)

    obj.integer_sliders[2].set_value(2)
    self.assertEqual(obj.integer_sliders[2].value, 2)
    self.assertEqual(obj.gc_iter.value, 2)
    obj.integer_sliders[2].set_value(10)
    self.assertEqual(obj.integer_sliders[2].value, 10)
    self.assertEqual(obj.gc_iter.value, 10)

''' Functionality test against NEFI1 not possible, since Grabcut seems to be
    non-deterministic. If you put the same image, as well as the
    same parameters for fg_iter, bg_iter and gc_iter into NEFI 1 twice
    and build a difference image of the both results you get small differences
    in the segmentation'''


if __name__ == '__main__':
    unittest.main()