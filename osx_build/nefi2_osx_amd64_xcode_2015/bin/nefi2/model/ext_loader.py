# -*- coding: utf-8 -*-
"""
This module contains ExtensionLoader class that works with "model"
folder and is used to initialize the pipeline with all available image
processing categories and their respective algorithms. It uses config.json
settings to initialize image processing categories accordingly.
ExtensionLoader creates a collection of categories and algorithms ready to
be loaded into the pipeline object.
"""
import re
import os
import xml.etree.ElementTree as et
import sys
from collections import OrderedDict as od
from importlib.machinery import SourceFileLoader


__authors__ = {"Pavel Shkadzko": "p.shkadzko@gmail.com"}


class ExtensionLoader:

    def __init__(self):
        """
        public Attributes:
            | *cats_container*: a dict with Category names and instances

        private Attributes:
            | *_category_dir*: a directory path for categories
            | *_config_path*: a path to config.xml
            | *_found_cats*: a list of category paths

        Returns:
            instance of the ExtensionLoader object

        """
        _category_dir = os.path.join(os.path.dirname(__file__), 'categories')
        _found_cats = self._scan_model(_category_dir)
        self.cats_container = self._instantiate_cats(_found_cats)

    @staticmethod
    def _scan_model(cat_dir):
        """
        Check for any available category files in cat_dir.
        Return found file names.
        Raise an error if no file was found.

        Args:
            | *cat_dir* (str): category dir provided by the ext_loader

        Vars:
            | *found_cats* (list): a filtered list of category file names
            | *category_files* (list): a list of algorithm file names
            | *ignored*: a regex object, used to filter unnecessary files

        Returns:
            | *found_cats_paths* (list): a list of found category paths

        """
        category_files = os.listdir(cat_dir)
        ign = re.compile(r'.*.pyc|__init__|_category.py|_alg.py|_utility.py')
        found_cats = list(filter(lambda x: not ign.match(x), category_files))
        if not found_cats:
            raise FileNotFoundError("No image processing categories "
                                    "found in ./model/categories")
        # add abs paths
        found_cats_paths = [os.path.join(os.path.dirname(__file__), 'categories', cat)
                            for cat in found_cats]
        return found_cats_paths

    @staticmethod
    def _instantiate_cats(found_cats):
        """
        Instantiate imported categories and return a list of instantiated
        categories.
        Create a list with methods that represent a pipeline with selected
        algorithms and predefined settings.
        <When the Category object is instantiated it automatically imports and
        creates a list of algorithms that belong to it>

        Args:
            | *found_cats*: a list of found category file names

        Vars:
            | *cats_inst*: a list of found and instantiated methods
            | *categories*: a dictionary of algs where {Algorithm: Category}

        Returns:
            | *categories*: a list with Method instances

        """
        cats_inst = []
        for cat_path in found_cats:
            cat_name = os.path.basename(cat_path).split('.')[0]
            cat = SourceFileLoader(cat_name, cat_path).load_module()
            inst = cat.CatBody()
            cats_inst.append(inst)
        # sort the cats
        order = ['Preprocessing', 'Segmentation', 'Graph Detection',
                 'Graph Filtering']
        # in case we have custom cats, add them
        for cat in cats_inst:
            if cat.name not in order:
                order.append(cat.name)

        cats_inst.sort(key=lambda x: order.index(x.name))
        # create a dict of {Category name: Category instance}
        cats = od()
        for category in cats_inst:
            cats[category.name] = category
        return cats


if __name__ == '__main__':
    pass
