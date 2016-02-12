# -*- coding: utf-8 -*-
"""
This is nefi's main view. Currently we deployed all controls of the
GUI in the MainView.ui. Static changes to the GUI should always been
done by the Qt designer since this reduces the amount of code dramatically.
To draw the complete UI the controllers are invoked and the draw_ui function is
called
"""
from PyQt5 import QtCore, QtGui, QtWidgets, uic, Qt
import sys
import qdarkstyle
from settings import *
from _alg import *
from adaptive import *

__authors__ = {"Dennis Groß": "gdennis91@googlemail.com"}


class SettingsController:
    def __init__(self):

        pass


