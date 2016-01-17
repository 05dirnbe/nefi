#!/usr/bin/env python3

__authors__ = {"Martino Bruni": "bruni.martino92@gmail.com"}

import unittest
import sys
import os
from nefi2.model.pipeline import Pipeline
from nefi2.model.ext_loader import ExtensionLoader
from nefi2.model.categories._category import Category

sys.path.insert(0, os.path.join(os.pardir,os.pardir,'nefi2'))
sys.path.insert(0, os.path.join(os.pardir,os.pardir, 'model'))
sys.path.insert(0, os.path.join(os.pardir,os.pardir, 'model', 'categories'))
sys.path.insert(0, os.path.join(os.pardir,os.pardir, 'model', 'algorithms'))

sys.path.remove(os.path.join(os.curdir,'model'))
sys.path.remove(os.path.join(os.curdir,'model','categories'))
sys.path.remove(os.path.join(os.curdir,'model','algorithms'))



class Test_Pipeline(unittest.TestCase):

    def test_new_Category(self):
        """
        Testing if the new_category(position) method insert in the executed_cats list at that position a new Category object
        """
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)
        pipeline.new_category('Preprocessing' ,1)
        standard = Category('Preprocessing')
        self.assertEqual(pipeline.executed_cats[1].name,standard.name)

    def test_move_category(self):
        """
        Testing if after creating 2 categories in the pipeline and moving one in another position the executed_cats list is modified
        TEST FAIL REVIEW pipeline.move_category() methods

        """
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)
        cat1 = pipeline.executed_cats[1]
        cat2 = pipeline.executed_cats[2]
        pipeline.move_category(2,1)
        self.assertNotEqual(pipeline.executed_cats[1],cat1)
        self.assertEqual(pipeline.executed_cats[1],cat2)
        self.assertEqual(pipeline.executed_cats[2],cat1)
        cat2 = pipeline.executed_cats[2]
        pipeline.move_category(2,2)
        self.assertEqual(pipeline.executed_cats[2],cat2)
        cat1= pipeline.executed_cats[1]
        cat2 = pipeline.executed_cats[2]
        pipeline.move_category(1,2)
        self.assertNotEqual(pipeline.executed_cats[1],cat1)
        self.assertEqual(pipeline.executed_cats[2],cat1)
        self.assertEqual(pipeline.executed_cats[1],cat2)


    def test_delete_category(self):
        """
        Testing if after deleting an object from the pipeline that object is not in the executed_cats list
        """
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)
        pipeline.new_category('Segmentation', 1)
        cat=pipeline.executed_cats[1]
        pipeline.delete_category(1)
        self.assertNotIn(cat,pipeline.executed_cats)

    def test_change_algorithm(self):
        """
        Method change_algorithm will return True for changing the modified attribute of the algorithm at the Step x
        TEST FAIL
        """
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)
        pipeline.new_category('Preprocessing',1)
        self.assertTrue(pipeline.change_algorithm(1,'Blur'))

    def test_get_executed_cats(self):
        """
        Method get_executed_cats will return the list of executed categories and the test will compare it with a set of standard ones
        """
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)
        standard = ['Preprocessing', 'Segmentation','Graph detection', 'Graph filtering']
        self.assertEqual(pipeline.get_executed_cats(),standard)

    def test_get_algorithm_list(self):
        """
        Method get_algorithm_list will return the list of available algorithms the test will compare it wiht the algorithms available for the Preprocessing categories
        TEST FAIL
        """
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)
        standard = ['Blur','Bilateral','Color enhancement','Fast nl Means Denoising','Fast nl Means Denoising Colored','Gaussian Blur','Invert Color','Median Blur']
        self.assertEqual(pipeline.get_algorithm_list(1),standard)


if __name__ == '__main':
    unittest.main()