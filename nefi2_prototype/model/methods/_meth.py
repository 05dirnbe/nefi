# -*- coding: utf-8 -*-
"""
This class represents image processing method that contains its respective
algorithms. Its main function is controlling an algorithm, collecting and
transmitting the output to the pipeline. It serves as an intermediate layer
between the algorithms and the pipeline.
"""


class Method:
    def __init__(self, name, methmap):
        """
        Method class gets instantiated with a methmap parameter that is
        created and returned by ModelScanner.
        Args:
            name -- Method's name
            methmap -- a simple dict: algorithm --> method
        Instance vars:
            self.name -- Method's name
            self.algs -- list with algorithm instances
            self.modified -- True if Method's state has been modified
            self.curalg -- Currently selected algorithm
        """
        self.name = name
        # get a list of algorithms that belong to current method instance
        self.algs = self.get_algs(methmap)
        self.modified = False

        # dummy implementation below, replace
        print '> Method: I am "%s" method' % self.name
        print '> I have the following algorithms:'
        for a in self.algs:
            print a
        print len(self.algs), 'in total.'
        print ''

    def get_algs(self, methmap):
        """
        Return the algorithms that belong to current method instance.
        Args:
            methmap -- a simple dict: algorithm --> method
        """
        return [k for k, v in methmap.items() if v == self.name]

    def use_alg(self, alg_name):
        """
        Explicitly set an algorithm for current method.
        Args:
            alg_name -- algorithm's name that was selected in the UI
        """
        print '> "%s" method: "%s" algorithm shall be used' % (self.name, alg_name)
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
        Args:
            image -- Image instance
            settings -- a dict with algorithm settings
        """
        print '> "%s" method: using "%s" algorithm' % (self.name, self.curalg)
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
        print '> Method: "%s" was modified. Start processing from "%s".' % (self.name, self.name)
        self.modified = True

    def get_modified(self):
        return self.modified


if __name__ == '__main__':
    pass
