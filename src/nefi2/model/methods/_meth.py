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
            Method knows everything about its algorithms.
            The class gets instantiated with a methmap parameter that is
            created and returned by ModelScanner.
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
        """Return the algorithms that belong to current method instance."""
        return [k for k, v in methmap.items() if v == self.name]

    def activate(self, alg_name):
        """Explicitly set an algorithm for current method."""
        print '> "%s" method: "%s" algorithm shall be used' % (self.name, alg_name)
        self.curalg = alg_name

    def get_activated(self):
        """Return the name of the currently set algorithm."""
        return self.curalg

    def run(self, image, settings):
        """Run a specific algorithm on the image."""
        print '> "%s" method: using "%s" algorithm' % (self.name, self.curalg)
        _algorithm = [mod for mod in self.algs
                      if self.curalg == mod.__algorithm__][0]
        changes = _algorithm.apply(image, settings)
        image.save(changes)
        image.processed = True
        return image

    def get_name(self):
        return self.name

    def set_modified(self):
        print '> Method: "%s" was modified. Start processing from "%s".' % (self.name, self.name)
        self.modified = True

    def get_modified(self):
        return self.modified


if __name__ == '__main__':
    pass
