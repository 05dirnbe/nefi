# -*- coding: utf-8 -*-

import ntpath


class Image:
    def __init__(self, fpath):
        _head, _tail = ntpath.split(fpath)
        self.name = _tail or ntpath.basename(_head)
        self.signature = ''
        self.processed = False
        self.result = self.read_image(fpath)
        print '> Image: initialized, processed: %s' % self.processed

    def get_status(self):
        print '> Image: "%s" processed: %s' % (self.name, self.processed)

    def read_image(self, img_path):
        return img_path
        print '> Image: "%s" image loaded.' % self.name

    @property
    def processed(self):
        return self.processed

    @processed.setter
    def processed(self, status):
        self.processed = status

    def save(self, output):
        """Save the result of algorithm processing."""
        self.result = output

    def sign(self, *signature):
        """Save the name of the algorithm that processed the image and its
        settings."""
        self.signature = signature

if __name__ == '__main__':
    pass
