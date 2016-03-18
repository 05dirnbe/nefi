.. _dev_guide:

Quick Start Guide for developers
================================

NEFI2 is built with `MVC pattern <https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller>`_, so you will find familiar directories like "model" and "view" (we removed "controller" in latest versions) inside the project repository.

There are 3 main components in NEFI2 that you need to know about: **Pipeline**, **Categories** and **Algorithms**.
**Pipeline** contains **Categories** which in turn contain **Algorithms**.
**Category** is a collection of algorithms that fulfill specific image processing task.

Basically, the most important files you need to know are:

::

  model/pipeline.py
  model/ext_loader.py
  view/controller.py
  view/MainView.ui

| **pipeline.py** --> controls application data flow, reading and writing any data to disk.
| **ext_loader.py** --> looks through available algorithms and categories and instantiates them at startup.
| **controller.py** --> contains various UI controllers and methods are here.
| **MainView.ui** --> a UI template created in QTDesigner.
|

NEFI2 Architechture
+++++++++++++++++++

.. figure::  images/nefi2.png
   :align:   center
   :scale: 85%

The core of NEFI2 is the **Pipeline** class which controls how data is processed.
Whenever an algorithm produces a result, the **Pipeline** passes the result to the next **Algorithm** in a queue.
Intermediate results are saved on disk.

NEFI2 Startup
+++++++++++++

.. figure::  images/pipeline_start.png
   :align:   center
   :scale: 85%

The idea behind **Extension Loader** class which resides in ``ext_loader.py`` is to search and instantiate **Categories** during startup.
The **Categories**, in turn, will instantiate all **Algorithms** (each category instantiates only the algorithms that belong to it). Once the **Algorithms** are instantiated controller creates the necessary widgets for **Algorithm** settings in the UI.


Keep in mind that this project is in its early stages and even though we tried our best it has bugs, so don't be shy add report bugs on our `Github page <http://www.github.com/???`_.
