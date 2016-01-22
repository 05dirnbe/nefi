# -*- coding: utf-8 -*-
import networkx as nx
from nefi2.model.algorithms._alg import *
"""
This class represents the algorithm Vertex degree filter
"""

__authors__ = {"Martino Bruni": "bruni.martino92@gmail.com"}


class AlgBody(Algorithm):
    """
    Vertex degree filter algorithm implementation
    """

    def __init__(self):
        """
        Edge attribute object constructor
            Instance vars:
                | *name* : name of the algorithm
                | *parent* : name of the appropriated category
                | *degree_threshold_value* : A threshold value for
                 the vertex degree
                | *operator* : A logical python operator.
                See python module operator
        """
        Algorithm.__init__(self)
        self.name = "Vertex degree filter"
        self.parent = "Graph filtering"
        self.degree_threshold_value =
        self.operator =

    def process(self, graph):

        """
        Implements a filter which filters a graph for vertex degrees according
        to a threshold value.
        To decide whether or not a vertex is removed the vertex degree
        and the threshold value are used together in a logical operation.

        Example: Remove all vertices with degree strictly smaller than 3
        Example: Remove all edges with degree greater or equal to 5
        Example: Remove all edges with degree exaclty 7

        Args:
            | *graph* : graph instance.
        Raises:
            | *KeyError* : Filtering failed because the degree threshold value
             is negative
        Returns:
            | *graph* : A filtered networkx graph
        """

        try:

            if self.degree_threshold_value < 0:

                raise NegativeNumberError('Vertex_Degree_Filter: Filtering'
                                          ' failed because the threshold \
                    degree is negative:', self.degree_threshold_value)

            to_be_removed = [u for u in graph.nodes_iter()
                if self.operator(graph.degree(u), self.degree_threshold_value)]
            graph.remove_nodes_from(to_be_removed)

            print 'discarding a total of', len(to_be_removed), 'vertices ...',

        except NegativeNumberError as e:

            print 'Exception caught in', e.msg, e.exp

        self.result['graph'] = graph

if __name__ == '__main__':
    pass

