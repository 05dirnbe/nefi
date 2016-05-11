#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Thinning is the operation that takes a binary image and contracts the
foreground until only single-pixel wide lines remain. It is also known as
skeletonization.

The algorithm below was taken from NEFI1. It uses thinning C module written by
`Adrian Neumann <https://bitbucket.org/adrian_n/thinning>`_.
The code was adapted for NEFI2.
"""
from nefi2.model.algorithms._alg import Algorithm
import cv2
import networkx as nx
import numpy as np
import thinning
import sys
import traceback
from collections import defaultdict
from itertools import chain


__author__ = {"Adrian Neumann": "", "Pavel Shkadzko": "p.shkadzko@gmail.com"}


class AlgBody(Algorithm):
    """
    Guo Hall thinning implementation.
    """
    def __init__(self):
        """
        Instance vars:
            | *name* : name of the algorithm
            | *parent* : name of the appropriate category

        """
        Algorithm.__init__(self)
        self.name = "Guo Hall Graph Detection"
        self.parent = "Graph Detection"

    def process(self, args):
        """
        Guo Hall thinning.
        Use ```zhang_suen_node_detection()``` for node detection.
        Use ```breadth_first_edge_detection()``` for edge detection.

        Args:
            | *args* : a list of arguments, e.g. image ndarray

        """
        # create a skeleton
        skeleton = args[2]
        image = args[0]
        # detect nodes
        graph = zhang_suen_node_detection(skeleton)
        # detect edges
        # graph = breadth_first_edge_detection(skeleton, gray_img, graph)
        graph = breadth_first_edge_detection(skeleton, image, graph)
        #skeleton = cv2.cvtColor(skeleton, cv2.COLOR_GRAY2BGR)
        self.result['graph'] = graph
        self.result['img'] = image

def zhang_suen_node_detection(skel):
    """
    (from nefi1)
    Node detection based on criteria put forward in "A fast parallel algorithm
    for thinning digital patterns" by T. Y. Zhang and C. Y. Suen. Pixels p of
    the skeleton are categorized as nodes/non-nodes based on the value of a
    function A(p) depending on the pixel neighborhood of p. Please check the
    above paper for details.

    A(p1) == 1: The pixel p1 sits at the end of a skeleton line, thus a node
    of degree 1 has been found.
    A(p1) == 2: The pixel p1 sits in the middel of a skeleton line but not at
    a branching point, thus a node of degree 2 has been found. Such nodes are
    ignored and not introduced to the graph.
    A(p1) >= 3: The pixel p1 belongs to a branching point of a skeleton line,
    thus a node of degree >=3 has been found.

    Args:
        *skel* : Skeletonised source image. The skeleton must be exactly 1
         pixel wide.

    Returns:
        *graph* : networkx Graph object with detected nodes.

    """
    def check_pixel_neighborhood(x, y, skel):
        """
        Check the number of components around a pixel.
        If it is either 1 or more than 3, it is a node.

        Args:
            | *x* : pixel location value
            | *y* : pixel location value
            | *skel* : skeleton Graph object

        Returns:
            *accept_pixel_as_node* : boolean value

        """
        accept_pixel_as_node = False
        item = skel.item
        p2 = item(x - 1, y) / 255
        p3 = item(x - 1, y + 1) / 255
        p4 = item(x, y + 1) / 255
        p5 = item(x + 1, y + 1) / 255
        p6 = item(x + 1, y) / 255
        p7 = item(x + 1, y - 1) / 255
        p8 = item(x, y - 1) / 255
        p9 = item(x - 1, y - 1) / 255

        # The function A(p1),
        # where p1 is the pixel whose neighborhood is beeing checked
        components = (p2 == 0 and p3 == 1) + (p3 == 0 and p4 == 1) + \
                     (p4 == 0 and p5 == 1) + (p5 == 0 and p6 == 1) + \
                     (p6 == 0 and p7 == 1) + (p7 == 0 and p8 == 1) + \
                     (p8 == 0 and p9 == 1) + (p9 == 0 and p2 == 1)
        if (components >= 3) or (components == 1):
            accept_pixel_as_node = True
        return accept_pixel_as_node

    graph = nx.Graph()
    w, h = skel.shape
    item = skel.item
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            if item(x, y) != 0 and check_pixel_neighborhood(x, y, skel):
                graph.add_node((x, y))
    return graph

def breadth_first_edge_detection(skel, segmented, graph):
    """
    (from nefi1)
    Detect edges in the skeletonized image.
    Also compute the following edge properties:

        | *pixels* : number of pixels on the edge in the skeleton
        | *length* : length in pixels, horizontal/vertikal steps count 1,
           diagonal steps count sqrt 2
        | *width* : the mean diameter of the edge
        | *width_var* : the variance of the width along the edge

    The runtime is linear in the number of pixels.
    White pixels are **much more** expensive though.
    """
    def neighbors(x, y):
        item = skel.item
        width, height = skel.shape
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                # the line below is ugly and is intended to be this way
                # do not try to modify it unless you know what you're doing
                if (dx != 0 or dy != 0) and \
                                        0 <= x + dx < width and \
                                        0 <= y + dy < height and \
                                item(x + dx, y + dy) != 0:
                    yield x + dx, y + dy

    def distance_transform_diameter(edge_trace, segmented):
        """
        (dev comments from nefi1)
        my cv2 lacks cv2.DIST_L2, it seems to have the value 2 though, so I use
        that, same for MASK_PRECISE
        <python3 cv2.DIST_L2 equals to 2>
        """
        dt = cv2.distanceTransform(segmented, 2, 0)
        edge_pixels = np.nonzero(edge_trace)
        diameters = defaultdict(list)
        for label, diam in zip(edge_trace[edge_pixels], 2.0 * dt[edge_pixels]):
            diameters[label].append(diam)
        return diameters

    # compute edge length
    # initialize: the neighbor pixels of each node get a distinct label
    # each label gets a queue
    label_node = dict()
    queues = []
    label = 1
    label_length = defaultdict(int)
    for x, y in graph.nodes_iter():
        for a, b in neighbors(x, y):
            label_node[label] = (x, y)
            label_length[label] = 1.414214 if abs(x - a) == 1 and \
                                              abs(y - b) == 1 else 1
            queues.append((label, (x, y), [(a, b)]))
            label += 1

    # bfs over the white pixels.
    # One phase: every entry in queues is handled
    # Each label grows in every phase.
    # If two labels meet, we have an edge.
    edges = set()
    edge_trace = np.zeros(skel.shape, np.uint32)
    edge_value = edge_trace.item
    edge_set_value = edge_trace.itemset
    label_histogram = defaultdict(int)

    while queues:
        new_queues = []
        for label, (px, py), nbs in queues:
            for (ix, iy) in nbs:
                value = edge_value(ix, iy)
                if value == 0:
                    edge_set_value((ix, iy), label)
                    label_histogram[label] += 1
                    # TODO consider using cv2.arcLength for this
                    label_length[label] += 1.414214 if abs(ix - px) == 1 and \
                                                       abs(iy - py) == 1 else 1
                    new_queues.append((label, (ix, iy), neighbors(ix, iy)))
                elif value != label:
                    edges.add((min(label, value), max(label, value)))
        queues = new_queues

    # compute edge diameters
    diameters = distance_transform_diameter(edge_trace, segmented)
    # add edges to graph
    for l1, l2 in edges:
        u, v = label_node[l1], label_node[l2]
        if u == v:
            continue
        d1, d2 = diameters[l1], diameters[l2]
        diam = np.fromiter(chain(d1, d2), np.uint, len(d1) + len(d2))
        graph.add_edge(u, v, pixels=label_histogram[l1] + label_histogram[l2],
                       length=label_length[l1] + label_length[l2],
                       width=np.mean(diam),
                       width_var=np.var(diam))
    return graph


if __name__ == '__main__':
    pass
