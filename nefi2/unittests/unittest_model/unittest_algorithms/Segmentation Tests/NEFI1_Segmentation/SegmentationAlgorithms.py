
"""@package SegmentationAlgorithms

This module implements a family of segmentation algorithms. Given an input image
each image pixel is classfied as foreground or background. The resulting
segmented image may serve as an input for subsequent thinning algorithms.

Currently supported are:

1.) opencv's watershed method
2.) opencv's grabcut method
3.) using thresholding for segmentation

Watershed as well as grabcut expect as additional input a marker supplying
additional information on each pixel. Markers can be constructed using
different marker strategies. Some markers in turn need a thresholded
version of the input image to operate on. To obtain such a thresholded
image different thresholding strategies may be applied.

Example:

    Construct a segmentation method based on opencv's watershed, a marker
    based on erosion/dilation using a thresholded image obtained by a constant
    threshold with threshold value 150.

    segmentation_method = Segmentation_Watershed(marker_strategy=Erosion_Dilation_Marker,
                                                threshold_strategy=Constant_Threshold,
                                                threshold_value=150)

    Note that strategies may be mixed and matched at will and several other keyword arguments
    may be supplied to further customization. Usually, these arguments are controlled via the gui.

Status of the module:

    *   functional
    *   adaptive threshold is a cheat and needs to be reworked or removed

TODO:

    *   Documentation needs to be refined and spellchecked
    *   Coopcut needs to be explored as an additional segmentation method

"""

__author__ = ['mtd', "adrian"]

import cv2 as cv
import numpy as np
from functools import partial

# Segmentation routines

THRESHOLD_FG_COLOR = 255
THRESHOLD_BG_COLOR = 0

#markers for grabcut, watershed denoting sure-fg, sure-bg and let-the-algorithm-figure-it-out
FG_MARKER = 255
BG_MARKER = 150
UNDECIDED_MARKER = 0

def segment(image, marker_strategy, masking_strategy):
    marker = marker_strategy(image=image)
    mask = masking_strategy(image=image, marker=marker)
    return apply_mask_to_image(mask, image)

get_strategy = partial

def apply_mask_to_image(mask, image):
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

#threshold strategies
# these functions have an **_ argument that is unused so that they can
# accomodate a marker keyword argument should they be used to as a masking strategy

def otsus_threshold(image, threshold_value=0, threshold_type=cv.THRESH_BINARY_INV, **_):
    threshold_type += cv.THRESH_OTSU
    return constant_threshold(image, threshold_value, threshold_type)

def constant_threshold(image, threshold_value=0, threshold_type=cv.THRESH_BINARY_INV, **_):
    """
    Computes a threshold image of the source image using a constant threshold value.

    Args:
        Image: An input image which will not be changed

    Returns:
        A threshold image
    """
    grayscale_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    threshold_image = cv.threshold(grayscale_image, threshold_value, THRESHOLD_FG_COLOR, threshold_type)[1]

    return threshold_image  

def adaptive_threshold(
    image,
    threshold_value=255,
    threshold_type=cv.THRESH_BINARY_INV,
    adaptive_type=cv.ADAPTIVE_THRESH_MEAN_C,
    block_size=11,
    constant=2,
    **_):

    grayscale_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    result = cv.adaptiveThreshold(grayscale_image, threshold_value, adaptive_type,
        threshold_type, block_size, constant)

    return result


# marker strategies

def user_defined_color_marker(image, fg_colors, bg_colors):
    """
    Implements the construction of a marker based on user defined colors. Via color picking the user
    supplies twos sets of colors, background colors and foreground colors. The algorithm uses these sets
    to construct a marker which subdivides the input image into the following areas:

    1.) Areas belonging to the foreground
    2.) Areas undecided
    3.) Areas belonging to the background

    """
    marker = np.zeros(image.shape[:2], np.uint8)
    marker += UNDECIDED_MARKER

    blue, green, red = image[:, :, 0], image[:, :, 1], image[:, :, 2]

    # pixel that exhibit a color that the user has picked to be foreground get set to a
    # color denoting foreground
    for b, g, r in fg_colors:
        foreground_mask = (blue == b) & (green == g) & (red == r)
        marker[foreground_mask == True] = FG_MARKER

    # pixel that exhibit a color that the user has picked to be background get set to a
    # color denoting background
    for b, g, r in bg_colors:
        background_mask = (blue == b) & (green == g) & (red == r)
        marker[background_mask == True] = BG_MARKER

    return marker

