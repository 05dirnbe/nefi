# -*- coding: utf-8 -*-
"""
Tests for the simple cycle algorithm
"""
from nefi2.model.algorithms.guo_hall import *
import cv2
import unittest

__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}

class GuoHallTest(unittest.TestCase):

    def test_instantiation(self):
        """
        Test the instantiation.
        """
        alg = AlgBody()
        self.assertEqual(alg.name, "Simple cycle filter")
        self.assertEqual(alg.parent, "Graph filtering")


if __name__ == '__main__':
    unittest.main()