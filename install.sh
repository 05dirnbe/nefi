#!/bin/bash
sudo pip install numpy
sudo pip install networkx
sudo pip install demjson
sudo pip install QDarkStyle
sudo easy_install deps/thinning_py3-1.2.3-py3.5-linux-x86_64.egg
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
sudo ln -s $DIR/nefi2.py /usr/local/bin/nefi2
echo -e "\nDon't forget!\nYou need to install PyQt5 and to compile OpenCV for Python3!"
