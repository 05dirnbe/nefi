# -*- coding: utf-8 -*-
from _category import Category


class CatBody(Category):
    def __init__(self):
        self.name = 'Graph filtering'
        # we need Category to load its algorithms after self.name assignment
        Category.__init__(self)


if __name__ == '__main__':
    pass
