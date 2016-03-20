#!/usr/bin/env python3
import os
import sys
os.chdir(os.path.dirname(os.path.realpath(__file__)))

from nefi2 import main
main.gui_mode()
