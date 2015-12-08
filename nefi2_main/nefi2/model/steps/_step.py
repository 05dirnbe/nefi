# -*- coding: utf-8 -*-
"""
This class represents image processing method that contains its respective
algorithms. Its main function is controlling an algorithm, collecting and
transmitting the output to the pipeline. It serves as an intermediate layer
between the algorithms and the pipeline.
"""


class Step:
    def __init__(self, name, stepmap):
        """
        Step class gets instantiated with a stepmap parameter that is
        created by ExtensionLoader.
        Params:
            name -- Method's name
            stepmap -- a simple dict: algorithm --> method
        Instance vars:
            self.name -- Method's name
            self.algs -- list with algorithm instances
            self.modified -- True if Method's state has been modified
            self.curalg -- Currently selected algorithm
        """
        self.name = name
        # get a list of algorithms that belong to current method instance
        self.algs = self.get_algs(stepmap)
        self.modified = False

        # dummy implementation below, replace
        print '> Step: I am "%s" step' % self.name
        print '> I have the following algorithms:'
        for a in self.algs:
            print a
        print len(self.algs), 'in total.'
        print ''

    def get_algs(self, stepmap):
        """
        Return the algorithms that belong to current method instance.
        Params:
            stepmap -- a simple dict: algorithm --> method
        """
        return [k for k, v in stepmap.items() if v == self.name]

    def use_alg(self, alg_name):
        """
        Explicitly set an algorithm for current method.
        Params:
            alg_name -- algorithm's name that was selected in the UI
        """
        print '> "%s" step: "%s" algorithm shall be used' % (self.name, alg_name)
        self.curalg = alg_name

    def get_used_alg(self):
        """
        Return the name of the currently set algorithm.
        Returns:
            self.curalg -- Currently selected algorithm
        """
        return self.curalg

    def run(self, image, settings):
        """
        Run a specific algorithm on the image.
        Params:
            image -- Image instance
            settings -- a dict with algorithm settings
        """
        print '> "%s" step: using "%s" algorithm' % (self.name, self.curalg)
        _algorithm = [mod for mod in self.algs
                      if self.curalg == mod.__algorithm__][0]
        changes = _algorithm.process(image, settings)
        image.save(changes)
        image.processed = True
        self.modified = False  # reset modified variable after processing
        return image

    def get_name(self):
        return self.name

    def set_modified(self):
        """Set True if method settings were modified."""
        print '> Step: "%s" was modified. Start processing from "%s".' % (self.name, self.name)
        self.modified = True

    def get_modified(self):
        return self.modified


if __name__ == '__main__':
    pass
