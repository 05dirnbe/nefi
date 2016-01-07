# -*- coding: utf-8 -*-
import random as rnd
import re
import os
import sys

__authors__ = {"Pavel Shkadzko": "p.shkadzko@gmail.com"}


class Category:
    """
    This class represents image processing method that contains its respective
    algorithms. Its main function is controlling an algorithm, collecting and
    transmitting the output to the pipeline. It serves as an intermediate layer
    between the algorithms and the pipeline.
    """

    def __init__(self, name=""):
        """
        # for debugging only
        # print '> Category: I am "%s" category' % self.name
        # print '> I have the following algorithms:'
        # for a in self.available_algs.values():
        #   print a
        # print len(self.available_algs.values()[0]), 'in total.'
        # print ''

        Args:
            name: Category name

        Private Attributes:
            _alg_dir: a directory path for algorithms

        Public Attributes:
            name: Category name
            available_algs: a dict of {Category: [alg, alg, ...]}
            alg_names (list): a list of algorithms for current category
            active_algorithm: Currently selected algorithm
        """
        for path in sys.path:
            if path.endswith('algorithms'):
                _alg_dir = path
        self.available_algs, self.alg_names = \
            self._get_available_algorithms(_alg_dir)
        # since no settings are implemented, use random choice for alg
        self.active_algorithm = rnd.choice(list(
                                            self.available_algs.values())[0])


    def set_available_algorithms(self):
        pass

    def _get_available_algorithms(self, alg_dir):
        """
        Create a new list of algorithm files from model/algorithms dir.
        Create a dict of {Category: [alg, alg, ...]} that will be used to
        instantiate a specific Algorithm for the current category.
        Create a list of algorithms available for current category.

        Args:
            alg_dir: a directory path for algorithms

        Vars:
            found_algs: a filtered list of algorithm file names
            ignored: a regex object, used to filter unnecessary files
            imported_algs: a list of imported algorithm files

        Returns:
            category_alg_map: a dict of {Category: [alg, alg, ...]}
            alg_names: a list of algorithms that belong to current category
        """
        alg_files = os.listdir(alg_dir)
        ignored = re.compile(r'.*.pyc|__init__|_alg.py')
        found_algs = filter(lambda x: not ignored.match(x), alg_files)
        # import all available algorithm files as modules
        imported_algs = []
        for alg in found_algs:
            imported_algs.append(__import__(alg.split('.')[0],
                                            fromlist=['AlgBody']))
        category_alg_map = {self.name: [alg for alg in imported_algs
                            if self.name == alg.AlgBody().belongs()]}
        alg_names = [alg.AlgBody().get_name() for alg in imported_algs
                     if self.name == alg.AlgBody().belongs()]
        return category_alg_map, alg_names

    def set_active_algorithm(self, alg_name):
        """
        Explicitly set an algorithm for current method.

        Args:
            alg_name: algorithm's name that was selected in the UI
        """
        self.active_algorithm = alg_name

    def get_active_algorithm(self):
        """
        Return the name of the currently set algorithm.

        Returns:
            self.active_algorithm: Currently selected algorithm
        """
        return self.active_algorithm

    def scan_algorithms(self):
        pass

    def process(self, image):
        """
        Run a specific algorithm on the image.

        Args:
            image: a path to image file
        """
        ralg = [alg for alg in list(self.available_algs.values())[0]
                if self.active_algorithm.AlgBody().name == alg.AlgBody().name][0]
        results = ralg.AlgBody().process(image)
        # reset modified variable after processing
        ralg.AlgBody().unset_modified()
        return results

    def get_name(self):
        """
        Returns:
            a category name that will be displayed in UI.
        """
        return self.name

    def set_name(self, name):
        """
        Set a category name that will be displayed in UI.

        Args:
            name: a name of the Category
        """
        self.name = name


if __name__ == '__main__':
    pass
