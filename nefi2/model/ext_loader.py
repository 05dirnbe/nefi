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
import xml.etree.ElementTree as et
from collections import OrderedDict as od
import sys

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
            self.cats_container -- a dict with Step names and Step instances
        Private vars:
            _category_dir -- a directory path for categories
            _config_path -- a path to config.xml
            _found_cats -- a list of category paths
            _order -- a list of available categories taken from config
        """
        for path in sys.path:
            if path.endswith('categories'):
                _category_dir = path
            elif path.endswith('model'):
                _config_path = os.path.join(path, 'config.xml')
        _found_cats = self._scan_model(_category_dir)
        _order = self._read_configs(_config_path)
        self.cats_container = self._instantiate_cats(_order, _found_cats)

    def _scan_model(self, cat_dir):
        """
        Search for new files in model directory and return two lists of found
        category and algorithm files.
        Vars:
            found_cats -- a filtered list of category file names
            category_files -- a list of algorithm file names
            ignored -- a regex object, used to filter unnecessary files
        Returns:
            a list of categories that were found
        """
        category_files = os.listdir(cat_dir)
        ignored = re.compile(r'.*.pyc|__init__|_category.py|_alg.py')
        found_cats = filter(lambda x: not ignored.match(x), category_files)
        return found_cats

    def _read_configs(self, config_path):
        """
        Parse config.xml, extract categories order.
        Params:
            config_path -- a path to config.xml
        Returns:
            order -- a list of categories order
        """
        tree = et.parse(config_path)  # categories order
        root = tree.getroot()
        # create categories order list
        order = [e.text for elem in root for e in elem.iter('category')]
        return order

    def _instantiate_cats(self, ordering, found_cats):
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
            found_cats -- a list of found category file names
        Vars:
            cats_inst -- a list of found and instantiated methods
            categories -- a dictionary of algs where {Algorithm: Step}
        Returns:
            categories -- a list with Method instances
        """
        cats_inst = []
        for category in found_cats:
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

