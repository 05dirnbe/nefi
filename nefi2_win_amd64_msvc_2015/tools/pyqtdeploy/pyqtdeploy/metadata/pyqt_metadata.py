# Copyright (c) 2015, Riverbank Computing Limited
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


class PyQtMetadata:
    """ Encapsulate the meta-data for a single PyQt module. """

    def __init__(self, group, deps, cpp11, gui, qt4, qt5, config4, config5, needs_suffix):
        """ Initialise the object. """

        # The group (either 'base', 'opengl', or 'addon') that the module
        # belongs to.
        self.group = group

        # The sequence of the names of other modules that this module is
        # dependent on.  These should be applied recursively to determine the
        # complete set of dependencies for a module.
        self.deps = deps

        # Set if C++11 compiler support is needed.
        self.cpp11 = cpp11

        # Set if the QtGui module is needed.
        self.gui = gui

        # The sequence of strings to add the qmake's QT variable when building
        # against Qt v4.
        self.qt4 = qt4

        # The sequence of strings to add the qmake's QT variable when building
        # against Qt v5.
        self.qt5 = qt5

        # The sequence of strings to add the qmake's CONFIG variable when
        # building against Qt v4.
        self.config4 = config4

        # The sequence of strings to add the qmake's CONFIG variable when
        # building against Qt v5.
        self.config5 = config5

        # Set if a suffix must be added to the name of the statically linked
        # module (in order to work around a quirk in Qt4's qmake).
        self.needs_suffix = needs_suffix
