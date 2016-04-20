**NEFI2** is a Python tool created to extract networks from images.

Given a suitable 2D image of a network as input, **NEFI2** outputs a mathematical representation of the structure of the depicted network as a weighted undirected planar graph.
Representing the structure of the network as a graph enables subsequent studies of its properties using tools and concepts from graph theory.

**NEFI2** builds on top of well-documented open source libraries in order to provide a reliable, transparent and extendable collection of interchangeable solutions. **NEFI2** facilitates single image analysis as well as batch processing and aims to enable scientists and practitioners of various domains to freely explore, analyze and process their data in an intuitive, hands-on fashion.

Our major motivation in developing **NEFI2** is to enable virtually everyone to automatically extract networks from images.
**NEFI2** was designed to be an extensible image processing pipeline which can be augmented with custom algorithms and algorithm configurations.
For example, you can add your own faster implementation of "Adaptive Threshold" or "Guided Watershed", you can easily set default settings and even construct a complete pipeline of your custom algorithms that solve a particular image processing task.
You don't need to write tons of boilerplate code, reimplement existing UI widgets and then connect them.


![0](http://i.imgur.com/HGBwF31.png)

### Installation

##### Linux

* Make sure you have your **Python 3.4** installed before performing the steps below.
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

* git clone https://github.com/05dirnbe/nefi.git
* `cd nefi`
* `./linux_install.sh`

If everything goes well, you can run **NEFI2** by typing in console `nefi2`.
