# -*- coding: utf-8 -*-
import networkx as nx
import operator as op
from _alg import Algorithm, DropDown, FloatSlider
from _utility import check_operator, draw_graph


__authors__ = {"Martino Bruni": "bruni.martino92@gmail.com"}


class AlgBody(Algorithm):
    """
    Edge attribute filter algorithm implementation
    """

    def __init__(self):
        """
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
        self.name = "Edge Attribute"
        self.parent = "Graph filtering"
        self.attribute = DropDown("Attribute", {"width", "length"})
        self.drop_downs.append(self.attribute)
        self.attribute_threshold_value = FloatSlider("Attribute treshold",
                                                     0.0, 20.0, 0.1, 10.0)
        self.float_sliders.append(self.attribute_threshold_value)
        self.operator = DropDown("Operator", {"Strictly smaller",
                                              "Smaller or equal",
                                              "Equal",
                                              "Greater or equal",
                                              "Strictly greater"})
        self.drop_downs.append(self.operator)

    def process(self, args):

        """
        Implements a filter which filters a graph for a certain edge attribute
        according to a threshold value.
        To decide whether or not an edge is removed the attribute value and
        the threshold value are used together in a logical operation.

        Example: Remove all edges with length strictly smaller than 10.5
        Example: Remove all edges with width greater or equal to 5
        Example: Remove all edges with length exaclty 7

        Args:
            | *input* : a list which contains the image and the graph

        Raises:
            | *KeyError* : Filtering failed because attribute is not present
             in the graph as an edge attribute

        Returns:
            | *graph* : A filtered networkx graph

        """
        try:
            self.operator.value = check_operator(self.operator)
            to_be_removed = [(u, v) for u, v, data in
                             args[1].edges_iter(data=True)
                             if self.operator.value(data[self.attribute.value],
                                                    self.attribute_threshold_value.value)]
            args[1].remove_edges_from(to_be_removed)
            print ('discarding a total of', len(to_be_removed), 'edges ...')
        except KeyError as kerror:
            print ('Exception caught in Edge_Attribute_Filter:' \
                  ' Filtering failed because', kerror)
            print ('is not present in the graph as an edge attribute.')

        self.result['img'] = args[0]
        self.result['graph'] = args[1]


if __name__ == '__main__':
    pass
