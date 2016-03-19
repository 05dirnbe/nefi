#!/usr/bin/env python3

import unittest
import os
import preprocessing
import segmentation
import gdetection
import gfiltering
from nefi2.model.ext_loader import ExtensionLoader

__authors__ = {"Martino Bruni": "bruni.martino92@gmail.com"}



class Test_Extension_Loader(unittest.TestCase):

    def test_scand_model(self):
        """
        The List standard should be the result of the method _scan_model(cat_dir) if the cat_dir is '../../model/categories'
        """
        ext_Loader = ExtensionLoader()
        standard = ['preprocessing.py', 'segmentation.py', 'gdetection.py', 'gfiltering.py']
        cat_dir = os.path.join(os.pardir,os.pardir, 'model', 'categories')
        self.assertEqual(ext_Loader._scan_model(cat_dir),standard)

    def test_read_config(self):
        """
        The List standard should be the result of the method read_config(config_path) if the config_path is the path of the file config.xml
        """
        ext_Loader = ExtensionLoader()
        standard = ['Preprocessing', 'Segmentation','Graph detection', 'Graph filtering']
        config_dir = os.path.join(os.pardir,os.pardir,'model','config.xml')
        self.assertEqual(ext_Loader._read_configs(config_dir),standard)

    def test_instantiate_cats(self):
        ext_loader = ExtensionLoader()
        ordering = ['Preprocessing', 'Segmentation', 'Graph detection', 'Graph filtering']
        found_cats = ['preprocessing.py', 'segmentation.py', 'gdetection.py', 'gfiltering.py']
        cats_container_test = list(ext_loader._instantiate_cats(ordering,found_cats).items())
        self.assertIsInstance(cats_container_test[0][1],preprocessing.CatBody)
        self.assertIsInstance(cats_container_test[1][1],segmentation.CatBody)
        self.assertIsInstance(cats_container_test[2][1],gdetection.CatBody)
        self.assertIsInstance(cats_container_test[3][1],gfiltering.CatBody)

if __name__ == '__main__':
    Test_Extension_Loader.test_read_config()
