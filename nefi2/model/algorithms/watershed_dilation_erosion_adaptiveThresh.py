#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This class represents the algorithm Watershed from the opencv package.
"""
import cv2
import numpy as np
from _alg import *


__authors__ = {"Sebastian Schattner": "s9sescat@stud.uni-saarland.de"}

# Segmentation routines

THRESHOLD_FG_COLOR = 255
THRESHOLD_BG_COLOR = 0

#markers for grabcut, watershed denoting sure-fg, sure-bg and let-the-algorithm-figure-it-out
FG_MARKER = 255
BG_MARKER = 150
UNDECIDED_MARKER = 0

class AlgBody(Algorithm):
    """
    Watershed algorithm implementation with dilation, erosion and adaptive threshold marker.
    """
    def __init__(self):
        """
        Watershed object constructor.

        Instance vars:
            | *name* : name of the algorithm
            | *parent* : name of the appropriate category
            | *kernelsize* : blurring kernel size that will be used as slider
              for the UI
            | *sigmaX* : gaussian kernel standard deviation in X direction

        """
        Algorithm.__init__(self)
        self.name = "Watershed - Dilation Erosion Adaptive Threshold"
        self.parent = "Segmentation"
        self.fg_iter = IntegerSlider("Foreground Iteration", 1,10, 1, 2)
        self.bg_iter = IntegerSlider("Background Iteration", 1, 10, 1, 1)
        self.block_size = IntegerSlider("Threshold Block Size", 1,20, 1, 5)
        self.constant = IntegerSlider("Threshold Constant", -10, 10, 1, 2)
        self.integer_sliders.append(self.fg_iter)
        self.integer_sliders.append(self.bg_iter)
        self.integer_sliders.append(self.block_size)
        self.integer_sliders.append(self.constant)

    def process(self, args):
        """
        Use the Watershed algorithm from the opencv package to the current
        image with the help of marker based ob dilation, erosion and
        adaptive threshold.

        Args:
            | *args* : a list of arguments, e.g. image ndarray

        """
        adapt_thresh = self.adaptive_threshold(image=args["img"],
                                               block_size=(self.block_size.value*2+1),
                                               constant=self.constant.value)
        seg1 = self.apply_mask_to_image(adapt_thresh,image=args["img"])
        marker = self.erosion_dilation_marker(image=args["img"],
                                              erosion_iterations=self.fg_iter.value,
                                              dilation_iterations=self.bg_iter.value,
                                              threshold_strategy=self.adaptive_threshold)
        watershed_marker = self.watershed(image=args["img"], marker=marker)
        seg2 = self.apply_mask_to_image(watershed_marker,image=args["img"])
        seg = cv2.bitwise_or(seg1, seg2)
        self.result['img'] = cv2.cvtColor(seg, cv2.COLOR_RGB2GRAY)

    def apply_mask_to_image(self, mask, image):
        """
        Constructs the segmented image based on the original image and the mask.

        Args:
            image: An input image which is not altered
            mask: A mask containing foreground and background information
        Returns:
             A segmented image
        """
        res = np.zeros_like(image)
        res[mask == THRESHOLD_FG_COLOR] = [THRESHOLD_FG_COLOR]*3

        return res

    def adaptive_threshold(self,
        image,
        threshold_value=255,
        threshold_type=cv2.THRESH_BINARY_INV,
        adaptive_type=cv2.ADAPTIVE_THRESH_MEAN_C,
        block_size=11,
        constant=2,
        **_):

        grayscale_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        result = cv2.adaptiveThreshold(grayscale_image, threshold_value, adaptive_type,
            threshold_type, block_size, constant)

        return result

    def erosion_dilation_marker(self,
        image,
        erosion_iterations=2,
        dilation_iterations=1,
        threshold_strategy=adaptive_threshold):
        """
        Applies morphological transformations to obtain the marker. The areas likely to be foreground
        are obtained by erosion. The areas likely to be background are obtained by dilation.
        The final marker is obtained by adding likely background to likely foreground where areas
        not part of either are considered undecided.

        Args:
            threshold_image: A properly thresholded image

        Returns:
            A marker subdividing image regions into likely foreground, likely background and undecided pixels
        """
        threshold_image = threshold_strategy(image)
        # determine likely foreground by erosion
        foreground_image = cv2.erode(threshold_image, None, iterations=erosion_iterations)

        # determine likely background by dilation
        background_image_tmp = cv2.dilate(threshold_image, None, iterations=dilation_iterations)
        background_image = cv2.threshold(background_image_tmp, 0, BG_MARKER, cv2.THRESH_BINARY_INV)[1]

        # regions not part of either likely foreground nor likely background are considered undecided
        marker = cv2.add(foreground_image, background_image)

        return marker

    def watershed(self,image, marker):
        """
        Applies opencv's watershed method iteratively to an input image. An initial marker containing
        preliminary information on which pixels are foreground serves as additional input.
        The initial marker can be based on user input (color-picking), or can be constructed
        with an automatic marker strategy. The marker decides from which pixels the flooding
        in the watershed method may start. Finally, the marker is used to obtain a mask
        classifying every pixel into foreground or background.

        Args:
            image: An input image which is not altered
            marker: A marer suitable for use with opencv's grabcut
            iterations: The number of iterations grabcut may update the marker

        Returns:
             A mask image classifying every pixel into foreground or background
        """

        if len(marker.shape) == 3:
            marker = marker[:,:,0]

        # convert the marker to the format watershed expects
        marker = np.int32(marker)

        # Use watershed to decide how to label the yet undecided regions.
        # This may produce may foreground areas labeld with different integers.
        cv2.watershed(image, marker)

        # Obtain the final mask by thresholding. Different foreground regions have different positive values.
        # We are only intrested in global foreground so we set all of them to be white, i.e. 255.
        mask_watershed = cv2.convertScaleAbs(marker)

        return mask_watershed


if __name__ == '__main__':
    pass