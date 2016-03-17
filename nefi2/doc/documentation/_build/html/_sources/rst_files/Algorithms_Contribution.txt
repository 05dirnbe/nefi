Algorithms Contribution
=======================

This guide will provide you with the necessary steps required to add your custom algorithms.

Introduction
------------------

First of all you have to create a **.py** file in the folder :mod:`module.algorithms`.
This file will contain the algorithm that you want to add.
As convention of Nefi 2.0, the name of the file will be the name of the algorithm,
for example if the new algorithm is **Blur** the file's name will be "**blur.py**".
The main structure of the file will be a main class :class:`AlgBody` and its main methods :func:`AlgBody.__init__` and :func:`AlgBody.process`.

Imports
------------------

You have to import from :mod:`module.algorithms._alg` the class :class:`model.algorithms._alg.Algorithm`.
Also you have to import, if the algorithm needs it, the UI widgets that allow the user to select the input values of the algorithm.
The UI widgets that Nefi 2.0 provides are:
	* :class:`model.algorithms._alg.IntegerSlider`.
	* :class:`model.algorithms._alg.FloatSlider`.
	* :class:`model.algorithms._alg.CheckBox`.
	* :class:`model.algorithms._alg.DropDown`.

AlgBody Class
------------------

The :class:`AlgBody` class will contain all the methods that you need to implement your algorithm and the methods :func:`__init__` and :func:`process`.

The :func:`__init__` method is necessary to set the name of the algorithm, to link the algorithm at its category and to set the UI widgets.

	The **name** of the algorithm is defined by the attribute ``self.name``.

	The **parent category** of the algorithm is defined by the attribute ``self.parent``.

	To add the **UI widgets** create an UI object and then append it to the list ``self.integer_sliders``, ``self.float_sliders``, ``self.checkboxes`` or ``self.drop_downs``.


The :func:`process` is the main method that contains the logic of the algorithm.

	The **results** of the algorithm must be saved in the object ``self.result['img']``, if it is an image, and/or in ``self.result['graph']``, if it is a graph.
