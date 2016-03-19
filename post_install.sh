#!/bin/bash
# Install thinning module
easy_install deps/thinning_py3-1.2.3-py3.5-linux-x86_64.egg
# Compile opencv 3.1.0 for python3
git clone https://github.com/Itseez/opencv.git
cd opencv
mkdir release
cd release
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=$(python3 -c "import sys; print(sys.prefix)") -D PYTHON_EXECUTABLE=$(which python3) ..
make -j4
sudo make install
