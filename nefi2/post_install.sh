#!/bin/bash

echo "Getting OpenCV"
git clone https://github.com/Itseezopencv.git
git checkout 3.1.0
mkdir release
cd release
echo "Building OpenCV 3.1.0"
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=$ (python3 -c "import sys; print(sys.prefix)") -D PYTHON_EXECUTABLE=$(which python3) ..
make j4
sudo make install
echo "Finished!"
