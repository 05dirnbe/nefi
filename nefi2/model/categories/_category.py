#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy
import re
import os
import sys
from importlib.machinery import SourceFileLoader


__authors__ = {"Pavel Shkadzko": "p.shkadzko@gmail.com",
               "Philipp Reichert": "prei@me.com"}


class Category:
    """
    This class represents image processing method that contains its respective
    algorithms. Its main function is controlling an algorithm, collecting and
    transmitting the output to the pipeline. It serves as an intermediate layer
    between the algorithms and the pipeline.
    """
    def __init__(self, name, icon=None):
        """
        Args:
            *name* (str): Category name

        Private Attributes:
            *_alg_dir* (str): a directory path for algorithms

        Public Attributes:
            | *name* (str): Category name
            | *icon* (str): Path to custom icon to be used for this category.
            | *available_algs* (dict): a dict of {Category: [alg, alg, ...]}
            | *alg_names* (list): a list of alg names for current category
            | *active_algorithm* (Algorithm): Currently selected algorithm

        """
        _alg_dir = os.path.join('nefi2', 'model', 'algorithms')
        self.name = name
        self.run_id = 1
        if icon is not None:
            self.icon = icon
        else:
            self.icon = os.path.join('nefi2', 'icons', 'missing.png')
        self.active_algorithm = None
        self.available_algs, self.alg_names = \
            self._get_available_algorithms(_alg_dir)

    def _get_available_algorithms(self, alg_dir):
        """
        Create a new list of algorithm files from model/algorithms dir.
        Create a dict of {Category: [alg, alg, ...]} that will be used to
        instantiate a specific Algorithm for the current category.
        Create a list of algorithms available for current category.
        Raise an error if no algorithm files were found.

        Args:
            *alg_dir* (str): a directory path for algorithms

        Vars:
            | *found_algs* (list): a filtered list of algorithm file names
            | *ignored*: a regex object, used to filter unnecessary files
            | *imported_algs* (list): a list of imported algorithm files

        Returns:
            | *category_alg_map* (dict): a dict of {Category: [alg, alg, ...]}
            | *alg_names* (list): algorithm list of the current category

        """
        alg_files = os.listdir(alg_dir)
        excluded = r'.*.pyc|__init__|_alg.py|__pycache__|_utility.py|_thread'
        ign = re.compile(excluded)
        found_algs = list(filter(lambda x: not ign.match(x), alg_files))
        if not found_algs:
            raise FileNotFoundError("No algorithm files were found in "
                                    "./model/algorithms")
        # add abs paths
        found_algs_paths = [os.path.join('nefi2', 'model', 'algorithms', alg)
                            for alg in found_algs]
        # import all available algorithm files as modules
        imported_algs = []
        for alg_path in found_algs_paths:
            alg_name = os.path.basename(alg_path).split('.')[0]
            algmod = SourceFileLoader(alg_name, alg_path).load_module()
            try:
                new_alg = algmod.AlgBody()
                new_alg_copy = copy.deepcopy(new_alg)
                imported_algs.append(new_alg_copy)  # instantiating algorithms
            except AttributeError as ex:
                print("AttributeError in _get_available_algorithms()", ex)
                continue
        # assign instantiated algorithms to corresponding categories
        category_alg_map = {self.name: [alg for alg in imported_algs
                                        if self.name == alg.belongs()]}
        alg_names = [alg.get_name() for alg in imported_algs
                     if self.name == alg.belongs()]
        return category_alg_map, alg_names

    def set_run_id(self, run_id):
        self.run_id = run_id

    def get_run_id(self):
        return self.run_id

    def set_active_algorithm(self, alg_name):
        """
        Explicitly set an algorithm for current method.

        Args:
            *alg_name* (str): algorithm's name that was selected in the UI

        """
        for alg in self.available_algs[self.name]:
            if alg.name == alg_name:
                self.active_algorithm = alg

    def get_active_algorithm(self):
        """
        Return the name of the currently set algorithm.

        Returns:
            *self.active_algorithm* (Algorithm): Currently selected algorithm

        """
        return self.active_algorithm

    def process(self, args):
        """
        Run a specific algorithm on the image.

        Args:
            *args* (ndarray|list): ndarray or a list of ndarray and Graph

        """
        selected_alg = [alg for alg in list(self.available_algs.values())[0]
                        if self.active_algorithm.name == alg.name][0]
        selected_alg.process(args)
        # reset modified variable after processing
        selected_alg.unset_modified()

    def copy_alg(self, alg_name):
        for alg in self.available_algs[self.name]:
            if alg.name == alg_name:
                return copy.copy(alg)

    def get_name(self):
        """
        Substitute spaces with underscores.

        Returns:
            a *category name* that will be displayed in UI

        """
        # return '_'.join(self.name.split())
        return self.name

    def set_name(self, name):
        """
        Set a category name that will be displayed in UI.

        Args:
            *name* (str): Category name

        """
        self.name = name

    def set_icon(self, icon_path):
        """
        Args:
            | *icon_path*: The path to the icon to be used

        """
        self.icon = icon_path

    def get_icon(self):
        """
        Returns:
            | *icon_path*: The path to the icon to be used

        """
        return self.icon


if __name__ == '__main__':
    pass
