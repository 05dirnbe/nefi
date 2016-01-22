# -*- coding: utf-8 -*-
import networkx as nx
from nefi2.model.algorithms._alg import *
"""
This class represents the algorithm Connected component filter
"""

__authors__ = {"Martino Bruni": "bruni.martino92@gmail.com"}


class AlgBody(Algorithm):
    """
    Connected component filter algorithm implementation
    """

    def __init__(self):
        """
        Connected component object constructor
            Instance vars:
                | *name* : name of the algorithm
                | *parent* : name of the appropriated category
                | *component_size* : A threshold value for the size of
                 the connected components
                | *operator* : A logical python operator.
                 See python module operator
        """
        Algorithm.__init__(self)
        self.name = "Connected component filter"
        self.component_size =
        self.operator =

    def process(self, graph):

        """
        Implements a filter which filters a graph for connected components
        according to a threshold value.
        To decide whether or not a connected component is removed the component
        size and the threshold value are used together in a logical operation.

        Example: Remove all connected components of size strictly
         smaller than 3
        Example: Remove all connected components of size greater or equal to 5
        Example: Remove all connected components of size exaclty 7

        Args:
            | *graph* : graph instance.
        Raises:
            | *KeyError* : Filtering failed because the
             threshold connected component size is negative
        Returns:
            | *graph* : A filtered networkx graph
        """

        try:

            if self.component_size < 0:

                raise NegativeNumberError('Connected_Components_Filter:'
                                          ' Filtering failed because the \
                    threshold connected component size is negative:',
                                          self.component_size)

            connected_components = sorted(
                list(nx.connected_component_subgraphs(graph)),
                key = lambda graph: graph.number_of_nodes())
            to_be_removed = [subgraph for subgraph in connected_components
                if self.operator(subgraph.number_of_nodes(),
                                 self.component_size)]

            for subgraph in to_be_removed:
                graph.remove_nodes_from(subgraph)

            print 'discarding a total of', len(to_be_removed),\
                'connected components ...',

        except NegativeNumberError as e:

            print 'Exception caught in', e.msg, e.exp

        self.result['graph'] = graph
if __name__ == '__main__':
    pass

