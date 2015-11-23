# -*- coding: utf-8 -*-

from images import Image
from out_container import OutContainer
from presenter import ModelScanner

import re
import os
import sys
sys.path.insert(0, os.path.join(os.curdir, 'model', 'methods'))
sys.path.insert(0, os.path.join(os.curdir, 'model', 'algorithms'))


# TODO: instance attributes self. should not be outside __init__ unless no other way.


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
        """Get image and its settings.
        Args:
            image -- Image instance that represents a physical image.
        """
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
        print '> Pipeline: pipeline started.'
        # dummy config, remove it when the settings implementation is done
        def_config = ['Blur', 'Otsus Threshold', 'Guo Hall graph detector',
                      'Keep only largest connected component']
        settings = {'param1': 50, 'param2': 25}
        # first check if pipeline was modified
        modified = [m.name for m in self.container if m.get_modified()]
        self._out_container.flush()
        if not modified:
            result = self.image
            for meth, alg in zip(self.container, def_config):
                meth.activate(alg)
                result = meth.run(result, settings)
                result.get_status()
                self._out_container.receive(result)
                print 'OUT:', result.result
        else:
            idx = [n[0] for n in enumerate(self.methods)
                         if n[-1].get_name() in modified][0]
            result = self.image
            for meth, alg in zip(self.container[idx:], def_config[idx:]):
                meth.activate(alg)
                result = meth.run(result, settings)
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

    # available samples: p_polycephalum.jpg, a_junius_wing.jpg
    impath = os.path.join('example_images', 'p_polycephalum.jpg')
    img = Image(impath)
    print '\nAction: selected method "Preprocessing"'
    meth = ppl.get_container_meth("Preprocessing")[0]
    print '\nAction: selected algorithm "Blur"'
    meth.activate('Blur')
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
    #ppl.mod_container_meth('Graph detection')
    #ppl.mod_container_meth('Graph filtering')
    out = ppl.run_meth_container()
    print 'LAST PROCESSED BY: ', out.signature
