# -*- coding: utf-8 -*-
import networkx as nx
from nefi2.model.algorithms._alg import *
"""
This class represents the algorithm Edge attribute filter
"""

__authors__ = {"Martino Bruni": "bruni.martino92@gmail.com"}


class AlgBody(Algorithm):
    """
    Edge attribute filter algorithm implementation
    """

    def __init__(self):
        """
        Edge attribute object constructor
            Instance vars:
                | *name* : name of the algorithm
                | *parent* : name of the appropriated category
                | *attribute* :  A valid edge attribute present in the graph.
                | *attribute_threshold_value* : A threshold value for
                 the given attribute
                | *operator* : A logical python operator.
                 See python module operator
        """
        Algorithm.__init__(self)
        self.name = "Edge attribute filter"
        self.parent = "Graph filtering"
        self.attribute =
        self.attribute_threshold_value =
        self.operator =

    def process(self, graph):

        """
        Implements a filter which filters a graph for a certain edge attribute
        according to a threshold value.
        To decide whether or not an edge is removed the attribute value and
        the threshold value are used together in a logical operation.

        Example: Remove all edges with length strictly smaller than 10.5
        Example: Remove all edges with width greater or equal to 5
        Example: Remove all edges with length exaclty 7

        Args:
            | *graph* : graph instance.
        Raises:
            | *KeyError* : Filtering failed because attribute is not present
             in the graph as an edge attribute
        Returns:
            | *graph* : A filtered networkx graph
        """
        try:

            to_be_removed = [(u, v) for u, v, data in
                             graph.edges_iter(data=True)
                if self.operator(data[self.attribute],
                                 self.attribute_threshold_value)]
            graph.remove_edges_from(to_be_removed)

            print 'discarding a total of', len(to_be_removed), 'edges ...',

        except KeyError as e:

            print 'Exception caught in Edge_Attribute_Filter:' \
                  ' Filtering failed because', e,
            print 'is not present in the graph as an edge attribute.'

        self.result['graph'] = graph

if __name__ == '__main__':
    pass
