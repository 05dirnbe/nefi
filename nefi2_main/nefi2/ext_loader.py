# -*- coding: utf-8 -*-
"""
A class that works with "model" folder and is used to initialize the pipeline
with all available image processing categories and their respective algorithms.
It uses config.json settings to initialize image processing categories
accordingly.
ExtensionLoader creates a collection of categories and algorithms ready to be
loaded into the pipeline object.
"""
__authors__ = {"Pavel Shkadzko": "p.shkadzko@gmail.com"}


import re
import os
import sys
sys.path.insert(0, os.path.join(os.curdir, 'model', 'categories'))
sys.path.insert(0, os.path.join(os.curdir, 'model', 'algorithms'))
import xml.etree.ElementTree as et
from collections import OrderedDict as od


def read_configs():
    """
    Parse config.xml, extract categories order.
    Returns:
        order -- a list of categories order
    """
    tree = et.parse('config.xml')  # categories order
    root = tree.getroot()
    # create categories order list
    order = [e.text for elem in root for e in elem.iter('category')]
    return order


class ExtensionLoader:
    """
    A class that imports and initializes all available image processing
    categories and their algorithms.
    It scans for new files in /model/algorithms and /model/categories.
    It checks these files for compliance with the interface, analyses which
    algorithm belongs to which method and creates a corresponding mapping that
    is used by Step class upon instantiating.
    """
    def __init__(self):
        """
        Constructor
        Instance vars:
            self.category_dir -- a directory path for categories
            self.loaded_algs -- a list of algorithm paths
            self.loaded_cats -- a list of category paths
            self.cats_container -- a dict with Step names and Step instances
        Private vars:
            _order -- a list of categories order in config.xml
            _loaded_cats -- a sorted list of imported categories
        """
        self.category_dir = os.path.join('model', 'categories')
        self.found_cats = self._scan_model()
        _order = read_configs()
        self.cats_container = self._instantiate_cats(_order)

    def _scan_model(self):
        """
        Search for new files in model directory and return two lists of found
        category and algorithm files.
        Vars:
            found_cats -- a filtered list of category file names
            found_algs -- a filtered list of algorithm file names
            category_files -- a list of algorithm file names
            alg_files -- a list of algorithm file names
            ignored -- a regex object, used to filter unnecessary files
        Returns:
            a list of categories that were checked for interface compliance
            a list of algorithms that were checked for interface compliance
        """
        category_files = os.listdir(self.category_dir)
        ignored = re.compile(r'.*.pyc|__init__|_category.py|_alg.py')
        found_cats = filter(lambda x: not ignored.match(x), category_files)
        return found_cats

    def _instantiate_cats(self, ordering):
        """
        Instantiate imported categories and return a list of instantiated
        categories.
        Create a list with methods that represent a pipeline with selected
        algorithms and predefined settings.
        Sort the imported categories according to provided order list and
        return a list of imported category modules.
        <When the Step object is instantiated it automatically imports and
        creates a list of algorithms that belong to it>
        Params:
            ordering -- a list of categories order
        Vars:
            cats_inst -- a list of found and instantiated methods
            categories -- a dictionary of algs where {Algorithm: Step}
        Returns:
            categories -- a list with Method instances
        """
        cats_inst = []
        for category in self.found_cats:
            imported = __import__(category.split('.')[0],
                                  fromlist=['CatBody'])  # import a category
            inst = imported.CatBody()
            # create a dict of instantiated Step objects
            cats_inst.append(inst)
        # sort methods according to ordering
        cats_inst.sort(key=lambda x: ordering.index(x.get_name()))
        # create an ordered dict of {Step name: Step instance}
        cats = od()
        for category in cats_inst:
            cats[category.get_name()] = category
        return cats


if __name__ == '__main__':
    pass

