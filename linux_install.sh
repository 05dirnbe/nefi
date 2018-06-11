#!/bin/bash
INSTALL_DIR=$HOME/.nefi2
SHORTCUT=/usr/local/bin/nefi2

echo "Copying files..."
# copy files
if [ -d "$INSTALL_DIR" ]; then
    rm -r $INSTALL_DIR
fi
mkdir $HOME/.nefi2
cp -r nefi2 $HOME/.nefi2
cp -r sample_images $HOME/.nefi2
cp nefi2.py $HOME/.nefi2
cp LICENSE $HOME/.nefi2
cp README.md $HOME/.nefi2

# create a symlink
if [ -L "$SHORTCUT" ]; then
    sudo rm /usr/local/bin/nefi2
fi
sudo ln -s $HOME/.nefi2/nefi2.py /usr/local/bin/nefi2

echo "Installing dependencies..."
# install python dependencies
sudo pip install numpy
sudo pip install networkx
sudo pip install demjson
sudo pip install QDarkStyle
sudo pip install thinning_py3
echo "Done"
