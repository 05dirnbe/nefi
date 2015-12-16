# -*- coding: utf-8 -*-
"""
This class represents image processing method that contains its respective
algorithms. Its main function is controlling an algorithm, collecting and
transmitting the output to the pipeline. It serves as an intermediate layer
between the algorithms and the pipeline.
"""

__author__ = "p.shkadzko@gmail.com"


import random as rnd
import re
import os
import sys


class Step:
    def __init__(self, name=""):
        """
        Step class
        Params:
            name -- Step name
        Private vars:
            _alg_dir -- a directory path for algorithms
        Instance vars:
            self.name -- Step name
            self.available_algs -- a dict of {Step: [alg, alg, ...]}
            self.active_algorithm -- Currently selected algorithm
        """
        _alg_dir = os.path.join('model', 'algorithms')
        self.name = name
        self.available_algs = self._get_available_algorithms(_alg_dir)
        # since no settings are implemented, use random choice for alg
        self.active_algorithm = rnd.choice(self.available_algs.values()[0])
        # for debugging only
        # print '> Step: I am "%s" step' % self.name
        # print '> I have the following algorithms:'
        # for a in self.available_algs.values():
        #   print a
        # print len(self.available_algs.values()[0]), 'in total.'
        # print ''

    def set_available_algorithms(self):
        pass

    def _get_available_algorithms(self, alg_dir):
        """
        Create a new list of algorithm files from model/algorithms dir.
        Create a dict of {Step: [alg, alg, ...]} that will be used to
        instantiate a specific Algorithm for the current step.
        Params:
            alg_dir -- a directory path for algorithms
        Vars:
            found_algs -- a filtered list of algorithm file names
            ignored -- a regex object, used to filter unnecessary files
            imported_algs -- a list of imported algorithm files
        Returns:
            step_alg_map -- a dict of {Step: [alg, alg, ...]}
        """
        alg_files = os.listdir(alg_dir)
        ignored = re.compile(r'.*.pyc|__init__|_alg.py')
        found_algs = filter(lambda x: not ignored.match(x), alg_files)
        # import all available algorithm files as modules
        imported_algs = []
        for alg in found_algs:
            imported_algs.append(__import__(alg.split('.')[0],
                                            fromlist=['Body']))
        step_alg_map = {self.name: [alg for alg in imported_algs
                        if self.name == alg.Body().belongs()]}
        return step_alg_map

    def set_active_algorithm(self, alg_name):
        """
        Explicitly set an algorithm for current method.
        Params:
            alg_name -- algorithm's name that was selected in the UI
        """
        # print '> "%s" step: "%s" algorithm shall be used' % (self.name, alg_name)
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
        #print '> "%s" step: using "%s" algorithm' % (self.name, self.active_algorithm)
        runalg = [alg for alg in self.available_algs.values()[0]
                  if self.active_algorithm.Body().name == alg.Body().name][0]
        results = runalg.Body().process(image)
        runalg.Body().unset_modified()  # reset modified variable after processing
        return results

    def get_name(self):
        return self.name


if __name__ == '__main__':
    pass
