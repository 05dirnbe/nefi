# -*- coding: utf-8 -*-
import sys
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

    def __init__(self, largest_components_to_keep=1):
        """
        Simple cycle object constructor
            Instance vars:
                | *name* : name of the algorithm
                | *parent* : name of the appropriated category
        """
        Algorithm.__init__(self)
        self.name = "Keep only largest component connected"
        self.parent = "Graph filtering"
        self.largest_components_to_keep = largest_components_to_keep


    def process(self, graph):

        """
        Implements a filter which filters a graph for connected components and
        keeps only the largest of them.

        Args:
            | *graph* : graph instance

        Raises:
            | *NegativeNumberError* : Filtering failed because the number of
            components not to be removed is negative


        Returns:
            | *graph* : A filtered networkx graph
        """
        try:

            if self.largest_components_to_keep < 0:

                raise NegativeNumberError('Largest_Connected_Components_Filter: Filtering failed \
                    because the number of components not to be removed is negative:',
                    self.largest_components_to_keep)

            connected_components = sorted(list(nx.connected_component_subgraphs(graph)), key = lambda graph: graph.number_of_nodes(), reverse = True)

            to_be_removed = connected_components[self.largest_components_to_keep:]

            for subgraph in to_be_removed:
                graph.remove_nodes_from(subgraph)

            print 'discarding a total of', len(to_be_removed), 'connected components ...',

        except NegativeNumberError as e:

            print 'Exception caught in', e.msg, e.exp

        return graph

    """Exception class todo"""

    def NegativeNumberError(self, msg, exp):
        """Attempted improper operation on negative number."""
        ArithmeticError.__init__(self)
        self.msg = msg
        self.exp = exp

    def __str__(self):

        return repr(self.parameter)

if __name__ == '__main__':
    pass
