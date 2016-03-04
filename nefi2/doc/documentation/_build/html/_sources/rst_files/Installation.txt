===============
Installation
===============

This document will guide you throuregh the installation of the nefi project.
We offer installation support for some of the most popular operating system. Please
take a deeper look into you OS section.

---------------
Windows
---------------

We provide a Windows installer which you can download from <link>.

---------------
MacOSX
---------------


---------------
Linux
---------------
Make sure you have your python 3.4 installed before performing the following steps below.

NetworkX
+++++++++++++

::

# pip3 install networkx

demjson
+++++++++++++

::

# pip3 install demjson

PyQt5
+++++++++++++

For build and use PyQt5 you must install before `SIP <https://riverbankcomputing.com/software/sip/download>`_.
Download the package from the link and then unpack it. Then you need to configure executing **configure.py**:

::

# python3.4 configure.py

Then build and install it:

::

# make
# make install

After the successfull installation of **SIP** download `PyQt5 <http://www.riverbankcomputing.com/software/pyqt/download5>`_.
Configure it executing **configure.py**:

::

# python3.4 configure.py

Then build and install it:

::

# make
# make install


OpenCV
+++++++++++++

To compile OpenCV you need to clone the repository on your system and then install it by the commands:

::

# git clone https://github.com/Itseezopencv.git
# git checkout 3.1.0
# mkdir relase
# cd relase
# cmake -D CMAKE_BUILD_TYPE=RELASE -D CMAKE_INSTALL_PREFIX=$ (python3 -c "import sys; print(sys.prefix)") -D PYTHON_EXECUTABLE=$(which python3) ..
# make j4
# sudo make install

Thinning
+++++++++++++
Download the file from
:download:`thinning <towards-nefi-2-0/nefi2/doc/documentation/thinning.zip>`. Unpack it and then:

::

# python3.4 setup.py install






---------------
From source
---------------
