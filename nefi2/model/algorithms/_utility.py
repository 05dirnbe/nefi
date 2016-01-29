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