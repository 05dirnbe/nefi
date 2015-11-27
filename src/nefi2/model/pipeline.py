# -*- coding: utf-8 -*-
"""
    A Pipeline class represents a central control mechanism over a sequential
    image processing pipeline. It controls all the available image processing
    methods, handles processing results and works as an mediator between the
    algorithms and UI.
"""

from images import Image
from container import OutContainer


class Pipeline:
    def __init__(self, methods, container):
        """Initialize default methods and their respective algorithms."""
        self.methods = methods
        self.container = container
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

    def run_meth(self, meth_name, alg):
        """Run a specific method."""
        # dummy settings, remove them
        settings = {'param1': 50, 'param2': 25}
        result = self.image
        for meth in self.container:
            if meth_name == meth.name:
                meth.activate(alg)
                result = meth.run(result, settings)
                break
        return result

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
    pass
