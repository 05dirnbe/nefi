# -*- coding: utf-8 -*-
"""
A Pipeline class represents a central control mechanism over a sequential
image processing pipeline. It controls all the available image processing
methods, handles processing results and works as an mediator between the
algorithms and UI.
"""
import sys
from container import OutContainer


class Pipeline:
    def __init__(self, container, default_pipe):
        """
        Initialize default methods and their respective algorithms.
        Args:
            container -- a list of instantiated Method objects
        Instance vars:
            self.container -- a list of instantiated Method objects
            self._pipe -- etree object of "pipeline" block in config.xml
            self._out_container -- a list that keeps processing results
            self.image -- Image object instance
        """
        self.container = container
        self._pipe = default_pipe
        self._out_container = OutContainer()
        print '> Pipeline: initialized with the following methods:'
        for m in self.container:
            print m
        print ''

    def load_new_pipeline(self, new_container, new_pipe):
        """
        Load a new pipeline and remove all previous results.
        Args:
            new_container -- a list with Method instances
            new_pipe -- xml.etree object of config.xml
        """
        self.container = new_container
        print '[ NEW CONTAINER LOADED ]', new_container
        self._pipe = new_pipe
        self._out_container.flush()  # removing all previous results

    def receive_image(self, image):
        """Get image and its settings.
        Args:
            image -- Image instance that represents a physical image.
        """
        print '> Pipeline: received "%s"' % image
        self.image = image

    def get_container_meth(self, name):
        """
        Get method instance from the container using its name.
        Args:
            name -- Method's name
        Returns:
            Method's instance
        """
        print '> Pipeline: "%s" is sent to the Pipeline.' % name
        return [inst for inst in self.container if inst.name == name]

    def mod_container_meth(self, methname):
        """
        Open up a container and make changes to a method.
        Args:
            methname -- Method's name
        """
        for meth in self.container:
            if meth.name == methname:
                meth.set_modified()

    def run_meth(self, meth_name, alg):
        """
        Run a specific method.
        Args:
            meth_name -- Method's name
            alg -- Algorithm's name
        Returns:
            return processing result
        """
        result = self.image
        for meth in self.container:
            if meth_name == meth.name:
                meth.use_alg(alg)
                result = meth.run(result, self._get_params(method=meth))
                break
        return result

    def run_meth_container(self):
        """
        Run each method in the container sequentially. If one of the methods
        was modified reprocess the pipeline from it.
        Returns:
            return processing result of all methods in the container
        """
        print '> Pipeline: pipeline started.'
        # first check if pipeline was modified
        modified = [m.name for m in self.container if m.get_modified()]
        self._out_container.flush()
        if not modified:
            result = self.image
            for meth in self.container:
                alg_name = self._get_params(method=meth.name).keys()[0]
                meth.use_alg(alg_name)
                result = meth.run(result, self._get_params(alg=alg_name))
                result.get_status()
                self._out_container.receive(result)
                print 'OUT:', result.result
        else:
            idx = [n[0] for n in enumerate(self.container)
                         if n[-1].get_name() in modified][0]
            result = self.image
            for meth in self.container[idx:]:
                alg_name = self._get_params(method=meth.name).keys()[0]
                meth.use_alg(alg_name)
                result = meth.run(result, self._get_params(alg=alg_name))
                result.get_status()
                self._out_container.receive(result)
                print 'OUT:', result.result
        print 'CONTAINER:', self._out_container.results
        return result

    def _get_params(self, **param):
        """
        Access default pipeline settings and get either an algorithm name and
        its parameters depending on the param argument.
        For example:
            _get_params(method="Preprocessing") -- returns a dict with
            algorithm name and its settings
            _get_params(alg="Blur") -- returns a dict with algorithm name and
            its settings
        Args:
            param -- a dict that specifies the required parameters
        Returns:
            settings -- a dict {algorithm_name: {parameter: value}}
        """
        ismethod = param.get('method')
        isalg = param.get('alg')
        settings = {}
        if ismethod:
            # get method settings with algorithm
            elems = [el for el in self._pipe.iter('settings')
                    if ismethod == el.attrib['method']][-1]
        elif isalg:
            # get algorithm settings and values
            elems = [el for el in self._pipe.iter('settings')
                    if isalg == el.attrib['alg']][0]
        else:
            # FIX: handle it differently
            print 'CRITICAL ERROR: No settings found for %s!' % param
            sys.exit(1)
        # get algorithm settings
        alg_pars = [(par.attrib['name'], par.text)
                    for par in elems.iter('param')]
        # store settings in dict
        settings[elems.attrib['alg']] = dict(alg_pars)
        return settings


if __name__ == '__main__':
    pass
