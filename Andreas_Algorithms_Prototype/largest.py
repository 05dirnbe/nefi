#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
(from networkx docs)
For undirected graphs only. Graph, node, and edge attributes are copied to
the subgraphs by default.
"""
import networkx as nx
from nefi2.model.algorithms._alg import Algorithm

__author__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}


class AlgBody(Algorithm):
    """
    Largest component filter implementation.
    """
    def __init__(self):
        """
        Instance vars:
            | *name* : name of the algorithm
            | *parent* : name of the appropriate category

        """
        Algorithm.__init__(self)
        self.name = "Keep only largest connected component"
        self.parent = "Graph filtering"

    def process(self, graph):
        """

        Args:
            | *graph* : networkx graph instance

        """
        # largest connected component
        largest = max(nx.connected_component_subgraphs(graph), key=len)

        self.result = largest


if __name__ == '__main__':
    pass

