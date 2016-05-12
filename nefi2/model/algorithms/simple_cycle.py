#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
(from networkx docs)
Biconnected components are maximal subgraphs such that the removal of a node
(and all edges incident on that node) will not disconnect the subgraph. Note
that nodes may be part of more than one biconnected component. Those nodes are
articulation points, or cut vertices. The removal of articulation points will
increase the number of connected components of the graph.
"""
from nefi2.model.algorithms._alg import Algorithm
import networkx as nx
import cv2 as cv
import numpy as np


__author__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}


class AlgBody(Algorithm):
    """
    Simple cycle filter implementation.
    """
    def __init__(self):
        """
        Instance vars:
            | *name* : name of the algorithm
            | *parent* : name of the appropriate category

        """
        Algorithm.__init__(self)
        self.name = "Simple Cycle"
        self.parent = "Graph Filtering"

    def process(self, args):
        """
        By using a generator of sets of nodes, one set for each biconnected
        component of the graph(biconnected_components) we remove all vertices
        which do not belong to a cycle (degree greater than two). The output is
        a graph including only biconnected components.

        Args:
            | *args* : a list containing image array and Graph object

        """
        image, graph = args[0:2]
        # create a set of all nodes
        nodes_not_in_a_cycle = set(graph.nodes())
        # filter all nodes which are not in a biconnected component
        for component in nx.biconnected_components(graph):
            if len(component) > 2:
                nodes_not_in_a_cycle -= component
        # remove all nodes which are not in a biconnected component from
        # the graph
        graph.remove_nodes_from(nodes_not_in_a_cycle)
        print ('discarding a total of', len(nodes_not_in_a_cycle), 'edges ...')
        self.result['graph'] = graph
        self.result['img'] = image

    @staticmethod
    def draw_nodes(args):
        """
        Draw nodes as rectangle into current image instance

        Args:
            | *args* : a list containing image array and Graph object
        """
        image, graph = args
        radius = 3
        for x, y in graph.nodes():
            cv.rectangle(image, (y-radius, x-radius),
                         (y+radius, x+radius), (255, 0, 0), -1)

        return image

    @staticmethod
    def draw_edges(args):
        """
        Draw edges into current image instance

        Args:
            | *args* : a list containing image array and Graph object
        """
        image, graph = args
        draw = np.copy(image)
        color=(0, 0, 255)
        for (x1, y1), (x2, y2) in graph.edges():
            start = (y1, x1)
            end = (y2, x2)
            diam = graph[(x1, y1)][(x2, y2)]['width']
            if diam == -1: diam = 2
            diam = int(round(diam))
            if diam > 255:
                diam = 255
            cv.line(draw, start, end, color, diam)
        draw = cv.addWeighted(image, 0.5, draw, 0.5, 0)

        return draw

if __name__ == '__main__':
    pass
