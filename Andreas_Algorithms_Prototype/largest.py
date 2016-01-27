#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
(from networkx docs)
For undirected graphs only. Graph, node, and edge attributes are copied to
the subgraphs by default.
"""
import networkx as nx
import cv2
import numpy as np
from nefi2.model.algorithms._alg import Algorithm

__author__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}


class AlgBody(Algorithm):
    """
    Largest component filter implementation.
    """
    def __init__(self):
        """
        Instance vars:
            | *name* : name of the algorithm
            | *parent* : name of the appropriate category

        """
        Algorithm.__init__(self)
        self.name = "Keep only largest connected component"
        self.parent = "Graph filtering"

    def process(self, args):
        """
        Keep only largest connected component from nefi1.

        Args:
            | *args* : a list containing image array and Graph object

        Raises:
            | *ValueError* : means filtering failed due to the number
              of components not to be removed is negative.

        Returns:
            | *graph* : a filtered networkx Graph

        """
        image, graph = args
        # get the largest connected component
        largest = max(nx.connected_component_subgraphs(graph), key=len)
        self.result['img'] = largest
        # draw edges into current image
        tmp = self.draw_edges(image, largest)
        # draw nodes into current image
        drawn = self.draw_nodes(tmp, largest)

        self.result['graph'] = drawn

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
            cv2.rectangle(image, (y-radius, x-radius),
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
            cv2.line(draw, start, end, color, diam)
        draw = cv2.addWeighted(image, 0.5, draw, 0.5, 0)

        return image

if __name__ == '__main__':
    pass

