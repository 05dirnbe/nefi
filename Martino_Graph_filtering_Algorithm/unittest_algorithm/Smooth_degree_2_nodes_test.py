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
        graph = self.should_alg(gd_alg.result['graph'])

        self.assertEqual(alg.result['graph'],graph)

    def should_alg(self,input_data):

        degree_two_nodes = [v for v in input_data.nodes_iter()
                            if input_data.degree(v) == 2]

        nodes_removed = []

        for n in degree_two_nodes:

            old_edges_data = []
            new_edge_data = {}

            neighbors = input_data.neighbors(n)
            n1 = neighbors[0]
            n2 = neighbors[1]

            for e in input_data.edges(n):
                old_edges_data.append(input_data.get_edge_data(*e))

            for d in old_edges_data:

                for key, value in d.items():

                    if key in ['length', 'pixels']:

                        if key in new_edge_data.keys():
                            new_edge_data[key] += value
                        else:
                            new_edge_data[key] = value

                    elif key in ['width']:

                        if key in new_edge_data.keys():
                            new_edge_data[key] += value * 0.5
                        else:
                            new_edge_data[key] = value * 0.5

                    else:
                        pass

            sample_size_1 = old_edges_data[0]['length']
            sample_size_2 = old_edges_data[1]['length']
            variance_1 = old_edges_data[0]['width_var']
            variance_2 = old_edges_data[1]['width_var']

            # computation of the pooled variance of the edge width
            new_edge_data['width_var'] = \
                ((sample_size_1 - 1) * variance_1 +
                 (sample_size_2 - 1) * variance_2) \
                / (sample_size_1 + sample_size_2 - 2)

            # prevent smoothing if it results in parallel edges
            if not input_data.has_edge(n1, n2) and n not in nodes_removed:
                input_data.add_edge(n1, n2, new_edge_data)
                input_data.remove_node(n)
                nodes_removed.append(n)

        return input_data

if __name__ == '__main__':
    unittest.main()
    