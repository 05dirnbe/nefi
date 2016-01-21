#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
(from networkx docs)
Biconnected components are maximal subgraphs such that the removal of a node
(and all edges incident on that node) will not disconnect the subgraph. Note
that nodes may be part of more than one biconnected component. Those nodes are
articulation points, or cut vertices. The removal of articulation points will
increase the number of connected components of the graph.
"""
import networkx as nx
from nefi2.model.algorithms._alg import Algorithm

__author__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}


class AlgBody(Algorithm):
    """
    Simple cycle filter implementation.
    """
    def __init__(self):
        """
        Instance vars:
            | *name* : name of the algorithm
            | *parent* : name of the appropriate category

        """
        Algorithm.__init__(self)
        self.name = "Simple cycle filter"
        self.parent = "Graph filtering"

    def process(self, graph):
        """
        By using a generator of sets of nodes, one set for each biconnected
        component of the graph(biconnected_components) we remove all vertices
        which do not belong to a cycle (degree greater than two). The output is
        a graph including only biconnected components.

        Args:
            | *graph* : networkx graph instance

        """
        # create a set of all nodes
        nodes_not_in_a_cycle = set(graph.nodes())
        # filter all nodes which are not in a biconnected component
        for component in nx.biconnected_components(graph):
            if len(component) > 2:
                nodes_not_in_a_cycle -= component
        # remove all nodes which are not in a biconnected component from
        # the graph
        graph.remove_nodes_from(nodes_not_in_a_cycle)

        self.result = graph


if __name__ == '__main__':
    pass

