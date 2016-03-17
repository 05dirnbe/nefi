# -*- coding: utf-8 -*-

import cv2
import numpy as np
import networkx as nx
from nefi2.model.algorithms._alg import *

"""
This class represents the algorithm Canny edge
"""

__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}


class AlgBody(Algorithm):
    """
    Guo Hall algorithm implementation
    """

    def __init__(self):
        """
        Canny object constructor
            Instance vars:
                | *name* : name of the algorithm
                | *parent* : name of the appropriated category
                | *threshold1* : first threshold for the hysteresis procedure
                | *threshold2* : second threshold for the hysteresis procedure

        """
        Algorithm.__init__(self)
        self.name = "Canny graph detector"
        self.parent = "Graph detection"
        self.threshold1 = FloatSlider("threshold1", 1.0, 100.0, 1.0, 1.0)
        self.integer_sliders.append(self.threshold1)
        self.threshold2 = FloatSlider("threshold2", 1.0, 100.0, 1.0, 1.0)
        self.integer_sliders.append(self.threshold2)

    def auto_canny(self, args):
        """
        Use Canny edge algorithm without providing threshold values.
        It takes the median of the image, and then constructs upper and
        lower thresholds based on a percentage of this median.
        Args:
            | *image* : image instance

        Returns:

        """
        sigma = 0.33
        v = np.median(args[0])
        lower = int(max(0, (1.0 - sigma) * v))
        upper = int(min(255, (1.0 + sigma) * v))
        args[0] = cv2.Canny(args[0], lower, upper)

    def node_detection(self, skeleton):
        """

        Args:
            skeleton:
            | *skeleton* : skeletonised image instance

        Returns:
            Networkx graph with detected nodes
        """
        graph = nx.Graph()
        width, height = skeleton.shape
        item = skeleton.item
        for i in xrange(1, width - 1):
            for j in xrange(1, height - 1):
                isnode = False
                p2 = item(i - 1, j) / 255
                p3 = item(i - 1, j + 1) / 255
                p4 = item(i, j + 1) / 255
                p5 = item(i + 1, j + 1) / 255
                p6 = item(i + 1, j) / 255
                p7 = item(i + 1, j - 1) / 255
                p8 = item(i, j - 1) / 255
                p9 = item(i - 1, j - 1) / 255
                A = (p2 == 0 and p3 == 1) + (p3 == 0 and p4 == 1) + \
                    (p4 == 0 and p5 == 1) + (p5 == 0 and p6 == 1) + \
                    (p6 == 0 and p7 == 1) + (p7 == 0 and p8 == 1) + \
                    (p8 == 0 and p9 == 1) + (p9 == 0 and p2 == 1)
                if (A >= 3) or (A == 1):
                    isnode = True
                if item(i, j) != 0 and isnode == True:
                    graph.add_node((i, j))

        return graph

    def process(self, args):
        """
        Use the Canny algorithm from the opencv package to the current image.
        The function finds edges in the input image image and marks them in
        the output map edges using the Canny algorithm. The smallest value
        between threshold1 and threshold2 is used for edge linking

        Args:
            image:
            | *image* : image instance

        """
        skeleton = cv2.Canny(args[0], self.threshold1.value,
                             self.threshold2.value)
        graph = self.node_detection(skeleton)
