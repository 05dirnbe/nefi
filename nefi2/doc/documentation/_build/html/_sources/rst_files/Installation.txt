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

There are two installation options: using **setup.py** or manually installing all the dependencies if for some reason **setup.py** won't work for you.
Make sure you have your **Python 3.4** installed before performing the steps below.

* git clone https://github.com/LumPenPacK/NetworkExtractionFromImages.git
* cd "NetworkExtractionFromImages"
* ``sudo pip3 install .``
* Install **PyQt5** using you default package manager.
* Next, you'll need to compile **OpenCV 3.1.0** for your Python 3.

::

    git clone https://github.com/Itseez/opencv.git
    git checkout 3.1.0a
    mkdir release
    cd release
    cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=$(python3 -c "import sys; print(sys.prefix)") -D PYTHON_EXECUTABLE=$(which python3) ..
    make -j4
    sudo make install

If everything goes well, you can run NEFI2 by typing in console **nefi2**.

If not, try manually installing all the dependencies via **pip3**.

`NetworkX <https://networkx.github.io/documentation/latest/index.html>`_
+++++++++++++

::

  sudo pip3 install networkx

`demjson <http://deron.meranda.us/python/demjson/>`_
+++++++++++++

::

  sudo pip3 install demjson

`PyQt5 <https://www.riverbankcomputing.com/software/pyqt/download5>`_
+++++++++++++

Install **python-pyqt5** using your package manager.


`OpenCV <http://opencv.org/>`_
+++++++++++++

You need to use OpenCV **version 3.1.0**.
Unfortunately there are no available binaries, you'll need to compile them from source.

::

    git clone https://github.com/Itseez/opencv.git
    mkdir release
    cd release
    cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=$(python3 -c "import sys; print(sys.prefix)") -D PYTHON_EXECUTABLE=$(which python3) ..
    make -j4
    sudo make install

`Thinning <https://bitbucket.org/adrian_n/thinning>`_
+++++++++++++

This module was converted for Python3 and can be `downloaded from here <https://pypi.python.org/pypi?name=thinning_py3&version=1.2.3&:action=display>`_.

Unzip and install.

::

 python3.4 setup.py install
