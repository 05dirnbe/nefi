# -*- coding: utf-8 -*-
from _category import Category


class CatBody(Category):
    """
    Implementation of the category graph detection
    """

    def __init__(self):
        """
        public Attributes:
            name (string): the name of the category

        Returns:
            instance of the gdetection object
        """
        self.name = 'Graph detection'
        # we need Category to load its algorithms after self.name assignment
        Category.__init__(self)


if __name__ == '__main__':
    pass
