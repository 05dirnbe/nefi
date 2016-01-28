# -*- coding: utf-8 -*-
"""
Tests for the guo hall thinning algorithm
"""
from nefi2.model.algorithms.guo_hall import *
import cv2
import unittest

__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}

class GuoHallTest(unittest.TestCase):

    def test_instantiation(self):
        """
        Test for the instantiation.
        """
        alg = AlgBody()
        self.assertEqual(alg.name, "Guo Hall Thinning")
        self.assertEqual(alg.parent, "Graph detection")

    def test_use(self):
        alg = AlgBody()
        test_image =cv2.imread("guohall_input.jpg")
        output = alg.process(test_image)
        self.assertEqual(output,"guohall_output.jpg")

if __name__ == '__main__':
    unittest.main()