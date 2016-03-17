===============
Installation
===============

This document will guide you throuregh the installation of NEFI2.
We offer installation support for some of the most popular operating systems.
Just pick your favourite OS section.

---------------
Windows
---------------

| x64 portable version is available <here>.
| x64 installer can be found <here>.
|

---------------
MacOSX
---------------

*to be added...*

---------------
Linux
---------------
Make sure you have your **Python 3.4** installed before performing the steps below.

`NetworkX <https://networkx.github.io/documentation/latest/index.html>`_
+++++++++++++

::

  sudo pip3 install networkx

`demjson <http://deron.meranda.us/python/demjson/>`_
+++++++++++++

::

  sudo pip3 install demjson

`sip <https://pypi.python.org/pypi/SIP>`_
+++++++++++++

::

  sudo pip3 install sip

`PyQt5 <https://www.riverbankcomputing.com/software/pyqt/download5>`_
+++++++++++++

::

  sudo pip3 install PyQt5

`OpenCV <http://opencv.org/>`_
+++++++++++++

You need to use OpenCV **version 3.1.0**.
Unfortunately there are no available binaries, you'll need to compile them from source.

::

  git clone https://github.com/Itseezopencv.git
  git checkout 3.1.0
  mkdir relase
  cd relase
  cmake -D CMAKE_BUILD_TYPE=RELASE -D CMAKE_INSTALL_PREFIX=$ (python3 -c "import sys; print(sys.prefix)") -D PYTHON_EXECUTABLE=$(which python3) ..
  make j4
  sudo make install

`Thinning <https://bitbucket.org/adrian_n/thinning>`_
+++++++++++++

This module was converted for Python3 and can be `downloaded from here <towards-nefi-2-0/nefi2/doc/documentation/thinning.zip>`_.

Unzip and install.

::

 python3.4 setup.py install

