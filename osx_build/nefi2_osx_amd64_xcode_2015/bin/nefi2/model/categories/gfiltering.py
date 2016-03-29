#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from nefi2.model.categories._category import Category
import os

class CatBody(Category):
    """
    Implementation of the category graph filtering
    """
    def __init__(self):
        """
        Public Attributes:
            | *name* (str): the name of the category

        Returns:
            | instance of the gfiltering object

        """
        self.name = 'Graph Filtering'
        self.icon = os.path.join(os.path.dirname(__file__), '..', '..', 'icons', 'F.png')
        # we need Category to load its algorithms after self.name assignment
        Category.__init__(self, self.name, self.icon)


if __name__ == '__main__':
    pass
