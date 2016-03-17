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


__all__ = ['pyqt5_metadata']


from .pyqt_metadata import PyQtMetadata


class PyQt5Metadata(PyQtMetadata):
    """ Encapsulate the meta-data for a single PyQt5 module. """

    def __init__(self, group='base', deps=(), cpp11=False, gui=True, qt5=(), config5=()):
        """ Initialise the object. """

        super().__init__(group=group, deps=deps, cpp11=cpp11, gui=gui, qt4=qt5,
                qt5=qt5, config4=config5, config5=config5, needs_suffix=False)


# The dictionary of meta-data for the PyQt5 modules.
pyqt5_metadata = {
    'sip':
        PyQt5Metadata(gui=False),

    'QAxContainer':
        PyQt5Metadata(deps=['QtWidgets'], qt5=['axcontainer']),

    'Qt':
        PyQt5Metadata(deps=['sip']),

    'QtBluetooth':
        PyQt5Metadata(deps=['QtCore'], gui=False, qt5=['bluetooth']),

    'QtCore':
        PyQt5Metadata(deps=['sip'], gui=False),

    'QtDBus':
        PyQt5Metadata(deps=['QtCore'], gui=False, qt5=['dbus']),

    'QtDesigner':
        PyQt5Metadata(deps=['QtWidgets'], qt5=['designer']),

    'QtGui':
        PyQt5Metadata(deps=['QtCore']),

    'QtHelp':
        PyQt5Metadata(deps=['QtWidgets'], qt5=['help']),

    'QtLocation':
        PyQt5Metadata(deps=['QtPositioning'], qt5=['location']),

    'QtMacExtras':
        PyQt5Metadata(deps=['QtGui'], qt5=['macextras']),

    'QtMultimedia':
        PyQt5Metadata(deps=['QtGui', 'QtNetwork'], qt5=['multimedia']),

    'QtMultimediaWidgets':
        PyQt5Metadata(deps=['QtMultimedia', 'QtWidgets'],
                qt5=['multimediawidgets', 'multimedia']),

    'QtNetwork':
        PyQt5Metadata(deps=['QtCore'], gui=False, qt5=['network']),

    'QtNfc':
        PyQt5Metadata(deps=['QtCore'], gui=False, qt5=['nfc']),

    'QtOpenGL':
        PyQt5Metadata(deps=['QtWidgets'], qt5=['opengl']),

    'QtPositioning':
        PyQt5Metadata(deps=['QtCore'], gui=False, qt5=['positioning']),

    'QtPrintSupport':
        PyQt5Metadata(deps=['QtWidgets'], qt5=['printsupport']),

    'QtQml':
        PyQt5Metadata(deps=['QtNetwork'], gui=False, qt5=['qml']),

    'QtQuick':
        PyQt5Metadata(deps=['QtGui', 'QtQml'], qt5=['quick']),

    'QtQuickWidgets':
        PyQt5Metadata(deps=['QtQuick', 'QtWidgets'], qt5=['quickwidgets']),

    'QtSensors':
        PyQt5Metadata(deps=['QtCore'], gui=False, qt5=['sensors']),

    'QtSerialPort':
        PyQt5Metadata(deps=['QtCore'], gui=False, qt5=['serialport']),

    'QtSql':
        PyQt5Metadata(deps=['QtWidgets'], qt5=['sql', 'widgets']),

    'QtSvg':
        PyQt5Metadata(deps=['QtWidgets'], qt5=['svg']),

    'QtTest':
        PyQt5Metadata(deps=['QtWidgets'], qt5=['testlib', 'widgets']),

    'QtWebChannel':
        PyQt5Metadata(deps=['QtCore'], gui=False, qt5=['webchannel']),

    'QtWebEngineWidgets':
        PyQt5Metadata(deps=['QtNetwork', 'QtWebChannel', 'QtWidgets'],
                cpp11=True, qt5=['webenginewidgets']),

    'QtWebKit':
        PyQt5Metadata(deps=['QtGui', 'QtNetwork'], qt5=['webkit', 'network']),

    'QtWebKitWidgets':
        PyQt5Metadata(deps=['QtPrintSupport', 'QtWebKit', 'QtWidgets'],
                qt5=['webkitwidgets']),

    'QtWebSockets':
        PyQt5Metadata(deps=['QtNetwork'], gui=False, qt5=['websockets']),

    'QtWidgets':
        PyQt5Metadata(deps=['QtGui'], qt5=['widgets']),

    'QtWinExtras':
        PyQt5Metadata(deps=['QtWidgets'], qt5=['winextras', 'widgets']),

    'QtX11Extras':
        PyQt5Metadata(deps=['QtCore'], qt5=['x11extras']),

    'QtXml':
        PyQt5Metadata(deps=['QtCore'], gui=False, qt5=['xml']),

    'QtXmlPatterns':
        PyQt5Metadata(deps=['QtNetwork'], gui=False,
                qt5=['xmlpatterns', 'network']),

    'Enginio':
        PyQt5Metadata(deps=['QtNetwork'], gui=False, qt5=['enginio']),

    'uic':
        PyQt5Metadata(deps=['QtWidgets']),

    '_QOpenGLFunctions_2_0':
        PyQt5Metadata(group='opengl', deps=['QtGui']),

    '_QOpenGLFunctions_2_1':
        PyQt5Metadata(group='opengl', deps=['QtGui']),

    '_QOpenGLFunctions_4_1_Core':
        PyQt5Metadata(group='opengl', deps=['QtGui']),

    '_QOpenGLFunctions_ES2':
        PyQt5Metadata(group='opengl', deps=['QtGui']),

    'QtChart':
        PyQt5Metadata(group='addon', deps=['QtWidgets'],
                config5=['qtcommercialchart']),

    'QtDataVisualization':
        PyQt5Metadata(group='addon', deps=['QtGui'],
                qt5=['datavisualization']),

    'QtPurchasing':
        PyQt5Metadata(group='addon', deps=['QtCore'], qt5=['purchasing']),

    'Qsci':
        PyQt5Metadata(group='addon', deps=['QtWidgets'],
                config5=['qscintilla2']),
}
