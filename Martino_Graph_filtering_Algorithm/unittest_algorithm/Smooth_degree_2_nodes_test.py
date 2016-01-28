# -*- coding: utf-8 -*-
import unittest
import networkx as nx
import cv2
from Martino_Graph_filtering_Algorithm.Smooth_degree_two_nodes import AlgBody as Smooth_body
from nefi2.model.algorithms.guo_hall import AlgBody as guo_body
from nefi2.model.algorithms.blur import AlgBody as blur_body
from nefi2.model.algorithms.adaptive import AlgBody as adaptive_body
import operator as op

__authors__ = {"Martino Bruni": "bruni.martino92@gmail.com"}

class Test_Edge_attribute (unittest.TestCase):

    def test_init(self):
        alg = Smooth_body()
        self.assertEqual(alg.name,"Smooth degree 2 nodes")
        self.assertEqual(alg.parent, "Graph filtering")

    def test_process(self):
        alg=Smooth_body()

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
        should_graph = gd_alg.result['graph']
        to_be_removed = [(u, v) for u, v, data in
                             graph.edges_iter(data=True)
                if op.lt(data["width"],10.0)]
        graph.remove_edges_from(to_be_removed)

        self.assertEqual(alg.result['graph'],graph)
        self.assertEqual(alg.result['img'],img_array)

    def should_alg(self):




if __name__ == '__main__':
    unittest.main()
