# -*- coding: utf-8 -*-

from images import Image
from out_container import OutContainer

import re
import os
import sys
sys.path.insert(0, os.path.join(os.curdir, 'model', 'methods'))
sys.path.insert(0, os.path.join(os.curdir, 'model', 'algorithms'))
import xml.etree.ElementTree as et


# TODO: instance attributes self. should not be outside __init__ unless no other way.

def read_config():
    with open('config.xml', 'r') as conf:
        etconf = et.fromstring(conf.read())
    return etconf


class ModelScanner:
    """
    A class that scans for new files in /model/algorithms and
    /model/methods. It checks these files for compliance with the interface,
    analyses which algorithm belongs to which method and creates a
    corresponding mapping that is used by Method class upon instantiating.
    """
    def __init__(self):
        self.algdir = os.path.join('model', 'algorithms')
        self.methdir = os.path.join('model', 'methods')
        self.scan_dirs()

    def scan_dirs(self):
        """
        Search for new files in model directory and check their
        interface compliance. Incompatible files shall be not included into
        the pipeline and registered with the UI!
        """
        _alg_files = os.listdir(self.algdir)
        _meth_files = os.listdir(self.methdir)
        _ignored = re.compile(r'.*.pyc|__init__|_meth.py|howto.txt')
        self.algs = filter(lambda x: not _ignored.match(x), _alg_files)
        self.meths = filter(lambda x: not _ignored.match(x), _meth_files)
        self._check_compliance()

    def scan_meths(self):
        """
        Scan methods dir for new methods, check interface compliance,
        import methods, get method order from config.xml and return a sorted
         list of imported method instances.

            Returns:
                imported_meths -- a sorted list of imported methods
        """
        meth_list = []
        imported_meths = []
        for met in self.meths:
            imported = __import__(met.split('.')[0])
            imported_meths.append(imported)
            meth_list.append(getattr(imported, 'get_name')())
        meth_order = [meth.text for meth in read_config().iter('method')]
        missing_meth = [i for i in meth_list if i not in meth_order]
        missing_conf = [i for i in meth_order if i not in meth_list]
        if missing_meth:
            print 'MethodNotPresentError: {0} not found in config.xml'.format(missing_meth)
            return 1
        elif missing_conf:
            print 'MethodNotPresentError: {0} not found in methods dir'.format(missing_conf)
            return 1
        # sorting methods according to config.xml order
        imported_meths.sort(key=lambda x: meth_order.index(x.get_name()))
        return imported_meths

    def _check_compliance(self):
        """Check extension's code compliance."""
        _alg_required = ('apply', 'belong', 'main', 'get_name')
        for ex in self.algs:
            fpath = os.path.join(self.algdir, ex)
            with open(fpath, 'r') as extfile:
                fdata = extfile.read()
            # WARNING! findall does not do full word match
            found = re.findall('|'.join(_alg_required), fdata)
            if len(found) < 4:
                print found
                print 'AlgorithmSyntaxError: {0} does not comply with code ' \
                      'requirements, skipping.'.format(fpath)
                self.algs.remove(ex)

        _meth_required = ('new', 'get_name')
        for me in self.meths:
            fpath = os.path.join(self.methdir, me)
            with open(fpath, 'r') as methfile:
                fdata = methfile.read()
            # WARNING! findall does not do full word match
            found = re.findall('|'.join(_meth_required), fdata)
            if len(found) < 3:
                print 'MethodSyntaxError: {0} does not comply with code ' \
                      'requirements, skipping.'.format(fpath)
                self.meths.remove(me)

    def _get_methmath(self):
        """
        Scan algorithms dir for new algorithms, check for compliance and
        build alg -> method mapping.

            Returns:
                dict -- algorithm -> method mapping
        """
        alg_meth_map = {}
        for ext in self.algs:
            imported = __import__(ext.split('.')[0])
            alg_meth_map[imported] = getattr(imported, 'belongs')()
        return alg_meth_map


class Pipeline:
    def __init__(self):
        """Initialize default methods and their respective algorithms."""
        _modder = ModelScanner()
        self.methods = _modder.scan_meths()
        _methmap = _modder._get_methmath()
        self.container = self.create_meth_container(_methmap)
        self._out_container = OutContainer()
        print '> Pipeline: initialized with the following methods:'
        for m in self.methods:
            print m
        print ''

    def receive_image(self, image):
        """Get image and its settings"""
        print '> Pipeline: received "%s"' % image
        self.image = image

    def get_container_meth(self, name):
        """Get method instance from the container."""
        print '> Pipeline: "%s" is sent to the Pipeline.' % name
        return [inst for inst in self.container if inst.name == name]

    def create_meth_container(self, methmap):
        """
        Create a container with methods that represent a pipeline with
        selected algorithms and predefined settings.
        """
        meth_container = []
        for meth in self.methods:
            inst = getattr(meth, 'new')(methmap)
            meth_container.append(inst)
        return meth_container

    def mod_container_meth(self, methname):
        """Open up a container and make changes to a method."""
        for meth in self.container:
            if meth.name == methname:
                meth.set_modified()

    def run_meth_container(self):
        """Run each method in the container sequentially."""
        print '> Pipeline: default pipeline loaded.'
        # dummy config, remove it when the settings implementation is done
        def_config = ['Blur', 'Otsus Threshold', 'Guo Hall graph detector',
                      'Keep only largest connected component']

        # first check if pipeline was modified
        modified = [m.name for m in self.container if m.get_modified()]
        self._out_container.flush()
        if not modified:
            result = self.image
            for meth, alg in zip(self.container, def_config):
                meth.activate(alg)
                result = meth.run(result, def_config)
                result.get_status()
                self._out_container.receive(result)
                print 'OUT:', result.result
        else:
            idx = [n[0] for n in enumerate(self.methods)
                         if n[-1].get_name() in modified][0]
            result = self.image
            for meth, alg in zip(self.container[idx:], def_config[idx:]):
                meth.activate(alg)
                result = meth.run(result, def_config)
                result.get_status()
                self._out_container.receive(result)
                print 'OUT:', result.result
        print 'CONTAINER:', self._out_container.results
        return result


if __name__ == '__main__':
    ppl = Pipeline()
    # A user wants to run one algorithm to process an image
    print '\nUI: ======= ALGORITHM TEST ======='
    """
    Choosing one single method and algorithm to process the image.
    """
    img = Image('Polycephalum image')
    print '\nAction: selected method "Preprocessing"'
    meth = ppl.get_container_meth("Preprocessing")[0]
    print '\nAction: selected algorithm "Blur"'
    meth.activate('Blur')
    print '\nAction: process "{0}"'.format(img.name)
    print 'Action: clicked Run button.'
    out = meth.run(img, 'Blur')
    img.get_status()
    print out.signature

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
    print out.signature

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
    ppl.mod_container_meth('Graph detection')
    out = ppl.run_meth_container()
    print out.signature
