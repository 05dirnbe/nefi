#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This class represents the algorithm Invert Color
"""
import cv2
from _alg import Algorithm, CheckBox


__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com",
               "Sebastian Schattner": "s9sescat@stud.uni-saarland.de"}


class AlgBody(Algorithm):
    """
    Invert Color algorithm implementation
    """
    def __init__(self):
        """
        Invert Color object constructor
            Instance vars:
                | *name* : name of the algorithm
                | *parent* : name of the appropriate category

        """
        Algorithm.__init__(self)
        self.name = "Invert Color"
        self.parent = "Preprocessing"
        self.channel1 = CheckBox("channel1", True)
        self.channel2 = CheckBox("channel2", True)
        self.channel3 = CheckBox("channel3", True)
        self.checkboxes.append(self.channel1)
        self.checkboxes.append(self.channel2)
        self.checkboxes.append(self.channel3)

    def process(self, args):
        """
        Invert the current image

        Args:
            | *args* : a list of arguments, e.g. image ndarray

        """
        channels = cv2.split(args[0])
        if self.channel1.value:
            channels[0] = (255-channels[0])
        if self.channel2.value:
            channels[1] = (255-channels[1])
        if self.channel3.value:
            channels[2] = (255-channels[2])
        self.result['img'] = cv2.merge(channels)


if __name__ == '__main__':
    pass
