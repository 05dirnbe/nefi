<<<<<<< HEAD
__author__ = 'martino'
import unittest
import sys
import os
from model.pipeline import Pipeline
from model.ext_loader import ExtensionLoader

sys.path.insert(0, os.path.join(os.curdir,'nefi2'))
sys.path.insert(0, os.path.join(os.curdir,'nefi2', 'model'))
sys.path.insert(0, os.path.join(os.curdir,'nefi2', 'model', 'categories'))
sys.path.insert(0, os.path.join(os.curdir,'nefi2', 'model', 'algorithms'))

class Test_Pipeline(unittest.TestCase):

    def test_new_Category(self):
        """
        Method new_Category will return True after the creation of the instance of Category's object at position x
        """
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)
        self.assertTrue(Pipeline.new_category(1))

    def test_move_category(self):
        """
        Method move_Category will return True after the moving of Category's objects from position x to position y
        """
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)
        self.assertTrue(pipeline.move_category(1,1))

    def test_delete_category(self):
        """
        Method delete_Category will return True after the deleting of Category's object at position x
        """
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)
        self.assertTrue(pipeline.delete_category(0))

    def test_change_algorithm(self):
        """
        Method change_algorithm will return True for changing the modified attribute of the algorithm at the Step x
        """
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)
        self.assertTrue(pipeline.change_algorithm(1,'Blur'))

    def test_get_executed_cats(self):
        """
        Method get_executed_cats will return the list of executed categories and the test will compare it with a set of standard ones
        """
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)
        standard = 'Preprocessing' #check which executed cats
        self.assertEqual(pipeline.get_executed_cats(),standard)

    def test_get_algorithm_list(self):
        """
        Method get_algorithm_list will return the list of available algorithms the test will compare it wiht the algorithms available for the Preprocessing categories
        """
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)
        standard = ['Blur','Bilateral','Color enhancement','Fast nl Means Denoising','Fast nl Means Denoising Colored','Gaussian Blur','Invert Color','Median Blur']
        self.assertEqual(pipeline.get_algorithm_list(1),standard)

    def test_read_pipeline_xml(self):
        ""
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)

if __name__ == '__main':
=======
#!/usr/bin/env python3


__authors__ = {"Martino Bruni": "bruni.martino92@gmail.com"}

import unittest
import sys
import os
from nefi2.model.pipeline import Pipeline
from nefi2.model.ext_loader import ExtensionLoader
from nefi2.model.categories._category import Category


sys.path.insert(0, os.path.join(os.curdir,'nefi2'))
sys.path.insert(0, os.path.join(os.curdir,'nefi2', 'model'))
sys.path.insert(0, os.path.join(os.curdir,'nefi2', 'model', 'categories'))
sys.path.insert(0, os.path.join(os.curdir,'nefi2', 'model', 'algorithms'))

class Test_Pipeline(unittest.TestCase):

    def test_new_Category(self):
        """
        Testing if the new_category(position) method insert in the executed_cats list at that position a new Category object
        """
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)
        pipeline.new_category(1)
        standard = Category()
        self.assertEqual(pipeline.executed_cats[1],standard)

    def test_move_category(self):
        """
        Testing if after creating 2 categories in the pipeline and moving one in another position the executed_cats list is modified
        """
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)
        pipeline.new_category(1)
        pipeline.new_category(2)
        cat1 = pipeline.executed_cats[1]
        cat2 = pipeline.executed_cats[2]
        pipeline.move_category(1,2)
        self.assertNotEqual(pipeline.executed_cats[1],cat1)
        self.assertEqual(pipeline.executed_cats[2],cat1)
        self.assertEqual(pipeline.executed_cats[3],cat2)

    def test_delete_category(self):
        """
        Testing if after deleting an object from the pipeline that object is not in the executed_cats list
        """
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)
        pipeline.new_category(1)
        cat=pipeline.executed_cats[1]
        pipeline.delete_category(1)
        self.assertNotIn(cat,pipeline.executed_cats)

    def test_change_algorithm(self):
        """
        Method change_algorithm will return True for changing the modified attribute of the algorithm at the Step x
        """
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)
        self.assertTrue(pipeline.change_algorithm(1,'Blur'))

    def test_get_executed_cats(self):
        """
        Method get_executed_cats will return the list of executed categories and the test will compare it with a set of standard ones
        """
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)
        standard = 'Preprocessing' #check which executed cats
        self.assertEqual(pipeline.get_executed_cats(),standard)

    def test_get_algorithm_list(self):
        """
        Method get_algorithm_list will return the list of available algorithms the test will compare it wiht the algorithms available for the Preprocessing categories
        """
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)
        standard = ['Blur','Bilateral','Color enhancement','Fast nl Means Denoising','Fast nl Means Denoising Colored','Gaussian Blur','Invert Color','Median Blur']
        self.assertEqual(pipeline.get_algorithm_list(1),standard)


if __name__ == '__main':
>>>>>>> aa8258dcb37ef294604cb514e42bc747555a26f0
    unittest.main()