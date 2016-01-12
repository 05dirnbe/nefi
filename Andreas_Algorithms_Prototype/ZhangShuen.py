# -*- coding: utf-8 -*-

import cv2
import numpy as np

from Andreas_Algorithms_Prototype import CannyEdge
from nefi2.model.algorithms._alg import *


"""
This class represents the algorithm Zhang Suen
"""
__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}

class AlgBody(Algorithm):
    """
    Zhang Suen algorithm implementation
    """

    def __init__(self):
        """
        Zhang Suen object constructor
            Instance vars:
                | *name* : name of the algorithm
                | *parent* : name of the appropriated category

        """
        Algorithm.__init__(self)
        self.name = "Zhang Suen graph detector"
        self.parent = "Graph detection"


    def process(self, image):
        """
        Use the Zhang Suen thining algorithm from the thinning package to
        the current image

        Args:
            | *image* : image instance

        """
        skeleton = self.thinningZhangSuen(image)
        graph = CannyEdge.node_detection(skeleton)

    def thinningZhangSuenIteration(self, image, iterations):
        """
        Perform one thinning iteration. See https://www.google.de/url?sa=t&rct=
        j&q=&esrc=s&source=web&cd=1&ved=0ahUKEwi-46321J_KAhWLnBoKHfeDA68QFgglMA
        A&url=http%3A%2F%2Fopencv-code.com%2Fquick-tips%2Fimplementation-of-
        thinning-algorithm-in-opencv%2F&usg=AFQjCNHIbo-7KLIUljKNEEKqBwu9R_6SIg
        &sig2=KQ0lXyE4DrAWlyqmOmqgrQ
        Args:
            | *image* : image instance (binary image with range = 0-1)
            | *iterations* : 0=even, 1=odd

        Returns:

        """
        size = np.size(image)
        #cv::Mat marker = cv::Mat::zeros(im.size(), CV_8UC1);
        marker = cv2.Mat.zeros(size, cv2.CV_8UC1)   #Is this right?
        weigth, height = image.shape
        item = image.item
        for i in xrange(1, weigth-1):
            for j in xrange(1, height-1):
                isnode = False
                p2 = item(i-1, j)/255
                p3 = item(i-1, j+1)/255
                p4 = item(i, j+1)/255
                p5 = item(i+1, j+1)/255
                p6 = item(i+1, j)/255
                p7 = item(i+1, j-1)/255
                p8 = item(i, j-1)/255
                p9 = item(i-1, j-1)/255
                A = (p2 == 0 and p3 == 1) + (p3 == 0 and p4 == 1) + \
                    (p4 == 0 and p5 == 1) + (p5 == 0 and p6 == 1) + \
                    (p6 == 0 and p7 == 1) + (p7 == 0 and p8 == 1) + \
                    (p8 == 0 and p9 == 1) + (p9 == 0 and p2 == 1)
                B = p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9
                if iterations == 0:
                    m1 = p2 * p4 * p6
                else:
                    m1 = p2 * p4 * p8
                if iterations == 0:
                    m2 = p4 * p6 * p8
                else:
                    m2 = p2 * p6 * p8
                if(A == 1 and (B>= 2 and B <= 6) and m1 == 0 and m2 == 0):
                    # marker.at<uchar>(i,j) = 1
                    # how to do this?
                    marker
        image = marker


    def thinningZhangSuen(self, image):
        """
        Perform Zhang Suen thinning for given binary image
        Args:
            | *image* : image instance (binary image with range = 0-1)

        Returns:

        """
        image /= 255
        size = np.size(image)
        #cv::Mat marker = cv::Mat::zeros(im.size(), CV_8UC1);
        prev = cv2.Mat.zeros(size, cv2.CV_8UC1)   #Is this right?
        diff = np.array(image.shape[0],image.shape[1])
        while cv2.countNonZero(diff) <= 0:
            self.thinningZhangSuenIteration(image,0)
            self.thinningZhangSuenIteration(image,1)
            cv2.absdiff(image,prev,diff)
            image.copyTo(prev)
        image *= 255