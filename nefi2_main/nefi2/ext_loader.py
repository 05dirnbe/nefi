# -*- coding: utf-8 -*-
"""
A class that works with "model" folder and is used to initialize the pipeline
with all available image processing steps and their respective algorithms.
It uses config.xml settings to initialize image processing steps accordingly.
ExtensionLoader creates a collection of steps and algorithms ready to be
loaded into the pipeline object.
"""

__author__ = "p.shkadzko@gmail.com"


import re
import os
import sys
sys.path.insert(0, os.path.join(os.curdir, 'model', 'steps'))
sys.path.insert(0, os.path.join(os.curdir, 'model', 'algorithms'))
import xml.etree.ElementTree as et
from collections import OrderedDict as od


def read_config(xml_path):
    """
    Parse config.xml, extract steps order and their default settings.
    Create a list with order of steps and a dictionary of default settings.
    Args:
        xml_path -- a path to config.xml
    Returns:
        order -- a list of steps order
        settings -- settings dictionary {Step: {Algorithm: {Param: val}}}
    """
    tree = et.parse(xml_path)
    root = tree.getroot()
    for elem in root:
        if elem.tag == 'order':
            # create steps order list
            order = [e.text for e in elem.iter('step')]
        elif elem.tag == 'pipeline':
            # create settings dictionary
            settings = {}
            for step in elem.iter('step'):
                step_name = step.attrib['name']
                settings[step_name] = {}
                for alg in step.iter('alg'):
                    alg_name = alg.attrib['name']
                    settings[step_name].update({alg_name: {}})
                    for param in alg.iter('param'):
                        params = {param.attrib['name']: param.text}
                        settings[step_name][alg_name].update(params)
    return order, settings


class ExtensionLoader:
    """
    A class that imports and initializes all available image processing steps
    and their algorithms.
    It scans for new files in /model/algorithms and /model/steps.
    It checks these files for compliance with the interface, analyses which
    algorithm belongs to which method and creates a corresponding mapping that
    is used by Step class upon instantiating.
    """
    def __init__(self):
        """
        Constructor
        Instance vars:
            self.step_dir -- a directory path for steps
            self.loaded_algs -- a list of algorithm paths
            self.loaded_steps -- a list of step paths
            self.steps_container -- a dict with Step names and Step instances
        Private vars:
            _order -- a list of steps order in config.xml
            _settings -- a dictionary of config.xml settings
            _loaded_steps -- a sorted list of imported steps
        """

        self.step_dir = os.path.join('model', 'steps')
        self.found_steps = self._scan_model()
        _order, _settings = read_config('config.xml')
        _loaded_steps = self._load_steps(_order)
        self.steps_container = self._instantiate_steps(_loaded_steps)

    def _scan_model(self):
        """
        Search for new files in model directory and return two lists of found
        step and algorithm files.
        Vars:
            found_steps -- a filtered list of step file names
            found_algs -- a filtered list of algorithm file names
            step_files -- a list of algorithm file names
            alg_files -- a list of algorithm file names
            ignored -- a regex object, used to filter unnecessary files
        Returns:
            a list of steps that were checked for interface compliance
            a list of algorithms that were checked for interface compliance
        """
        step_files = os.listdir(self.step_dir)
        ignored = re.compile(r'.*.pyc|__init__|_step.py|_alg.py')
        found_steps = filter(lambda x: not ignored.match(x), step_files)
        return found_steps

    def _load_steps(self, ordering):
        """
        Import steps, sort them according to provided order list and return a
        list of imported step modules.
        Params:
            ordering -- a list of steps order
        Args:
            step_list -- a list of step names, used to find a step missing in
                         config.xml
            missing_step -- a list of steps missing from config.xml
            missing_conf -- a list of steps missing in steps dir
        Returns:
            imported_steps -- a sorted list of imported step modules
        """
        print '> ExtLoader: Importing methods...'
        step_list = []
        imported_steps = []
        for step_name in ordering:
            for step in self.found_steps:
                imported = __import__(step.split('.')[0])  # import a step
                imp_name = getattr(imported, 'get_name')()  # get a step name
                if imp_name == step_name:
                    imported_steps.append(imported)
                    step_list.append(imp_name)
        missing_step = [i for i in step_list if i not in ordering]
        missing_conf = [i for i in ordering if i not in step_list]
        if missing_step:
            print 'MethodNotPresentError: {0} not found in config.xml'\
                    .format(missing_step)
            sys.exit("Critical Error!")
        elif missing_conf:
            print 'MethodNotPresentError: {0} not found in steps dir'\
                    .format(missing_conf)
            sys.exit("Critical Error!")
        # sorting methods according to config.xml order
        imported_steps.sort(key=lambda x: ordering.index(x.get_name()))
        return imported_steps

    def _instantiate_steps(self, imported_steps):
        """
        Instantiate imported steps and return a list of instantiated steps.
        Create a list with methods that represent a pipeline with
        selected algorithms and predefined settings.
        <When the Step object is instantiated it automatically imports and
        creates a list of algorithms that belong to it>
        Params:
            imported_steps -- a list of found and imported methods
        Args:
            alg_meth_map -- a dictionary of algs where {Algorithm: Step}
        Returns:
            steps -- a list with Method instances
        """
        # create a dict of instantiated Step objects
        steps = od()
        for step in imported_steps:
            inst = getattr(step, 'new')()  # instantiating Steps
            steps[step] = inst
        return steps


if __name__ == '__main__':
    pass

