# -*- coding: utf-8 -*-
"""
    A class that works with "model" folder and is used by the pipeline in order
    to know about currently available algorithms and their respective methods.
"""
import inspect
import re
import os
import sys
sys.path.insert(0, os.path.join(os.curdir, 'model', 'methods'))
sys.path.insert(0, os.path.join(os.curdir, 'model', 'algorithms'))
import xml.etree.ElementTree as et


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

