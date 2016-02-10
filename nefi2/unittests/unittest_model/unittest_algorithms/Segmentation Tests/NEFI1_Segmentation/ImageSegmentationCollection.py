""" different methods for segmenting an image

TODO
    * do something about color picking
    * pro mode
"""
from SegmentationAlgorithms import get_strategy
import SegmentationAlgorithms as SA
from functools import partial
import cv2 as cv

#TODO things can be made nicer by naming the parameters here the same as the parameters in
#SegmentationAlgorithms and manipulating dictionaries.

def __algorithms__():
    return {'Guided Watershed with adaptive threshold': guided_watershed_deletion_erosion_adaptive_threshold,
            'Guided Grabcut with deletion and erosion': guided_grabcut_deletion_erosion_otsus_threshold,
            'Guided Grabcut with distance transform': guided_grabcut_distance_transform_otsus_threshold,
            'Guided Watershed with deletion and erosion': guided_watershed_deletion_erosion_otsus_threshold,
            'Guided Watershed with distance transform' : guided_watershed_distance_transform_otsus_threshold,
            'Otsus Threshold': otsus_threshold,
            'Constant Threshold': constant_threshold,
            'Adaptive Threshold': adaptive_threshold}

def segment(img, method_dict):
    """ Segment the image with the method as indicated in the method dict """
    segmentations = __algorithms__()
    method = method_dict['method']
    parameters = method_dict['parameters']
    return segmentations[method](img, **parameters)

def guided_watershed_deletion_erosion_adaptive_threshold(src, fg_iter, bg_iter, constant, block_size, color_dict=None):
    adapt_thres = get_strategy(SA.adaptive_threshold, constant=constant, block_size=block_size)
    if color_dict is not None:
        marker_strategy1 = get_strategy(
            SA.user_defined_color_marker,
            fg_colors=color_dict['foreground'],
            bg_colors=color_dict['background'],
            threshold_strategy=SA.otsus_threshold)
        marker_strategy2 = partial(marker_strategy1, threshold_strategy=adapt_thres)
    else:
        marker_strategy1 = get_strategy(
            SA.erosion_dilation_marker,
            dilation_iterations=bg_iter,
            erosion_iterations=fg_iter,
            threshold_strategy=SA.adaptive_threshold)
        marker_strategy2 = partial(marker_strategy1, threshold_strategy=adapt_thres)

    seg_img_1 = SA.segment(src, marker_strategy1, get_strategy(SA.watershed))
    # seg_img_2 = SA.segment(src, marker_strategy2, get_strategy(SA.watershed))
    seg_img_2 = SA.segment(src, marker_strategy=get_strategy(SA.null_marker, image=src), masking_strategy=adapt_thres)

    return cv.bitwise_or(seg_img_1, seg_img_2)

def guided_watershed_deletion_erosion_otsus_threshold(src, fg_iter, bg_iter, color_dict=None):
    if color_dict is not None:
        marker_strategy = get_strategy(
            SA.user_defined_color_marker,
            fg_colors=color_dict['foreground'],
            bg_colors=color_dict['background'],
            threshold_strategy=SA.otsus_threshold)
    else:
        marker_strategy = get_strategy(SA.erosion_dilation_marker,
            dilation_iterations=bg_iter,
            erosion_iterations=fg_iter,
            threshold_strategy=SA.otsus_threshold)

    return SA.segment(src, marker_strategy, get_strategy(SA.watershed))

def guided_watershed_distance_transform_otsus_threshold(src, fg_iter, bg_iter, color_dict=None):
    if color_dict is not None:
        marker_strategy = get_strategy(
            SA.user_defined_color_marker,
            fg_colors=color_dict['foreground'],
            bg_colors=color_dict['background'],
            threshold_strategy=SA.otsus_threshold)
    else:
        marker_strategy = get_strategy(
            SA.distance_transform_dilation_marker,
            dilation_iterations=bg_iter,
            opening_iterations=fg_iter,
            threshold_strategy=SA.otsus_threshold)

    return SA.segment(src, marker_strategy, get_strategy(SA.watershed))

def guided_grabcut_deletion_erosion_otsus_threshold(src, fg_iter, bg_iter, gc_iter, color_dict=None):
    if color_dict is not None:
        marker_strategy = get_strategy(
            SA.user_defined_color_marker,
            fg_colors=color_dict['foreground'],
            bg_colors=color_dict['background'],
            threshold_strategy=SA.otsus_threshold)
    else:
        marker_strategy = get_strategy(SA.erosion_dilation_marker,
            dilation_iterations=bg_iter,
            erosion_iterations=fg_iter,
            threshold_strategy=SA.otsus_threshold)

    return SA.segment(src, marker_strategy, get_strategy(SA.grabcut, grabcut_iterations=gc_iter))

def guided_grabcut_distance_transform_otsus_threshold(src, fg_iter, bg_iter, gc_iter, color_dict=None):
    if color_dict is not None:
        marker_strategy = get_strategy(
            SA.user_defined_color_marker,
            fg_colors=color_dict['foreground'],
            bg_colors=color_dict['background'],
            threshold_strategy=SA.otsus_threshold)
    else:
        marker_strategy = get_strategy(
            SA.distance_transform_dilation_marker,
            dilation_iterations=bg_iter,
            opening_iterations=fg_iter,
            threshold_strategy=SA.otsus_threshold)

    return SA.segment(src, marker_strategy, get_strategy(SA.grabcut, grabcut_iterations=gc_iter))

def otsus_threshold(src, color_dict=None):

    return SA.segment(src, marker_strategy=get_strategy(SA.null_marker, image=src), masking_strategy=SA.otsus_threshold)

def adaptive_threshold(src, constant, block_size, color_dict=None):
    adapt_thres = get_strategy(SA.adaptive_threshold, constant=constant, block_size=block_size, threshold_type=cv.THRESH_BINARY_INV)
    return SA.segment(src, marker_strategy=get_strategy(SA.null_marker, image=src), masking_strategy=adapt_thres)

def constant_threshold(src, threshold_value, color_dict=None):
    return SA.segment(src,
        marker_strategy=get_strategy(SA.null_marker, image=src),
        masking_strategy=get_strategy(SA.constant_threshold,
        threshold_value=threshold_value))


