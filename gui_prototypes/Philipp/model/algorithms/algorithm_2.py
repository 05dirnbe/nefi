# -*- coding: utf-8 -*-
"""
This class represents the algorithm EXAMPLE_ONE
"""
__authors__ = {"Philipp Reichert": "prei@me.com"}

from model.algorithms._alg import *


class AlgBody(Algorithm):
    """EXAMPLE_ONE algorithm implementation"""

    def report_pip(self):
        """
        Todo: implement
        Returns:

        """
        pass

    def __init__(self):
        """
        Blur object constructor
        Instance vars:
            self.name -- name of the algorithm
            self.parent -- name of the appropriated category
        """
        self.name = "EXAMPLE_ALGORITHM_2"
        self.parent = "EXAMPLE_CATEGORY_2"

        self.Slider1 = IntegerSlider("Setting 1", -10, 10, 1, 5)
        self.integer_sliders.append(self.Slider1)

        self.Slider2 = IntegerSlider("Setting 2",   0, 10, 2, 2)
        self.integer_sliders.append(self.Slider2)

        self.Slider3 = FloatSlider("Setting 3", -1.0, 2.0, 0.1, 1.2)
        self.float_sliders.append(self.Slider3)

        self.Checkbox1 = CheckBox("Checkbox 1", True)
        self.checkboxes.append(self.Checkbox1)

        self.DropDown1 = DropDown("DropDown 1", ["bla", "blup"])
        self.drop_downs.append(self.DropDown1)

    def process(self, image):
        pass


if __name__ == '__main__':
    pass
