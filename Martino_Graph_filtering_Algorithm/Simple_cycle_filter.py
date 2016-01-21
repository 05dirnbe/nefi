# -*- coding: utf-8 -*-
import networkx as nx
from nefi2.model.algorithms._alg import *
"""
This class represents the algorithm Smooth degree two nodes
"""

__authors__ = {"Martino Bruni": "bruni.martino92@gmail.com"}


class AlgBody(Algorithm):
    """
    Simple cycle filter algorithm implementation
    """

    def __init__(self):
        """
        Simple cycle object constructor
            Instance vars:
                | *name* : name of the algorithm
                | *parent* : name of the appropriated category
        """
        Algorithm.__init__(self)
        self.name = "Simple cycle filter"
        self.parent = "Graph filtering"

    def process(self, graph):

        """
        Implements a filter removing every vertex not part of at least one
        simple cycle.

        Args:
            | *graph* : graph instance
        Returns:
            | *graph* : A filtered networkx graph
        """
        vertices_not_in_a_cycle = set(graph.nodes_iter())
        for component in nx.biconnected_components(graph):
            if len(component)>2:
                vertices_not_in_a_cycle -= component


        graph.remove_nodes_from(vertices_not_in_a_cycle)
        # cycle_basis = nx.cycle_basis(graph)
        # vertices_not_in_a_cycle = [u for u in graph.nodes_iter()
        #     if not any(u in cycle for cycle in cycle_basis)]
        # graph.remove_nodes_from(vertices_not_in_a_cycle)

        print 'discarding a total of', len(vertices_not_in_a_cycle),
        print 'vertices which do not belong to any cycle ...',

        return graph

if __name__ == '__main__':
    pass
