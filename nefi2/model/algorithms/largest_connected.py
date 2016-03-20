#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
(taken from NEFI1)
Implementation of an algorithm which filters a graph for connected components
and keeps only the largest of them, e.g remove all connected components except
the 4 largest.
"""
from model.algorithms._alg import Algorithm
import networkx as nx

__author__ = {
    "Andreas Firczynski": "andreasfir91@googlemail.com",
    "Pavel Shkadzko": "p.shkadzko@gmail.com"}


class AlgBody(Algorithm):
    """
    Keep only largest connected component algorithm implementation.
    """
    def __init__(self):
        """
        Instance vars:
            | *name* : name of the algorithm
            | *parent* : name of the appropriate category

        """
        Algorithm.__init__(self)
        self.name = "Keep only LCC"
        self.parent = "Graph Filtering"

    def process(self, args):
        """
        Keep only largest connected component from nefi1.

        Args:
            | *args* : a list containing image array and Graph object

        Raises:
            | *ValueError* : means filtering failed due to the number
              of components not to be removed is negative.

        Returns:
            | *graph* : a filtered networkx Graph

        """
        image_arr, graph = args[0:2]
        try:
            graph = max(nx.connected_component_subgraphs(graph), key=len)
            # supposedly slower
            # graph = list(nx.connected_components(graph))[0]
        except ValueError as e:
            print('ValueError exception:', e)
        self.result['graph'], self.result['img'] = graph, image_arr


if __name__ == '__main__':
    pass
