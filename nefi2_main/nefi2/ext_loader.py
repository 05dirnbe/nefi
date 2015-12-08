# -*- coding: utf-8 -*-
"""
A class that works with "model" folder and is used to initialize the pipeline
with all available image processing steps and their respective algorithms.
It uses config.xml settings to initialize image processing steps accordingly.
ExtensionLoader creates a collection of steps and algorithms ready to be
loaded into the pipeline object.
"""
import re
import os
import sys
sys.path.insert(0, os.path.join(os.curdir, 'model', 'steps'))
sys.path.insert(0, os.path.join(os.curdir, 'model', 'algorithms'))
import xml.etree.ElementTree as et


def read_config(xml_path):
    """
    Parse config.xml, extract steps order and their default settings.
    Create a list with order of steps and a dictionary of default settings.
    Args:
        xml_path -- a path to config.xml
    Returns:
        order -- a list of steps order
        settings -- a settings dictionary of {Step: {Algorithm: {Param: val}}}
    """
    tree = et.parse(xml_path)
    root = tree.getroot()
    for elem in root:
        if elem.tag == 'order':
            # create steps order list
            order = [e.text for e in elem.iter('step')]
        elif elem.tag == 'default':
            # create a settings dictionary
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
            self.alg_dir -- a directory path for algorithms
            self.step_dir -- a directory path for steps
            self.loaded_algs -- a list of algorithm paths
            self.loaded_steps -- a list of step paths
        Private vars:
            _order -- a list of steps order in config.xml
            _settings -- a dictionary of config.xml settings
            _loaded_steps -- a sorted list of imported steps
            _steps_container -- a list with Step instances
        """
        self.alg_dir = os.path.join('model', 'algorithms')
        self.step_dir = os.path.join('model', 'steps')
        self.found_steps, self.found_algs = self._check(*self.scan_dirs())
        # _alg_presenter<String, Presenter>
        # _alg_view<String, View>
        _order, _settings = read_config('config.xml')
        _loaded_steps = self.load_steps(_order)
        _steps_container = self._create_steps_container(_loaded_steps)
        print _settings
        sys.exit()
        self.pipeline = Pipeline(_steps_container, _default_config)

    def scan_dirs(self):
        """
        Search for new files in model directory and check their interface
        compliance. Incompatible files shall be not included into the pipeline
        and registered with the UI!
        Vars:
            found_steps -- a filtered list of step file names
            found_algs -- a filtered list of algorithm file names
        Private vars:
            _step_files -- a list of algorithm file names
            _alg_files -- a list of algorithm file names
            _ignored -- a regex object, used to filter unnecessary files
        Returns:
            a list of steps that were checked for interface compliance
            a list of algorithms that were checked for interface compliance
        """
        _step_files = os.listdir(self.step_dir)
        _alg_files = os.listdir(self.alg_dir)
        _ignored = re.compile(r'.*.pyc|__init__|_step.py|HOWTO.txt')
        found_steps = filter(lambda x: not _ignored.match(x), _step_files)
        found_algs = filter(lambda x: not _ignored.match(x), _alg_files)
        return found_steps, found_algs

    def load_steps(self, ordering):
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

    def _check(self, steps, algs):
        """
        Check extension's code compliance. If a file does not comply with the
        interface a warning message will be send to std.out and the file will
        be skipped (won't be listed in the program UI).
        Params:
            steps -- a filtered list of step file names
            algs -- a filtered list of algorithm file names
        Private vars:
            _step_interface -- a list of required functions for steps
            _alg_interface -- a list of required functions for algorithms
        Returns:
            a list of steps checked for interface compliance
            a list of algorithms checked for interface compliance
        """
        # check algorithm files
        _alg_interface = ('process', 'belong', 'main', 'get_name')
        for alg in algs:
            fpath = os.path.join(self.alg_dir, alg)
            with open(fpath, 'r') as algfile:
                fdata = algfile.read()
            # WARNING! findall does not do full word match
            found = re.findall('|'.join(_alg_interface), fdata)  # FIX: weak matching
            if len(found) < 4:
                print found
                print 'AlgorithmSyntaxError: {0} does not comply with code ' \
                      'requirements, skipping.'.format(fpath)
                algs.remove(alg)
        # check step files
        _step_interface = ('new', 'get_name')
        for step in steps:
            fpath = os.path.join(self.step_dir, step)
            with open(fpath, 'r') as stepfile:
                fdata = stepfile.read()
            # WARNING! findall does not do full word match
            found = re.findall('|'.join(_step_interface), fdata)  # FIX: weak matching
            if len(found) < 3:
                print 'MethodSyntaxError: {0} does not comply with code ' \
                      'requirements, skipping.'.format(fpath)
                steps.remove(step)
        return steps, algs

    def _create_steps_container(self, imported_steps):
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
            step_container -- a list with Method instances
        """
        # to instantiate a step we need a mapping of {Algorithm: Step} first
        alg_meth_map = {}
        for ext in self.found_algs:
            imported = __import__(ext.split('.')[0])
            alg_meth_map[imported] = getattr(imported, 'belongs')()
        # create Step objects
        step_container = []
        for step in imported_steps:
            inst = getattr(step, 'new')(alg_meth_map)  # instantiating Steps
            step_container.append(inst)
        return step_container


if __name__ == '__main__':
    pass

