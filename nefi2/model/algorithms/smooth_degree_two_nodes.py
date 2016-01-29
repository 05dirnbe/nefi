# -*- coding: utf-8 -*-
"""
This class represents the algorithm Smooth degree two nodes
"""
import sys
import networkx as nx
from _alg import Algorithm


__authors__ = {"Martino Bruni": "bruni.martino92@gmail.com"}


class AlgBody(Algorithm):
    """
    Smooth degree two nodes algorithm implementation
    """

    def __init__(self):
        """
        Smooth degree object constructor
            Instance vars:
                | *name* : name of the algorithm
                | *parent* : name of the appropriated category
        """
        Algorithm.__init__(self)
        self.name = "Smooth degree 2 nodes"
        self.parent = "Graph filtering"

    def process(self, input_data):

        """
        Implements a filter which smooths nodes of degree two.
        The edge attributes of the evolved edges are treated as follows:
        Lengths are added to each other. The new edge length will be the sum of
        the individual lengths.
        Widths are combined using the mean. The new edge width will be the
        mean of the individual widths.

        Args:
            | *input* : A list which contains the image and the graph
        Returns:
            | *graph* : A filtered networkx graph
        """
        try:

            degree_two_nodes = [v for v in input_data[1].nodes_iter()
                                if input_data[1].degree(v) == 2]

            nodes_removed = []

            for n in degree_two_nodes:

                old_edges_data = []
                new_edge_data = {}

                neighbors = input_data[1].neighbors(n)
                n1 = neighbors[0]
                n2 = neighbors[1]

                for e in input_data[1].edges(n):
                    old_edges_data.append(input_data[1].get_edge_data(*e))

                for d in old_edges_data:

                    for key, value in d.items():

                        if key in ['length', 'pixels']:

                            if key in new_edge_data.keys():
                                new_edge_data[key] += value
                            else:
                                new_edge_data[key] = value

                        elif key in ['width']:

                            if key in new_edge_data.keys():
                                new_edge_data[key] += value * 0.5
                            else:
                                new_edge_data[key] = value * 0.5

                        else:
                            pass

                sample_size_1 = old_edges_data[0]['length']
                sample_size_2 = old_edges_data[1]['length']
                variance_1 = old_edges_data[0]['width_var']
                variance_2 = old_edges_data[1]['width_var']

                # computation of the pooled variance of the edge width
                new_edge_data['width_var'] = \
                    ((sample_size_1 - 1) * variance_1 +
                     (sample_size_2 - 1) * variance_2) \
                    / (sample_size_1 + sample_size_2 - 2)

                # prevent smoothing if it results in parallel edges
                if not input_data[1].has_edge(n1, n2) and n not in nodes_removed:
                    input_data[1].add_edge(n1, n2, new_edge_data)
                    input_data[1].remove_node(n)
                    nodes_removed.append(n)

            print ('Smoothed a total of', len(
                nodes_removed), 'degree 2 nodes ...')

        except:

            print ("Unexpected error:", sys.exc_info()[0])

        self.result['img'] = input_data[0]
        self.result['graph'] = input_data[1]

if __name__ == '__main__':
    pass