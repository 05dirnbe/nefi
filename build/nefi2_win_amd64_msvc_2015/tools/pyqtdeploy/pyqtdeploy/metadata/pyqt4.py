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


__all__ = ['pyqt4_metadata']


from .pyqt_metadata import PyQtMetadata


class PyQt4Metadata(PyQtMetadata):
    """ Encapsulate the meta-data for a single PyQt4 module. """

    def __init__(self, group='base', deps=(), gui=True, qt4=(), qt5=(), config4=(), config5=(), needs_suffix=True):
        """ Initialise the object. """

        super().__init__(group=group, deps=deps, cpp11=False, gui=gui, qt4=qt4,
                qt5=qt5, config4=config4, config5=config5,
                needs_suffix=needs_suffix)


# The dictionary of meta-data for the PyQt4 modules.
pyqt4_metadata = {
    'sip':
            PyQt4Metadata(gui=False),

    'QAxContainer':
        PyQt4Metadata(deps=['QtGui'], config4=['qaxcontainer'],
                qt5=['axcontainer']),

    'Qt':
        PyQt4Metadata(deps=['sip']),

    'QtCore':
        PyQt4Metadata(deps=['sip'], gui=False),

    'QtDBus':
        PyQt4Metadata(deps=['QtCore'], gui=False, qt4=['dbus'], qt5=['dbus']),

    'QtDeclarative':
        PyQt4Metadata(deps=['QtGui', 'QtNetwork'],
                qt4=['declarative', 'network'],
                qt5=['declarative', 'network']),

    'QtDesigner':
        PyQt4Metadata(deps=['QtGui'], config4=['designer'], qt5=['designer']),

    'QtGui':
        PyQt4Metadata(deps=['QtCore'], qt5=['widgets', 'printsupport']),

    'QtHelp':
        PyQt4Metadata(deps=['QtGui'], config4=['help'], qt5=['help']),

    'QtMultimedia':
        PyQt4Metadata(deps=['QtGui'], qt4=['multimedia'], qt5=['multimedia']),

    'QtNetwork':
        PyQt4Metadata(deps=['QtCore'], gui=False, qt4=['network'],
                qt5=['network']),

    'QtOpenGL':
        PyQt4Metadata(deps=['QtGui'], qt4=['opengl'], qt5=['opengl']),

    'QtScript':
        PyQt4Metadata(deps=['QtCore'], gui=False, qt4=['script'],
                qt5=['script']),

    'QtScriptTools':
        PyQt4Metadata(deps=['QtGui', 'QtScript'],
                qt4=['scripttools', 'script'],
                qt5=['scripttools', 'script', 'widgets']),

    'QtSql':
        PyQt4Metadata(deps=['QtGui'], qt4=['sql'], qt5=['sql', 'widgets']),

    'QtSvg':
        PyQt4Metadata(deps=['QtGui'], qt4=['svg'], qt5=['svg']),

    'QtTest':
        PyQt4Metadata(deps=['QtGui'], qt4=['testlib'],
                qt5=['testlib', 'widgets']),

    'QtWebKit':
        PyQt4Metadata(deps=['QtGui', 'QtNetwork'], qt4=['webkit', 'network'],
                qt5=['webkit', 'webkitwidgets', 'network']),

    'QtXml':
        PyQt4Metadata(deps=['QtCore'], gui=False, qt4=['xml'], qt5=['xml']),

    'QtXmlPatterns':
        PyQt4Metadata(deps=['QtNetwork'], gui=False,
                qt4=['xmlpatterns', 'network'],
                qt5=['xmlpatterns', 'network']),

    'phonon':
        PyQt4Metadata(deps=['QtGui'], qt4=['phonon']),

    'uic':
        PyQt4Metadata(deps=['QtGui']),

    'QtChart':
        PyQt4Metadata(group='addon', deps=['QtGui'],
                config4=['qtcommercialchart'], config5=['qtcommercialchart'],
                needs_suffix=False),

    'Qsci':
        PyQt4Metadata(group='addon', deps=['QtGui'], config4=['qscintilla2'],
                config5=['qscintilla2'], needs_suffix=False),
}
