**NEFI2** is a Python tool created to extract networks from images.

Given a suitable 2D image of a network as input, NEFI outputs a mathematical representation of the structure of the depicted network as a weighted undirected planar graph.
Representing the structure of the network as a graph enables subsequent studies of its properties using tools and concepts from graph theory.

![0](http://i.imgur.com/HGBwF31.png)

### Installation on Linux

Make sure you have your **Python 3.4** installed before performing the steps below.

* git clone https://github.com/05dirnbe/nefi.git
* cd "NetworkExtractionFromImages"
* `./install.sh`
* Install **PyQt5** using you default package manager.
* Next, you'll need to compile **OpenCV 3.1.0** for your Python 3.

```
    git clone https://github.com/Itseez/opencv.git
    git checkout 3.1.0a
    mkdir release
    cd release
    cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=$(python3 -c "import sys; print(sys.prefix)") -D PYTHON_EXECUTABLE=$(which python3) ..
    make -j4
    sudo make install
```

If everything goes well, you can run NEFI2 by typing in console **nefi2**.

