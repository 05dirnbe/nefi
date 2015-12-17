# -*- coding: utf-8 -*-
"""
This class represents a central control mechanism over a sequential
image processing pipeline. It controls all the available image processing
categories, handles processing results and works as an mediator between the
algorithms and UI.
"""
__authors__ = {"Pavel Shkadzko": "p.shkadzko@gmail.com"}


import os
import xml.etree.ElementTree as et
from .categories._category import Category
import sys


class Pipeline:
    def __init__(self, categories):
        """
        Pipeline constructor
        Params:
            categories -- OrderedDict of category names and their instances
        Instance vars:
            self.available_cats -- dict of {Category name: Category}
            self.executed_cats -- a list of Categories
            self.pipeline_path -- a path to a saved pipelines
            self.image_path -- a path to an image file
        """
        self.available_cats = categories
        self.executed_cats = [v for v in self.available_cats.values()]
        self.pipeline_path = 'saved_pipelines'  # default dir
        self.image_path = None
        print(self.available_cats)

    def new_category(self, position):
        """
        Create an instance of a new Category.
        Params:
            position -- a category index in self.executed_cats
        """
        self.executed_cats.insert(position, Category())
        return True

    def move_category(self, origin_pos, destination_pos):
        """
        Move Category instance within the pipeline using indices.
        Params:
            origin_pos (int) -- Category index number
            destination_pos (int) -- new position for Category
        """
        self.executed_cats.insert(destination_pos,
                                  self.executed_cats[origin_pos])
        del self.executed_cats[origin_pos]
        return True

    def delete_category(self, position):
        """
        Remove a Category from the pipeline.
        Params:
            position (int) -- Category index number
        """
        del self.executed_cats[position]
        return True

    def process(self):
        pass

    def change_algorithm(self, position, alg_name):
        """
        Set the algorithm of the category in position to modified = True
        Params:
            position -- list index of the category in the pipeline
            alg_name -- algorithm name
        """
        for v in self.executed_cats[position].available_algs.values()[0]:
            if alg_name == v.Body().get_name():
                v.Body().set_modified()
        return True

    def get_executed_cats(self):
        """
        Create and return a list of currently executed categories.
        Returns:
            executed_cat_names -- list of Category names
        No cats are actually harmed during execution of this method >_<
        """
        executed_cat_names = [cat.get_name() for cat in self.executed_cats]
        return executed_cat_names

    def get_algorithm_list(self, position):
        """
        Get names of all available algorithms for the category in position.
        Sort the list and return.
        Params:
            position (int) -- Category index number
        Returns:
            alg_names (list) -- a sorted list of algorithm names
        """
        alg_names = self.available_cats.values()[position].alg_names
        alg_names.sort()
        return alg_names

    def read_pipeline_xml(self, xml_file):
        """
        Parse the xml file of a saved pipeline.
        Create and return a dictionary representation of the xml file.
        Params:
            xml_file -- a path to an xml file of a saved pipeline
        Returns:
            settings dictionary {Category: {Algorithm: {Param: val}}}
        """
        tree = et.parse(xml_file)
        root = tree.getroot()
        for elem in root:
            if elem.tag == 'pipeline':
                # create settings dictionary
                settings = {}
                for category in elem.iter('category'):
                    category_name = category.attrib['name']
                    settings[category_name] = {}
                    for alg in category.iter('alg'):
                        alg_name = alg.attrib['name']
                        settings[category_name].update({alg_name: {}})
                        for param in alg.iter('param'):
                            params = {param.attrib['name']: param.text}
                            settings[category_name][alg_name].update(params)
        return settings

    def read_image(self, img_path):
        pass

    def save_pipeline_xml(self, save_path):
        pass


if __name__ == '__main__':
    pass
