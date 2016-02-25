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
            | *fg_iter* : Number of foreground iterations for markers
            | *bg_iter* : Number of background iterations for markers

        """
        Algorithm.__init__(self)
        self.name = "Watershed - Distance Transform Otsu"
        self.parent = "Segmentation"
        self.fg_iter = IntegerSlider("Foreground Iteration", 1,10, 1, 2)
        self.bg_iter = IntegerSlider("Background Iteration", 1, 10, 1, 1)
        self.integer_sliders.append(self.fg_iter)
        self.integer_sliders.append(self.bg_iter)

    def process(self, args):
        """
        Use the Watershed algorithm from the opencv package to the current
        image with the help of marker based ob dilation, erosion and
        adaptive threshold.

        Args:
            | *args* : a list of arguments, e.g. image ndarray

        """
        marker = self.distance_transform_dilation_marker(image=args[0],
                                                         opening_iterations=self.fg_iter.value,
                                                         dilation_iterations=self.bg_iter.value,
                                                         threshold_strategy=self.otsus_threshold)
        watershed_marker = self.watershed(image=args[0], marker=marker)
        seg = self.apply_mask_to_image(watershed_marker, image=args[0])

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

    def otsus_threshold(self, image, threshold_value=0, threshold_type=cv2.THRESH_BINARY_INV, **_):
        if (len(image.shape) == 3):
            greyscale_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            greyscale_image = image

        threshold_type += cv2.THRESH_OTSU
        threshold_image = cv2.threshold(greyscale_image, threshold_value, THRESHOLD_FG_COLOR, threshold_type)[1]
        return threshold_image

    def distance_transform_dilation_marker(self,image,
        opening_iterations=2,
        dilation_iterations=1,
        kernel=np.ones((3, 3), np.uint8),
        distance_factor=0.7,
        threshold_strategy=otsus_threshold):

        """
        Applies morphological transformation, i.e. morphological opening using a kernel to obtain the areas
        of the image likely to be foreground. The areas likely to be background are obtained by dilation.
        The final marker is obtained by adding likely background to likely foreground where areas not part of
        either are considered undecided.

        Args:
            threshold_image: A properly thresholded image

        Returns:
            A marker subdividing image regions into likely foreground, likely background and undecided pixels
        """

        threshold_image = threshold_strategy(image)

        # noise removal by morphological opening. This removes stray white pixels from the image
        morphological_opening = cv2.morphologyEx(threshold_image, cv2.MORPH_OPEN, kernel,
                                                iterations=opening_iterations)

        # determine likely foreground by distance transform. Regions near the center of objects
        # are most likely foreground.
        distance_transformation = cv2.distanceTransform(morphological_opening, cv2.DIST_L2, 5)
        foreground_image = np.uint8(
            cv2.threshold(
                distance_transformation,
                distance_factor*distance_transformation.max(),
                FG_MARKER,
                cv2.THRESH_BINARY)[1])

        # determine likely background by dilation
        background_image = cv2.dilate(morphological_opening, kernel, iterations=dilation_iterations)
        background_image = cv2.threshold(background_image, 0, BG_MARKER, cv2.THRESH_BINARY_INV)[1]

        # regions not part of either likely foreground nor likely background are considered undecided
        return cv2.add(foreground_image, background_image)

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