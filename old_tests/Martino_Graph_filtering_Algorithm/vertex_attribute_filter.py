# -*- coding: utf-8 -*-
import networkx as nx
import operator as op
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
        self.attribute = DropDown("Attribute", {"potential", "weight","temperature"})
        self.drop_downs.append(self.attribute)
        self.attribute_threshold_value = FloatSlider("Attribute treshold",0.0,20.0,0.1,10.0)
        self.float_sliders.append(self.attribute_threshold_value)
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

            self.operator.value = self.checkOperator()
            to_be_removed = [(u, v) for u, v, data in
                             input_data[1].nodes_iter(data=True)
                if self.operator.value(data[self.attribute],
                                 self.attribute_threshold_value)]
            input_data[1].remove_nodes_from(to_be_removed)

            print ('discarding a total of', len(to_be_removed), 'vertices ...')

        except KeyError as e:

            print ('Exception caught in Vertex_Attribute_Filter: ' \
                  'Filtering failed because', e)
            print ('is not present in the graph as a vertex attribute.')

        self.result['graph'] = input_data[1]

if __name__ == '__main__':
    pass

