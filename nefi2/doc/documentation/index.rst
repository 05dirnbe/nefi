.. nefi documentation master file, created by
   sphinx-quickstart on Wed Jan  6 09:39:16 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to NEFI2's documentation!
================================

Well, I bet you've already read that NEFI2 is a cool tool to do Network Extraction from Images.
It is, but it is more than that.
NEFI2 was designed to be an extensible image processing pipeline which can be augmented with custom algorithms and algorithm configurations.
For example, you can add your own faster implementation of "Adaptive Threshold" or "Guided Watershed", you can easily set default settings and even construct a complete pipeline of your custom algorithms that solve a particular image processing task.
You don't need to write tons of boilerplate code, reimplement existing UI widgets and then connect them.
All you have to do is to grab a cup of coffee and read these docs.

Also, if you are interested in contributing in some way, this documentation is a good starting point.
Interested users might check out "Quick Start Guide for users".
People who'd like to poke into the code are advised to take a look into "Quick Start Guide for devs" first.
Those who decide that the documentation lacks are cordially invited to make it better.

Contents:

.. toctree::

   rst_files/Installation
   rst_files/Quick_Start_Guide_for_users
   rst_files/Quick_Start_Guide_for_developers
   rst_files/Development
   rst_files/Technologies

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
