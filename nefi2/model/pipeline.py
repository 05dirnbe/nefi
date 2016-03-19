#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains Pipeline class that represents a central control
mechanism over a sequential image processing pipeline. It controls all the
available image processing categories, handles processing results and works
as an mediator between the algorithms and UI.
"""
import demjson
import networkx.readwrite as nx
import os
import re
import shutil
import sys
import copy
import zope.event.classhandler
import cv2

sys.path.insert(0, os.path.join(os.curdir, 'view'))
sys.path.insert(0, os.path.join(os.curdir, 'model'))
sys.path.insert(0, os.path.join(os.curdir, 'model', 'categories'))
sys.path.insert(0, os.path.join(os.curdir, 'model', 'algorithms'))

from categories._category import Category
from algorithms import _utility


__authors__ = {"Pavel Shkadzko": "p.shkadzko@gmail.com",
               "Dennis Groß": "gdennis91@googlemail.com",
               "Philipp Reichert": "prei@me.com"}


def filter_images(file_list):
    """
    Filter out all non-image files.
    <This function is used to protect the pipeline from attempting to process
    any non-image files existing in the input directory.>
    """
    valid_ext = ['.bmp', '.jpg', '.jpeg', '.png', '.tif', '.tiff', '.gif']
    return [f for f in file_list if os.path.splitext(f)[-1] in valid_ext]


def read_image_file(fpath, prev_cat, start_from):
    """
    Read and return an image file as a numpy ndarray.
    If the name of the previous Category is Segmentation, read grayscaled img.

    Args:
        | *fpath* (str): file path
        | *prev_cat* (str): name of the previous Category
        | *start_from* (int): starting Category position

    """
    try:
        if prev_cat == 'Segmentation' and start_from != 0:
            img = cv2.imread(fpath, cv2.IMREAD_GRAYSCALE)
        else:
            img = cv2.imread(fpath, cv2.IMREAD_COLOR)
    except (IOError, cv2.error) as ex:
        print(ex)
        print('ERROR in read_image_file() '+
              'Cannot read the image file, make sure it is readable')
        sys.exit(1)
    return img


class Pipeline:
    def __init__(self, categories):
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
        self.cache = []
        self.available_cats = categories
        self.executed_cats = []
        self.pipeline_path = os.path.join('assets', 'json')  # default dir
        self.out_dir = os.path.join(os.getcwd(), 'output')  # default out dir
        if not os.path.exists(self.out_dir):
            os.mkdir(self.out_dir)
        self.input_files = None
        self.original_img = None  # original image file as read first time
        # remember the results of each algorithm in the pipeline
        self.pipeline_memory = {}

    def subscribe_cache_event(self, function):
        """
        Subscribe to the cache event which tells the maincontroller about
        new images in the cache folder
        Args:
            function: the subscriber
        """
        self.cache_event.onChange += function

    def subscribe_progress_event(self, function):
        """
        Subscribe to the progress event which tells the maincontroller about
        the progress of the pipeline
        Args:
            function: the subscriber
        """
        self.progress_event.onChange += function

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
        # creating new blank Category
        if cat_name is None:
            blank_cat = Category("blank")
            blank_cat_copy = copy.deepcopy(blank_cat)
            self.executed_cats.insert(position, blank_cat_copy)
            return self.executed_cats[position]

        # inserting named Category
        for v in list(self.available_cats.values()):
            if v.name == cat_name:
                cat_copy = copy.deepcopy(v)
                self.executed_cats.insert(position, cat_copy)

        # setting active Algorithm
        for v in list(self.executed_cats[position].available_algs.values())[0]:
            if alg_name == v.name:
                v.set_modified()
                self.executed_cats[position].set_active_algorithm(alg_name)
                break

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

    def get_index(self, cat):
        """
        Gets the index of a given Category entry from the pipeline.

        Args:
            | *category* (cat): Category object

        Returns:
            | *index* (int): index of Category object in the pipeline

        """
        return self.executed_cats.index(cat)

    def process(self):
        """
        Process input image selected in UI, save intermediate results in
        _cache_ and enable pipeline recalculation from the category that was
        first changed.
        Keep all intermediate results.
        <This function will be obviously slower than the console variant due
        to IO operations on the _cache_ directory.>
        """
        # reset cache list
        self.cache = []

        # create and set output dir name
        img_fpath = self.input_files[0]
        orig_fname = os.path.splitext(os.path.basename(img_fpath))[0]
        pip_name = os.path.splitext(os.path.basename(self.pipeline_path))[0]
        out_path = os.path.join(self.out_dir,
                                '_'.join([pip_name, orig_fname]))

        # check if any algorithm has changed
        for idx, cat in enumerate(self.executed_cats):
            if cat.active_algorithm.modified:
                prev_cat_idx = 0 if idx - 1 < 0 else idx - 1
                if idx - 1 < 0:
                    start_idx = 0
                    prev_cat_name = self.executed_cats[0].name
                else:
                    start_idx = idx
                    prev_cat_name = self.executed_cats[prev_cat_idx].name
                break
            prev_cat_idx = 0
            start_idx = 0
            prev_cat_name = self.executed_cats[prev_cat_idx].name

        # decide which category to continue from if any, act accordingly
        if prev_cat_idx == 0 and start_idx == 0:
            # new pipeline, read original img
            orig_arr = read_image_file(img_fpath, '', start_idx)
            self.pipeline_memory[prev_cat_idx] = orig_arr
            data = [self.pipeline_memory[prev_cat_idx], None]
            self.original_img = data[0]
        else:
            # get the results of the previous (unmodified) algorithm
            data = self.pipeline_memory.get(prev_cat_idx)
            # remember the prev path
            prev_path = self.pipeline_memory[prev_cat_idx][0]
            # we need to read grayscale if previous category was Segmentation
            data[0] = read_image_file(prev_path, prev_cat_name, start_idx)

        # release memory
        if start_idx != 0:
            released = [prev_path, data[1] or None, prev_cat_name]
            self.pipeline_memory[prev_cat_idx] = released
        # main pipeline loop, execute the pipeline from the modified category
        for num, cat in enumerate(self.executed_cats[start_idx:], start_idx):
            progress = (num / len(self.executed_cats)) * 100
            report = cat.name + " - " + cat.active_algorithm.name
            zope.event.notify(ProgressEvent(progress, report))
            cat.process(data)
            # reassign results of the prev alg for the next one
            data = list(cat.active_algorithm.result.items())
            data.sort(key=lambda x: ['img', 'graph'].index(x[0]))
            data = [i[1] for i in data]
            # check if we have graph
            if data[1]:
                # draw the graph into the original image
                data[0] = _utility.draw_graph(self.original_img, data[1])
            # save the results
            save_fname = self.get_results_fname(img_fpath, cat)
            save_path = os.path.join(out_path, save_fname)
            self.save_results(save_path, save_fname, data)
            # update the cache
            self.update_cache(cat, save_path)
            cache_path = os.path.join(os.getcwd(), '_cache_', save_fname)
            self.pipeline_memory[num] = [cache_path, data[1], cat.name]
            # release memory
            cat.active_algorithm.result['img'] = ''

    def process_batch(self):
        """
        Process a given image or a directory of images using predefined
        pipeline.
        """
        for fpath in self.input_files:
            # create and set output dir name
            orig_fname = os.path.splitext(os.path.basename(fpath))[0]
            pip_name = os.path.splitext(os.path.basename(self.pipeline_path))[0]
            dir_name = os.path.join(self.out_dir, '_'.join([pip_name,
                                                            orig_fname]))
            data = [read_image_file(fpath, '', None), None]
            self.original_img = data[0]
            # process given image with the pipeline
            last_cat = None
            for cat in self.executed_cats:
                cat.process(data)
                # reassign results of the prev alg for the next one
                data = list(cat.active_algorithm.result.items())
                data.sort(key=lambda x: ['img', 'graph'].index(x[0]))
                data = [i[1] for i in data]
                last_cat = cat
            if data[1]:
                # draw the graph into the original image
                data[0] = _utility.draw_graph(self.original_img, data[1])
            # save the results and update the cache if store_image is True
            save_fname = self.get_results_fname(fpath, last_cat)
            save_path = os.path.join(dir_name, save_fname)
            self.save_results(save_path, save_fname, data)

    def save_results(self, save_path, image_name, results):
        """
        Create a directory of the following format: current pipeline + fname.
        Save and put the results of algorithm processing in the directory.

        Args:
            | *save_path* (str): image save path
            | *image_name* (str): image name
            | *results* (list): a list of arguments to save

        """
        # check if the save directory exists
        dir_to_save = os.path.dirname(save_path)
        if not os.path.exists(dir_to_save):
            os.mkdir(dir_to_save)
        # saving the processed image
        try:
            saved = cv2.imwrite(save_path, results[0])
            if not saved:
                print('ERROR in save_results(), ' +
                      'cv2.imwrite could not save the results!')
                sys.exit(1)
        except (IOError, cv2.error) as ex:
            print(ex)
            print('ERROR in save_results() ' +
                  'Cannot write an image file, make sure there is ' +
                  'enough free space on disk')
            sys.exit(1)
        # exporting graph object
        if results[1]:
            image_name = os.path.splitext(image_name)[0] + '.txt'
            nx.write_multiline_adjlist(results[1], os.path.join(dir_to_save,
                                                                image_name),
                                       delimiter='|')
            print('Success!', image_name, 'saved in', dir_to_save)

    def sanity_check(self):
        """
        The order of the categories is important in the pipeline.
        You can not execute graph filtering before graph detection or
        segmentation after graph filtering (graph filtering requires
        graph object which only graph detection produces).
        Therefor we check if the pipeline is in an illegal state before we
        execute it.

        Returns:
            ("", -1) if the pipeline is NOT in an illegae state,
            (*message*, i) an error message with the position in pipeline otherwise.
        """
        if len(self.executed_cats) == 0:
            return ("Nothing to do."), 0
        pipeline_cats = self.executed_cats
        is_graph = False
        is_segmented = False
        for i in range(0, len(pipeline_cats)):
            cat = pipeline_cats[i].get_name()
            if (cat == "Segmentation" or cat == "Preprocessing") and is_graph:
                return (("You cannot process '{0}' after 'Graph Detection'.".format(cat)), pipeline_cats[i])
            if (cat == "Graph Detection") and is_graph:
                return (("You cannot process '{0}' more than once.".format(cat)), pipeline_cats[i])
            if (cat == "Graph Filtering") and not is_graph:
                return (("You need to process 'Graph Detection' before '{0}'.".format(cat)), pipeline_cats[i])
            if (cat == "Graph Detection") and not is_segmented:
                return (("You need to process 'Segmentation' before '{0}'.".format(cat)), pipeline_cats[i])
            if cat == "blank":
                return (("Specify step {0} in the pipeline first.".format(i)), pipeline_cats[i])
            if cat == "Graph Detection":
                is_graph = True
            if cat == "Segmentation":
                is_segmented = True
        return "", None

    def report_available_cats(self, selected_cat=None):
        """
        The order of the categories is important in the pipeline.
        You can not execute graph filtering before graph detection or
        segmentation after graph filtering (graph filtering requires
        graph object which only graph detection produces).
        When a user selects a category from a drop-down menu we provide only
        currently allowed categories.

        Args:
            *selected_cat* (str): Category selected by the user

        Returns:
            a list of currently allowed category names

        <Deprecated function>
        """
        available_cats = [cat.name for cat in self.get_available_cats()]
        if selected_cat is None:
            return available_cats
        elif selected_cat not in available_cats:
            return available_cats
        elif selected_cat == 'Graph Detection':
            return available_cats[available_cats.index(selected_cat) + 1:]
        else:
            return available_cats[available_cats.index(selected_cat):]

    def allow_cat_swap(self, pos1, pos2):
        """
        Check the order after potential category swapping and return a bool if
        it should be allowed or not.

        Args:
            |*pos1* (int): position to be swapped
            |*pos2* (int): position to be swapped

        Returns:
            True if allowed and False otherwise
        """
        current_list = self.get_available_cat_names()
        return current_list[pos1] == current_list[pos2]

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
                self.executed_cats[position] = copy.deepcopy(v)

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

    def get_category(self, key):
        """
        Keys are the names of the categories.

        Returns:
            *category*: Category

        """
        return self.available_cats.get(key)

    def get_available_cat_names(self):
        """
        Create and return a list of currently loaded categories as strings.
        Names are used as keys in ``executed_cats`` list.

        Returns:
            a list of current Category names in the pipeline

        """
        return [cat.get_name() for cat in self.executed_cats]

    def get_available_cats(self):
        """
        Create and return a list of currently available categories as list of
        categorie objects.

        *<Get your cat for free ^-_-^>*

        Returns:
            *available_cats*: list of Category classes

        """
        available_cats = list(self.available_cats.values())
        return available_cats

    def get_algorithm_list(self, position):
        """
        Get names of all available algorithms for the category in position
        available in the pipeline.
        Sort the list and return.

        Args:
            *position* (int): Category index number

        Returns:
            *alg_names* (list): a sorted list of algorithm names

        """
        alg_names = self.executed_cats[position].alg_names
        alg_names.sort()
        return alg_names

    def get_all_algorithm_list(self, category):
        """
        Get names of all available algorithms for a given category.
        Sort the list and return.

        Args:
            *category*: Category

        Returns:
            *alg_names* (list): a sorted list of algorithm names

        """
        alg_names = category.alg_names
        alg_names.sort()
        return alg_names

    def get_results_fname(self, img_fpath, cat):
        """
        Create a file name for algorithm results.

        Args:
            | *img_fpath* (str): img file path
            | *cat* (Category): category instance

        Returns:
            *img_name* (str): image file name to save

        """
        alg_name = re.sub(' ', '_', cat.active_algorithm.name.lower())
        basename = os.path.basename(img_fpath)
        img_name = '_'.join([cat.get_name(), alg_name,
                             basename])
        return img_name

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
        if not os.path.exists('_cache_'):
            self.set_cache()
        zope.event.notify(CacheInputEvent(os.path.basename(input_source), input_source))
        shutil.copy(self.input_files[0], '_cache_')

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
        for position, alg in enumerate(json):
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
        self.pipeline_path = url
        # reset current cache
        self.set_cache()

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

        with open(url + ".json", "wb+") as outfile:
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
                print('ERROR in set_cache() ' +
                      'Cannot remove _cache_ directory, make sure it ' +
                      'is not open or locked by some other process.')
                sys.exit(1)
        os.mkdir('_cache_')
        self.cache = []

    def update_cache(self, cat, img_path):
        """
        Copy an img to cache dir and update the cache list.

        Args:
            | *category*: Category
            | *img_path* (str): image path

        """
        try:
            shutil.copy(img_path, '_cache_')
        except (IOError, OSError) as ex:
            print(ex)
            print('ERROR in update_cache() ' +
                  'Cannot copy to _cache_ directory, make sure there ' +
                  'is enough space on disk')
            sys.exit(1)

        cache_img_path = os.path.join(os.getcwd(), '_cache_',
                                      os.path.basename(img_path))

        zope.event.notify(CacheAddEvent(cat, cache_img_path))
        self.cache.append((cat, cache_img_path))


class ProgressEvent(object):
    """
    This event is used to report the progress back to the maincontroller
    """

    def __init__(self, value, report):
        self.value = value
        self.report = report


class CacheAddEvent(object):
    """
    This event is used to report the maincontroller the new cached image
    """

    def __init__(self, cat, path):
        self.cat = cat
        self.path = path


class CacheRemoveEvent(object):
    """
    This event is used to report the maincontroller the new cached image
    """

    def __init__(self, cat, path):
        self.cat = cat
        self.path = path


class CacheInputEvent(object):
    """
    This event is used to report the maincontroller the new cached image
    """

    def __init__(self, image_name, path):
        self.image_name = image_name
        self.path = path


if __name__ == '__main__':
    pass
