# -*- coding: utf-8 -*-


class Method:
    def __init__(self, name, methmap):
        """Method knows everything about its algorithms."""
        self.name = name
        # get a list of algorithms that belong to current method instance
        self.algs = self.get_algs(methmap)
        self.modified = False
        print '> Method: I am "%s" method' % self.name
        print '> I have the following algorithms:'
        print len(self.algs), 'in total.'
        print ''

    def get_algs(self, methmap):
        """Return the algorithms that belong to current method instance."""
        return [k for k, v in methmap.items() if v == self.name]

    def set_alg(self, alg_name):
        """Explicitly set an algorithm for current method"""
        print '> "%s" method: "%s" algorithm shall be used' % (self.name, alg_name)
        self.alg = alg_name

    def run(self, image, settings):
        """Run a specific algorithm on the image."""
        print '> "%s" method: using "%s" algorithm' % (self.name, self.alg)
        _algorithm = [mod for mod in self.algs
                      if self.alg == mod.__algorithm__][0]
        _algorithm.apply(image, settings)
        image.processed = True

    def get_name(self):
        return self.name

    def set_modified(self):
        print '> Method: "%s" was modified.' % self.name
        self.modified = True

    def get_modified(self):
        return self.modified


if __name__ == '__main__':
    pass
