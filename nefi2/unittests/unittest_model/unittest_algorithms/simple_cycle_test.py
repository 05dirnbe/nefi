# -*- coding: utf-8 -*-
"""
Tests for the simple cycle algorithm
"""
from simple_cycle import *
from guo_hall import AlgBody as guo_body
from blur import AlgBody as blur_body
from adaptive import AlgBody as adaptive_body
import networkx as nx
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

    def test_process(self):
        alg= AlgBody()

        #Detect the graph from an image
        pp_alg = blur_body()
        seg_alg = adaptive_body()
        gd_alg = guo_body()
        img = cv2.imread("p_polycephalum.jpg")
        graph = ""
        pp_alg.process([img,graph])
        seg_alg.process([pp_alg.result['img'],pp_alg.result['graph']])
        gd_alg.process([seg_alg.result['img'],seg_alg.result['graph']])

        alg.process([gd_alg.result['img'],gd_alg.result['graph']])

        #Should be
        graph = self.should_alg(gd_alg.result['graph'])

        self.assertEqual(alg.result['graph'],graph)

    def should_alg(self,arg):

        nodes_not_in_a_cycle = set(arg.nodes())
        # filter all nodes which are not in a biconnected component
        for component in nx.biconnected_components(arg):
            if len(component) > 2:
                nodes_not_in_a_cycle -= component
        # remove all nodes which are not in a biconnected component from
        # the graph
        arg.remove_nodes_from(nodes_not_in_a_cycle)
        return arg


if __name__ == '__main__':
    unittest.main()