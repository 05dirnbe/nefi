Dependencies
============

This document provides you with a listing of all the dependencies used for the development process of the application.
This is going to be useful if you intend to contribute to NEFI2 and want to create a proper development environment.
You will also find suggestions where you can download the dependencies in the Listing below.
If you contribute to this project and include additional dependencies, please make sure that you list them below and provide the information about access and installation procedure.

Python
++++++
Python 3.4
Download : https://www.python.org/download/releases/3.4.0/

The following is a general overview of all used dependencies in Nefi 2.0.

We will shortly introduce you all packages and where you can find more informations about it.


NumPy 1.10.4
+++++++++++++++++++


NumPy is an extension package to Python adding support for large, multi-dimensional arrays and matrices, along with a large library of high-level mathematical functions to operate on these arrays.
Since the images in OpenCV are represented as arrays, NumPy was a great help for us.
More informations you can find on the webpage of NumPy_

.. _NumPy: http://www.numpy.org


NetworkX 1.10
+++++++++++++++++++

NetworkX is a Python language software package for studying graphs and networks.
We used it to construct and refine the graphs from the images in the Graph detection and Graph filtering section.
More informations you can find on the webpage of NetworkX_

.. _NetworkX: https://networkx.github.io

demjson 2.2.4
+++++++++++++++++++

The “demjson” module, and the included “jsonlint” script, provide methods for encoding and decoding JSON formatted data, as well as checking JSON data for errors and/or portability issues.
The jsonlint command/script can be used from the command line without needing any programming.
More informations you can find on the webpage of demjson_

.. _demjson: https://pypi.python.org/pypi/demjson/2.2.4

decorator 4.0.9
+++++++++++++++++++

Python decorators are an interesting example of why syntactic sugar matters.
It is your best option if you want to preserve the signature of decorated functions in a consistent way across Python releases.
It helped us to reduce boilerplate code and by the separation of concerns, so that it enhanced the readability and maintenability of this project.
More informations you can find on the webpage of decorator_

.. _decorator: https://pypi.python.org/pypi/decorator

QDarkStyleSheet
+++++++++++++++++++


A dark stylesheet for Qt applications, which looks awesome.
More informations you can find on the webpage of QDarkStyleSheet_

.. _QDarkStyleSheet: https://github.com/ColinDuquesnoy/QDarkStyleSheet

thinning 1.2.3
+++++++++++++++++++

Thinning is the operation that takes a binary image and contracts the foreground until only single-pixel wide lines remain.
It is also known as skeletonization.
This package implements the thinning algorithm by Guo and Hall[1] for Numpy arrays.
It is thus compatible with OpenCV.
The algorithm is implemented in C and fairly fast.
More informations you can find on the webpage of thinning_

.. _thinning: https://github.com/tastyminerals/thinning_py3

OpenCV 3.1.0
+++++++++++++++++++

OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library.
OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products.
Being a BSD-licensed product, OpenCV makes it easy for businesses to utilize and modify the code.
More informations you can find on the webpage of OpenCV_

.. _OpenCV: http://opencv.org

PyQt5
+++++++++++++++++++
PyQt is a Python binding of the cross-platform GUI toolkit Qt.
It is one of Python's options for GUI programming and runs on all platforms supported by Qt including Windows, MacOS/X and Linux.
The bindings are implemented as a set of Python modules.
More informations you can find on the webpage of PyQt_

.. _PyQt: https://riverbankcomputing.com/software/pyqt/intro

.. toctree::
   :maxdepth: 2
