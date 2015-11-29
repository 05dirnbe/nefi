# -*- coding: utf-8 -*-
"""
A class that works with "model" folder and is used to initialize the
pipeline with available methods and their respective algorithms.
"""
import inspect
import re
import os
import sys
sys.path.insert(0, os.path.join(os.curdir, 'model', 'methods'))
sys.path.insert(0, os.path.join(os.curdir, 'model', 'algorithms'))
import xml.etree.ElementTree as et

from model.pipeline import Pipeline
from model.images import Image


def read_config(xml_path):
    """
    Parse config.xml and return its xml representation.
    """
    tree = et.parse(xml_path)
    return tree.getroot()


class ExtensionLoader:
    """
    A class that initializes the pipeline and fills it with available method
    instances and algorithms. It scans for new files in /model/algorithms and
    /model/methods. It checks these files for compliance with the interface,
    analyses which algorithm belongs to which method and creates a
    corresponding mapping that is used by Method class upon instantiating.
    """
    def __init__(self):
        """
        Class constructor
        Instance vars:
            self.algdir -- a direcory path for algorithms
            self.methdir -- a directory path for methods
            self.all_algs -- a list of algorithm paths
            self.all_meths -- a list of method paths
            self.pipeline -- Pipeline instance
        Private vars:
            _default_pipe -- xml.etree object of config.xml
            _found_methods -- a sorted list of imported methods
            _container -- a list with Method instances
        """
        self.algdir = os.path.join('model', 'algorithms')
        self.methdir = os.path.join('model', 'methods')
        self.scan_dirs()
        _default_pipe = read_config('config.xml')
        _found_methods = self.scan_meths(_default_pipe)
        _container = self._get_meth_container(_found_methods)
        self.pipeline = Pipeline(_container, _default_pipe)

    def new_pipeline(self, pipe_path):
        """
        Replace currently active pipeline with a new one.
        Args:
            pipe_path -- a file path to a new pipeline
        """
        _new_pipe = read_config(pipe_path)  # xml.etree object
        new_meths = [elem.attrib['method'] for elem in _new_pipe]
        _found_methods = self.scan_meths(_new_pipe)
        self.pipeline.container = []  # erasing current method container
        _new_container = self._get_meth_container(_found_methods)
        self.pipeline.load_new_pipeline(_new_container, _new_pipe)

    def scan_dirs(self):
        """
        Search for new files in model directory and check their
        interface compliance. Incompatible files shall be not included into
        the pipeline and registered with the UI!
        """
        _alg_files = os.listdir(self.algdir)
        _meth_files = os.listdir(self.methdir)
        _ignored = re.compile(r'.*.pyc|__init__|_meth.py|HOWTO.txt')
        self.all_algs = filter(lambda x: not _ignored.match(x), _alg_files)
        self.all_meths = filter(lambda x: not _ignored.match(x), _meth_files)
        self._check_compliance()

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
            meth_name = settings.attrib['method']
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
            print 'MethodNotPresentError: {0} not found in methods dir'.format(missing_conf)
            return 1
        # sorting methods according to config.xml order
        print meth_order
        imported_meths.sort(key=lambda x: meth_order.index(x.get_name()))
        return imported_meths

    def _check_compliance(self):
        """
        Check extension's code compliance. If a file does not comply with the
        interface, skip it (it won't be displayed in UI).
        """
        _alg_required = ('apply', 'belong', 'main', 'get_name')
        for ex in self.all_algs:
            fpath = os.path.join(self.algdir, ex)
            with open(fpath, 'r') as extfile:
                fdata = extfile.read()
            # WARNING! findall does not do full word match
            found = re.findall('|'.join(_alg_required), fdata)  # FIX: weak matching
            if len(found) < 4:
                print found
                print 'AlgorithmSyntaxError: {0} does not comply with code ' \
                      'requirements, skipping.'.format(fpath)
                self.all_algs.remove(ex)

        _meth_required = ('new', 'get_name')
        for me in self.all_meths:
            fpath = os.path.join(self.methdir, me)
            with open(fpath, 'r') as methfile:
                fdata = methfile.read()
            # WARNING! findall does not do full word match
            found = re.findall('|'.join(_meth_required), fdata)  # FIX: weak matching
            if len(found) < 3:
                print 'MethodSyntaxError: {0} does not comply with code ' \
                      'requirements, skipping.'.format(fpath)
                self.all_meths.remove(me)

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


    def _sniff(self, alg_fun):
        """
        Inspect the algorithm function arguments and their respective types
        in order to inform the UI about the widgets that are required to
        correctly display the algorithm settings.

        <There should be two widgets available. Basically two of them
        actually make sense: checkbox and slider. I think other widgets are
        redundant and only add more unneeded complexity. If we detect that
        algorithm function requires bool argument we create a checkbox,
            else a slider.>
        """
        return inspect.getargspec(alg_fun)

    def get_pipeline(self):
        """
        Return a pipeline instance filled with methods and algorithms.
        """
        return self.pipeline


if __name__ == '__main__':
    loader = ExtensionLoader()
    ppl = loader.get_pipeline()
    # available samples: p_polycephalum.jpg, a_junius_wing.jpg
    impath = os.path.join('example_images', 'p_polycephalum.jpg')
    img = Image(impath)
    #ppl.receive_image(img)
    #ppl.run_meth('Preprocessing', 'Blur')
    # A user wants to run one algorithm to process an image
    print '\nUI: ======= ALGORITHM TEST ======='
    """
    Choosing one single method and algorithm to process the image.
    """
    print '\nAction: selected method "Segmentation"'
    meth = ppl.get_container_meth("Segmentation")[0]
    print '\nAction: selected algorithm "Otsus Threshold"'
    meth.use_alg('Otsus Threshold')
    print '\nAction: process "{0}"'.format(img.name)
    print 'Action: clicked Run button.'
    out = meth.run(img, 'Blur')
    img.get_status()
    print 'LAST PROCESSED BY: ', out.signature

    # A user runs a pipeline of algorithms
    print '\nUI: ======= PIPELINE TEST ======='
    """
    Choosing a predefined pipeline and running it.
    """
    img = Image('A Junius wing')
    ppl.receive_image(img)
    print '\nAction: selected default pipeline'
    print 'Action: clicked Run button.'
    out = ppl.run_meth_container()
    print 'LAST PROCESSED BY: ', out.signature

    # A user changes algorithm settings, we do not recalculate the pipeline.
    print '\nUI: ======= PIPELINE RECALC TEST ======='
    """
    This is a scenario, when a user modifies one of the algorithms
    in the pipeline and the pipeline starts from the method which algorithm
    has been changed.
    Original NEFI recalculates the whole pipeline for this user case.
    """
    print 'Action: changed settings in "Segmentation" method.'
    print 'Action: clicked Run button.'
    #ppl.mod_container_meth('Preprocessing')
    #ppl.mod_container_meth('Segmentation')
    ppl.mod_container_meth('Graph detection')
    #ppl.mod_container_meth('Graph filtering')
    out = ppl.run_meth_container()
    print 'LAST PROCESSED BY: ', out.signature

    # A user selects a different pipeline
    print '\nUI: ======= NEW PIPELINE TEST ======='
    """User loads previously saved pipeline into current instance"""
    loader.new_pipeline('saved_pipelines/a_junius.xml')
    img = Image('A Junius wing')
    ppl.receive_image(img)
    print '\nAction: selected default pipeline'
    print 'Action: clicked Run button.'
    out = ppl.run_meth_container()
    print 'LAST PROCESSED BY: ', out.signature

