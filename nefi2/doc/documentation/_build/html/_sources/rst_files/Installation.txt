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

Get **homebrew**, a powerful package manger for mac os, by running:

::

  $ cd ~
  $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  $ brew update

If you don't have it already install python 3 like so:

::

  $ brew install python3
  $ brew linkapps

Next we update our PATH in ``~/.bash_profile`` to indicate that Homebrew packages should be used before any system packages. Simply add the following line to ``~/.bash_profile``:

::

  $ export PATH=/usr/local/bin:$PATH

Next reload the contents of ``~/.bash_profile``:

::

  $ source ~/.bash_profile

After typing:

::

  $ which python3

you should see:

::

  /usr/local/bin/python

Now we can install the actual dependencies by using **brew** and **pip3**:

::

  $ pip3 install numpy
  $ pip3 install networkx
  $ pip3 install demjson
  $ pip3 install PyQt5

Some of these packages rely on a compiler being present. If you don't have we highly recommend to get the current version of clang.

Finally, we install **OpenCV 3** with the necessary python bindings. To do so we execute:

::

  $ brew install opencv3 --with-python3

At this point I recommend to start a python3 interpreter and to test whether the import statements go through.

::

    Python 3.5.1 (default, Jan 22 2016, 08:52:08)
    [GCC 4.2.1 Compatible Apple LLVM 7.0.2 (clang-700.1.81)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import networkx
    >>> import numpy
    >>> import demjson
    >>> import PyQt5
    >>> import cv2
    >>>

Ideally, all imports go through and you are ready to start **NEFI2**.

At the time of testing this, however, it seemed that importing OpenCV3 failed, with the interpreter claiming that it doesn't know the module. Upon closer inspection it was found that the necessary files where there, but a link between the opencv stuff and the python3 site-packages was missing. I expect this issue to be resolved soon by the developers of brew and opencv. In the meantime, it is possible to rectify the situation manually as follows.

Brew has placed OpenCV3 somewhere in the its "cellar" which on my system resides here:

::

  /usr/local/Cellar/opencv3

Somewhere below this path there is a ``.so`` file that we need to symlink to the site-packages folder of our python 3. On my system this file was found to be here:

::

  /usr/local/Cellar/opencv3/3.1.0_1/lib/python3.5/site-packages/cv2.cpython-35m-darwin.so

In the site-packes directory of my python 3 a corresponding ``cv2.so`` files was missing. You can find this directory by running:

::

  $ brew info python3

All that is left to be done is to symlink the well-hidden, and strangely named, ``cv2.cpython-35m-darwin.so`` to its proper place in site-packages. On my system it was done as follows:

::

  $ sudo ln -s /usr/local/Cellar/opencv3/3.1.0_1/lib/python3.5/site-packages/cv2.cpython-35m-darwin.so /usr/local/lib/python3.5/site-packages/cv2.so

If the paths differ on your system you need to change the command accordingly. If done correctly the last import should succeed and you are good to go.

---------------
Linux
---------------

Make sure you have your **Python 3.4** installed before performing the steps below.
Please use ``linux_install.sh`` script for Linux. The script copies the required files into ``~/.nefi2`` directory and creates **nefi2** symlink in ``/usr/local/bin``.
It also installs necessary Python dependencies.

* git clone https://github.com/tastyminerals/NEFI2.git
* cd "NEFI2"
* ``./linux_install.sh``
* Install **PyQt5** using you default package manager.
* Next, you'll need to compile **OpenCV 3.1.0** for your Python 3.

Next, you'll need to compile **OpenCV** for Python3.

::

    git clone https://github.com/Itseez/opencv.git
    git checkout 3.1.0a
    mkdir release
    cd release
    cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=$(python3 -c "import sys; print(sys.prefix)") -D PYTHON_EXECUTABLE=$(which python3) ..
    make -j4
    sudo make install

If everything goes well, you can run NEFI2 by typing in console **nefi2**.
If not, try to perform the installation below step by step.

`NetworkX <https://networkx.github.io/documentation/latest/index.html>`_
+++++++++++++

::

  sudo pip3 install networkx

`demjson <http://deron.meranda.us/python/demjson/>`_
+++++++++++++

::

  sudo pip3 install demjson

`zope.event <https://pypi.python.org/pypi/zope.event/4.2.0>`_
+++++++++++++

::

  sudo pip3 install zope.event

`QDarkStyle <https://pypi.python.org/pypi/QDarkStyle/2.1>`_
+++++++++++++

::

  sudo pip3 install qdarkstyle


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
