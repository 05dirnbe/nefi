"""
Various help functions for processing results.
"""
import cv2
import numpy
import operator


__authors__ = {"Martino Bruni": "bruni.martino92@gmail.com"}


NODESIZESCALING = 750
EDGETRANSPARENCYDIVIDER = 5
EDGETRANSPARENCY = False


def draw_graph(image, graph):
    """
    Draw the graph on the image by traversing the graph structure.

    Args:
        | *image* : the image where the graph needs to be drawn
        | *graph* : the *.txt file containing the graph information

    Returns:

    """
    tmp = draw_edges(image, graph)
    node_size = int(numpy.ceil((max(image.shape) / float(NODESIZESCALING))))
    return draw_nodes(tmp, graph, max(node_size, 1))


def draw_nodes(img, graph, radius=1):
    """
    Draw all nodes on the input image.

    Args:
        | *img* : Input image where nodes are drawn
        | *graph* : Input graph containing the nodes

    Kwargs:
        | *radius* : Radius of drawn nodes

    Returns:
        Input image img with nodes drawn into it
    """
    for x, y in graph.nodes():
        cv2.rectangle(img, (y - radius, x - radius), (y + radius, x + radius),
                     (255, 0, 0), -1)
    return img


def draw_edges(img, graph, col=(0, 0, 255)):
    """
    Draw network edges on the input image.

    Args:
        | *img* : Input image where edges are drawn
        | *graph* : Input graph containing the edges
    Kwargs:
        | *col* : colour for drawing

    Returns:
        Input image img with nodes drawn into it
    """
    edg_img = numpy.copy(img)

    max_standard_deviation = 0
    if EDGETRANSPARENCY:
        max_standard_deviation = find_max_edge_deviation(graph)

    for (x1, y1), (x2, y2) in graph.edges():
        start = (y1, x1)
        end = (y2, x2)
        diam = graph[(x1, y1)][(x2, y2)]['width']
        # variance value computed during graph detection
        width_var = graph[(x1, y1)][(x2, y2)]['width_var']
        # compute edges standard deviation by applying sqrt(var(edge))
        standard_dev = numpy.sqrt(width_var)
        if diam == -1: diam = 2
        diam = int(round(diam))
        if diam > 255:
            print('Warning: edge diameter too large for display. Diameter has been reset.')
            diam = 255
        if EDGETRANSPARENCY:
            edge_cur_standard_deviation = graph[(x1, y1)][(x2, y2)]['standard_deviation']

            # calculate the opacity based on the condition opacity_max_standard_deviation = 0.8
            opacity = edge_cur_standard_deviation / max_standard_deviation * 0.8

            # access color triple
            (b, g, r) = col

            # set overlay in this case white
            overlay = (0, 0 ,0)
            # compute target color based on the transparency formula
            target_col = (b == 0 if 0 else opacity * 255 + (1 - opacity) * b,
                          g == 0 if 0 else opacity * 255 + (1 - opacity) * g,
                          r == 0 if 0 else opacity * 255 + (1 - opacity) * r)

            # draw the line
            cv2.line(edg_img, start, end, target_col, diam)

        else:
            # simply draw a red line since we are not in the edge transparency mode
            cv2.line(edg_img, start, end, col, diam)

    edg_img = cv2.addWeighted(img, 0.5, edg_img, 0.5, 0)

    MAXIMUMSTANDARDDEVIATION = 0

    return edg_img

def find_max_edge_deviation(graph):
    """
    This methode calculates for each edge its standard deviation and also
    tracks the maximum standard deviation among all edges.
    The maximum standard deviation will then be stored in the graph.
    """
    max_standard_deviation = 0
    for (x1, y1), (x2, y2) in graph.edges():
        deviation = graph[(x1, y1)][(x2, y2)]['width_var']
        standard_deviation = numpy.sqrt(deviation)
        graph[(x1, y1)][(x2, y2)]['standard_deviation'] = standard_deviation

        if max_standard_deviation < standard_deviation:
            max_standard_deviation = standard_deviation

    return max_standard_deviation




def check_operator(dropdown):
    """
    Converts the string value of the DropDown element in operator object

    Args:
        | *dropdown* : DropDown object from the algorithm class

    Returns:
        | *op_object*: operator object converted
    """
    op_object = None

    if dropdown.value == "strictly smaller":
        op_object = operator.lt
    if dropdown.value == "smaller or equal":
        op_object = operator.le
    if dropdown.value == "equal":
        op_object = operator.eq
    if dropdown.value == "greater or equal":
        op_object = operator.ge
    if dropdown.value == "strictly greater":
        op_object = operator.gt
    return op_object

if __name__ == '__main__':
    pass
