#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
from _alg import Algorithm, FloatSlider, CheckBox


__authors__ = {"Sebastian Schattner": "s9sescat@stud.uni-saarland.de"}


class AlgBody(Algorithm):
    """Color enhancement algorithm implementation"""
    def __init__(self):
        Algorithm.__init__(self)
        self.name = "Color Enchance"
        self.parent = "Preprocessing"
        self.left_pct = FloatSlider("left percentage", 0.0, 10.0, 0.1, 2.5)
        self.right_pct = FloatSlider("right percentage", 0.0, 10.0, 0.1, 2.5)
        self.channel1 = CheckBox("channel1", True)
        self.channel2 = CheckBox("channel2", True)
        self.channel3 = CheckBox("channel3", True)
        self.float_sliders.append(self.left_pct)
        self.float_sliders.append(self.right_pct)
        self.checkboxes.append(self.channel1)
        self.checkboxes.append(self.channel2)
        self.checkboxes.append(self.channel3)

    def process(self, args):
        channels = cv2.split(args[0])
        if self.channel1.value:
            channels[0] = self.compute_channels(channels[0])
        if self.channel2.value:
            channels[1] = self.compute_channels(channels[1])
        if self.channel3.value:
            channels[2] = self.compute_channels(channels[2])
        self.result['img'] = cv2.merge(channels)

    def compute_channels(self, image_channel):
        vmin = 0
        vmax = 255
        hist = cv2.calcHist([image_channel], [0], None, [256], [0, 256])
        cdf = hist.cumsum()

        for i, e in list(enumerate(cdf)):
            if e > image_channel.size * (self.left_pct.value / 100):
                if i != 0:
                    vmin = i-1
                break

        for i, e in list(enumerate(cdf)):
            if e > image_channel.size * (1 - (self.right_pct.value / 100)):
                vmax = i
                break

        if vmax != vmin:
            for i in range(image_channel.shape[0]):
                for j in range(image_channel.shape[1]):
                    pix = image_channel.item(i, j)
                    if pix < vmin:
                        image_channel.itemset((i, j), vmin)
                    elif pix > vmax:
                        image_channel.itemset((i, j), vmax)
                    vmin_ij = image_channel.item(i, j) - vmin
                    image_channel.itemset((i, j), vmin_ij * 255 / (vmax-vmin))
        return image_channel


if __name__ == '__main__':
    pass
