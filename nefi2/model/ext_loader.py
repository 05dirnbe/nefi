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
            | *_order*: a list of available categories taken from config

        Returns:
            instance of the ExtensionLoader object

        """
        for path in sys.path:
            if path.endswith('categories'):
                _category_dir = path
            elif path.endswith('model'):
                _config_path = os.path.join(path, 'config.xml')
        _found_cats = self._scan_model(_category_dir)
        _order = self._read_configs(_config_path)
        self.cats_container = self._instantiate_cats(_order, _found_cats)

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
            | *found_cats* (list): a list of categories that were found

        """
        category_files = os.listdir(cat_dir)
        ign = re.compile(r'.*.pyc|__init__|_category.py|_alg.py|_utility.py')
        found_cats = list(filter(lambda x: not ign.match(x), category_files))
        if not found_cats:
            raise FileNotFoundError("No image processing categories "
                                    "found in ./model/categories")
            sys.exit(1)
        return found_cats

    @staticmethod
    def _read_configs(config_path):
        """
        Read configuration file which contains category order.

        Args:
            | *config_path*: a path to config.xml

        Returns:
            | *order*: a list of categories order

        """
        tree = et.parse(config_path)  # categories order
        root = tree.getroot()
        # create categories order list
        order = [e.text for elem in root for e in elem.iter('category')]
        return order

    @staticmethod
    def _instantiate_cats(ordering, found_cats):
        """
        Instantiate imported categories and return a list of instantiated
        categories.
        Create a list with methods that represent a pipeline with selected
        algorithms and predefined settings.
        Sort the imported categories according to provided order list and
        return a list of imported category modules.
        <When the Category object is instantiated it automatically imports and
        creates a list of algorithms that belong to it>

        Args:
            | *ordering*: a list of categories order
            | *found_cats*:a list of found category file names

        Vars:
            | *cats_inst*: a list of found and instantiated methods
            | *categories*: a dictionary of algs where {Algorithm: Category}

        Returns:
            | *categories*: a list with Method instances

        """
        cats_inst = []
        for category in found_cats:
            imported = __import__(category.split('.')[0],
                                  fromlist=['CatBody'])  # import a category
            inst = imported.CatBody()
            # create a dict of instantiated Category objects
            cats_inst.append(inst)
        # sort methods according to ordering
        cats_inst.sort(key=lambda x: ordering.index(x.get_name()))
        # create an ordered dict of {Category name: Category instance}
        cats = od()
        for category in cats_inst:
            cats[category.get_name()] = category
        return cats


if __name__ == '__main__':
    pass
