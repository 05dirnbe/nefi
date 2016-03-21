.. _add_cats:

Categories Creation
===================

Even though the default *Preprocessing*, *Segmentation*, *Graph Detection*, *Graph Filtering* categories should be enough for an image processing pipeline.
You might want to add a custom one, for example, for testing purposes.
NEFI2 **Category** is a simple container for the **Algorithms**.
Whenever a new **Category** appears in ``model/categories`` directory it is automatically loaded and displayed in the UI.

Let's go through a small tutorial.

Tutorial
--------

So, you decided to add a new **Category** which will be called "Testing".

1. Goto ``model/categories`` directory and create a file **testing.py**
2. Use **Category** header code below and paste it into **testing.py**.

::

    # -*- coding: utf-8 -*-
    from _category import Category


    class CatBody(Category):
        """My Testing category"""
        def __init__(self):
            self.name = ""
            self.icon = ""
            Category.__init__(self, self.name, self.icon)


    if __name__ == '__main__':
        pass

3. Define the name: ``self.name = "Testing"`` and the icon which this category shall use (optional): ``self.icon = "./assets/images/P.png"``.

This is it! Test it by running NEFI2.

.. figure::  images/tutorial2.png
   :align:   center
   :scale: 85%

In order to add an existing **Algorithm** to this new **Category**, replace ``self.parent = "Preprocessing"`` to ``self.parent = "Testing"`` in the algorithm class constructor.
For more details, see section :ref:`alg_contrib`.
