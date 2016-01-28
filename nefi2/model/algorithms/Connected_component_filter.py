# -*- coding: utf-8 -*-
import networkx as nx
import operator as op
from Martino_Graph_filtering_Algorithm.ExceptionCollection import \
    NegativeNumberError
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
        self.parent = "Graph filtering"
        self.component_size = IntegerSlider("Component Size",0.0,20.0,1.0,10)
        self.integer_sliders.append(self.component_size)
        self.operator = DropDown("Operator", {"Strictly smaller",
                                              "Smaller or equal",
                                              "Equal",
                                              "Greater or equal",
                                              "Strictly greater"})
        self.drop_downs.append(self.operator)

    def checkOperator(self):
        if self.operator.value == "Strictly smaller":
            return op.lt
        if self.operator.value == "Smaller or equal":
            return op.le
        if self.operator.value == "Equal":
            return op.eq
        if self.operator.value == "Greater or equal":
            return op.ge
        if self.operator.value == "Strictly greater":
            return op.gt

    def process(self, input_data):

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
            | *input_data* : A list which contains the image and the graph
        Raises:
            | *KeyError* : Filtering failed because the
             threshold connected component size is negative
        Returns:
            | *graph* : A filtered networkx graph
        """

        try:

            if self.component_size.value < 0:

                raise NegativeNumberError('Connected_Components_Filter:'
                                          ' Filtering failed because the \
                    threshold connected component size is negative:',
                                          self.component_size.value)

            self.operator.value=self.checkOperator()
            connected_components = sorted(
                list(nx.connected_component_subgraphs(input_data[1])),
                key = lambda graph: graph.number_of_nodes())
            to_be_removed = [subgraph for subgraph in connected_components
                if self.operator.value(subgraph.number_of_nodes(),
                                 self.component_size.value)]

            for subgraph in to_be_removed:
                input_data[1].remove_nodes_from(subgraph)

            print ('discarding a total of', len(to_be_removed),\
                'connected components ...')

        except NegativeNumberError as e:

            print ('Exception caught in', e.msg, e.exp)

        self.result['img'] = input_data[0]
        self.result['graph'] = input_data[1]

if __name__ == '__main__':
    pass

