#!/usr/bin/env python3

__authors__ = {"Dennis Groß": "gdennis91@googlemail.com"}

import unittest
from ext_loader import ExtensionLoader
from pipeline import Pipeline


def setup():
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)
        return pipeline


class PipelineTest2(unittest.TestCase):

    def test_create_blank_cat(self):
        pipeline = setup()
        pipeline.new_category(0)

        self.assertEqual(pipeline.executed_cats[0].name, "blank")

    def test_create_cat_well(self):
        pipeline = setup()
        pipeline.new_category(0, "Preprocessing", "Bilateral Filter")

        self.assertEqual(pipeline.executed_cats[0].name, "Preprocessing")
        self.assertEqual(pipeline.executed_cats[0].active_algorithm.name, "Bilateral Filter")

    def test_cat_change(self):
        pipeline = setup()
        pipeline.new_category(0)
        pipeline.change_category("Preprocessing", 0)

        self.assertEqual(pipeline.executed_cats[0].name, "Preprocessing")

    def test_alg_change(self):
        pipeline = setup()
        pipeline.new_category(0)
        pipeline.change_category("Preprocessing", 0)
        pipeline.change_algorithm("Bilateral Filter", 0)

        self.assertEqual(pipeline.executed_cats[0].active_algorithm.name, "Bilateral Filter")

    def test_delete_category(self):
        pipeline = setup()
        pipeline.new_category(0)
        pipeline.delete_category(0)

        self.assertEqual(len(pipeline.executed_cats), 0)

    def test_delet_category_name(self):
        pipeline = setup()
        pipeline.new_category(0)
        pipeline.change_category("Segmentation", 0)
        pipeline.delete_category("Segmentation")

        self.assertEqual(len(pipeline.executed_cats), 0)

    def test_move_category(self):
        pipeline = setup()
        pipeline.new_category(0)
        pipeline.new_category(1)
        pipeline.new_category(2)
        pipeline.new_category(3)

        pipeline.change_category("Preprocessing", 0)
        pipeline.change_category("Segmentation", 3)

        pipeline.move_category(0, 3)

        self.assertEqual(pipeline.executed_cats[0].name, "Segmentation")
        self.assertEqual(pipeline.executed_cats[3].name, "Preprocessing")