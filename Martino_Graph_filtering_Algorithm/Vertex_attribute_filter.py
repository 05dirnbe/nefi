# -*- coding: utf-8 -*-
import networkx as nx
from nefi2.model.algorithms._alg import *
"""
This class represents the algorithm Vertex attribute filter
"""

__authors__ = {"Martino Bruni": "bruni.martino92@gmail.com"}


class AlgBody(Algorithm):
    """
    Vertex attribute filter algorithm implementation
    """

    def __init__(self):
        """
        Vertex attribute object constructor
            Instance vars:
                | *name* : name of the algorithm
                | *parent* : name of the appropriated category
                | *attribute* :  A valid vertex attribute present in the graph.
                | *attribute_threshold_value* : A threshold value for
                 the given attribute
                | *operator* : A logical python operator.
                See python module operator
        """
        Algorithm.__init__(self)
        self.name = "Vertex attribute filter"
        self.parent = "Graph filtering"
        self.attribute =
        self.attribute_threshold_value =
        self.operator =

    def process(self, graph):

        """
        Implements a filter which filters a graph for a certain
        vertex attribute according to a threshold value.
        To decide whether or not a vertex is removed the attribute value
        and the threshold value are used together in a logical operation.

        Example: Remove all vertices with potential strictly smaller than 10.5
        Example: Remove all edges with weight greater or equal to 5
        Example: Remove all edges with temperature exaclty 7

        Args:
            | *graph* : graph instance.
        Raises:
            | *KeyError* : Filtering failed because attribute is not present
             in the graph as a vertex attribute
        Returns:
            | *graph* : A filtered networkx graph
        """
        try:

            to_be_removed = [(u, v) for u, v, data in
                             graph.nodes_iter(data=True)
                if self.operator(data[self.attribute],
                                 self.attribute_threshold_value)]
            graph.remove_nodes_from(to_be_removed)

            print 'discarding a total of', len(to_be_removed), 'vertices ...',

        except KeyError as e:

            print 'Exception caught in Vertex_Attribute_Filter: ' \
                  'Filtering failed because', e,
            print 'is not present in the graph as a vertex attribute.'

        self.result['graph'] = graph

if __name__ == '__main__':
    pass

