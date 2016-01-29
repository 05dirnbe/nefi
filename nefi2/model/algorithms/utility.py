"""
This python file contains helpful methods which
are of static nature and are beneficial for several
algorithms. The main reason for the creation of this file
is to provide the user with a toolbox of methods and
don't force him to copy and paste methods from other algorithm
sections.
"""
import operator as op


def draw_graph(image, graph):
    """
    draws the graph in the image by traversing the graph structure

    Args:
        image: the image where the graph needs to be drawn
        graph: the *.txt file containing the graph information

    Returns:

    """

def checkOperator(operator):
        if operator.value == "Strictly smaller":
            return op.lt
        if operator.value == "Smaller or equal":
            return op.le
        if operator.value == "Equal":
            return op.eq
        if operator.value == "Greater or equal":
            return op.ge
        if operator.value == "Strictly greater":
            return op.gt

if __name__ == '__main__':
    pass