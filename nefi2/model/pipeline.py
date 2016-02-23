#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains the class Pipeline that represents a central control
mechanism over a sequential image processing pipeline. It controls all the
available image processing categories, handles processing results and works
as an mediator between the algorithms and UI.
"""
import cv2
import demjson
import networkx as nx
import os
import re
import shutil
import sys
import copy


sys.path.insert(0, os.path.join(os.curdir, 'view'))
sys.path.insert(0, os.path.join(os.curdir, 'model'))
sys.path.insert(0, os.path.join(os.curdir, 'model', 'categories'))
sys.path.insert(0, os.path.join(os.curdir, 'model', 'algorithms'))

from _category import Category
from algorithms import _utility


__authors__ = {"Pavel Shkadzko": "p.shkadzko@gmail.com",
               "Dennis Groß": "gdennis91@googlemail.com"}


def filter_images(file_list):
    """
    Filter out all non-image files.
    <This function is used to protect the pipeline from attempting to process
    any non-image files existing in the input directory.>
    """
    valid_ext = ['.bmp', '.jpg', '.jpeg', '.jp2', '.jpx', '.j2k', '.j2c',
                 '.png', '.tif', '.tiff', '.gif', ]
    return [f for f in file_list if os.path.splitext(f)[-1] in valid_ext]


class Pipeline:
    def __init__(self, categories, isui):
        """
        Args:
            | *categories* : OrderedDict of category names and their instances
            | *isui* (bool) : True if Pipeline is running in UI mode

        public Attributes:
            | *available_cats* (dict): dict of {Category name: Category}
            | *executed_cats* (list): a list of Categories in the pipeline
            | *pipeline_path* (str): a path to a saved pipelines
            | *out_dir* (str): a path where processing results are saved
            | *input_files* (list): a list of image files in the input dir
            | *cache* (list): a list of tuples where (Category name, img url)

        """
        self.isui = isui
        if self.isui:
            self.set_cache()
            self.cache = []
        self.available_cats = categories
        self.executed_cats = []
        self.pipeline_path = os.path.join('assets', 'json')  # default dir
        self.out_dir = os.path.join(os.getcwd(), 'output')  # default out dir
        self.input_files = None

    def new_category(self, position, cat_name=None, alg_name=None):
        """
        This method is used by the json parser to create a category.
        The parser knows already the cat type and alg type as well
        as the position. So it doesnt make sense to create a blank and
        change it.

        Args:
            | *cat_name* (str): name of the category also indicating its cat type
            | *alg_name* (str): name of the active algoirthm indicating its alg type
            | *position* (int): position in the executed_cats

        """
        if cat_name is None:
            self.executed_cats.insert(position, Category("blank"))
            return

        for v in list(self.available_cats.values()):
            if v.name == cat_name:
                self.executed_cats.insert(position, copy.copy(v))

        for v in list(self.executed_cats[position].available_algs.values())[0]:
            if alg_name == v.name:
                v.set_modified()
                self.executed_cats[position].set_active_algorithm(alg_name)

    def move_category(self, origin_pos, destination_pos):
        """
        Move Category instance within the pipeline using indices.

        Args:
            | *origin_pos* (int): Category index number
            | *destination_pos* (int): new position for Category

        """
        buf = self.executed_cats[origin_pos]
        self.executed_cats[origin_pos] = self.executed_cats[destination_pos]
        self.executed_cats[destination_pos] = buf

    def delete_category(self, category):
        """
        Remove Category from the pipeline.

        Args:
            *category* (int|str): Category position index or Category name

        """
        if type(category) == int:
            del self.executed_cats[category]
        elif type(category) == str:
            for i, cat in enumerate(self.executed_cats):
                if category == cat.name:
                    del self.executed_cats[i]

    def process(self):
        """
        Execute current pipeline starting from the first modified image
        processing category.

        Returns:
            *image* (ndarray): processed image

        """
        # find the first category which contains the modified algorithm
        for idx, cat in enumerate(self.executed_cats):
            if cat.active_algorithm.modified:
                start_from = idx, cat.name
                break
        # process all images in the input
        for image_name in self.input_files:
            self.process_image(image_name, start_from)

    def process_image(self, orig_fpath, start_from):
        def get_fname():
            # creating a file name
            alg_name = re.sub(' ', '_', cat.active_algorithm.name.lower())
            basename = os.path.basename(orig_fpath)
            img_name = '_'.join([cat.name.lower(), alg_name, basename])
            return img_name

        # create output dir name
        orig_fname = os.path.splitext(os.path.basename(orig_fpath))[0]
        pip_name = os.path.splitext(os.path.basename(self.pipeline_path))[0]
        default_out = os.path.join(os.getcwd(), 'output')
        dir_name = os.path.join(default_out, '_'.join([pip_name, orig_fname]))
        self.set_output_dir(dir_name)
        # read in the input image file
        try:
            img_origin = cv2.imread(orig_fpath, cv2.IMREAD_COLOR)
        except (IOError, cv2.error):
            print('ERROR! Cannot read the image file, make sure it is readable')
            sys.exit(1)
        img_arr = img_origin
        # execute the pipeline from the category with the modified alg
        for _, cat in enumerate(self.executed_cats[start_from[0]:]):
            if cat.name == "Graph detection":
                # get results of graph detection
                cat.process(img_arr)
                graph = cat.active_algorithm.result['graph']
                # draw the graph into the original image
                img_arr = _utility.draw_graph(img_origin, graph)
                if cat.active_algorithm.store_image:
                    self.save_results(get_fname(), img_arr, graph)
                if self.isui:
                    self.save_results(get_fname(), img_arr, None)
                    self.update_cache('Graph detection',
                                      os.path.join(self.out_dir, get_fname()))
            elif cat.name == "Graph filtering":
                cat.process(img_arr, graph)  # image array always first!
                # now get the results of graph filtering
                graph = cat.active_algorithm.result['graph']
                # draw the graph into the original image
                img_arr = _utility.draw_graph(img_origin, graph)
                if cat.active_algorithm.store_image:
                    self.save_results(get_fname(), img_arr, graph)
                if self.isui:
                    self.save_results(get_fname(), img_arr, None)
                    self.update_cache('Graph filtering',
                                      os.path.join(self.out_dir, get_fname()))
            else:
                cat.process(img_arr)
                img_arr = cat.active_algorithm.result['img']
                graph = None
                # saving current algorithm results
                if cat.active_algorithm.store_image:
                    self.save_results(get_fname(), img_arr, graph)
                if self.isui:
                    self.save_results(get_fname(), img_arr, None)
                    self.update_cache(cat.get_name(),
                                      os.path.join(self.out_dir, get_fname()))

    def save_results(self, image_name, *results):
        """
        Create a directory of the following format: current pipeline + fname.
        Save and put the results of algorithm processing in the directory.

        Args:
            | *image_name* (str): image name
            | *results* (list): a list of arguments to save

        """
        # saving the processed image
        try:
            cv2.imwrite(os.path.join(self.out_dir, image_name), results[0])
        except (IOError, cv2.error):
            print('ERROR! Could not write an image file, make sure there is ' +
                  'enough free space on disk')
            sys.exit(1)
        if not self.isui:
            print('Success!', image_name, 'saved in', self.out_dir)
        # exporting graph object
        if results[1]:
            image_name = os.path.splitext(image_name)[0] + '.txt'
            nx.write_multiline_adjlist(results[1], os.path.join(self.out_dir,
                                                                image_name),
                                       delimiter='|')
            print('Success!', image_name, 'saved in', self.out_dir)

    def report_available_cats(self, selected_cat):
        """
        The order of the categories is important in the pipeline.
        You can not execute graph filtering before graph detection or
        segmentation after graph filtering.
        When a user selects a category from a drop-down menu we provide only
        currently allowed categories.

        Args:
            *selected_cat* (str): Category selected by the user

        Returns:
            a list of currently allowed cats

        """
        current_cats = self.get_executed_cats()
        if not selected_cat or selected_cat not in current_cats:
            return current_cats
        elif selected_cat == 'Graph detection':
            return current_cats[current_cats.index(selected_cat) + 1:]
        else:
            return current_cats[current_cats.index(selected_cat):]

    def change_category(self, cat_name, position):
        """
        Change the type of the category at position in the executed_cats.
        This is needed for the ui since the categorys in the executed_cats
        need to be changed because of the dropdown menus.

        Args:
            | *cat_name*: the name of the category as it should be
            | *position*: the position in the executed_cats

        """
        for v in list(self.available_cats.values()):
            if v.name == cat_name:
                self.executed_cats[position] = copy.copy(v)

    def change_algorithm(self, alg_name, position):
        """
        Set the algorithm of the category in position to modified = *True*.
        Also change the selected algorithm of the category in position.

        Args:
            | *position*: list index of the category in the pipeline
            | *alg_name*: algorithm name

        """
        for v in list(self.executed_cats[position].available_algs.values())[0]:
            if alg_name == v.name:
                v.set_modified()
                self.executed_cats[position].set_active_algorithm(alg_name)

    def get_executed_cats(self):
        """
        Create and return a list of currently executed categories.

        *No cats are actually harmed during execution of this method >_<*

        Returns:
            *executed_cat_names*: list of Category names

        """
        executed_cat_names = [cat.get_name() for cat in self.executed_cats]
        return executed_cat_names

    def get_algorithm_list(self, position):
        """
        Get names of all available algorithms for the category in position.
        Sort the list and return.

        Args:
            *position* (int): Category index number

        Returns:
            *alg_names* (list): a sorted list of algorithm names

        """
        alg_names = self.executed_cats[position].alg_names
        alg_names.sort()
        return alg_names

    def set_input(self, input_source):
        """
        Set the directory where original images are located or set a file path.

        Args:
            *input_source* (str): directory path with original images or a
            single file path

        """
        if os.path.isdir(input_source):
            files = filter_images(os.listdir(input_source))
            self.input_files = [os.path.join(input_source, f) for f in files]
        elif os.path.isfile(input_source):
            self.input_files = [input_source]
        # if UI mode create cache dir, copy input file and update cache list
        if self.isui:
            if not os.path.exists('_cache_'):
                self.set_cache()
            shutil.copy(self.input_files[0], '_cache_')
            # self.update_cache('INPUT', self.input_files[0])

    def set_output_dir(self, dir_path):
        """
        Create and set the directory where to save the results of processing.
        <Used in console mode>.

        Args:
            *dir_path* (str): directory path for processing results

        """
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        self.out_dir = dir_path

    def load_pipeline_json(self, url):
        """
        Loads the Pipeline from the url location and parses all data to
        create the corresponding executed_cats

        Args:
            | *url*: location identifier for the pipeline.json

        """
        try:
            json = demjson.decode_file(url, "UTF-8")
        except demjson.JSONDecodeError as e:
            e = sys.exc_info()[0]
            print("Unable to parse " + url + " trace: " + e)
        position = 0
        for alg in json:
            alg_name = alg[0]
            alg_attributes = alg[1]

            cat_name = alg_attributes["type"]
            self.new_category(position, cat_name, alg_name)

            active_alg = self.executed_cats[position].active_algorithm
            active_alg.store_image = alg_attributes["store_image"]

            for name in alg_attributes.keys():
                if name == "type" or name == "store_image":
                    continue
                value = alg_attributes[name]
                active_alg.find_ui_element(name).set_value(value)
            position += 1
        self.pipeline_path = url

    def save_pipeline_json(self, name, url):
        """
        Goes trough the list of executed_cats and calls for every
        selected_algorithm its report_pip method. With the returned
        dictionary's, it builds the pipeline.json file and stores it
        at the given url location on the file system.

        Args:
            | *url*: location identifier for the pipeline.json

        """
        alg_reports = []
        for cat in self.executed_cats:
            alg = cat.get_active_algorithm()
            cat_name, alg_dic = alg.report_pip()
            alg_reports.append([cat_name, alg_dic])

        with open(os.path.join(url, name + ".json"), "wb+") as outfile:
            # ord_alg_reps = OrderedDict(alg_reports)
            outfile.write(bytes(demjson.encode(alg_reports), "UTF-8"))

    def set_cache(self):
        """
        Create cache dir in order to save in it the intermediate results of
        processing and an original image.
        Recreate dir if exists or before running image processing.
        <This is done to make thumbnails in the left pane available in UI.>
        """
        if os.path.exists('_cache_'):
            try:
                shutil.rmtree('_cache_')
            except (IOError, OSError):
                print('ERROR! Cannot remove _cache_ directory, make sure it ' +
                      'is not open or locked by some other process.')
                sys.exit(1)
        os.mkdir('_cache_')
        self.cache = []

    def update_cache(self, category, img_path):
        """
        Copy an img to cache dir and update the cache list.

        Args:
            | *category* (str): Category name
            | *img_path* (str): image path

        """
        try:
            shutil.copy(img_path, '_cache_')
        except (IOError, OSError):
            print('ERROR! Cannot copy to _cache_ directory, make sure there ' +
                  'is enough space on disk')
            sys.exit(1)
        cache_img_path = os.path.join(os.getcwd(), '_cache_',
                                      os.path.basename(img_path))
        self.cache.append((category, cache_img_path))


if __name__ == '__main__':
    pass
