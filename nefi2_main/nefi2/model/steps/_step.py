# -*- coding: utf-8 -*-
"""
This class represents image processing method that contains its respective
algorithms. Its main function is controlling an algorithm, collecting and
transmitting the output to the pipeline. It serves as an intermediate layer
between the algorithms and the pipeline.
"""

__author__ = "p.shkadzko@gmail.com"


import random as rnd
import sys


class Step:
    def __init__(self, name, imported_algs):
        """
        Step class
        Params:
            name -- Step name
            imported_algs -- a list of imported algorithm files
        Instance vars:
            self.name -- Step name
            self.available_algs -- a dict of {Step: [alg, alg, ...]}
            self.modified -- True if Method's state has been modified
            self.active_algorithm -- Currently selected algorithm
        """
        self.name = name
        self.available_algs = self.get_available_algorithms(imported_algs)
        self.modified = False
        self.active_algorithm = rnd.choice(self.available_algs.values()[0])
        # for debugging only
        print '> Step: I am "%s" step' % self.name
        print '> I have the following algorithms:'
        for a in self.available_algs.values():
            print a
        print len(self.available_algs.values()[0]), 'in total.'
        print ''

    def set_available_algorithms(self):
        pass

    def get_available_algorithms(self, imported):
        """
        Create a dict of {Step: [alg, alg, ...]} that will be used to
        instantiate a specific Algorithm for the current step.
        Params:
            imported -- a list of imported algorithm files
        Returns:
            step_alg_map -- a dict of {Step: [alg, alg, ...]}
        """
        step_alg_map = {self.name: [alg for alg in imported
                        if self.name == alg.Body().belongs()]}
        return step_alg_map

    def set_active_algorithm(self, alg_name):
        """
        Explicitly set an algorithm for current method.
        Params:
            alg_name -- algorithm's name that was selected in the UI
        """
        print '> "%s" step: "%s" algorithm shall be used' % (self.name, alg_name)
        self.active_algorithm = alg_name

    def get_active_algorithm(self):
        """
        Return the name of the currently set algorithm.
        Returns:
            self.active_algorithm -- Currently selected algorithm
        """
        return self.active_algorithm

    def scan_algorithms(self):
        pass

    def process(self, image):
        """
        Run a specific algorithm on the image.
        Params:
            image -- a path to image file
        """
        print '> "%s" step: using "%s" algorithm' % (self.name, self.active_algorithm)
        runalg = [alg for alg in self.available_algs.values()[0]
                  if self.active_algorithm.Body().name == alg.Body().name][0]
        results = runalg.Body().process(image)
        self.modified = False  # reset modified variable after processing
        return results

    def get_name(self):
        return self.name

    def get_modified(self):
        return self.modified


if __name__ == '__main__':
    pass