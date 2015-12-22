__author__ = 'martino'

import unittest
import sys
import os
from model.categories import preprocessing
from model.categories import segmentation
from model.categories import gdetection
from model.categories import gfiltering
from collections import OrderedDict as od


from model.ext_loader import ExtensionLoader
from collections import OrderedDict as od, OrderedDict

sys.path.insert(0, os.path.join(os.curdir,'nefi2'))
sys.path.insert(0, os.path.join(os.curdir,'nefi2', 'model'))
sys.path.insert(0, os.path.join(os.curdir,'nefi2', 'model', 'categories'))
sys.path.insert(0, os.path.join(os.curdir,'nefi2', 'model', 'algorithms'))

class Test_Extension_Loader(unittest.TestCase):



    def test_scand_model(self):
        """
        The List standard will be the result of the method _scan_model(cat_dir) if the cat_dir is './model/categories'
        """
        ext_Loader = ExtensionLoader()
        standard = ['preprocessing.py', 'segmentation.py', 'gdetection.py', 'gfiltering.py']
        cat_dir = os.path.join(os.curdir, 'model', 'categories')
        self.assertEqual(self.ext_Loader._scan_model(cat_dir),standard)

    def test_read_config(self):

        ext_Loader = ExtensionLoader()
        standard = ['Preprocessing', 'Segmentation','Graph Detection', 'Graph Filtering']
        self.assertEqual(self.ext_Loader._read_configs(),standard)
        self.ext_Loader._instantiate_cats()


"""
    def test_instantiate_cats(self):
        ordering = ['Preprocessing', 'Segmentation', 'Graph detection', 'Graph filtering']
        found_cats = ['preprocessing.py', 'segmentation.py', 'gdetection.py', 'gfiltering.py']
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
        standard = OrderedDict([('Preprocessing', <preprocessing.CatBody instance at 0x7fe82e967cb0>), ('Segmentation', <segmentation.CatBody instance at 0x7fe82e967b90>), ('Graph detection', <gdetection.CatBody instance at 0x7fe8306b7cb0>), ('Graph filtering', <gfiltering.CatBody instance at 0x7fe8306388c0>)])
"""



if __name__ == '__main__':
    unittest.main()