#!/usr/bin/env python3
"""
Generates a json pipeline representation using default! settings for each
algorithm.
"""

import re


ALGS = {
    # preprocessing
    0: ["Bilateral Filter",
        "Blur",
        "Color enhancement",
        "Fast nl Means Denoising Colored",
        "Fast nl Means Denoising",
        "Gaussian Blur",
        "Invert Color",
        "Median Blur"],
    # segmentation
    1: ["Adaptive Threshold",
        "Constant Threshold",
        "Grabcut - Dilation Erosion Otsu",
        "Grabcut - Distance Transform Otsu",
        "Otsus Threshold",
        "Watershed - Dilation Erosion Adaptive Threshold",
        "Watershed - Dilation Erosion Otsu",
        "Watershed - Distance Transform Otsu"],
    # graph detection
    2: ["Guo Hall Thinning"],
    # graph filtering
    3: ["Connected component filter",
        "Edge attribute filter",
        "Keep only largest connected component",
        "Simple cycle filter",
        "Smooth degree 2 nodes"]
}

SETTINGS = {
    "Bilateral Filter": {"channel1": "true",
                         "channel2": "true",
                         "channel3": "true",
                         "diameter": 1,
                         "sigmaColor": 30.0,
                         "sigmaSpace": 30.0,
                         "store_image": "false",
                         "type": "Preprocessing"},
    "Blur": {"channel1": "true",
             "channel2": "true",
             "channel3": "true",
             "kernelsize": 1,
             "store_image": "false",
             "type": "Preprocessing"},
    "Color enhancement": {"channel1": "true",
                          "channel2": "true",
                          "channel3": "true",
                          "left percentage": 2.5,
                          "right percentage": 2.5,
                          "store_image": "false",
                          "type": "Preprocessing"},
    "Fast nl Means Denoising Colored": {"filter strength": 1.0,
                                        "filter strength color": 1.0,
                                        "template window size": 3,
                                        "search window size": 10,
                                        "store_image": "false",
                                        "type": "Preprocessing"},
    "Fast nl Means Denoising": {"channel1": "true",
                                "channel2": "true",
                                "channel3": "true",
                                "filter strength": 1.0,
                                "template window size": 3,
                                "search window size": 10,
                                "store_image": "false",
                                "type": "Preprocessing"},
    "Gaussian Blur": {"channel1": "true",
                      "channel2": "true",
                      "channel3": "true",
                      "kernelsize": 1,
                      "sigmaX": 1.0,
                      "store_image": "false",
                      "type": "Preprocessing"},
    "Invert Color": {"channel1": "true",
                     "channel2": "true",
                     "channel3": "true",
                     "store_image": "false",
                     "type": "Preprocessing"},
    "Median Blur": {"channel1": "true",
                    "channel2": "true",
                    "channel3": "true",
                    "kernelsize": 1,
                    "store_image": "false",
                    "type": "Preprocessing"},
    "Adaptive Threshold": {"store_image": "false",
                           "type": "Segmentation"},
    "Constant Threshold": {"Threshold": 127,
                           "store_image": "false",
                           "type": "Segmentation"},
    "Grabcut - Dilation Erosion Otsu": {"Foreground Iteration": 2,
                                        "Background Iteration": 1,
                                        "GrabCut Iteration": 5,
                                        "store_image": "false",
                                        "type": "Segmentation"},
    "Grabcut - Distance Transform Otsu": {"Foreground Iteration": 2,
                                          "Background Iteration": 1,
                                          "GrabCut Iteration": 5,
                                          "store_image": "false",
                                          "type": "Segmentation"},
    "Otsus Threshold": {"store_image": "false",
                        "type": "Segmentation"},
    "Watershed - Dilation Erosion Adaptive Threshold": {"Foreground Iteration": 2,
                                                        "Background Iteration": 1,
                                                        "Threshold Block Size": 5,
                                                        "Threshold Constant": 2,
                                                        "store_image": "false",
                                                        "type": "Segmentation"},
    "Watershed - Dilation Erosion Otsu": {"Foreground Iteration": 2,
                                          "Background Iteration": 1,
                                          "store_image": "false",
                                          "type": "Segmentation"},
    "Watershed - Distance Transform Otsu": {"Foreground Iteration": 2,
                                            "Background Iteration": 1,
                                            "store_image": "false",
                                            "type": "Segmentation"},
    "Guo Hall Thinning": {"store_image": "false",
                          "type": "Graph detection"},
    "Connected component filter": {"Operator":"Strictly smaller",
                                   "store_image": "false",
                                   "type": "Graph filtering"},
    "Edge attribute filter": {"Operator":"Strictly smaller",
                              "Attribute":"width",
                              "store_image": "false",
                              "type": "Graph filtering"},
    "Keep only largest connected component": {"store_image": "false",
                                              "type": "Graph filtering"},
    "Simple cycle filter": {"store_image": "false",
                            "type": "Graph filtering"},
    "Smooth degree 2 nodes": {"store_image": "false",
                              "type": "Graph filtering"}
}


def format_node(node):
    # convert node to json format
    node = re.sub('\'', '"', str(node))
    node = re.sub('"false"', 'false', node)
    node = re.sub('"true"', 'true', node)
    node = re.sub('{', '', node, 1)
    node = re.sub('}', '', node, 1)
    node = re.sub('"true"', 'true', node)
    return node


def generate_pips():
    """
    Using globals, generate a pipelines list.
    """
    preprocessing = ALGS[0]
    segmentation = ALGS[1]
    d = "Guo Hall Thinning"
    d_settings = format_node(SETTINGS[d])
    filtering = ALGS[3]
    json_pips = []
    pip_chain = []
    for f in filtering:
        for s in segmentation:
            for p in preprocessing:
                p_settings = format_node(SETTINGS[p])
                s_settings = format_node(SETTINGS[s])
                f_settings = format_node(SETTINGS[f])
                pip_chain.append('{0} -> {1} -> {2} -> {3}'.format(p, s, d, f))
                json_pips.append('[["{0}", {{{1}}}],'
                                 '["{2}", {{{3}}}],'
                                 '["{4}", {{{5}}}],'
                                 '["{6}", {{{7}}}]]'.format(p, p_settings,
                                                            s, s_settings,
                                                            d, d_settings,
                                                            f, f_settings
                                                           )
                                )
    return json_pips, pip_chain


if __name__ == "__main__":
    pass
