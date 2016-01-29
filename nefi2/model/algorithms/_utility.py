"""
This python file contains helpful methods which
are of static nature and are beneficial for several
algorithms. The main reason for the creation of this file
is to provide the user with a toolbox of methods and
don't force him to copy and paste methods from other algorithm
sections.
"""
import operator as op
import cv2 as cv
import numpy as np
import networkx as nx

__authors__ = {"Martino Bruni": "bruni.martino92@gmail.com"}


NODESIZESCALING = 750

def draw_graph(image, graph):
    """
    draws the graph in the image by traversing the graph structure

    Args:
        | *image* : the image where the graph needs to be drawn
        | *graph* : the *.txt file containing the graph information

    Returns:

    """
    tmp = draw_edges(image, graph)
    node_size = int(np.ceil((max(image.shape) / float(NODESIZESCALING))))
    return draw_nodes(tmp, graph, max(node_size, 3))

def draw_nodes(img, graph, radius=3):
    """
    Draws all nodes into an input image

    Args:
        | *img* : Input image where nodes are drawn
        | *graph* : Input graph containing the nodes

    Kwargs:
        | *radius* : Radius of drawn nodes

    Returns:
        Input image img with nodes drawn into it
    """

    for x, y in graph.nodes_iter():
        cv.rectangle(img, (y-radius, x-radius), (y+radius, x+radius), (0, 255, 0), -1)

    return img

def draw_edges(img, graph, col=(0, 0, 255)):
    """
        Draw edges into input image.

    Args:
        | *img* : Input image where edges are drawn
        | *graph* : Input graph containing the edges
    Kwargs:
        | *col* : colour for drawing

    Returns:
        Input image img with nodes drawn into it
    """
    edg_img = np.copy(img)
    for (x1, y1), (x2, y2) in graph.edges_iter():
        start = (y1, x1)
        end = (y2, x2)
        diam = graph[(x1, y1)][(x2, y2)]['width']
        if diam == -1: diam = 2
        diam = int(round(diam))
        if diam > 255:
            print ('Warning: edge diameter too large for display. Diameter has been reset.')
            #diam = 255
            diam = 100
        cv.line(edg_img, start, end, col, diam)
    edg_img = cv.addWeighted(img, 0.5, edg_img, 0.5, 0)
    return edg_img

def check_operator(operator):
    """
    Converts the string value of the DropDown element in operator object

    Args:
        | *operator* : DropDown object from the algorithm class

    Returns:
        | *op_object*: operator object converted
    """
    op_object = None

    if operator.value == "Strictly smaller":
        op_object = op.lt
    if operator.value == "Smaller or equal":
        op_object = op.le
    if operator.value == "Equal":
        op_object = op.eq
    if operator.value == "Greater or equal":
        op_object = op.ge
    if operator.value == "Strictly greater":
        op_object = op.gt
    return op_object

if __name__ == '__main__':
    pass