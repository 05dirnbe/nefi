# -*- coding: utf-8 -*-
import networkx as nx
import operator as op
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
        self.degree_threshold_value = FloatSlider("Degree treshold",0.0,20.0,0.1,10.0)
        self.float_sliders.append(self.degree_threshold_value)
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
            self.operator.value = self.checkOperator()
            if self.degree_threshold_value.value < 0:

                raise ArithmeticError('Vertex_Degree_Filter: Filtering'
                                          ' failed because the threshold \
                    degree is negative:', self.degree_threshold_value.value)

            to_be_removed = [u for u in input_data[1].nodes_iter()
                if self.operator.value(input_data[1].degree(u), self.degree_threshold_value.value)]
            input_data[1].remove_nodes_from(to_be_removed)

            print ('discarding a total of', len(to_be_removed), 'vertices ...')

        except ArithmeticError as e:

            print ('Exception caught in', e.msg, e.exp)

        self.result['graph'] = input_data[1]

if __name__ == '__main__':
    pass

