# -*- coding: utf-8 -*-
"""
A class that works with "model" folder and is used to initialize the pipeline
with all available image processing steps and their respective algorithms.
It uses config.xml settings to initialize image processing steps accordingly.
ExtensionLoader creates a collectiong of steps and algorithms ready to be
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
                for alg in step.iter('alg'):
                    alg_name = alg.attrib['name']
                    settings[step_name] = {alg_name: {}}
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
            self.alg_dir -- a direcory path for algorithms
            self.step_dir -- a directory path for steps
            self.all_algs -- a list of algorithm paths
            self.all_steps -- a list of step paths
        Private vars:
            _default_config -- xml.etree object of config.xml
            _loaded_steps -- a sorted list of imported steps
            _steps_container -- a list with Step instances
        """
        self.alg_dir = os.path.join('model', 'algorithms')
        self.step_dir = os.path.join('model', 'steps')
        self.all_steps, self.all_algs = self._check(*self.scan_dirs())
        ###
        _default_config = read_config('config.xml')
        _found_steps = self.scan_meths(_default_config)
        _steps_container = self._get_meth_container(_found_steps)
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
        _ignored = re.compile(r'.*.pyc|__init__|_meth.py|HOWTO.txt')
        found_steps = filter(lambda x: not _ignored.match(x), _step_files)
        found_algs = filter(lambda x: not _ignored.match(x), _alg_files)
        return found_steps, found_algs

    def scan_meths(self, pipe_config):
        """
        Scan methods dir for new methods, check interface compliance,
        import methods according to provided pipeline config, sort them and
        return a list of imported method instances.
        Args:
            pipe_config -- xml.etree object of config.xml
        Returns:
            imported_meths -- a sorted list of imported methods
        """
        print '> ExtLoader: Importing methods...'
        meth_list = []
        imported_meths = []
        for settings in pipe_config:
            meth_name = settings.attrib['step']
            for met in self.all_meths:
                imported = __import__(met.split('.')[0])
                imp_name = getattr(imported, 'get_name')()
                if imp_name == meth_name:
                    imported_meths.append(imported)
                    meth_list.append(imp_name)

        meth_order = [m.attrib['method'] for m in pipe_config.iter('settings')]
        missing_meth = [i for i in meth_list if i not in meth_order]
        missing_conf = [i for i in meth_order if i not in meth_list]
        if missing_meth:
            print 'MethodNotPresentError: {0} not found in config.xml'.format(missing_meth)
            return 1
        elif missing_conf:
            print 'MethodNotPresentError: {0} not found in steps dir'.format(missing_conf)
            return 1
        # sorting methods according to config.xml order
        imported_meths.sort(key=lambda x: meth_order.index(x.get_name()))
        return imported_meths

    def _check(self, steps, algs):
        """
        Check extension's code compliance. If a file does not comply with the
        interface a warning message will be send to std.out and the file will
        be skipped (won't be listed in the program UI).
        Args:
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


    def _get_meth_container(self, found_meths):
        """
        Build alg -> method mapping.
        Create a container with methods that represent a pipeline with
        selected algorithms and predefined settings.
        Args:
            found_meths -- a list of found and imported methods
        Returns:
            meth_container -- a list with Method instances
        """
        alg_meth_map = {}
        for ext in self.all_algs:
            imported = __import__(ext.split('.')[0])
            alg_meth_map[imported] = getattr(imported, 'belongs')()

        meth_container = []
        for meth in found_meths:
            inst = getattr(meth, 'new')(alg_meth_map)  # creating Method objects
            meth_container.append(inst)
        return meth_container


if __name__ == '__main__':
    pass

