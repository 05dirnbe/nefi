# -*- coding: utf-8 -*-
"""
Tests for the simple cycle algorithm
"""
from largest_connected import AlgBody as largest_body
from guo_hall import AlgBody as guo_body
from blur import AlgBody as blur_body
from adaptive import AlgBody as adaptive_body
import cv2
import unittest
import networkx as nx


__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com",
               "Martino Bruni": "bruni.martino92@gmail.com"}

class Largest_connected_test(unittest.TestCase):

    def test_instantiation(self):
        """
        Test the instantiation.
        """
        alg = largest_body()
        self.assertEqual(alg.name, "Keep only largest connected component")
        self.assertEqual(alg.parent, "Graph filtering")

    def test_process(self):

        alg= largest_body()

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
        should_graph = max(nx.connected_component_subgraphs(
            gd_alg.result['graph']), key=len)

        #All the attribute of the graphs are equals but running
        #the test for the 2 object we got error
        #self.assertEqual(alg.result['graph'],should_graph)

        self.assertEqual(alg.result['graph'].adjlist_dict_factory,
                         should_graph.adjlist_dict_factory)
        self.assertEqual(alg.result['graph'].edge_attr_dict_factory,
                         should_graph.edge_attr_dict_factory)
        self.assertEqual(alg.result['graph'].node_dict_factory,
                         should_graph.node_dict_factory)
        self.assertEqual(alg.result['graph'].adj,should_graph.adj)
        self.assertEqual(alg.result['graph'].edge,should_graph.edge)
        self.assertEqual(alg.result['graph'].node,should_graph.node)
        self.assertEqual(alg.result['graph'].name,should_graph.name)
        self.assertEqual(alg.result['graph'].graph,should_graph.graph)




if __name__ == '__main__':
    unittest.main()