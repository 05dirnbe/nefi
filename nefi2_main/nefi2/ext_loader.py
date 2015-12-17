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


def read_configs():
    """
    Parse config.xml, extract steps order.
    Returns:
        order -- a list of steps order
    """
    tree = et.parse('config.xml')  # steps order
    root = tree.getroot()
    # create steps order list
    order = [e.text for elem in root for e in elem.iter('step')]
    return order


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
            _loaded_steps -- a sorted list of imported steps
        """
        self.step_dir = os.path.join('model', 'steps')
        self.found_steps = self._scan_model()
        _order = read_configs()
        self.steps_container = self._instantiate_steps(_order)

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

    def _instantiate_steps(self, ordering):
        """
        Instantiate imported steps and return a list of instantiated steps.
        Create a list with methods that represent a pipeline with selected
        algorithms and predefined settings.
        Sort the imported steps according to provided order list and return a
        list of imported step modules.
        <When the Step object is instantiated it automatically imports and
        creates a list of algorithms that belong to it>
        Params:
            ordering -- a list of steps order
        Vars:
            steps_inst -- a list of found and instantiated methods
            steps -- a dictionary of algs where {Algorithm: Step}
        Returns:
            steps -- a list with Method instances
        """
        steps_inst = []
        for step in self.found_steps:
            imported = __import__(step.split('.')[0],
                                  fromlist=['StepBody'])  # import a step
            inst = imported.StepBody()
            # create a dict of instantiated Step objects
            steps_inst.append(inst)
        # sort methods according to ordering
        steps_inst.sort(key=lambda x: ordering.index(x.get_name()))
        # create an ordered dict of {Step name: Step instance}
        steps = od()
        for step in steps_inst:
            steps[step.get_name()] = step
        return steps


if __name__ == '__main__':
    pass

