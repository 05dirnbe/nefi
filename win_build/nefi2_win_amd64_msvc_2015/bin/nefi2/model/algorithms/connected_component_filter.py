# -*- coding: utf-8 -*-
from nefi2.model.algorithms._alg import Algorithm, IntegerSlider, DropDown
from nefi2.model.algorithms._utility import check_operator, draw_graph
import networkx as nx


__authors__ = {"Martino Bruni": "bruni.martino92@gmail.com"}


class AlgBody(Algorithm):
    """
    Connected Component Filter algorithm implementation
    """

    def __init__(self):
        """
        Instance vars:
            | *name* : name of the algorithm
            | *parent* : name of the appropriated category
            | *compnt_size* : A threshold value for the size of
             the connected components
            | *operator* : A logical python operator.
             See python module operator

        """
        Algorithm.__init__(self)
        self.name = "Connected Component"
        self.parent = "Graph Filtering"
        self.compnt_size = IntegerSlider("Component Size", 0.0, 20.0, 1.0, 10)
        self.integer_sliders.append(self.compnt_size)
        self.operator = DropDown("Operator", {"strictly smaller",
                                              "smaller or equal",
                                              "equal",
                                              "greater or equal",
                                              "strictly greater"})
        self.drop_downs.append(self.operator)

    def process(self, args):

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
            | *args* : A list which contains the image and the graph
        Raises:
            | *KeyError* : Filtering failed because the
             threshold connected component size is negative
        Returns:
            | *graph* : A filtered networkx graph

        """
        oper_str_value = self.operator.value
        try:
            if self.compnt_size.value < 0:
                raise ArithmeticError("Connected_Components_Filter: Filtering \
                                      failed because the threshold connected \
                                      component size is negative:",
                                      self.compnt_size.value)

            self.operator.value = check_operator(self.operator)
            connected_components = sorted(
                list(nx.connected_component_subgraphs(args[1])),
                key=lambda graph: graph.number_of_nodes())
            to_be_removed = [subgraph for subgraph in connected_components
                             if self.operator.value(subgraph.number_of_nodes(),
                                                    self.compnt_size.value)]
            for subgraph in to_be_removed:
                args[1].remove_nodes_from(subgraph)
            print ('discarding a total of', len(to_be_removed),
                   'connected components ...')
        except ArithmeticError as ex:
            print ('Exception caught in', ex)
        self.operator.value = oper_str_value
        self.result['img'] = args[0]
        self.result['graph'] = args[1]


if __name__ == '__main__':
    pass