def distance_transform_dilation_marker(image,
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
    morphological_opening = cv.morphologyEx(threshold_image, cv.MORPH_OPEN, kernel,
                                            iterations=opening_iterations)

    # determine likely foreground by distance transform. Regions near the center of objects
    # are most likely foreground.
    distance_transformation = cv.distanceTransform(morphological_opening, cv.DIST_L2, 5)
    foreground_image = np.uint8(
        cv.threshold(
            distance_transformation,
            distance_factor*distance_transformation.max(),
            FG_MARKER,
            cv.THRESH_BINARY)[1])

    # determine likely background by dilation
    background_image = cv.dilate(morphological_opening, kernel, iterations=dilation_iterations)
    background_image = cv.threshold(background_image, 0, BG_MARKER, cv.THRESH_BINARY_INV)[1]

    # regions not part of either likely foreground nor likely background are considered undecided
    return cv.add(foreground_image, background_image)

def erosion_dilation_marker(
    image,
    erosion_iterations=2,
    dilation_iterations=1,
    threshold_strategy=otsus_threshold):
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
    foreground_image = cv.erode(threshold_image, None, iterations=erosion_iterations)

    # determine likely background by dilation
    background_image_tmp = cv.dilate(threshold_image, None, iterations=dilation_iterations)
    background_image = cv.threshold(background_image_tmp, 0, BG_MARKER, cv.THRESH_BINARY_INV)[1]

    # regions not part of either likely foreground nor likely background are considered undecided
    marker = cv.add(foreground_image, background_image)

    return marker

def threshold_marker(image, threshold_strategy=otsus_threshold):
    """
    Executes the threshold strategy of self to obtain a threshold image of the source image.
    Furthermore the thresholded image is used to create a marker. This marker subdivides the source
    image into regions of foreground and background pixels and may be used as an
    input for different segmentation algorithms.

    The function realizes a marker strategy to be used in segmentation algorithms.
    It executes a threshold strategy to do so.

    Args:
        self: An instance of an object implementing apply_threshold()
        src: Source image.
        parameter_map: A map with all parameters

    Returns:
        A marker subdividing image regions into foreground and background
    """
    threshold_image = threshold_strategy(image)

    marker = np.zeros_like(image)
    marker += BG_MARKER
    marker[threshold_image == THRESHOLD_FG_COLOR] = FG_MARKER

    return marker


def null_marker(image, **_):
    return image

# masking strategies

def grabcut(image, marker, grabcut_iterations=5):
    """
    Applies opencv's grabcut method iteratively to an input image. An initial marker containing
    preliminary information on whether a pixel is foreground, background or probably background
    serves as additional input. The initial marker can be based on user input (color-picking),
    or can be constructed with an automatic marker strategy. The marker is updated and improved
    by the grabcut method iteratively. Finally, the marker is used to obtain a mask classifying
    every pixel into foreground or background.

    Args:
        image: An input image which is not altered
        marker: A marker suitable for use with opencv's grabcut
    Returns:
         A mask image classifying every pixel into foreground or background
    """

    # data structures grabcut needs to operate
    background_model = np.zeros((1, 65), np.float64)
    foreground_model = np.zeros((1, 65), np.float64)

    # an empty mask to start from
    grabcut_mask = np.zeros(image.shape[:2], np.uint8)
    grabcut_mask = np.zeros_like(marker)

    #set undecided pixel to grabcuts probably background
    grabcut_mask[marker == UNDECIDED_MARKER] = cv.GC_PR_BGD
    # #set undecided pixel to grabcuts probably foreground
    grabcut_mask[marker == UNDECIDED_MARKER] = cv.GC_PR_FGD
    #set black pixel to grabcuts definitely background
    grabcut_mask[marker == BG_MARKER] = cv.GC_BGD
    #set white pixel to grabcuts definitely foreground
    grabcut_mask[marker == FG_MARKER] = cv.GC_FGD

    #run grabcut and let it figure out the undecided areas of the image and update the guiding grabcut_mask
    cv.grabCut(image,
        grabcut_mask,
        None,
        background_model,
        foreground_model,
        grabcut_iterations,
        mode=cv.GC_INIT_WITH_MASK)

    mask = np.zeros_like(grabcut_mask)

    # replace probable background/foreground with definite background/foreground respectively and the final mask is done
   
    mask[grabcut_mask == cv.GC_FGD] = FG_MARKER
    mask[grabcut_mask == cv.GC_PR_FGD] = FG_MARKER
    mask[grabcut_mask == cv.GC_BGD] = BG_MARKER
    mask[grabcut_mask == cv.GC_PR_BGD] = BG_MARKER

    return mask

def watershed(image, marker):
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
    cv.watershed(image, marker)

    # Obtain the final mask by thresholding. Different foreground regions have different positive values.
    # We are only intrested in global foreground so we set all of them to be white, i.e. 255.
    mask_watershed = cv.convertScaleAbs(marker)
    
    return mask_watershed

