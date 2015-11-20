# -*- coding: utf-8 -*-


class Image:
    def __init__(self):
        self.processed = False
        print '> Image: initialized, processed: %s' % self.processed

    def get_status(self):
        print '> Image: "%s" processed: %s' % (self.img, self.processed)

    def read_image(self, img_path):
        self.img = img_path
        print '> Image: "%s" image loaded.' % self.img

    @property
    def processed(self):
        return self.processed

    @processed.setter
    def processed(self, status):
        self.processed = status


if __name__ == '__main__':
    pass
