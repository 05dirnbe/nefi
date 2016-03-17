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


__all__ = ['ExtensionModule', 'get_python_metadata', 'PLATFORM_SCOPES']


# The diffent qmake platform scopes and their corresponding descriptive names
# and sub-scopes.
PLATFORM_SCOPES = (('android', "Android", ()), ('linux-*', "Linux", ()),
        ('macx', "OS X", ()), ('win32', "Windows", ('win32_x86', 'win32_x64')))


class StdlibModule:
    """ Encapsulate the meta-data for a module in the standard library. """

    def __init__(self, internal, scope, deps, hidden_deps, core, builtin, defines, xlib, modules, source, libs, includepath, pyd, dlls):
        """ Initialise the object. """

        # Set if the module is internal.
        self.internal = internal

        # The qmake scope of the module.  If specified then it is automatically
        # applied to any unscoped values.  Note that the code assumes that this
        # will be an empty string, a single scope or the logical-not of a
        # single scope.
        self.scope = scope

        # The sequence of modules that this one is dependent on.
        self.deps = (deps, ) if isinstance(deps, str) else deps

        # The sequence of additional modules that this one is dependent on.
        # These dependencies are hidden from the user and (most importantly)
        # further sub-dependencies are ignored.  The use case is the warnings
        # module in Python v3 which is a dependency of the core (for a simple
        # function that should never be called) but drags in a lot of other
        # stuff.
        self.hidden_deps = (hidden_deps, ) if isinstance(hidden_deps, str) else hidden_deps

        # Set if the module is always compiled in to the interpreter library
        # (if it is an extension module) or if it is required (if it is a
        # Python module).
        self.core = core

        # Set if the module is a core Python module that is embedded as a
        # builtin.
        self.builtin = builtin

        # The sequence of (possibly scoped) DEFINES to add to the .pro file.
        self.defines = (defines, ) if isinstance(defines, str) else defines

        # The internal identifier of a required external library.
        self.xlib = xlib

        # The sequence of modules or sub-packages if this is a package,
        # otherwise None.
        self.modules = (modules, ) if isinstance(modules, str) else modules

        # The sequence of (possibly scoped) source files relative to the
        # Modules directory if this is an extension module, otherwise None.
        self.source = (source, ) if isinstance(source, str) else source

        # The sequence of (possibly scoped) LIBS to add to the .pro file.
        self.libs = (libs, ) if isinstance(libs, str) else libs

        # The sequence of (possibly scoped) directories relative to the Modules
        # directory to add to INCLUDEPATH.
        self.includepath = (includepath, ) if isinstance(includepath, str) else includepath

        # Set if the extension modules is implemented as a .pyd file included
        # in the Windows installer from python.org.
        self.pyd = pyd

        # The sequence of additional DLLs needed by the extension module and
        # included in the Windows installer from python.org.
        self.dlls = (dlls, ) if isinstance(dlls, str) else dlls


class VersionedModule:
    """ Encapsulate the meta-data common to all types of module. """

    def __init__(self, min_version=None, version=None, max_version=None, internal=False, scope='', deps=(), hidden_deps=(), core=False, builtin=False, defines=None, xlib=None, modules=None, source=None, libs=None, includepath=None, pyd=None, dlls=None):
        """ Initialise the object. """

        # A meta-datum is uniquely identified by a range of version numbers.  A
        # version number is a 3-tuple of major, minor and patch number.  It is
        # an error if version numbers for a particular module overlaps.
        if version is None:
            if min_version is None:
                min_version = 2

            if max_version is None:
                max_version = 3
        else:
            min_version = max_version = version

        self.min_version = self._expand_version(min_version, 0)
        self.max_version = self._expand_version(max_version, 255)

        self.module = StdlibModule(internal, scope, deps, hidden_deps, core,
                builtin, defines, xlib, modules, source, libs, includepath,
                pyd, dlls)

    @staticmethod
    def _expand_version(version, default):
        """ Ensure a version number is a 3-tuple. """

        if not isinstance(version, tuple):
            version = (version, )

        default = (default, )

        while len(version) < 3:
            version += default

        return version


class ExtensionModule(VersionedModule):
    """ Encapsulate the meta-data for a single extension module. """

    def __init__(self, source, libs=None, includepath=None, min_version=None, version=None, max_version=None, internal=False, scope='', deps=(), hidden_deps=(), core=False, defines=None, xlib=None, pyd=None, dlls=None):
        """ Initialise the object. """

        super().__init__(min_version=min_version, version=version,
                max_version=max_version, internal=internal, scope=scope,
                deps=deps, hidden_deps=hidden_deps, core=core, defines=defines,
                xlib=xlib, source=source, libs=libs, includepath=includepath,
                pyd=pyd, dlls=dlls)


class CoreExtensionModule(ExtensionModule):
    """ Encapsulate the meta-data for an extension module that is always
    compiled in to the interpreter library.
    """

    def __init__(self, min_version=None, version=None, max_version=None, internal=False, scope='', deps=(), hidden_deps=()):
        """ Initialise the object. """

        super().__init__(source=(), min_version=min_version, version=version,
                max_version=max_version, internal=internal, scope=scope,
                deps=deps, hidden_deps=hidden_deps, core=True)


class PythonModule(VersionedModule):
    """ Encapsulate the meta-data for a single Python module. """

    def __init__(self, min_version=None, version=None, max_version=None, internal=False, scope='', deps=(), hidden_deps=(), core=False, builtin=False, modules=None):
        """ Initialise the object. """

        super().__init__(min_version=min_version, version=version,
                max_version=max_version, internal=internal, scope=scope,
                deps=deps, hidden_deps=hidden_deps, core=core, builtin=builtin,
                modules=modules)


class CorePythonModule(PythonModule):
    """ Encapsulate the meta-data for a Python module that is always required
    by an application.
    """

    def __init__(self, min_version=None, version=None, max_version=None, internal=False, scope='', deps=(), hidden_deps=(), builtin=False, modules=None):
        """ Initialise the object. """

        super().__init__(min_version=min_version, version=version,
                max_version=max_version, internal=internal, scope=scope,
                deps=deps, hidden_deps=hidden_deps, core=True, builtin=builtin,
                modules=modules)


class CodecModule(PythonModule):
    """ Encapsulate the meta-data for a Python module that implements a codec
    in the encodings package.
    """

    def __init__(self, min_version=None, version=None, max_version=None, scope='', deps=(), core=False):
        """ Initialise the object. """

        if isinstance(deps, str):
            deps = (deps, )

        all_deps = ('encodings', 'codecs') + deps

        super().__init__(min_version=min_version, version=version,
                max_version=max_version, scope=scope, deps=all_deps, core=core)


# The meta-data for each module.
_metadata = {
    # These are the public modules.

    '__future__':
        PythonModule(),

    '_thread':
        CoreExtensionModule(version=3),

    'abc': (
        PythonModule(version=2, deps=('types', '_weakrefset')),
        PythonModule(version=3, deps='_weakrefset')),

    'aifc': (
        PythonModule(version=2,
                deps=('audioop', 'chunk', 'cl', 'math', 'struct')),
        PythonModule(version=(3, 3),
                deps=('audioop', 'chunk', 'math', 'struct', 'warnings')),
        PythonModule(min_version=(3, 4),
                deps=('audioop', 'chunk', 'collections', 'math', 'struct',
                        'warnings'))),

    'anydbm':
        PythonModule(version=2, deps='whichdb'),

    'argparse': (
        PythonModule(version=2,
                deps=('collections', 'copy', 'gettext', 'os', 're', 'textwrap',
                        'warnings')),
        PythonModule(min_version=(3, 3),
                deps=('collections', 'copy', 'gettext', 'os', 're',
                        'textwrap'))),

    'array':
        ExtensionModule(source='arraymodule.c'),

    'ast':
        PythonModule(deps=('_ast', 'collections', 'inspect')),

    'asynchat': (
        PythonModule(max_version=(2, 7, 8),
                deps=('asyncore', 'collections', 'socket', 'warnings')),
        PythonModule(min_version=(2, 7, 9), max_version=2,
                deps=('asyncore', 'collections', 'errno', 'socket',
                        'warnings')),
        PythonModule(version=(3, 3),
                deps=('asyncore', 'collections', 'socket')),
        PythonModule(version=(3, 4), deps=('asyncore', 'collections')),
        PythonModule(min_version=(3, 5),
                deps=('asyncore', 'collections', 'warnings'))),

    'asyncore': (
        PythonModule(max_version=(3, 4),
                deps=('errno', 'fcntl', 'os', 'select', 'socket', 'time',
                        'warnings')),
        PythonModule(min_version=(3, 5),
                deps=('errno', 'os', 'select', 'socket', 'time', 'warnings'))),

    'asyncio': (
        PythonModule(min_version=(3, 4, 0), max_version=(3, 4, 1),
                deps=('asyncio.events', 'asyncio.futures', 'asyncio.locks',
                        'asyncio.protocols', 'asyncio.queues',
                        'asyncio.streams', 'asyncio.subprocess',
                        'asyncio.tasks', 'asyncio.transports',
                        'asyncio.unix_events', 'asyncio.windows_events',
                        'selectors')),
        PythonModule(version=(3, 4, 2),
                deps=('asyncio.coroutines', 'asyncio.events',
                        'asyncio.futures', 'asyncio.locks',
                        'asyncio.protocols', 'asyncio.queues',
                        'asyncio.streams', 'asyncio.subprocess',
                        'asyncio.tasks', 'asyncio.transports',
                        'asyncio.unix_events', 'asyncio.windows_events',
                        'selectors')),
        PythonModule(min_version=(3, 4, 3),
                deps=('asyncio.base_events', 'asyncio.coroutines',
                        'asyncio.events', 'asyncio.futures', 'asyncio.locks',
                        'asyncio.protocols', 'asyncio.queues',
                        'asyncio.streams', 'asyncio.subprocess',
                        'asyncio.tasks', 'asyncio.transports',
                        'asyncio.unix_events', 'asyncio.windows_events',
                        'selectors'))),

    'atexit': (
        CorePythonModule(version=2),
        ExtensionModule(version=(3, 3), source='atexitmodule.c'),
        CoreExtensionModule(min_version=(3, 4))),

    'audioop':
        ExtensionModule(source='audioop.c'),

    'base64': (
        PythonModule(max_version=(2, 7, 10),
                deps=('binascii', 're', 'struct')),
        PythonModule(min_version=(2, 7, 11), max_version=2,
                deps=('binascii', 're', 'string', 'struct')),
        PythonModule(version=3,
                deps=('binascii', 're', 'struct', 'warnings'))),

    'BaseHTTPServer':
        PythonModule(version=2,
                deps=('mimetools', 'socket', 'SocketServer', 'time',
                        'warnings')),

    'bdb': (
        PythonModule(version=2,
                deps=('fnmatch', 'linecache', 'os', 'repr', 'types')),
        PythonModule(version=(3, 3),
                deps=('fnmatch', 'linecache', 'os', 'reprlib')),
        PythonModule(min_version=(3, 4),
                deps=('fnmatch', 'inspect', 'linecache', 'os', 'reprlib'))),

    'binascii':
        ExtensionModule(source='binascii.c'),

    'binhex': (
        PythonModule(version=2, deps=('binascii', 'os', 'struct')),
        PythonModule(version=3, deps=('binascii', 'io', 'os', 'struct'))),

    'bisect':
        PythonModule(deps='_bisect'),

    'bsddb':
        PythonModule(version=2,
                deps=('bsddb.dbutils', '_bsddb', 'collections', 'os', 'thread',
                        'warnings', 'weakref')),

    'bz2': (
        ExtensionModule(version=2, source='bz2module.c', xlib='bz2',
                pyd='bz2.pyd'),
        PythonModule(min_version=3, max_version=(3, 4),
                deps=('_thread', '_bz2', 'io', 'warnings')),
        PythonModule(min_version=(3, 5),
                deps=('_compression', '_thread', '_bz2', 'io', 'warnings'))),

    'calendar':
        PythonModule(deps=('datetime', 'locale')),

    'cgi': (
        PythonModule(version=2,
                deps=('cStringIO', 'mimetools', 'operator', 'os', 're',
                        'rfc822', 'tempfile', 'traceback', 'urlparse',
                        'UserDict', 'warnings')),
        PythonModule(version=3,
                deps=('collections', 'email.message', 'email.parser', 'html',
                        'http.client', 'io', 'locale', 'os', 're', 'tempfile',
                        'traceback', 'urllib.parse', 'warnings'))),

    'CGIHTTPServer':
        PythonModule(version=2,
                deps=('base64', 'BaseHTTPServer', 'binascii', 'copy', 'os',
                        'pwd', 'select', 'SimpleHTTPServer', 'subprocess',
                        'urllib')),

    'cgitb': (
        PythonModule(version=2,
                deps=('inspect', 'keyword', 'linecache', 'os', 'pydoc',
                        'tempfile', 'time', 'tokenize', 'traceback', 'types')),
        PythonModule(version=3,
                deps=('inspect', 'keyword', 'linecache', 'os', 'pydoc',
                        'tempfile', 'time', 'tokenize', 'traceback'))),

    'chunk':
        PythonModule(deps='struct'),

    'cmath':
        ExtensionModule(source=('cmathmodule.c', '_math.c'),
                libs='linux-*#-lm'),

    'cmd':
        PythonModule(deps='string'),

    'code': (
        PythonModule(max_version=(3, 4), deps=('codeop', 'traceback')),
        PythonModule(min_version=(3, 5),
                deps=('argparse', 'codeop', 'traceback'))),

    'codecs':
        PythonModule(deps='_codecs'),

    'codeop':
        PythonModule(deps='__future__'),

    'collections': (
        PythonModule(version=2,
                deps=('_abcoll', '_collections', 'heapq', 'itertools',
                        'keyword', 'operator', 'thread')),
        PythonModule(version=(3, 3),
                deps=('collections.abc', '_collections', 'copy', 'heapq',
                        'itertools', 'keyword', 'operator', 'reprlib',
                        'weakref'),
                modules='collections.abc'),
        PythonModule(min_version=(3, 4), max_version=(3, 4, 3),
                deps=('_collections', '_collections_abc', 'copy', 'heapq',
                        'itertools', 'keyword', 'operator', 'reprlib',
                        '_weakref'),
                modules='collections.abc'),
        PythonModule(min_version=(3, 4, 4), max_version=(3, 4),
                deps=('_collections', '_collections_abc', 'copy', 'heapq',
                        'itertools', 'keyword', 'operator', 'reprlib',
                        'warnings', '_weakref'),
                modules='collections.abc'),
        PythonModule(version=(3, 5, 0),
                deps=('_collections', '_collections_abc', 'copy', 'heapq',
                        'itertools', 'keyword', 'operator', 'reprlib',
                        '_weakref'),
                modules='collections.abc'),
        PythonModule(min_version=(3, 5, 1),
                deps=('_collections', '_collections_abc', 'copy', 'heapq',
                        'itertools', 'keyword', 'operator', 'reprlib',
                        'warnings', '_weakref'),
                modules='collections.abc')),

    'collections.abc': (
        PythonModule(version=(3, 3), deps='abc'),
        PythonModule(min_version=(3, 4), deps='_collections_abc')),

    'colorsys':
        PythonModule(),

    'commands':
        PythonModule(version=2, scope='!win32', deps=('os', 'warnings')),

    'compileall': (
        PythonModule(version=2, deps=('imp', 'os', 'py_compile', 'struct')),
        PythonModule(version=(3, 3),
                deps=('errno', 'imp', 'os', 'py_compile', 'struct')),
        PythonModule(version=(3, 4),
                deps=('importlib.util', 'os', 'py_compile', 'struct')),
        PythonModule(min_version=(3, 5),
                deps=('concurrent.futures', 'functools', 'importlib.util',
                        'os', 'py_compile', 'struct'))),

    'concurrent':
        PythonModule(version=3, modules='concurrent.futures'),

    'concurrent.futures':
        PythonModule(version=3,
                deps=('concurrent', 'concurrent.futures._base',
                        'concurrent.futures.process',
                        'concurrent.futures.thread')),

    'ConfigParser':
        PythonModule(version=2, deps=('collections', 're', 'UserDict')),

    'configparser':
        PythonModule(version=3,
                deps=('collections', 'collections.abc', 'functools', 'io',
                        'itertools', 're', 'warnings')),

    'contextlib': (
        PythonModule(version=2, deps=('functools', 'warnings')),
        PythonModule(version=3, deps=('collections', 'functools'))),

    'Cookie':
        PythonModule(version=2,
                deps=('cPickle', 're', 'string', 'time', 'warnings')),

    'cookielib':
        PythonModule(version=2,
                deps=('calendar', 'copy', 'httplib', '_LWPCookieJar',
                        '_MozillaCookieJar', 're', 'threading', 'time',
                        'urllib', 'urlparse')),

    'copy': (
        PythonModule(version=2, deps=('copy_reg', 'types', 'weakref')),
        PythonModule(version=3, deps=('copyreg', 'types', 'weakref'))),

    'copy_reg':
        PythonModule(version=2, deps='types'),

    'copyreg':
        PythonModule(version=3),

    'cPickle':
        ExtensionModule(version=2, source='cPickle.c'),

    'cProfile': (
        PythonModule(max_version=(3, 3),
                deps=('_lsprof', 'marshal', 'pstats')),
        PythonModule(min_version=(3, 4),
                deps=('_lsprof', 'marshal', 'profile', 'pstats'))),

    'crypt': (
        ExtensionModule(version=2, scope='!win32', source='cryptmodule.c'),
        PythonModule(version=3, scope='!win32',
                deps=('collections', '_crypt', 'random', 'string'))),

    'cStringIO':
        ExtensionModule(version=2, source='cStringIO.c'),

    'csv': (
        PythonModule(version=2, deps=('cStringIO', '_csv', 'functools', 're')),
        PythonModule(version=3, deps=('_csv', 'io', 're'))),

    'ctypes':
        PythonModule(deps=('_ctypes', 'ctypes._endian', 'os', 'struct'),
                modules=('ctypes.util', 'ctypes.wintypes')),

    'ctypes.util': (
        PythonModule(version=2,
                deps=('ctypes', 'ctypes.macholib.dyld', 'errno', 'imp', 'os',
                        're', 'struct', 'tempfile')),
        PythonModule(version=(3, 3),
                deps=('ctypes', 'contextlib', 'ctypes.macholib.dyld', 'errno',
                        'importlib.machinery', 'os', 're', 'struct',
                        'subprocess', 'tempfile')),
        PythonModule(min_version=(3, 4),
                deps=('ctypes', 'contextlib', 'ctypes.macholib.dyld',
                        'importlib.machinery', 'os', 're', 'struct',
                        'subprocess', 'tempfile'))),

    'ctypes.wintypes':
        PythonModule(deps='ctypes', scope='win32'),

    'curses': (
        PythonModule(version=2, scope='!win32',
                deps=('curses.has_key', 'curses.wrapper', '_curses', 'os'),
                modules=('curses.ascii', 'curses.panel', 'curses.textpad')),
        PythonModule(version=3, scope='!win32',
                deps=('curses.has_key', '_curses', 'os'),
                modules=('curses.ascii', 'curses.panel', 'curses.textpad'))),

    'curses.ascii':
        PythonModule(scope='!win32', deps='curses'),

    'curses.panel':
        PythonModule(scope='!win32', deps=('curses', '_curses_panel')),

    'curses.textpad':
        PythonModule(scope='!win32', deps=('curses', 'curses.ascii')),

    'datetime': (
        ExtensionModule(version=2, source=('datetimemodule.c', 'timemodule.c'),
                deps='_strptime'),
        PythonModule(version=3,
                deps=('_datetime', 'math', '_strptime', 'time'))),

    'dbhash':
        PythonModule(version=2, deps=('bsddb', 'warnings')),

    'dbm': (
        ExtensionModule(version=2, scope='!win32', source='dbmmodule.c',
                defines='HAVE_NDBM_H', xlib='ndbm'),
        PythonModule(version=3, deps=('io', 'os', 'struct'),
                modules=('dbm.dumb', 'dbm.gnu', 'dbm.ndbm'))),

    'dbm.dumb': (
        PythonModule(min_version=3, max_version=(3, 4, 3),
                deps=('dbm', 'collections', 'io', 'os')),
        PythonModule(min_version=(3, 4, 4),
                deps=('dbm', 'ast', 'collections', 'io', 'os'))),

    'dbm.gnu':
        PythonModule(version=3, scope='!win32', deps=('dbm', '_gdbm')),

    'dbm.ndbm':
        PythonModule(version=3, scope='!win32', deps=('dbm', '_dbm')),

    'decimal': (
        PythonModule(max_version=(2, 7, 8),
                deps=('collections', 'copy', 'itertools', 'locale', 'math',
                        'numbers', 're', 'threading')),
        PythonModule(min_version=(2, 7, 9), max_version=2,
                deps=('collections', 'itertools', 'locale', 'math', 'numbers',
                        're', 'threading')),
        PythonModule(min_version=3, max_version=(3, 4, 0),
                deps=('collections', 'copy', 'itertools', 'locale', 'math',
                        'numbers', 're', 'threading')),
        PythonModule(min_version=(3, 4, 1), max_version=(3, 4),
                deps=('collections', 'itertools', 'locale', 'math', 'numbers',
                        're', 'threading')),
        PythonModule(min_version=(3, 5), deps='_pydecimal')),

    'difflib': (
        PythonModule(version=2,
                deps=('collections', 'functools', 'heapq', 're')),
        PythonModule(version=(3, 3),
                deps=('collections', 'heapq', 're', 'warnings')),
        PythonModule(min_version=(3, 4), deps=('collections', 'heapq', 're'))),

    'dis': (
        PythonModule(max_version=(3, 3), deps=('opcode', 'types')),
        PythonModule(min_version=(3, 4),
                deps=('collections', 'io', 'opcode', 'types'))),

    'distutils':
        PythonModule(
                modules=('distutils.archive_util', 'distutils.bcppcompiler',
                        'distutils.ccompiler', 'distutils.cmd',
                        'distutils.command', 'distutils.core',
                        'distutils.cygwincompiler', 'distutils.debug',
                        'distutils.dep_util', 'distutils.dir_util',
                        'distutils.dist', 'distutils.errors',
                        'distutils.extension', 'distutils.fancy_getopt',
                        'distutils.file_util', 'distutils.filelist',
                        'distutils.log', 'distutils.msvccompiler',
                        'distutils.spawn', 'distutils.sysconfig',
                        'distutils.text_file', 'distutils.unixccompiler',
                        'distutils.util', 'distutils.version')),

    'distutils.archive_util':
        PythonModule(
                deps=('distutils.dir_util', 'distutils.errors',
                        'distutils.log', 'distutils.spawn',
                        'grp', 'os', 'pwd', 'tarfile', 'warnings', 'zipfile')),

    'distutils.bcppcompiler':
        PythonModule(
                deps=('distutils.ccompiler', 'distutils.dep_util',
                        'distutils.errors', 'distutils.file_util',
                        'distutils.log', 'os')),

    'distutils.ccompiler':
        PythonModule(
                deps=('distutils.debug', 'distutils.dep_util',
                        'distutils.dir_util', 'distutils.errors',
                        'distutils.fancy_getopt', 'distutils.file_util',
                        'distutils.log', 'distutils.spawn',
                        'distutils.sysconfig', 'distutils.util', 'os', 're',
                        'tempfile')),

    'distutils.cmd':
        PythonModule(
                deps=('distutils.archive_util', 'distutils.debug',
                        'distutils.dep_util', 'distutils.dir_util',
                        'distutils.dist', 'distutils.errors',
                        'distutils.fancy_getopt', 'distutils.file_util',
                        'distutils.log', 'distutils.spawn', 'distutils.util',
                        'os', 're')),

    'distutils.command':
        PythonModule(
                modules=('distutils.command.bdist',
                        'distutils.command.bdist_dumb',
                        'distutils.command.bdist_msi',
                        'distutils.command.bdist_rpm',
                        'distutils.command.bdist_wininst',
                        'distutils.command.build',
                        'distutils.command.build_clib',
                        'distutils.command.build_ext',
                        'distutils.command.build_py',
                        'distutils.command.build_scripts',
                        'distutils.command.check', 'distutils.command.clean',
                        'distutils.command.config',
                        'distutils.command.install',
                        'distutils.command.install_data',
                        'distutils.command.install_egg_info',
                        'distutils.command.install_headers',
                        'distutils.command.install_lib',
                        'distutils.command.install_scripts',
                        'distutils.command.register',
                        'distutils.command.sdist',
                        'distutils.command.upload')),

    'distutils.command.bdist':
        PythonModule(
                deps=('distutils.core', 'distutils.errors',
                        'distutils.fancy_getopt', 'distutils.util', 'os')),

    'distutils.command.bdist_dumb': (
        PythonModule(version=2,
                deps=('distutils.core', 'distutils.dir_util',
                        'distutils.errors', 'distutils.log', 'distutils.util',
                        'os', 'sysconfig')),
        PythonModule(version=3,
                deps=('distutils.core', 'distutils.dir_util',
                        'distutils.errors', 'distutils.log',
                        'distutils.sysconfig', 'distutils.util', 'os'))),

    'distutils.command.bdist_msi': (
        PythonModule(version=2,
                deps=('distutils.core', 'distutils.dir_util',
                        'distutils.errors', 'distutils.log', 'distutils.util',
                        'distutils.version', 'msilib', 'os', 'sysconfig')),
        PythonModule(version=3,
                deps=('distutils.core', 'distutils.dir_util',
                        'distutils.errors', 'distutils.log',
                        'distutils.sysconfig', 'distutils.util',
                        'distutils.version', 'msilib', 'os'))),

    'distutils.command.bdist_rpm': (
        PythonModule(version=2,
                deps=('distutils.core', 'distutils.debug', 'distutils.errors',
                        'distutils.file_util', 'distutils.log',
                        'distutils.sysconfig', 'os', 'string')),
        PythonModule(version=3,
                deps=('distutils.core', 'distutils.debug', 'distutils.errors',
                        'distutils.file_util', 'distutils.log',
                        'distutils.sysconfig', 'distutils.util', 'os',
                        'subprocess'))),

    'distutils.command.bdist_wininst': (
        PythonModule(version=2,
                deps=('distutils.core', 'distutils.dir_util',
                        'distutils.errors', 'distutils.log',
                        'distutils.msvccompiler', 'distutils.util', 'os',
                        'string', 'struct', 'sysconfig', 'tempfile', 'time')),
        PythonModule(min_version=3, max_version=(3, 4),
                deps=('distutils.core', 'distutils.dir_util',
                        'distutils.errors', 'distutils.log',
                        'distutils.msvccompiler', 'distutils.sysconfig',
                        'distutils.util', 'os', 'struct', 'tempfile',
                        'time')),
        PythonModule(min_version=(3, 5),
                deps=('distutils.core', 'distutils.dir_util',
                        'distutils.errors', 'distutils.log',
                        'distutils.sysconfig', 'distutils.util', 'msvcrt',
                        'os', 'struct', 'tempfile', 'time'))),

    'distutils.command.build':
        PythonModule(
                deps=('distutils.ccompiler', 'distutils.core',
                        'distutils.errors', 'distutils.util', 'os')),

    'distutils.command.build_clib':
        PythonModule(
                deps=('distutils.ccompiler', 'distutils.core',
                        'distutils.errors', 'distutils.log',
                        'distutils.sysconfig', 'os')),

    'distutils.command.build_ext': (
        PythonModule(version=2,
                deps=('distutils.ccompiler', 'distutils.core',
                        'distutils.dep_util', 'distutils.errors',
                        'distutils.extension', 'distutils.log',
                        'distutils.msvccompiler', 'distutils.sysconfig',
                        'distutils.util', 'os', 're', 'string', 'types')),
        PythonModule(min_version=3, max_version=(3, 4),
                deps=('distutils.ccompiler', 'distutils.core',
                        'distutils.dep_util', 'distutils.errors',
                        'distutils.extension', 'distutils.log',
                        'distutils.msvccompiler', 'distutils.sysconfig',
                        'distutils.util', 'os', 're')),
        PythonModule(min_version=(3, 5),
                deps=('concurrent.futures', 'contextlib',
                        'distutils.ccompiler', 'distutils.core',
                        'distutils.dep_util', 'distutils.errors',
                        'distutils.extension', 'distutils.log',
                        'distutils._msvccompiler', 'distutils.sysconfig',
                        'distutils.util', 'os', 're'))),

    'distutils.command.build_py': (
        PythonModule(version=2,
                deps=('distutils.core', 'distutils.errors', 'distutils.log',
                        'distutils.util', 'glob', 'os')),
        PythonModule(version=3,
                deps=('distutils.core', 'distutils.errors', 'distutils.log',
                        'distutils.util', 'glob', 'importlib.util', 'os'))),

    'distutils.command.build_scripts': (
        PythonModule(version=2,
                deps=('distutils.core', 'distutils.dep_util', 'distutils.log',
                        'distutils.util', 'os', 're', 'stat', 'sysconfig')),
        PythonModule(version=3,
                deps=('distutils.core', 'distutils.dep_util', 'distutils.log',
                        'distutils.sysconfig', 'distutils.util', 'os', 're',
                        'stat', 'tokenize'))),

    'distutils.command.check': (
        PythonModule(version=2,
                deps=('distutils.core', 'distutils.dist', 'distutils.errors')),
        PythonModule(version=3, deps=('distutils.core', 'distutils.errors'))),

    'distutils.command.clean':
        PythonModule(
                deps=('distutils.core', 'distutils.dir_util', 'distutils.log',
                        'os')),

    'distutils.command.config':
        PythonModule(
                deps=('distutils.ccompiler', 'distutils.core',
                        'distutils.errors', 'distutils.log',
                        'distutils.sysconfig', 'os', 're')),

    'distutils.command.install': (
        PythonModule(version=2,
                deps=('distutils.core', 'distutils.debug', 'distutils.errors',
                        'distutils.fancy_getopt', 'distutils.file_util',
                        'distutils.log', 'distutils.sysconfig',
                        'distutils.util', 'os', 'pprint', 'string', 'types')),
        PythonModule(version=3,
                deps=('distutils.core', 'distutils.debug', 'distutils.errors',
                        'distutils.fancy_getopt', 'distutils.file_util',
                        'distutils.log', 'distutils.sysconfig',
                        'distutils.util', 'os', 'pprint'))),

    'distutils.command.install_data':
        PythonModule(deps=('distutils.core', 'distutils.util', 'os')),

    'distutils.command.install_egg_info':
        PythonModule(
                deps=('distutils.cmd', 'distutils.dir_util', 'distutils.log',
                        'os', 're')),

    'distutils.command.install_headers':
        PythonModule(deps='distutils.core'),

    'distutils.command.install_lib': (
        PythonModule(version=2,
                deps=('distutils.core', 'distutils.errors', 'distutils.util',
                        'os')),
        PythonModule(version=3,
                deps=('distutils.core', 'distutils.errors', 'distutils.util',
                        'importlib.util', 'os'))),

    'distutils.command.install_scripts':
        PythonModule(deps=('distutils.core', 'distutils.log', 'os', 'stat')),

    'distutils.command.register': (
        PythonModule(version=2,
                deps=('distutils.core', 'distutils.log', 'getpass', 'urllib2',
                        'urlparse', 'warnings')),
        PythonModule(version=3,
                deps=('distutils.core', 'distutils.errors', 'distutils.log',
                        'getpass', 'io', 'os', 'string', 'urllib.parse',
                        'urllib.request', 'warnings'))),

    'distutils.command.sdist': (
        PythonModule(version=2,
                deps=('distutils.archive_util', 'distutils.core',
                        'distutils.dep_util', 'distutils.dir_util',
                        'distutils.errors', 'distutils.fancy_getopt',
                        'distutils.file_util', 'distutils.filelist',
                        'distutils.log', 'distutils.text_file',
                        'distutils.util', 'glob', 'os', 'string', 'warnings')),
        PythonModule(version=3,
                deps=('distutils.archive_util', 'distutils.core',
                        'distutils.dep_util', 'distutils.dir_util',
                        'distutils.errors', 'distutils.fancy_getopt',
                        'distutils.file_util', 'distutils.filelist',
                        'distutils.log', 'distutils.text_file',
                        'distutils.util', 'glob', 'os', 'string', 'types',
                        'warnings'))),

    'distutils.command.upload': (
        PythonModule(version=2,
                deps=('base64', 'cStringIO', 'distutils.core',
                        'distutils.errors', 'distutils.log', 'distutils.spawn',
                        'hashlib', 'os', 'platform', 'socket', 'urllib2',
                        'urlparse')),
        PythonModule(min_version=3, max_version=(3, 4),
                deps=('base64', 'distutils.core', 'distutils.errors',
                        'distutils.log', 'distutils.spawn', 'hashlib', 'io',
                        'os', 'platform', 'socket', 'urllib.parse',
                        'urllib.request')),
        PythonModule(min_version=(3, 5),
                deps=('base64', 'distutils.core', 'distutils.errors',
                        'distutils.log', 'distutils.spawn', 'hashlib', 'io',
                        'os', 'platform', 'urllib.parse', 'urllib.request'))),

    'distutils.core':
        PythonModule(
                deps=('distutils.cmd', 'distutils.config', 'distutils.debug',
                        'distutils.dist', 'distutils.errors',
                        'distutils.extension', 'os')),

    'distutils.cygwincompiler': (
        PythonModule(version=2,
                deps=('copy', 'distutils.ccompiler', 'distutils.errors',
                        'distutils.file_util', 'distutils.log',
                        'distutils.spawn', 'distutils.sysconfig',
                        'distutils.unixccompiler', 'distutils.version', 'os',
                        're', 'string')),
        PythonModule(version=3,
                deps=('copy', 'distutils.ccompiler', 'distutils.errors',
                        'distutils.file_util', 'distutils.log',
                        'distutils.spawn', 'distutils.sysconfig',
                        'distutils.unixccompiler', 'distutils.version', 'os',
                        're', 'subprocess'))),

    'distutils.debug':
        PythonModule(deps='os'),

    'distutils.dep_util':
        PythonModule(deps=('distutils.errors', 'os', 'stat')),

    'distutils.dir_util':
        PythonModule(deps=('distutils.errors', 'distutils.file_util',
                'distutils.log', 'errno', 'os')),

    'distutils.dist': (
        PythonModule(version=2,
                deps=('ConfigParser', 'distutils.cmd', 'distutils.command',
                        'distutils.core', 'distutils.debug',
                        'distutils.errors', 'distutils.fancy_getopt',
                        'distutils.log', 'distutils.util',
                        'distutils.versionpredicate', 'email', 'os', 'pprint',
                        're', 'warnings')),
        PythonModule(version=3,
                deps=('configparser', 'distutils.cmd', 'distutils.command',
                        'distutils.core', 'distutils.debug',
                        'distutils.errors', 'distutils.fancy_getopt',
                        'distutils.log', 'distutils.util',
                        'distutils.versionpredicate', 'email', 'os', 'pprint',
                        're', 'warnings'))),

    'distutils.errors':
        PythonModule(),

    'distutils.extension': (
        PythonModule(version=2,
                deps=('distutils.sysconfig', 'distutils.text_file',
                        'distutils.util', 'os', 'string', 'types',
                        'warnings')),
        PythonModule(version=3,
                deps=('distutils.sysconfig', 'distutils.text_file',
                        'distutils.util', 'os', 'warnings'))),

    'distutils.fancy_getopt':
        PythonModule(
                deps=('distutils.errors', 'getopt', 're', 'string')),

    'distutils.file_util':
        PythonModule(
                deps=('distutils.dep_util', 'distutils.errors',
                        'distutils.log', 'errno', 'os', 'stat')),

    'distutils.filelist':
        PythonModule(
                deps=('distutils.debug', 'distutils.errors', 'distutils.log',
                        'distutils.util', 'fnmatch', 'os', 're', 'stat')),

    'distutils.log':
        PythonModule(),

    'distutils.msvccompiler': (
        PythonModule(version=2,
                deps=('distutils.ccompiler', 'distutils.errors',
                        'distutils.log', 'distutils.msvc9compiler', 'os',
                        'string', '_winreg')),
        PythonModule(version=3,
                deps=('distutils.ccompiler', 'distutils.errors',
                        'distutils.log', 'distutils.msvc9compiler', 'os',
                        'winreg'))),

    'distutils.spawn': (
        PythonModule(max_version=(3, 4),
                deps=('distutils.debug', 'distutils.errors', 'distutils.log',
                        'distutils.sysconfig', 'errno', 'os')),
        PythonModule(min_version=(3, 5),
                deps=('distutils.debug', 'distutils.errors', 'distutils.log',
                        'distutils.sysconfig', 'os'))),

    'distutils.sysconfig': (
        PythonModule(version=2,
                deps=('distutils.errors', 'distutils.text_file', 'os',
                        '_osx_support', 're', 'string')),
        PythonModule(min_version=3, max_version=(3, 4),
                deps=('distutils.errors', 'distutils.text_file', 'os',
                        '_osx_support', 're', 'warnings')),
        PythonModule(min_version=(3, 5),
                deps=('distutils.errors', 'distutils.text_file', '_imp', 'os',
                        '_osx_support', 're', 'warnings'))),

    'distutils.text_file': (
        PythonModule(version=2),
        PythonModule(version=3, deps=('io', 'os'))),

    'distutils.unixccompiler': (
        PythonModule(version=2,
                deps=('distutils.ccompiler', 'distutils.dep_util',
                        'distutils.errors', 'distutils.log',
                        'distutils.sysconfig', 'os', '_osx_support', 're',
                        'types')),
        PythonModule(version=3,
                deps=('distutils.ccompiler', 'distutils.dep_util',
                        'distutils.errors', 'distutils.log',
                        'distutils.sysconfig', 'os', '_osx_support', 're'))),

    'distutils.util': (
        PythonModule(version=2,
                deps=('distutils.dep_util', 'distutils.errors',
                        'distutils.log', 'distutils.spawn',
                        'distutils.sysconfig', 'os', '_osx_support', 'pwd',
                        'py_compile', 're', 'string', 'tempfile')),
        PythonModule(version=3,
                deps=('distutils.dep_util', 'distutils.errors',
                        'distutils.log', 'distutils.spawn',
                        'distutils.sysconfig', 'importlib.util', 'os',
                        '_osx_support', 'pwd', 'py_compile', 're', 'string',
                        'tempfile'))),

    'distutils.version': (
        PythonModule(version=2, deps=('re', 'string', 'types')),
        PythonModule(version=3, deps='re')),

    'DocXMLRPCServer':
        PythonModule(version=2,
                deps=('inspect', 'pydoc', 're', 'SimpleXMLRPCServer')),

    'dumbdbm': (
        PythonModule(max_version=(2, 7, 9), deps=('os', 'UserDict')),
        PythonModule(min_version=(2, 7, 10), max_version=2,
                deps=('ast', 'os', 'UserDict'))),

    'email': (
        PythonModule(version=2, deps=('email.mime', 'email.parser'),
                modules=('email.charset', 'email.encoders', 'email.errors',
                        'email.generator', 'email.header', 'email.iterators',
                        'email.message', 'email.mime', 'email.parser',
                        'email.utils')),
        PythonModule(version=(3, 3), deps='email.parser',
                modules=('email.charset', 'email.encoders', 'email.errors',
                        'email.generator', 'email.header',
                        'email.headerregistry', 'email.iterators',
                        'email.message', 'email.mime', 'email.parser',
                        'email.policy', 'email.utils')),
        PythonModule(min_version=(3, 4), deps='email.parser',
                modules=('email.charset', 'email.contentmanager',
                        'email.encoders', 'email.errors', 'email.generator',
                        'email.header', 'email.headerregistry',
                        'email.iterators', 'email.message', 'email.mime',
                        'email.parser', 'email.policy', 'email.utils'))),

    'email.charset': (
        PythonModule(version=2,
                deps=('email', 'codecs', 'email.base64mime', 'email.encoders',
                        'email.errors', 'email.quoprimime')),
        PythonModule(version=3,
                deps=('email', 'email.base64mime', 'email.encoders',
                        'email.errors', 'email.quoprimime', 'functools'))),

    'email.contentmanager':
        PythonModule(min_version=(3, 4),
                deps=('email', 'binascii', 'email.charset', 'email.errors',
                        'email.message', 'email.quoprimime')),

    'email.encoders':
        PythonModule(deps=('email', 'base64', 'quopri')),

    'email.errors':
        PythonModule(deps='email'),

    'email.generator': (
        PythonModule(version=2,
                deps=('email', 'cStringIO', 'email.header', 'random', 're',
                        'time', 'warnings')),
        PythonModule(version=(3, 3),
                deps=('email', 'copy', 'email.charset', 'email.header',
                        'email._policybase', 'email.utils', 'io', 'random',
                        're', 'time', 'warnings')),
        PythonModule(min_version=(3, 4),
                deps=('email', 'copy', 'email.utils', 'io', 'random', 're',
                        'time'))),

    'email.header':
        PythonModule(
                deps=('email', 'binascii', 'email.base64mime', 'email.charset',
                        'email.errors', 'email.quoprimime', 're')),

    'email.headerregistry': (
        PythonModule(min_version=3, max_version=(3, 4, 2),
                deps=('email', 'email.errors', 'email._header_value_parser',
                        'email.utils')),
        PythonModule(min_version=(3, 4, 3),
                deps=('email', 'email.errors', 'email._header_value_parser',
                        'email.utils', 'types'))),

    'email.iterators': (
        PythonModule(version=2, deps=('email', 'cStringIO')),
        PythonModule(version=3, deps=('email', 'io'))),

    'email.message': (
        PythonModule(version=2,
                deps=('email', 'binascii', 'cStringIO', 'email.charset',
                        'email.errors', 'email.generator', 'email.iterators',
                        'email.utils', 're', 'uu', 'warnings')),
        PythonModule(version=(3, 3),
                deps=('email', 'base64', 'binascii', 'email.charset',
                        'email._encoded_words', 'email.errors',
                        'email.generator', 'email.iterators',
                        'email._policybase', 'email.utils', 'io', 're', 'uu')),
        PythonModule(min_version=(3, 4, 0), max_version=(3, 4, 1),
                deps=('email', 'email.charset', 'email._encoded_words',
                        'email.errors', 'email.generator', 'email.iterators',
                        'email.policy', 'email._policybase', 'email.utils',
                        'io', 'quopri', 're', 'uu')),
        PythonModule(min_version=(3, 4, 2),
                deps=('email', 'email.charset', 'email._encoded_words',
                        'email.errors', 'email.generator', 'email.iterators',
                        'email.policy', 'email._policybase', 'email.utils',
                        'io', 'quopri', 're', 'uu', 'warnings'))),

    'email.mime':
        PythonModule(deps='email',
                modules=('email.mime.application', 'email.mime.audio',
                        'email.mime.base', 'email.mime.image',
                        'email.mime.message', 'email.mime.multipart',
                        'email.mime.nonmultipart', 'email.mime.text')),

    'email.mime.application':
        PythonModule(
                deps=('email.mime', 'email.encoders',
                        'email.mime.nonmultipart')),

    'email.mime.audio': (
        PythonModule(version=2,
                deps=('email.mime', 'cStringIO', 'email.encoders',
                        'email.mime.nonmultipart', 'sndhdr')),
        PythonModule(version=3,
                deps=('email.mime', 'email.encoders',
                        'email.mime.nonmultipart', 'io', 'sndhdr'))),

    'email.mime.base':
        PythonModule(deps=('email.mime', 'email.message')),

    'email.mime.image':
        PythonModule(
                deps=('email.mime', 'email.encoders',
                        'email.mime.nonmultipart', 'imghdr')),

    'email.mime.message':
        PythonModule(
                deps=('email.mime', 'email.message',
                        'email.mime.nonmultipart')),

    'email.mime.multipart':
        PythonModule(deps=('email.mime', 'email.mime.base')),

    'email.mime.nonmultipart':
        PythonModule(deps=('email.mime', 'email.errors', 'email.mime.base')),

    'email.mime.text': (
        PythonModule(max_version=(3, 3),
                deps=('email.mime', 'email.encoders',
                        'email.mime.nonmultipart')),
        PythonModule(version=(3, 4),
                deps=('email.mime', 'email.mime.nonmultipart')),
        PythonModule(min_version=(3, 5),
                deps=('email.mime', 'email.charset',
                        'email.mime.nonmultipart'))),

    'email.parser': (
        PythonModule(version=2,
                deps=('email', 'cStringIO', 'email.feedparser',
                        'email.message', 'warnings')),
        PythonModule(version=(3, 3),
                deps=('email', 'email.feedparser', 'email.message',
                        'email._policybase', 'io', 'warnings')),
        PythonModule(min_version=(3, 4),
                deps=('email', 'email.feedparser', 'email._policybase',
                        'io'))),

    'email.policy': (
        PythonModule(version=(3, 3),
                deps=('email', 'email.headerregistry', 'email._policybase',
                        'email.utils')),
        PythonModule(min_version=(3, 4),
                deps=('email', 'email.contentmanager', 'email.headerregistry',
                        'email._policybase', 'email.utils'))),
    'email.utils': (
        PythonModule(version=2,
                deps=('email', 'base64', 'email.encoders', 'email._parseaddr',
                        'os', 'quopri', 'random', 're', 'socket', 'time',
                        'urllib', 'warnings')),
        PythonModule(version=(3, 3),
                deps=('email', 'base64', 'datetime', 'email.charset',
                        'email.encoders', 'email._parseaddr', 'io', 'os',
                        'quopri', 'random', 're', 'socket', 'time',
                        'urllib.parse', 'warnings')),
        PythonModule(min_version=(3, 4),
                deps=('email', 'datetime', 'email.charset', 'email._parseaddr',
                        'os', 'random', 're', 'socket', 'time',
                        'urllib.parse'))),

    'encodings':
        PythonModule(deps=('codecs', 'encodings.aliases'),
                modules=('encodings.ascii', 'encodings.base64_codec',
                        'encodings.big5', 'encodings.big5hkscs',
                        'encodings.bz2_codec', 'encodings.charmap',
                        'encodings.cp037', 'encodings.cp1006',
                        'encodings.cp1026', 'encodings.cp1125',
                        'encodings.cp1140', 'encodings.cp1250',
                        'encodings.cp1251', 'encodings.cp1252',
                        'encodings.cp1253', 'encodings.cp1254',
                        'encodings.cp1255', 'encodings.cp1256',
                        'encodings.cp1257', 'encodings.cp1258',
                        'encodings.cp273', 'encodings.cp424',
                        'encodings.cp437', 'encodings.cp500',
                        'encodings.cp65001', 'encodings.cp720',
                        'encodings.cp737', 'encodings.cp775',
                        'encodings.cp850', 'encodings.cp852',
                        'encodings.cp855', 'encodings.cp856',
                        'encodings.cp857', 'encodings.cp858',
                        'encodings.cp860', 'encodings.cp861',
                        'encodings.cp862', 'encodings.cp863',
                        'encodings.cp864', 'encodings.cp865',
                        'encodings.cp866', 'encodings.cp869',
                        'encodings.cp874', 'encodings.cp875',
                        'encodings.cp932', 'encodings.cp949',
                        'encodings.cp950', 'encodings.euc_jis_2004',
                        'encodings.euc_jisx0213', 'encodings.euc_jp',
                        'encodings.euc_kr', 'encodings.gb18030',
                        'encodings.gb2312', 'encodings.gbk',
                        'encodings.hex_codec', 'encodings.hp_roman8',
                        'encodings.hz', 'encodings.idna',
                        'encodings.iso2022_jp', 'encodings.iso2022_jp_1',
                        'encodings.iso2022_jp_2', 'encodings.iso2022_jp_2004',
                        'encodings.iso2022_jp_3', 'encodings.iso2022_jp_ext',
                        'encodings.iso2022_jp_kr', 'encodings.iso8859_1',
                        'encodings.iso8859_10', 'encodings.iso8859_11',
                        'encodings.iso8859_13', 'encodings.iso8859_14',
                        'encodings.iso8859_15', 'encodings.iso8859_16',
                        'encodings.iso8859_2', 'encodings.iso8859_3',
                        'encodings.iso8859_4', 'encodings.iso8859_5',
                        'encodings.iso8859_6', 'encodings.iso8859_7',
                        'encodings.iso8859_8', 'encodings.iso8859_9',
                        'encodings.johab', 'encodings.koi8_r',
                        'encodings.koi8_t', 'encodings.koi8_u',
                        'encodings.kz1048', 'encodings.latin_1',
                        'encodings.mac_arabic', 'encodings.mac_centeuro',
                        'encodings.mac_croatian', 'encodings.mac_cyrillic',
                        'encodings.mac_farsi', 'encodings.mac_greek',
                        'encodings.mac_iceland', 'encodings.mac_latin2',
                        'encodings.mac_roman', 'encodings.mac_romanian',
                        'encodings.mac_turkish', 'encodings.mbcs',
                        'encodings.palmos', 'encodings.ptcp154',
                        'encodings.punycode', 'encodings.quopri_codec',
                        'encodings.raw_unicode_escape', 'encodings.rot_13',
                        'encodings.shift_jis', 'encodings.shift_jis_2004',
                        'encodings.shift_jisx0213', 'encodings.tis_620',
                        'encodings.undefined', 'encodings.unicode_escape',
                        'encodings.unicode_internal', 'encodings.utf_16',
                        'encodings.utf_16_be', 'encodings.utf_16_le',
                        'encodings.utf_32', 'encodings.utf_32_be',
                        'encodings.utf_32_le', 'encodings.utf_7',
                        'encodings.utf_8', 'encodings.utf_8_sig',
                        'encodings.uu_codec', 'encodings.zlib_codec')),

    'encodings.ascii': (
        CodecModule(version=2),
        CodecModule(version=3, core=True)),

    'encodings.base64_codec':
        CodecModule(deps='base64'),

    'encodings.big5':
        CodecModule(deps=('_codecs_tw', '_multibytecodec')),

    'encodings.big5hkscs':
        CodecModule(deps=('_codecs_hk', '_multibytecodec')),

    'encodings.bz2_codec':
        CodecModule(deps='bz2'),

    'encodings.charmap':
        CodecModule(),

    'encodings.cp037':
        CodecModule(),

    'encodings.cp1006':
        CodecModule(),

    'encodings.cp1026':
        CodecModule(),

    'encodings.cp1125':
        CodecModule(min_version=(3, 4)),

    'encodings.cp1140':
        CodecModule(),

    'encodings.cp1250':
        CodecModule(),

    'encodings.cp1251':
        CodecModule(),

    'encodings.cp1252':
        CodecModule(),

    'encodings.cp1253':
        CodecModule(),

    'encodings.cp1254':
        CodecModule(),

    'encodings.cp1255':
        CodecModule(),

    'encodings.cp1256':
        CodecModule(),

    'encodings.cp1257':
        CodecModule(),

    'encodings.cp1258':
        CodecModule(),

    'encodings.cp273':
        CodecModule(min_version=(3, 4)),

    'encodings.cp424':
        CodecModule(),

    'encodings.cp437': (
        CodecModule(version=2),
        CodecModule(version=3, core=True)),

    'encodings.cp500':
        CodecModule(),

    'encodings.cp65001':
        CodecModule(version=3),

    'encodings.cp720':
        CodecModule(),

    'encodings.cp737':
        CodecModule(),

    'encodings.cp775':
        CodecModule(),

    'encodings.cp850':
        CodecModule(),

    'encodings.cp852':
        CodecModule(),

    'encodings.cp855':
        CodecModule(),

    'encodings.cp856':
        CodecModule(),

    'encodings.cp857':
        CodecModule(),

    'encodings.cp858':
        CodecModule(),

    'encodings.cp860':
        CodecModule(),

    'encodings.cp861':
        CodecModule(),

    'encodings.cp862':
        CodecModule(),

    'encodings.cp863':
        CodecModule(),

    'encodings.cp864':
        CodecModule(),

    'encodings.cp865':
        CodecModule(),

    'encodings.cp866':
        CodecModule(),

    'encodings.cp869':
        CodecModule(),

    'encodings.cp874':
        CodecModule(),

    'encodings.cp875':
        CodecModule(),

    'encodings.cp932':
        CodecModule(deps=('_codecs_jp', '_multibytecodec')),

    'encodings.cp949':
        CodecModule(deps=('_codecs_kr', '_multibytecodec')),

    'encodings.cp950':
        CodecModule(deps=('_codecs_tw', '_multibytecodec')),

    'encodings.euc_jis_2004':
        CodecModule(deps=('_codecs_jp', '_multibytecodec')),

    'encodings.euc_jisx0213':
        CodecModule(deps=('_codecs_jp', '_multibytecodec')),

    'encodings.euc_jp':
        CodecModule(deps=('_codecs_jp', '_multibytecodec')),

    'encodings.euc_kr':
        CodecModule(deps=('_codecs_kr', '_multibytecodec')),

    'encodings.gb18030':
        CodecModule(deps=('_codecs_cn', '_multibytecodec')),

    'encodings.gb2312':
        CodecModule(deps=('_codecs_cn', '_multibytecodec')),

    'encodings.gbk':
        CodecModule(deps=('_codecs_cn', '_multibytecodec')),

    'encodings.hex_codec':
        CodecModule(deps='binascii'),

    'encodings.hp_roman8':
        CodecModule(),

    'encodings.hz':
        CodecModule(deps=('_codecs_cn', '_multibytecodec')),

    'encodings.idna':
        PythonModule(
                deps=('encodings', 'codecs', 're', 'stringprep',
                        'unicodedata')),

    'encodings.iso2022_jp':
        CodecModule(deps=('_codecs_iso2022', '_multibytecodec')),

    'encodings.iso2022_jp_1':
        CodecModule(deps=('_codecs_iso2022', '_multibytecodec')),

    'encodings.iso2022_jp_2':
        CodecModule(deps=('_codecs_iso2022', '_multibytecodec')),

    'encodings.iso2022_jp_2004':
        CodecModule(deps=('_codecs_iso2022', '_multibytecodec')),

    'encodings.iso2022_jp_3':
        CodecModule(deps=('_codecs_iso2022', '_multibytecodec')),

    'encodings.iso2022_jp_ext':
        CodecModule(deps=('_codecs_iso2022', '_multibytecodec')),

    'encodings.iso2022_jp_kr':
        CodecModule(deps=('_codecs_iso2022', '_multibytecodec')),

    'encodings.iso8859_1':
        CodecModule(),

    'encodings.iso8859_10':
        CodecModule(),

    'encodings.iso8859_11':
        CodecModule(),

    'encodings.iso8859_13':
        CodecModule(),

    'encodings.iso8859_14':
        CodecModule(),

    'encodings.iso8859_15':
        CodecModule(),

    'encodings.iso8859_16':
        CodecModule(),

    'encodings.iso8859_2':
        CodecModule(),

    'encodings.iso8859_3':
        CodecModule(),

    'encodings.iso8859_4':
        CodecModule(),

    'encodings.iso8859_5':
        CodecModule(),

    'encodings.iso8859_6':
        CodecModule(),

    'encodings.iso8859_7':
        CodecModule(),

    'encodings.iso8859_8':
        CodecModule(),

    'encodings.iso8859_9':
        CodecModule(),

    'encodings.johab':
        CodecModule(deps=('_codecs_kr', '_multibytecodec')),

    'encodings.koi8_r':
        CodecModule(),

    'encodings.koi8_t':
        CodecModule(min_version=(3, 5)),

    'encodings.koi8_u':
        CodecModule(),

    'encodings.kz1048':
        CodecModule(min_version=(3, 5)),

    'encodings.latin_1': (
        CodecModule(version=2),
        CodecModule(version=3, core=True)),

    'encodings.mac_arabic':
        CodecModule(),

    'encodings.mac_centeuro':
        CodecModule(),

    'encodings.mac_croatian':
        CodecModule(),

    'encodings.mac_cyrillic':
        CodecModule(),

    'encodings.mac_farsi':
        CodecModule(),

    'encodings.mac_greek':
        CodecModule(),

    'encodings.mac_iceland':
        CodecModule(),

    'encodings.mac_latin2':
        CodecModule(),

    'encodings.mac_roman':
        CodecModule(),

    'encodings.mac_romanian':
        CodecModule(),

    'encodings.mac_turkish':
        CodecModule(),

    'encodings.mbcs': (
        CodecModule(version=2, scope='win32'),
        CodecModule(version=3, scope='win32', core=True)),

    'encodings.palmos':
        CodecModule(),

    'encodings.ptcp154':
        CodecModule(),

    'encodings.punycode':
        CodecModule(),

    'encodings.quopri_codec': (
        CodecModule(version=2, deps=('cStringIO', 'quopri')),
        CodecModule(version=3, deps=('io', 'quopri'))),

    'encodings.raw_unicode_escape':
        CodecModule(),

    'encodings.rot_13':
        CodecModule(),

    'encodings.shift_jis':
        CodecModule(deps=('_codecs_jp', '_multibytecodec')),

    'encodings.shift_jis_2004':
        CodecModule(deps=('_codecs_jp', '_multibytecodec')),

    'encodings.shift_jisx0213':
        CodecModule(deps=('_codecs_jp', '_multibytecodec')),

    'encodings.tis_620':
        CodecModule(),

    'encodings.undefined':
        CodecModule(),

    'encodings.unicode_escape':
        CodecModule(),

    'encodings.unicode_internal':
        CodecModule(),

    'encodings.utf_16':
        CodecModule(),

    'encodings.utf_16_be':
        CodecModule(),

    'encodings.utf_16_le':
        CodecModule(),

    'encodings.utf_32':
        CodecModule(),

    'encodings.utf_32_be':
        CodecModule(),

    'encodings.utf_32_le':
        CodecModule(),

    'encodings.utf_7':
        CodecModule(),

    'encodings.utf_8': (
        CodecModule(version=2),
        CodecModule(version=3, core=True)),

    'encodings.utf_8_sig':
        CodecModule(),

    'encodings.uu_codec': (
        CodecModule(version=2, deps=('binascii', 'cStringIO')),
        CodecModule(version=3, deps=('binascii', 'io'))),

    'encodings.zlib_codec':
        CodecModule(deps='zlib'),

    'enum':
        PythonModule(version=3, deps=('collections', 'types')),

    'errno':
        CoreExtensionModule(),

    'exceptions':
        CoreExtensionModule(version=2),

    'faulthandler':
        CoreExtensionModule(version=3),

    'fcntl':
        ExtensionModule(scope='!win32', source='fcntlmodule.c'),

    'filecmp':
        PythonModule(deps=('itertools', 'os', 'stat')),

    'fileinput': (
        PythonModule(max_version=(3, 3), deps='os'),
        PythonModule(min_version=(3, 4), deps=('os', 'warnings'))),

    'fnmatch': (
        PythonModule(version=2, deps=('os', 'posixpath', 're')),
        PythonModule(version=3, deps=('functools', 'os', 'posixpath', 're'))),

    'formatter': (
        PythonModule(max_version=(3, 3)),
        PythonModule(min_version=(3, 4), deps='warnings')),

    'fpformat':
        PythonModule(version=2, deps=('re', 'warnings')),

    'fractions': (
        PythonModule(version=2,
                deps=('__future__', 'decimal', 'math', 'numbers', 'operator',
                        're')),
        PythonModule(min_version=3, max_version=(3, 4),
                deps=('decimal', 'math', 'numbers', 'operator', 're')),
        PythonModule(min_version=(3, 5),
                deps=('decimal', 'math', 'numbers', 'operator', 're',
                        'warnings'))),

    'ftplib': (
        PythonModule(max_version=(3, 3),
                deps=('os', 're', 'socket', '?ssl')),
        PythonModule(min_version=(3, 4),
                deps=('os', 're', 'socket', '?ssl', 'warnings'))),

    'functools': (
        PythonModule(version=2, deps='_functools'),
        PythonModule(version=(3, 3),
                deps=('collections', '_functools', '_thread')),
        PythonModule(min_version=(3, 4),
                deps=('abc', 'collections', '_functools', '_thread', 'types',
                        'weakref'))),

    'future_builtins':
        ExtensionModule(version=2, source='future_builtins.c'),

    'gc':
        CoreExtensionModule(),

    'gdbm':
        ExtensionModule(version=2, source='gdbmmodule.c', xlib='gdbm'),

    'getopt': (
        PythonModule(version=2, deps='os'),
        PythonModule(version=3, deps=('gettext', 'os'))),

    'getpass': (
        PythonModule(version=2,
                deps=('msvcrt', 'os', 'pwd', 'termios', 'warnings')),
        PythonModule(version=3,
                deps=('contextlib', 'io', 'msvcrt', 'os', 'pwd', 'termios',
                        'warnings'))),

    'gettext': (
        PythonModule(version=2,
                deps=('copy', 'cStringIO', 'errno', 'locale', 'os', 're',
                        'struct', 'token', 'tokenize')),
        PythonModule(version=3,
                deps=('copy', 'errno', 'io', 'locale', 'os', 're', 'struct',
                        'token', 'tokenize'))),

    'glob':
        PythonModule(deps=('fnmatch', 'os', 're')),

    'grp':
        ExtensionModule(scope='!win32', source='grpmodule.c'),

    'gzip': (
        PythonModule(max_version=(3, 4),
                deps=('errno', 'io', 'os', 'struct', 'time', 'warnings',
                        'zlib')),
        PythonModule(min_version=(3, 5),
                deps=('_compression', 'errno', 'io', 'os', 'struct', 'time',
                        'warnings', 'zlib'))),

    'hashlib': (
        PythonModule(version=2,
                deps=('binascii', '?_hashlib', '!_md5', '!_sha', '!_sha256',
                        '!_sha512', 'struct')),
        PythonModule(version=3,
                deps=('?_hashlib', '!_md5', '!_sha1', '!_sha256',
                        '!_sha512'))),

    'heapq': (
        PythonModule(version=2, deps=('_heapq', 'itertools', 'operator')),
        PythonModule(min_version=3, max_version=(3, 4),
                deps=('_heapq', 'itertools')),
        PythonModule(min_version=(3, 5), deps='_heapq')),

    'hmac': (
        PythonModule(max_version=(3, 3),
                deps=('hashlib', 'operator', 'warnings')),
        PythonModule(min_version=(3, 4),
                deps=('hashlib', '_operator', 'warnings'))),

    'hotshot':
        PythonModule(version=2, deps=('_hotshot', 'warnings'),
                modules='hotshot.stats'),

    'hotshot.stats':
        PythonModule(version=2,
                deps=('hotshot', 'hotshot.log', 'profile', 'pstats')),

    'html': (
        PythonModule(version=(3, 3), modules=('html.entities', 'html.parser')),
        PythonModule(min_version=(3, 4), deps=('html.entities', 're'),
                modules=('html.entities', 'html.parser'))),

    'html.entities':
        PythonModule(version=3, deps='html'),

    'html.parser': (
        PythonModule(version=(3, 3),
                deps=('html', 'html.entities', '_markupbase', 're',
                        'warnings')),
        PythonModule(min_version=(3, 4),
                deps=('html', '_markupbase', 're', 'warnings'))),

    'htmlentitydefs':
        PythonModule(version=2),

    'htmllib':
        PythonModule(version=2,
                deps=('formatter', 'htmlentitydefs', 'sgmllib', 'warnings')),

    'HTMLParser':
        PythonModule(version=2, deps=('htmlentitydefs', 'markupbase', 're')),

    'http': (
        PythonModule(min_version=3, max_version=(3, 4),
                modules=('http.client', 'http.cookiejar', 'http.cookies',
                        'http.server')),
        PythonModule(min_version=(3, 5), deps='enum',
                modules=('http.client', 'http.cookiejar', 'http.cookies',
                        'http.server'))),

    'http.client': (
        PythonModule(version=(3, 3),
                deps=('http', 'collections', 'email.message', 'email.parser',
                        'io', 'os', 'socket', '?ssl', 'urllib.parse',
                        'warnings')),
        PythonModule(min_version=(3, 4), max_version=(3, 4, 3),
                deps=('http', 'collections', 'email.message', 'email.parser',
                        'io', 'os', 'socket', '?ssl', 'urllib.parse')),
        PythonModule(min_version=(3, 4, 4),
                deps=('http', 'collections', 'email.message', 'email.parser',
                        'io', 'os', 're', 'socket', '?ssl', 'urllib.parse'))),

    'http.cookiejar':
        PythonModule(version=3,
                deps=('http', 'calendar', 'copy', 'datetime', 'http.client',
                        're', 'threading', 'time', 'urllib.parse',
                        'urllib.request')),

    'http.cookies': (
        PythonModule(min_version=3, max_version=(3, 4),
                deps=('http', 're', 'string', 'time')),
        PythonModule(min_version=(3, 5),
                deps=('http', 're', 'string', 'time', 'warnings'))),

    'http.server': (
        PythonModule(version=(3, 3),
                deps=('http', 'argparse', 'base64', 'binascii', 'copy',
                        'email.message', 'email.parser', 'html', 'http.client',
                        'io', 'mimetypes', 'os', 'posixpath', 'pwd', 'select',
                        'shutil', 'socket', 'socketserver', 'subprocess',
                        'time', 'urllib.parse')),
        PythonModule(min_version=(3, 4),
                deps=('http', 'argparse', 'base64', 'binascii', 'copy', 'html',
                        'http.client', 'io', 'mimetypes', 'os', 'posixpath',
                        'pwd', 'select', 'shutil', 'socket', 'socketserver',
                        'subprocess', 'time', 'urllib.parse'))),

    'httplib': (
        PythonModule(max_version=(2, 7, 9),
                deps=('array', 'cStringIO', 'mimetools', 'os', 'socket',
                        '?ssl', 'urlparse', 'warnings')),
        PythonModule(min_version=(2, 7, 10), max_version=2,
                deps=('array', 'cStringIO', 'mimetools', 'os', 're', 'socket',
                        '?ssl', 'urlparse', 'warnings'))),

    'imageop':
        ExtensionModule(version=2, source='imageop.c'),

    'imaplib': (
        PythonModule(version=2,
                deps=('binascii', 'errno', 'hmac', 'random', 're', 'socket',
                        '?ssl', 'subprocess', 'time')),
        PythonModule(version=3,
                deps=('binascii', 'calendar', 'datetime', 'errno', 'hmac',
                        'io', 'random', 're', 'socket', '?ssl', 'subprocess',
                        'time'))),
    'imghdr':
        PythonModule(),

    'imp': (
        CoreExtensionModule(version=2),
        CorePythonModule(version=(3, 3),
                deps=('_imp', 'importlib', 'importlib._bootstrap',
                        'importlib.machinery', 'os', 'tokenize', 'warnings')),
        CorePythonModule(version=(3, 4),
                deps=('_imp', 'importlib', 'importlib._bootstrap',
                        'importlib.machinery', 'importlib.util', 'os',
                        'tokenize', 'types', 'warnings')),
        CorePythonModule(min_version=(3, 5),
                deps=('_imp', 'importlib', 'importlib._bootstrap',
                        'importlib._bootstrap_external', 'importlib.machinery',
                        'importlib.util', 'os', 'tokenize', 'types',
                        'warnings'))),

    'importlib': (
        PythonModule(version=2, modules=()),
        CorePythonModule(version=(3, 3), deps=('importlib._bootstrap', '_imp'),
                modules=('importlib.abc', 'importlib.machinery',
                        'importlib.util')),
        CorePythonModule(version=(3, 4),
                deps=('importlib._bootstrap', '_imp', 'types'),
                hidden_deps='warnings',
                modules=('importlib.abc', 'importlib.machinery',
                        'importlib.util')),
        CorePythonModule(min_version=(3, 5),
                deps=('importlib._bootstrap', 'importlib._bootstrap_external',
                        '_imp', 'types'),
                hidden_deps='warnings',
                modules=('importlib.abc', 'importlib.machinery',
                        'importlib.util'))),

    'importlib.abc': (
        PythonModule(version=(3, 3),
                deps=('importlib', 'abc', 'imp', 'importlib._bootstrap',
                        'importlib.machinery', 'marshal', 'tokenize',
                        'warnings')),
        PythonModule(version=(3, 4),
                deps=('importlib', 'abc', 'importlib._bootstrap',
                        'importlib.machinery')),
        PythonModule(min_version=(3, 5),
                deps=('importlib', 'abc', 'importlib._bootstrap',
                        'importlib._bootstrap_external',
                        'importlib.machinery'))),

    'importlib.machinery': (
        PythonModule(min_version=3, max_version=(3, 4),
                deps=('importlib', '_imp', 'importlib._bootstrap')),
        PythonModule(min_version=(3, 5),
                deps=('importlib', '_imp', 'importlib._bootstrap',
                        'importlib._bootstrap_external'))),

    'importlib.util': (
        PythonModule(version=(3, 3),
                deps=('importlib', 'importlib._bootstrap')),
        PythonModule(version=(3, 4),
                deps=('importlib', 'contextlib', 'functools',
                        'importlib._bootstrap', 'warnings')),
        PythonModule(min_version=(3, 5),
                deps=('importlib', 'contextlib', 'functools', 'importlib.abc',
                        'importlib._bootstrap',
                        'importlib._bootstrap_external', 'types',
                        'warnings'))),

    'imputil':
        PythonModule(version=2, deps=('imp', 'marshal', 'struct', 'warnings')),

    'inspect': (
        PythonModule(version=2,
                deps=('collections', 'dis', 'imp', 'linecache', 'operator',
                        'os', 're', 'string', 'tokenize', 'types')),
        PythonModule(version=(3, 3),
                deps=('collections', 'functools', 'imp', 'importlib.machinery',
                        'itertools', 'linecache', 'operator', 'os', 're',
                        'tokenize', 'types', 'warnings')),
        PythonModule(version=(3, 4),
                deps=('ast', 'collections', 'functools', 'imp',
                        'importlib.machinery', 'itertools', 'linecache',
                        'operator', 'os', 're', 'token', 'tokenize', 'types',
                        'warnings')),
        PythonModule(min_version=(3, 5),
                deps=('ast', 'collections', 'collections.abc', 'dis', 'enum',
                        'functools', 'imp', 'importlib.machinery', 'itertools',
                        'linecache', 'operator', 'os', 're', 'token',
                        'tokenize', 'types', 'warnings'))),

    'io': (
        PythonModule(version=2, deps=('abc', '_io')),
        CorePythonModule(version=3, deps=('abc', '_io'))),

    'ipaddress':
        PythonModule(version=3, deps='functools'),

    'itertools': (
        ExtensionModule(version=2, source='itertoolsmodule.c'),
        CoreExtensionModule(version=3)),

    'json':
        PythonModule(deps=('json.decoder', 'json.encoder'), modules=()),

    'keyword':
        PythonModule(),

    'linecache': (
        PythonModule(version=2, deps='os'),
        PythonModule(min_version=3, max_version=(3, 4),
                deps=('os', 'tokenize')),
        PythonModule(min_version=(3, 5),
                deps=('functools', 'os', 'tokenize'))),

    'linuxaudiodev':
        ExtensionModule(version=2, source='linuxaudiodev.c'),

    'locale': (
        PythonModule(version=2,
                deps=('encodings', 'encodings.aliases', 'functools', '_locale',
                        'os', 'operator', 're')),
        PythonModule(version=(3, 3),
                deps=('collections', 'encodings', 'encodings.aliases',
                        'functools', '_locale', 'os', 're')),
        PythonModule(min_version=(3, 4),
                deps=('_bootlocale', 'collections', 'encodings',
                        'encodings.aliases', 'functools', '_locale', 'os',
                        're'))),

    'logging': (
        PythonModule(version=2,
                deps=('atexit', 'codecs', 'collections', 'cStringIO', 'os',
                        'thread', 'threading', 'time', 'traceback', 'warnings',
                        'weakref'),
                modules=('logging.config', 'logging.handlers')),
        PythonModule(version=(3, 3),
                deps=('atexit', 'io', 'os', 'string', 'threading', 'time',
                        'traceback', 'warnings', 'weakref'),
                modules=('logging.config', 'logging.handlers')),
        PythonModule(min_version=(3, 4),
                deps=('atexit', 'collections', 'io', 'os', 'string',
                        'threading', 'time', 'traceback', 'warnings',
                        'weakref'),
                modules=('logging.config', 'logging.handlers'))),

    'logging.config': (
        PythonModule(version=2,
                deps=('logging', 'ConfigParser', 'cStringIO', 'errno', 'io',
                        'json', 'logging.handlers', 'os', 're', 'select',
                        'socket', 'SocketServer', 'struct', 'tempfile',
                        'thread', 'threading', 'traceback', 'types')),
        PythonModule(version=(3, 3),
                deps=('logging', 'configparser', 'io', 'json',
                        'logging.handlers', 're', 'select', 'socket',
                        'socketserver', 'struct', '_thread', 'threading',
                        'traceback')),
        PythonModule(min_version=(3, 4),
                deps=('logging', 'errno', 'configparser', 'io', 'json',
                        'logging.handlers', 're', 'select', 'socketserver',
                        'struct', '_thread', 'threading', 'traceback'))),

    'logging.handlers': (
        PythonModule(version=2,
                deps=('logging', 'codecs', 'cPickle', 'email.utils', 'errno',
                        'httplib', 'os', 're', 'socket', 'smtplib', 'stat',
                        'struct', 'time', 'urllib')),
        PythonModule(min_version=(3, 3), max_version=(3, 4, 3),
                deps=('logging', 'base64', 'codecs', 'email.utils', 'errno',
                        'http.client', 'os', 'pickle', 'queue', 're', 'socket',
                        'smtplib', 'stat', 'struct', 'threading', 'time',
                        'urllib.parse')),
        PythonModule(min_version=(3, 4, 4), max_version=(3, 4),
                deps=('logging', 'base64', 'codecs', 'email.message',
                        'email.utils', 'errno', 'http.client', 'os', 'pickle',
                        'queue', 're', 'socket', 'smtplib', 'stat', 'struct',
                        'threading', 'time', 'urllib.parse')),
        PythonModule(version=(3, 5, 0),
                deps=('logging', 'base64', 'codecs', 'email.utils', 'errno',
                        'http.client', 'os', 'pickle', 'queue', 're', 'socket',
                        'smtplib', 'stat', 'struct', 'threading', 'time',
                        'urllib.parse')),
        PythonModule(min_version=(3, 5, 1),
                deps=('logging', 'base64', 'codecs', 'email.message',
                        'email.utils', 'errno', 'http.client', 'os', 'pickle',
                        'queue', 're', 'socket', 'smtplib', 'stat', 'struct',
                        'threading', 'time', 'urllib.parse'))),

    'lzma': (
        PythonModule(min_version=3, max_version=(3, 4), deps=('io', '_lzma')),
        PythonModule(min_version=(3, 5),
                deps=('_compression', 'io', '_lzma'))),

    'MacOS':
        ExtensionModule(version=2, scope='macx',
                source='../Mac/Modules/MacOS.c'),

    'macpath': (
        PythonModule(version=2,
                deps=('genericpath', 'os', 'stat', 'warnings')),
        PythonModule(version=3, deps=('genericpath', 'os', 'stat'))),

    'mailbox': (
        PythonModule(version=2,
                deps=('calendar', 'copy', 'email', 'email.generator',
                        'email.message', 'errno', 'fcntl', 'os', 're',
                        'rfc822', 'socket', 'StringIO', 'time', 'warnings')),
        PythonModule(version=3,
                deps=('calendar', 'contextlib', 'copy', 'email',
                        'email.generator', 'email.message', 'errno', 'fcntl',
                        'io', 'os', 'socket', 'time', 'warnings'))),

    'mailcap':
        PythonModule(deps='os'),

    'marshal':
        CoreExtensionModule(),

    'math':
        ExtensionModule(source=('mathmodule.c', '_math.c'),
                libs='linux-*#-lm'),

    'md5':
        PythonModule(version=2, deps=('hashlib', 'warnings')),

    'mhlib':
        PythonModule(version=2,
                deps=('bisect', 'cStringIO', 'mimetools', 'multifile', 'os',
                        're', 'shutil', 'warnings')),

    'mimetools':
        PythonModule(version=2,
                deps=('base64', 'os', 'quopri', 'rfc822', 'socket', 'tempfile',
                        'thread', 'time', 'uu', 'warnings')),

    'mimetypes': (
        PythonModule(version=2, deps=('os', 'posixpath', 'urllib', '_winreg')),
        PythonModule(version=3,
                deps=('os', 'posixpath', 'urllib.parse', 'winreg'))),

    'MimeWriter':
        PythonModule(version=2, deps=('mimetools', 'warnings')),

    'mimify':
        PythonModule(version=2, deps=('base64', 'os', 're', 'warnings')),

    'mmap': (
        ExtensionModule(max_version=(3, 4), source='mmapmodule.c'),
        ExtensionModule(min_version=(3, 5), source='mmapmodule.c',
                defines='Py_BUILD_CORE')),

    'modulefinder': (
        PythonModule(version=2,
                deps=('__future__', 'dis', 'imp', 'marshal', 'os', 'types',
                        'struct')),
        PythonModule(version=(3, 3),
                deps=('dis', 'imp', 'importlib.machinery', 'marshal', 'os',
                        'types', 'struct')),
        PythonModule(version=(3, 4),
                deps=('dis', 'importlib._bootstrap', 'importlib.machinery',
                        'marshal', 'os', 'types', 'struct', 'warnings')),
        PythonModule(min_version=(3, 5),
                deps=('dis', 'importlib._bootstrap_external',
                        'importlib.machinery', 'marshal', 'os', 'types',
                        'struct', 'warnings'))),

    'msilib':
        PythonModule(scope='win32',
                deps=('_msi', 'os', 're', 'string', 'tempfile')),

    'msvcrt': (
        ExtensionModule(max_version=(3, 4), scope='win32',
                source='../PC/msvcrtmodule.c'),
        ExtensionModule(min_version=(3, 5), scope='win32',
                source='../PC/msvcrtmodule.c', defines='Py_BUILD_CORE')),

    'multifile':
        PythonModule(version=2, deps='warnings'),

    'multiprocessing': (
        PythonModule(version=2,
                deps=('_multiprocessing', 'multiprocessing.connection',
                        'multiprocessing.forking', 'multiprocessing.managers',
                        'multiprocessing.pool', 'multiprocessing.process',
                        'multiprocessing.queues', 'multiprocessing.reduction',
                        'multiprocessing.sharedctypes',
                        'multiprocessing.synchronize', 'multiprocessing.util',
                        'os'),
                modules=('multiprocessing.connection',
                        'multiprocessing.managers', 'multiprocessing.pool',
                        'multiprocessing.sharedctypes')),
        PythonModule(version=(3, 3),
                deps=('_multiprocessing', 'multiprocessing.connection',
                        'multiprocessing.forking', 'multiprocessing.managers',
                        'multiprocessing.pool', 'multiprocessing.process',
                        'multiprocessing.queues',
                        'multiprocessing.sharedctypes',
                        'multiprocessing.synchronize', 'multiprocessing.util',
                        'os'),
                modules=('multiprocessing.connection',
                        'multiprocessing.managers', 'multiprocessing.pool',
                        'multiprocessing.sharedctypes')),
        PythonModule(min_version=(3, 4),
                deps='multiprocessing.context',
                modules=('multiprocessing.connection',
                        'multiprocessing.managers', 'multiprocessing.pool',
                        'multiprocessing.sharedctypes'))),

    'multiprocessing.connection': (
        PythonModule(version=2,
                deps=('multiprocessing', 'errno', 'hmac', 'itertools',
                        '_multiprocessing', 'multiprocessing.forking',
                        'multiprocessing.util', 'os', 'socket', 'tempfile',
                        'time', 'xmlrpclib')),
        PythonModule(version=(3, 3),
                deps=('multiprocessing', 'errno', 'hmac', 'io', 'itertools',
                        '_multiprocessing', 'multiprocessing.forking',
                        'multiprocessing.reduction', 'multiprocessing.util',
                        'os', 'pickle', 'select', 'socket', 'struct',
                        'tempfile', 'time', '_winapi', 'xmlrpc.client')),
        PythonModule(min_version=(3, 4),
                deps=('multiprocessing', 'hmac', 'io', 'itertools',
                        '_multiprocessing', 'multiprocessing.reduction',
                        'multiprocessing.resource_sharer',
                        'multiprocessing.util', 'os', 'selectors', 'socket',
                        'struct', 'tempfile', 'time', '_winapi',
                        'xmlrpc.client'))),

    'multiprocessing.dummy': (
        PythonModule(version=2,
                deps=('multiprocessing', 'array', 'itertools',
                        'multiprocessing.dummy.connection',
                        'multiprocessing.pool', 'Queue', 'threading',
                        'weakref'),
                modules=()),
        PythonModule(version=3,
                deps=('multiprocessing', 'array',
                        'multiprocessing.dummy.connection',
                        'multiprocessing.pool', 'queue', 'threading',
                        'weakref'),
                modules=())),

    'multiprocessing.managers': (
        PythonModule(version=2,
                deps=('multiprocessing', 'array', 'multiprocessing.forking',
                        'multiprocessing.process', 'multiprocessing.util',
                        'cPickle', 'os', 'Queue', 'threading', 'traceback',
                        'weakref')),
        PythonModule(version=(3, 3),
                deps=('multiprocessing', 'array', 'copyreg',
                        'multiprocessing.forking', 'multiprocessing.process',
                        'queue', 'threading', 'time', 'traceback')),
        PythonModule(min_version=(3, 4),
                deps=('multiprocessing', 'array', 'multiprocessing.connection',
                        'multiprocessing.context', 'multiprocessing.pool',
                        'multiprocessing.process', 'multiprocessing.reduction',
                        'multiprocessing.util', 'queue', 'threading', 'time',
                        'traceback'))),

    'multiprocessing.pool': (
        PythonModule(version=2,
                deps=('multiprocessing', 'collections', 'itertools',
                        'multiprocessing.dummy', 'multiprocessing.queues',
                        'multiprocessing.util', 'Queue', 'threading', 'time')),
        PythonModule(version=(3, 3),
                deps=('multiprocessing', 'collections', 'itertools',
                        'multiprocessing.dummy', 'multiprocessing.queues',
                        'multiprocessing.util', 'queue', 'threading', 'time')),
        PythonModule(min_version=(3, 4),
                deps=('multiprocessing', 'collections', 'itertools',
                        'multiprocessing.dummy', 'multiprocessing.util',
                        'queue', 'threading', 'time', 'traceback'))),

    'multiprocessing.sharedctypes': (
        PythonModule(max_version=(3, 3),
                deps=('multiprocessing', 'ctypes', 'multiprocessing.forking',
                        'multiprocessing.heap', 'weakref')),
        PythonModule(min_version=(3, 4),
                deps=('multiprocessing', 'ctypes', 'multiprocessing.context',
                        'multiprocessing.heap', 'multiprocessing.reduction',
                        'weakref'))),

    'mutex':
        PythonModule(version=2, deps=('collections', 'warnings')),

    'netrc':
        PythonModule(deps=('os', 'pwd', 'shlex', 'stat')),

    'new':
        PythonModule(version=2, deps=('types', 'warnings')),

    'nis':
        ExtensionModule(scope='!win32', source='nismodule.c', libs='-lnsl'),

    'nntplib': (
        PythonModule(version=2, deps=('netrc', 're', 'socket')),
        PythonModule(version=3,
                deps=('collections', 'datetime', 'email.header', 'netrc', 're',
                        'socket', '?ssl', 'warnings'))),

    'numbers': (
        PythonModule(version=2, deps=('__future__', 'abc')),
        PythonModule(version=3, deps='abc')),

    'operator': (
        ExtensionModule(version=2, source='operator.c'),
        CoreExtensionModule(version=(3, 3)),
        PythonModule(version=(3, 4), deps='_operator'),
        PythonModule(min_version=(3, 5), deps=('functools', '_operator'))),

    'optparse': (
        PythonModule(version=2, deps=('gettext', 'os', 'textwrap', 'types')),
        PythonModule(version=3, deps=('gettext', 'os', 'textwrap'))),

    'os': (
        PythonModule(version=2,
                deps=('copy_reg', 'errno', 'nt', 'ntpath', 'posix',
                        'posixpath', 'subprocess', 'warnings')),
        PythonModule(version=3,
                deps=('collections', 'copyreg', 'errno', 'io', 'nt',
                        'ntpath', 'posix', 'posixpath', 'stat', 'subprocess',
                        'warnings'))),

    'ossaudiodev':
        ExtensionModule(source='ossaudiodev.c'),

    'parser':
        ExtensionModule(source='parsermodule.c'),

    'pathlib':
        PythonModule(min_version=(3, 4),
                deps=('collections', 'contextlib', 'errno', 'fnmatch',
                        'functools', 'grp', 'io', 'nt', 'ntpath', 'operator',
                        'os', 'posixpath', 'pwd', 're', 'stat',
                        'urllib.parse')),

    'pdb': (
        PythonModule(version=2,
                deps=('bdb', 'cmd', 'linecache', 'os', 'pprint', 're', 'repr',
                        'shlex', 'traceback')),
        PythonModule(version=3,
                deps=('bdb', 'cmd', 'code', 'dis', 'glob', 'inspect',
                        'linecache', 'os', 'pprint', 'pydoc', 're', 'shlex',
                        'signal', 'traceback'))),

    'pickle': (
        PythonModule(version=2,
                deps=('binascii', 'copy_reg', 'cStringIO', 'marshal', 're',
                        'struct', 'types')),
        PythonModule(version=(3, 3),
                deps=('codecs', '_compat_pickle', 'copyreg', 'io', 'marshal',
                        '_pickle', 're', 'struct', 'types')),
        PythonModule(min_version=(3, 4),
                deps=('codecs', '_compat_pickle', 'copyreg', 'io', 'itertools',
                        'marshal', '_pickle', 're', 'struct', 'types'))),

    'pickletools': (
        PythonModule(version=2, deps=('cStringIO', 'pickle', 're', 'struct')),
        PythonModule(version=3,
                deps=('codecs', 'io', 'pickle', 're', 'struct'))),

    'pipes': (
        PythonModule(version=2, scope='!win32',
                deps=('os', 're', 'string', 'tempfile')),
        PythonModule(version=3, scope='!win32',
                deps=('os', 're', 'shlex', 'tempfile'))),

    'pkgutil': (
        PythonModule(version=2,
                deps=('imp', 'inspect', 'marshal', 'os', 'types')),
        PythonModule(version=(3, 3),
                deps=('imp', 'importlib', 'inspect', 'marshal', 'os', 'types',
                        'warnings')),
        PythonModule(min_version=(3, 4),
                deps=('functools', 'importlib', 'importlib.machinery',
                        'importlib.util', 'inspect', 'marshal', 'os', 'types',
                        'warnings'))),

    'platform': (
        PythonModule(max_version=(2, 7, 10),
                deps=('gestalt', 'MacOS', 'os', 'plistlib', 're', 'socket',
                        'string', 'struct', 'subprocess', 'tempfile',
                        '_winreg')),
        PythonModule(min_version=(2, 7, 11), max_version=2,
                deps=('ctypes', 'ctypes.wintypes', 'gestalt', 'MacOS', 'os',
                        'plistlib', 're', 'socket', 'string', 'struct',
                        'subprocess', 'tempfile', '_winreg')),
        PythonModule(version=(3, 3),
                deps=('collections', '_gestalt', 'os', 'plistlib', 're',
                        'socket', 'struct', 'subprocess', 'warnings',
                        'winreg')),
        PythonModule(min_version=(3, 4), max_version=(3, 4, 3),
                deps=('collections', 'os', 'plistlib', 're', 'socket',
                        'struct', 'subprocess', 'warnings', 'winreg')),
        PythonModule(min_version=(3, 4, 4), max_version=(3, 4),
                deps=('collections', 'ctypes', 'ctypes.wintypes', 'os',
                        'plistlib', 're', 'socket', 'struct', 'subprocess',
                        'warnings', 'winreg')),
        PythonModule(version=(3, 5, 0),
                deps=('collections', 'os', 'plistlib', 're', 'socket',
                        'struct', 'subprocess', 'warnings', 'winreg')),
        PythonModule(min_version=(3, 5, 1),
                deps=('collections', 'ctypes', 'ctypes.wintypes', 'os',
                        'plistlib', 're', 'socket', 'struct', 'subprocess',
                        'warnings', 'winreg'))),

    'plistlib': (
        PythonModule(version=2,
                deps=('binascii', 'cStringIO', 'datetime', 're', 'warnings',
                        'xml.parsers.expat')),
        PythonModule(version=(3, 3),
                deps=('binascii', 'datetime', 'io', 're', 'warnings',
                        'xml.parsers.expat')),
        PythonModule(min_version=(3, 4),
                deps=('binascii', 'codecs', 'contextlib', 'datetime', 'enum',
                        'io', 'itertools', 'os', 're', 'struct', 'warnings',
                        'xml.parsers.expat'))),

    'popen2':
        PythonModule(version=2, deps=('os', 'warnings')),

    'poplib': (
        PythonModule(max_version=(3, 3),
                deps=('hashlib', 're', 'socket', '?ssl')),
        PythonModule(min_version=(3, 4),
                deps=('errno', 'hashlib', 're', 'socket', '?ssl'))),

    'posix':
        CoreExtensionModule(scope='!win32'),

    'posixfile':
        PythonModule(version=2, scope='!win32',
                deps=('fcntl', 'os', 'posix', 'struct', 'types', 'warnings')),

    'pprint': (
        PythonModule(version=2, deps=('cStringIO', 'time', 'warnings')),
        PythonModule(version=(3, 3), deps=('collections', 'io', 'time')),
        PythonModule(version=(3, 4), deps=('collections', 'io', 're', 'time')),
        PythonModule(min_version=(3, 5),
                deps=('collections', 'io', 're', 'time', 'types'))),

    'profile':
        PythonModule(
                deps=('marshal', 'optparse', 'os', 'pstats', 'resource',
                        'time')),

    'pstats':
        PythonModule(deps=('functools', 'marshal', 'os', 're', 'time')),

    'pty':
        PythonModule(scope='!win32', deps=('fcntl', 'os', 'select', 'tty')),

    'pwd':
        CoreExtensionModule(scope='!win32'),

    'py_compile': (
        PythonModule(version=2, deps=('imp', 'marshal', 'os', 'traceback')),
        PythonModule(version=(3, 3),
                deps=('errno', 'imp', 'marshal', 'os', 'tokenize',
                        'traceback')),
        PythonModule(version=(3, 4),
                deps=('importlib._bootstrap', 'importlib.machinery',
                        'importlib.util', 'os', 'traceback')),
        PythonModule(min_version=(3, 5),
                deps=('importlib._bootstrap_external', 'importlib.machinery',
                        'importlib.util', 'os', 'traceback'))),

    'pyclbr': (
        PythonModule(version=2, deps=('imp', 'operator', 'token', 'tokenize')),
        PythonModule(version=(3, 3),
                deps=('importlib', 'io', 'operator', 'os', 'token',
                        'tokenize')),
        PythonModule(min_version=(3, 4),
                deps=('importlib.util', 'io', 'operator', 'os', 'token',
                        'tokenize'))),

    'pydoc': (
        PythonModule(version=2,
                deps=('BaseHTTPServer', 'collections', 'formatter', 'imp',
                        'inspect', 'locale', 'mimetools', 'nturl2path', 'os',
                        'pkgutil', 'select', 'string', 're', 'repr',
                        'StringIO', 'tempfile', 'traceback', 'tty', 'types',
                        'warnings')),
        PythonModule(version=(3, 3),
                deps=('collections', 'email.message', 'formatter',
                        'http.server', 'imp', 'importlib.machinery', 'inspect',
                        'io', 'nturl2path', 'os', 'pkgutil', 'platform', 're',
                        'reprlib', 'select', 'tempfile', 'threading', 'time',
                        'tokenize', 'traceback', 'tty', 'warnings')),
        PythonModule(min_version=(3, 4, 0), max_version=(3, 4, 1),
                deps=('collections', 'email.message', 'http.server',
                        'importlib._bootstrap', 'importlib.machinery',
                        'importlib.util', 'inspect', 'io', 'nturl2path', 'os',
                        'pkgutil', 'platform', 're', 'reprlib', 'select',
                        'tempfile', 'textwrap', 'threading', 'time',
                        'tokenize', 'traceback', 'tty', 'warnings')),
        PythonModule(min_version=(3, 4, 2), max_version=(3, 4, 3),
                deps=('collections', 'email.message', 'http.server',
                        'importlib._bootstrap', 'importlib.machinery',
                        'importlib.util', 'inspect', 'io', 'os', 'pkgutil',
                        'platform', 're', 'reprlib', 'select', 'tempfile',
                        'textwrap', 'threading', 'time', 'tokenize',
                        'traceback', 'tty', 'urllib.parse', 'warnings')),
        PythonModule(min_version=(3, 4, 4), max_version=(3, 4),
                deps=('collections', 'email.message', 'http.server',
                        'importlib._bootstrap', 'importlib.machinery',
                        'importlib.util', 'inspect', 'io', 'os', 'pkgutil',
                        'platform', 're', 'reprlib', 'select', 'subprocess',
                        'tempfile', 'textwrap', 'threading', 'time',
                        'tokenize', 'traceback', 'tty', 'urllib.parse',
                        'warnings')),
        PythonModule(min_version=(3, 5),
                deps=('collections', 'email.message', 'http.server',
                        'importlib._bootstrap',
                        'importlib._bootstrap_external', 'importlib.machinery',
                        'importlib.util', 'inspect', 'io', 'os', 'pkgutil',
                        'platform', 're', 'reprlib', 'select', 'subprocess',
                        'tempfile', 'textwrap', 'threading', 'time',
                        'tokenize', 'traceback', 'tty', 'urllib.parse',
                        'warnings'))),

    'Queue':
        PythonModule(version=2,
                deps=('collections', 'heapq', 'threading', 'time')),

    'queue':
        PythonModule(version=3,
                deps=('collections', 'heapq', 'threading', 'time')),

    'quopri': (
        PythonModule(version=2, deps=('binascii', 'cStringIO')),
        PythonModule(version=3, deps=('binascii', 'io'))),

    'random': (
        PythonModule(version=2,
                deps=('__future__', 'binascii', 'hashlib', 'math', 'os',
                        '_random', 'time', 'types', 'warnings')),
        PythonModule(version=(3, 3),
                deps=('collections', 'hashlib', 'math', 'os', '_random',
                        'time', 'types', 'warnings')),
        PythonModule(min_version=(3, 4),
                deps=('_collections_abc', 'hashlib', 'math', 'os', '_random',
                        'time', 'types', 'warnings'))),

    're': (
        PythonModule(max_version=(2, 7, 8),
                deps=('copy_reg', 'sre_compile', 'sre_constants',
                        'sre_parse')),
        PythonModule(min_version=(2, 7, 9), max_version=2,
                deps=('copy_reg', '_locale', 'sre_compile', 'sre_constants',
                        'sre_parse')),
        PythonModule(version=(3, 3),
                deps=('copyreg', 'functools', 'sre_compile', 'sre_constants',
                        'sre_parse')),
        PythonModule(min_version=(3, 4, 0), max_version=(3, 4, 2),
                deps=('copyreg', 'sre_compile', 'sre_constants', 'sre_parse')),
        PythonModule(min_version=(3, 4, 3),
                deps=('copyreg', '_locale', 'sre_compile', 'sre_constants',
                        'sre_parse'))),

    'readline':
        ExtensionModule(scope='!win32', source='readline.c', xlib='readline'),

    'repr':
        PythonModule(version=2, deps='itertools'),

    'reprlib':
        PythonModule(version=3, deps=('itertools', '_thread')),

    'resource':
        ExtensionModule(scope='!win32', source='resource.c'),

    'rfc822':
        PythonModule(version=2, deps=('time', 'warnings')),

    'rlcompleter': (
        PythonModule(max_version=(3, 3), deps=('keyword', 're', 'readline')),
        PythonModule(min_version=(3, 4),
                deps=('atexit', 'keyword', 're', 'readline'))),

    'robotparser':
        PythonModule(version=2, deps=('time', 'urllib', 'urlparse')),

    'runpy': (
        PythonModule(version=2, deps=('imp', 'pkgutil')),
        PythonModule(version=(3, 3),
                deps=('imp', 'importlib.machinery', 'os', 'pkgutil')),
        PythonModule(min_version=(3, 4),
                deps=('importlib.machinery', 'importlib.util', 'pkgutil',
                        'types'))),

    'sched': (
        PythonModule(version=2, deps=('collections', 'heapq')),
        PythonModule(version=3,
                deps=('collections', 'heapq', 'threading', 'time'))),

    'select':
        ExtensionModule(source='selectmodule.c', pyd='select.pyd'),

    'selectors':
        PythonModule(min_version=(3, 4),
                deps=('abc', 'collections', 'math', 'select')),

    'sets':
        PythonModule(version=2, deps=('copy', 'itertools', 'warnings')),

    'sgmllib':
        PythonModule(version=2, deps=('markupbase', 're', 'warnings')),

    'sha':
        PythonModule(version=2, deps=('hashlib', 'warnings')),

    'shelve': (
        PythonModule(version=2,
                deps=('anydbm', 'cPickle', 'cStringIO', 'UserDict')),
        PythonModule(version=3, deps=('collections', 'dbm', 'io', 'pickle'))),

    'shlex': (
        PythonModule(version=2, deps=('collections', 'cStringIO', 'os')),
        PythonModule(version=3, deps=('collections', 'io', 'os', 're'))),

    'shutil': (
        PythonModule(version=2,
                deps=('collections', 'errno', 'fnmatch', 'grp', 'os', 'pwd',
                        'stat', 'tarfile')),
        PythonModule(min_version=3, max_version=(3, 4),
                deps=('collections', 'errno', 'fnmatch', 'grp', 'nt', 'os',
                        'pwd', 'stat', 'tarfile')),
        PythonModule(min_version=(3, 5),
                deps=('collections', 'errno', 'fnmatch', 'grp', 'nt', 'os',
                        'pwd', 'stat', 'tarfile', 'zipfile'))),

    'signal': (
        CoreExtensionModule(max_version=(3, 4)),
        PythonModule(min_version=(3, 5),
                deps=('enum', 'functools', '_signal'))),

    'SimpleHTTPServer': (
        PythonModule(max_version=(2, 7, 9),
                deps=('BaseHTTPServer', 'cgi', 'cStringIO', 'mimetypes', 'os',
                        'posixpath', 'shutil', 'urllib')),
        PythonModule(min_version=(2, 7, 10), max_version=2,
                deps=('BaseHTTPServer', 'cgi', 'cStringIO', 'mimetypes', 'os',
                        'posixpath', 'shutil', 'urllib', 'urlparse'))),

    'SimpleXMLRPCServer': (
        PythonModule(version=2,
                deps=('BaseHTTPServer', 'fcntl', 'os', 'pydoc', 're',
                        'SocketServer', 'traceback', 'xmlrpclib'))),

    'smtpd': (
        PythonModule(version=2,
                deps=('asynchat', 'asyncore', 'errno', 'getopt', 'os',
                        'smtplib', 'socket', 'time')),
        PythonModule(version=3,
                deps=('asynchat', 'asyncore', 'collections',
                        'email._header_value_parser', 'errno', 'getopt', 'os',
                        'smtplib', 'socket', 'time', 'warnings'))),

    'smtplib': (
        PythonModule(version=2,
                deps=('base64', 'email.base64mime', 'email.utils', 'hmac',
                        're', 'socket', '?ssl')),
        PythonModule(min_version=3, max_version=(3, 4),
                deps=('base64', 'copy', 'email.base64mime', 'email.generator',
                        'email.message', 'email.utils', 'hmac', 'io', 're',
                        'socket', '?ssl')),
        PythonModule(min_version=(3, 5),
                deps=('base64', 'copy', 'datetime', 'email.base64mime',
                        'email.generator', 'email.message', 'email.utils',
                        'hmac', 'io', 're', 'socket', '?ssl'))),

    'sndhdr': (
        PythonModule(max_version=(3, 3), deps='aifc'),
        PythonModule(version=(3, 4), deps=('aifc', 'wave')),
        PythonModule(min_version=(3, 5),
                deps=('aifc', 'collections', 'wave'))),

    'spwd':
        ExtensionModule(scope='!win32', source='spwdmodule.c'),

    'socket': (
        PythonModule(version=2,
                deps=('cStringIO', 'errno', 'functools', 'os', '?ssl', '?_ssl',
                        '_socket', 'types', 'warnings')),
        PythonModule(version=(3, 3), deps=('errno', 'io', 'os', '_socket')),
        PythonModule(version=(3, 4),
                deps=('errno', 'enum', 'io', 'os', '_socket')),
        PythonModule(min_version=(3, 5),
                deps=('errno', 'enum', 'io', 'os', 'selectors', '_socket'))),

    'SocketServer':
        PythonModule(version=2,
                deps=('cStringIO', 'errno', 'os', 'select', 'socket',
                        'threading', 'traceback')),

    'socketserver': (
        PythonModule(min_version=3, max_version=(3, 4),
                deps=('errno', 'io', 'os', 'select', 'socket', 'traceback',
                        'threading')),
        PythonModule(min_version=(3, 5),
                deps=('errno', 'io', 'os', 'selectors', 'socket', 'time',
                        'traceback', 'threading'))),

    'sqlite3':
        PythonModule(deps='sqlite3.dbapi2', modules=('sqlite3.dbapi2')),

    'sqlite3.dbapi2': (
        PythonModule(version=2,
                deps=('sqlite3', 'collections', 'datetime', '_sqlite3',
                        'time')),
        PythonModule(min_version=(3, 0, 0), max_version=(3, 4, 1),
                deps=('sqlite3', 'datetime', '_sqlite3', 'time')),
        PythonModule(min_version=(3, 4, 2),
                deps=('sqlite3', 'collections.abc', 'datetime', '_sqlite3',
                        'time'))),

    'ssl': (
        PythonModule(max_version=(2, 7, 8),
                deps=('base64', 'errno', 'socket', '_ssl', 'textwrap',
                        'time')),
        PythonModule(min_version=(2, 7, 9), max_version=2,
                deps=('base64', 'calendar', 'collections', 'contextlib',
                        'errno', 'os', 're', 'socket', '_ssl', 'textwrap',
                        'time')),
        PythonModule(version=(3, 3),
                deps=('base64', 'errno', 're', 'socket', '_ssl', 'textwrap',
                        'time', 'traceback')),
        PythonModule(version=(3, 4),
                deps=('base64', 'collections', 'enum', 'errno', 'os', 're',
                        'socket', '_ssl', 'textwrap', 'time')),
        PythonModule(min_version=(3, 5),
                deps=('base64', 'calendar', 'collections', 'enum', 'errno',
                        'ipaddress', 'os', 're', 'socket', '_ssl', 'textwrap',
                        'time'))),

    'stat': (
        PythonModule(version=2),
        PythonModule(version=(3, 3)),
        PythonModule(min_version=(3, 4), deps='_stat')),

    'statistics': (
        PythonModule(min_version=(3, 4), max_version=(3, 4, 3),
                deps=('collections', 'decimal', 'fractions', 'math')),
        PythonModule(min_version=(3, 4, 4), max_version=(3, 4),
                deps=('collections', 'decimal', 'fractions', 'itertools',
                        'math')),
        PythonModule(min_version=(3, 5),
                deps=('collections', 'decimal', 'fractions', 'math'))),

    'statvfs':
        PythonModule(version=2, deps='warnings'),

    'string': (
        PythonModule(version=2, deps=('re', 'strop')),
        PythonModule(min_version=3, max_version=(3, 4),
                deps=('collections', 're', '_string')),
        PythonModule(min_version=(3, 5),
                deps=('collections', 're', '_string', 'warnings'))),

    'StringIO':
        PythonModule(version=2, deps='errno'),

    'stringprep':
        PythonModule(deps='unicodedata'),

    'struct':
        PythonModule(deps='_struct'),

    'sysconfig': (
        PythonModule(version=2,
                deps=('imp', 'os', '_osx_support', 'pprint', 're',
                        '_sysconfigdata')),
        PythonModule(version=(3, 3),
                deps=('os', '_osx_support', 'pprint', '_sysconfigdata')),
        PythonModule(min_version=(3, 4),
                deps=('os', '_osx_support', 'pprint', 're', '_sysconfigdata',
                        'types', 'warnings'))),

    'subprocess': (
        PythonModule(version=2,
                deps=('errno', 'fcntl', 'gc', 'msvcrt', 'os', 'pickle',
                        'select', 'signal', '_subprocess', 'threading',
                        'traceback', 'types')),
        PythonModule(version=(3, 3),
                deps=('errno', 'gc', 'io', 'msvcrt', 'os', '_posixsubprocess',
                        'select', 'signal', 'threading', 'time', 'traceback',
                        'warnings', '_winapi')),
        PythonModule(min_version=(3, 4),
                deps=('errno', 'gc', 'io', 'msvcrt', 'os', '_posixsubprocess',
                        'select', 'selectors', 'signal', 'threading', 'time',
                        'traceback', 'warnings', '_winapi'))),

    'sunau': (
        PythonModule(max_version=(3, 3), deps='audioop'),
        PythonModule(min_version=(3, 4), deps=('audioop', 'collections'))),

    'symbol':
        PythonModule(),

    'symtable':
        PythonModule(deps=('_symtable', 'weakref')),

    'syslog':
        ExtensionModule(scope='!win32', source='syslogmodule.c'),

    'tabnanny':
        PythonModule(deps=('getopt', 'os', 'tokenize')),

    'tarfile': (
        PythonModule(version=2,
                deps=('calendar', 'copy', 'cStringIO', 'errno', 'grp',
                        'operator', 'pwd', 'os', 're', 'shutil', 'stat',
                        'struct', 'time', 'warnings')),

        PythonModule(version=3,
                deps=('calendar', 'copy', 'errno', 'grp', 'io', 'pwd', 'os',
                        're', 'shutil', 'stat', 'struct', 'time',
                        'warnings'))),

    'telnetlib': (
        PythonModule(version=2,
                deps=('errno', 're', 'select', 'socket', 'thread', 'time')),
        PythonModule(version=(3, 3),
                deps=('errno', 're', 'select', 'socket', '_thread', 'time')),
        PythonModule(min_version=(3, 4),
                deps=('errno', 're', 'selectors', 'socket', '_thread',
                        'time'))),

    'tempfile': (
        PythonModule(version=2,
                deps=('cStringIO', 'errno', 'fcntl', 'io', 'os', 'random',
                        'thread')),
        PythonModule(version=(3, 3),
                deps=('atexit', 'errno', 'fcntl', 'functools', 'io', 'os',
                        'random', 'shutil', '_thread', 'warnings')),
        PythonModule(min_version=(3, 4),
                deps=('errno', 'functools', 'io', 'os', 'random', 'shutil',
                        '_thread', 'warnings', 'weakref'))),

    'termios':
        ExtensionModule(scope='!win32', source='termios.c'),

    'textwrap': (
        PythonModule(version=2, deps=('re', 'string')),
        PythonModule(version=3, deps='re')),

    'thread':
        CoreExtensionModule(version=2),

    'threading': (
        PythonModule(max_version=(2, 7, 8),
                deps=('collections', 'random', 'thread', 'time', 'traceback',
                        'warnings')),
        PythonModule(min_version=(2, 7, 9), max_version=2,
                deps=('collections', 'itertools', 'random', 'thread', 'time',
                        'traceback', 'warnings')),
        PythonModule(version=(3, 3),
                deps=('_thread', 'time', 'traceback', '_weakrefset')),
        PythonModule(min_version=(3, 4),
                deps=('_collections', 'itertools', '_thread', 'time',
                        'traceback', '_weakrefset'))),

    'time': (
        ExtensionModule(max_version=(3, 4), source='timemodule.c',
                libs='linux-*#-lm'),
        ExtensionModule(min_version=(3, 5), source='timemodule.c',
                defines='Py_BUILD_CORE', libs='linux-*#-lm')),

    'timeit':
        PythonModule(
                deps=('gc', 'itertools', 'linecache', 'time', 'traceback')),

    'token':
        PythonModule(),

    'tokenize': (
        PythonModule(version=2, deps=('itertools', 're', 'string', 'token')),
        PythonModule(version=3,
                deps=('codecs', 'collections', 'io', 'itertools', 're',
                        'token'))),

    'trace': (
        PythonModule(version=2,
                deps=('cPickle', 'dis', 'gc', 'inspect', 'linecache', 'os',
                        're', 'threading', 'time', 'token', 'tokenize')),
        PythonModule(version=3,
                deps=('dis', 'gc', 'inspect', 'linecache', 'os', 'pickle',
                        're', 'threading', 'time', 'token', 'tokenize',
                        'warnings'))),

    'traceback': (
        PythonModule(version=2, deps=('linecache', 'types')),
        PythonModule(version=(3, 3), deps='linecache'),
        PythonModule(version=(3, 4), deps=('linecache', 'operator')),
        PythonModule(min_version=(3, 5),
                deps=('collections', 'itertools', 'linecache'))),

    'tracemalloc':
        PythonModule(min_version=(3, 4),
                deps=('collections', 'fnmatch', 'functools', 'linecache', 'os',
                        'pickle', '_tracemalloc')),

    'tty':
        PythonModule(scope='!win32', deps='termios'),

    'types': (
        PythonModule(max_version=(3, 4)),
        PythonModule(min_version=(3, 5),
                deps=('collections.abc', 'functools'))),

    'typing':
        PythonModule(min_version=(3, 5),
                deps=('abc', 'collections', 'collections.abc', 'functools',
                        're', 'types')),

    'unicodedata':
        ExtensionModule(source='unicodedata.c', pyd='unicodedata.pyd'),

    'urllib': (
        PythonModule(version=2,
                deps=('base64', 'cStringIO', 'email.utils', 'ftplib',
                        'getpass', 'httplib', 'mimetools', 'mimetypes',
                        'nturl2path', 'os', 're', '_scproxy', 'socket', '?ssl',
                        'string', 'tempfile', 'time', 'urlparse', 'warnings',
                        '_winreg')),
        PythonModule(version=3,
                modules=('urllib.error', 'urllib.parse', 'urllib.request',
                        'urllib.response', 'urllib.robotparser'))),

    'urllib.error':
        PythonModule(version=3, deps=('urllib', 'urllib.response')),

    'urllib.parse':
        PythonModule(version=3, deps=('urllib', 'collections', 're')),

    'urllib.request':
        PythonModule(version=3,
                deps=('urllib', 'base64', 'bisect', 'collections',
                        'contextlib', 'email', 'email.utils', 'fnmatch',
                        'ftplib', 'getpass', 'hashlib', 'http.client',
                        'http.cookiejar', 'io', 'mimetypes', 'nturl2path',
                        'os', 'posixpath', 're', '_scproxy', 'socket', '?ssl',
                        'tempfile', 'time', 'urllib.error', 'urllib.parse',
                        'urllib.response', 'warnings', 'winreg')),

    'urllib.response': (
        PythonModule(version=(3, 3), deps='urllib'),
        PythonModule(min_version=(3, 4), deps=('urllib', 'tempfile'))),

    'urllib.robotparser':
        PythonModule(version=3,
                deps=('urllib', 'time', 'urllib.parse', 'urllib.request')),

    'urllib2': (
        PythonModule(max_version=(2, 7, 8),
                deps=('base64', 'bisect', 'cStringIO', 'cookielib',
                        'email.utils', 'ftplib', 'hashlib', 'httplib',
                        'mimetools', 'mimetypes', 'os', 'posixpath', 'random',
                        're', 'socket', 'time', 'types', 'urllib', 'urlparse',
                        'warnings')),
        PythonModule(min_version=(2, 7, 9), max_version=2,
                deps=('base64', 'bisect', 'cStringIO', 'cookielib',
                        'email.utils', 'ftplib', 'hashlib', 'httplib',
                        'mimetools', 'mimetypes', 'os', 'posixpath', 'random',
                        're', 'socket', '?ssl', 'time', 'types', 'urllib',
                        'urlparse', 'warnings'))),

    'urlparse':
        PythonModule(version=2, deps=('collections', 're')),

    'user':
        PythonModule(version=2, deps=('os', 'warnings')),

    'UserDict': (
        PythonModule(max_version=(2, 7, 10), deps=('_abcoll', 'copy')),
        PythonModule(min_version=(2, 7, 11), max_version=2,
                deps=('_abcoll', 'copy', 'warnings'))),

    'UserList':
        PythonModule(version=2, deps='collections'),

    'UserString':
        PythonModule(version=2, deps=('collections', 'warnings')),

    'uu':
        PythonModule(deps=('binascii', 'os')),

    'uuid': (
        PythonModule(version=2,
                deps=('ctypes', 'hashlib', 'os', 'random', 're', 'socket',
                        'time')),
        PythonModule(min_version=3, max_version=(3, 4),
                deps=('ctypes', 'hashlib', 'os', 'random', 're', 'shutil',
                        'socket', 'time')),
        PythonModule(min_version=(3, 5),
                deps=('ctypes', 'hashlib', 'os', 'random', 're', 'shutil',
                        'socket', 'subprocess', 'time'))),

    'warnings': (
        PythonModule(version=2,
                deps=('linecache', 'types', 're', '_warnings')),
        PythonModule(version=3, deps=('linecache', 're', '_warnings'))),

    'wave': (
        PythonModule(max_version=(3, 3), deps=('array', 'chunk', 'struct')),
        PythonModule(min_version=(3, 4),
                deps=('audioop', 'chunk', 'collections', 'struct'))),

    'weakref': (
        PythonModule(version=2,
                deps=('exceptions', 'UserDict', '_weakref', '_weakrefset')),
        PythonModule(version=(3, 3),
                deps=('collections', 'copy', '_weakref', '_weakrefset')),
        PythonModule(min_version=(3, 4),
                deps=('atexit', 'collections', 'copy', 'gc', 'itertools',
                        '_weakref', '_weakrefset'))),

    'webbrowser': (
        PythonModule(version=2,
                deps=('copy', 'glob', 'os', 'pwd', 'shlex', 'socket', 'stat',
                        'subprocess', 'tempfile', 'time')),
        PythonModule(version=(3, 3),
                deps=('copy', 'glob', 'io', 'os', 'pwd', 'shlex', 'socket',
                        'stat', 'subprocess', 'tempfile', 'time')),
        PythonModule(min_version=(3, 4),
                deps=('copy', 'glob', 'os', 'pwd', 'shlex', 'shutil', 'socket',
                        'subprocess', 'tempfile'))),

    'whichdb':
        PythonModule(version=2, deps=('dbm', 'os', 'struct')),

    '_winreg':
        ExtensionModule(version=2, scope='win32', source='../PC/_winreg.c'),

    'winreg':
        CoreExtensionModule(version=3, scope='win32'),

    'winsound':
        ExtensionModule(scope='win32', source='../PC/winsound.c',
                libs='-lwinmm', pyd='winsound.pyd'),

    'wsgiref':
        PythonModule(
                modules=('wsgiref.handlers', 'wsgiref.headers',
                        'wsgiref.simple_server', 'wsgiref.util',
                        'wsgiref.validate')),

    'wsgiref.handlers': (
        PythonModule(version=2,
                deps=('wsgiref', 'os', 'time', 'traceback', 'types',
                        'wsgiref.headers', 'wsgiref.util')),
        PythonModule(version=3,
                deps=('wsgiref', 'os', 'time', 'traceback', 'wsgiref.headers',
                        'wsgiref.util'))),

    'wsgiref.headers': (
        PythonModule(version=2, deps=('wsgiref', 're', 'types')),
        PythonModule(version=3, deps=('wsgiref', 're'))),

    'wsgiref.simple_server': (
        PythonModule(version=2,
                deps=('wsgiref', 'BaseHTTPServer', 'urllib',
                        'wsgiref.handlers')),
        PythonModule(version=3,
                deps=('wsgiref', 'http.server', 'platform', 'urllib.parse',
                        'wsgiref.handlers'))),

    'wsgiref.util': (
        PythonModule(version=2, deps=('wsgiref', 'posixpath', 'urllib')),
        PythonModule(version=3,
                deps=('wsgiref', 'posixpath', 'urllib.parse'))),

    'wsgiref.validate': (
        PythonModule(version=2, deps=('wsgiref', 're', 'types', 'warnings')),
        PythonModule(version=3, deps=('wsgiref', 're', 'warnings'))),

    'xdrlib': (
        PythonModule(max_version=(2, 7, 8), deps=('cStringIO', 'struct')),
        PythonModule(min_version=(2, 7, 9), max_version=2,
                deps=('cStringIO', 'functools', 'struct')),
        PythonModule(min_version=3, max_version=(3, 4, 2),
                deps=('io', 'struct')),
        PythonModule(min_version=(3, 4, 3),
                deps=('functools', 'io', 'struct'))),

    'xml':
        PythonModule(
                modules=('xml.dom', 'xml.etree', 'xml.parsers', 'xml.sax')),

    'xml.dom':
        PythonModule(deps=('xml', 'xml.dom.domreg'),
                modules=('xml.dom.minidom', 'xml.dom.pulldom')),

    'xml.dom.minidom': (
        PythonModule(version=2,
                deps=('xml.dom', 'codecs', 'StringIO', 'xml.dom.minicompat',
                        'xml.dom.xmlbuilder')),
        PythonModule(version=3,
                deps=('xml.dom', 'codecs', 'io', 'xml.dom.minicompat',
                        'xml.dom.xmlbuilder'))),

    'xml.dom.pulldom': (
        PythonModule(version=2,
                deps=('xml.dom', 'cStringIO', 'types', 'xml.dom.minidom',
                        'xml.sax.handler')),
        PythonModule(version=3,
                deps=('xml.dom', 'io', 'xml.dom.minidom', 'xml.sax.handler'))),

    'xml.etree': (
        PythonModule(version=2, deps='xml',
                modules=('xml.etree.cElementTree', 'xml.etree.ElementTree')),
        PythonModule(version=3, deps='xml', modules='xml.etree.ElementTree')),

    'xml.etree.cElementTree':
        PythonModule(version=2, deps=('xml.etree', '_elementtree')),

    'xml.etree.ElementTree': (
        PythonModule(version=2,
                deps=('xml.etree', 're', 'warnings', 'xml.etree.ElementPath',
                        'xml.parsers.expat')),
        PythonModule(version=3,
                deps=('xml.etree', 'contextlib', '_elementtree', 'io',
                        'locale', 're', 'warnings', 'xml.etree.ElementPath',
                        'xml.parsers.expat'))),

    'xml.parsers':
        PythonModule(deps='xml', modules='xml.parsers.expat'),

    'xml.parsers.expat':
        PythonModule(deps=('xml.parsers', 'pyexpat')),

    'xml.sax': (
        PythonModule(version=2,
                deps=('xml.sax', 'cStringIO', 'os', 'xml.sax._exceptions',
                        'xml.sax.handler', 'xml.sax.xmlreader'),
                modules=('xml.sax.handler', 'xml.sax.saxutils',
                        'xml.sax.xmlreader')),
        PythonModule(version=3,
                deps=('xml.sax', 'io', 'os', 'xml.sax._exceptions',
                        'xml.sax.handler', 'xml.sax.xmlreader'),
                modules=('xml.sax.handler', 'xml.sax.saxutils',
                        'xml.sax.xmlreader'))),

    'xml.sax.handler':
        PythonModule(deps='xml.sax'),

    'xml.sax.saxutils': (
        PythonModule(version=2,
                deps=('xml.sax', 'io', 'os', 'types', 'urlparse', 'urllib',
                        'xml.sax.handler', 'xml.sax.xmlreader')),
        PythonModule(version=3,
                deps=('xml.sax', 'codecs', 'io', 'os', 'urllib.parse',
                        'urllib.request', 'xml.sax.handler',
                        'xml.sax.xmlreader'))),

    'xml.sax.xmlreader':
        PythonModule(
                deps=('xml.sax', 'xml.sax._exceptions', 'xml.sax.handler',
                        'xml.sax.saxutils')),

    'xmlrpc':
        PythonModule(version=3, modules=('xmlrpc.client', 'xmlrpc.server')),

    'xmlrpc.client':
        PythonModule(version=3,
                deps=('xmlrpc', 'base64', 'datetime', 'errno', 'http.client',
                        'io', 'socket', 'time', 'urllib.parse',
                        'xml.parsers.expat')),

    'xmlrpc.server':
        PythonModule(version=3,
                deps=('xmlrpc', 'fcntl', 'http.server', 'inspect', 'os',
                        'pydoc', 're', 'socketserver', 'traceback',
                        'xmlrpc.client')),

    'xmlrpclib':
        PythonModule(version=2,
                deps=('base64', 'cStringIO', 'datetime', 'errno', 'httplib',
                        'operator', 're', 'socket', 'string', 'time', 'types',
                        'urllib', 'xml.parsers.expat')),

    'zipapp':
        PythonModule(min_version=(3, 5),
                deps=('contextlib', 'os', 'pathlib', 'shutil', 'stat',
                        'zipfile')),

    'zipfile': (
        PythonModule(version=2,
                deps=('binascii', 'cStringIO', 'io', 'os', 're', 'shutil',
                        'stat', 'string', 'struct', 'time', 'zlib')),
        PythonModule(version=(3, 3),
                deps=('binascii', 'imp', 'io', 'os', 're', 'shutil', 'stat',
                        'struct', 'time', 'warnings', 'zlib')),
        PythonModule(version=(3, 4),
                deps=('binascii', 'importlib.util', 'io', 'os', 're', 'shutil',
                        'stat', 'struct', 'time', 'warnings', 'zlib')),
        PythonModule(min_version=(3, 5),
                deps=('binascii', 'importlib.util', 'io', 'os', 're', 'shutil',
                        'stat', 'struct', 'threading', 'time', 'warnings',
                        'zlib'))),

    'zipimport':
        ExtensionModule(source='zipimport.c', deps='zlib'),

    'zlib':
        ExtensionModule(source='zlibmodule.c', xlib='zlib'),

    # These are internal modules.

    '_abcoll':
        PythonModule(version=2, internal=True, deps='abc'),

    '_ast':
        CoreExtensionModule(internal=True),

    'asyncio.base_events': (
        PythonModule(min_version=(3, 4, 0), max_version=(3, 4, 1),
                internal=True,
                deps=('asyncio', 'asyncio.events', 'asyncio.futures',
                        'asyncio.log', 'asyncio.tasks', 'collections',
                        'concurrent.futures', 'heapq', 'logging', 'os',
                        'socket', 'subprocess', 'time')),
        PythonModule(version=(3, 4, 2), internal=True,
                deps=('asyncio', 'asyncio.coroutines', 'asyncio.events',
                        'asyncio.futures', 'asyncio.log', 'asyncio.tasks',
                        'collections', 'concurrent.futures', 'heapq',
                        'inspect', 'logging', 'os', 'socket', 'subprocess',
                        'time', 'traceback')),
        PythonModule(version=(3, 4, 3), internal=True,
                deps=('asyncio', 'asyncio.coroutines', 'asyncio.events',
                        'asyncio.futures', 'asyncio.log', 'asyncio.tasks',
                        'collections', 'concurrent.futures', 'heapq',
                        'inspect', 'logging', 'os', 'socket', 'subprocess',
                        'threading', 'time', 'traceback', 'warnings')),
        PythonModule(version=(3, 4, 4), internal=True,
                deps=('asyncio', 'asyncio.compat', 'asyncio.coroutines',
                        'asyncio.events', 'asyncio.futures', 'asyncio.log',
                        'asyncio.tasks', 'collections', 'concurrent.futures',
                        'heapq', 'inspect', 'itertools', 'logging', 'os',
                        'socket', 'subprocess', 'threading', 'time',
                        'traceback', 'warnings')),
        PythonModule(version=(3, 5, 0), internal=True,
                deps=('asyncio', 'asyncio.compat', 'asyncio.coroutines',
                        'asyncio.events', 'asyncio.futures', 'asyncio.log',
                        'asyncio.tasks', 'collections', 'concurrent.futures',
                        'heapq', 'inspect', 'logging', 'os', 'socket',
                        'subprocess', 'threading', 'time', 'traceback',
                        'warnings')),
        PythonModule(min_version=(3, 5, 1), internal=True,
                deps=('asyncio', 'asyncio.compat', 'asyncio.coroutines',
                        'asyncio.events', 'asyncio.futures', 'asyncio.log',
                        'asyncio.tasks', 'collections', 'concurrent.futures',
                        'heapq', 'inspect', 'itertools', 'logging', 'os',
                        'socket', 'subprocess', 'threading', 'time',
                        'traceback', 'warnings'))),

    'asyncio.base_subprocess': (
        PythonModule(min_version=(3, 4, 0), max_version=(3, 4, 1),
                internal=True,
                deps=('asyncio', 'asyncio.protocols', 'asyncio.tasks',
                        'asyncio.transports', 'collections', 'subprocess')),
        PythonModule(version=(3, 4, 2), internal=True,
                deps=('asyncio', 'asyncio.coroutines', 'asyncio.log',
                        'asyncio.protocols', 'asyncio.transports',
                        'collections', 'subprocess')),
        PythonModule(version=(3, 4, 3), internal=True,
                deps=('asyncio', 'asyncio.coroutines', 'asyncio.futures',
                        'asyncio.log', 'asyncio.protocols',
                        'asyncio.transports', 'collections', 'subprocess',
                        'warnings')),
        PythonModule(min_version=(3, 4, 4), internal=True,
                deps=('asyncio', 'asyncio.compat', 'asyncio.coroutines',
                        'asyncio.futures', 'asyncio.log', 'asyncio.protocols',
                        'asyncio.transports', 'collections', 'subprocess',
                        'warnings'))),

    'asyncio.compat':
        PythonModule(min_version=(3, 4, 4), internal=True, deps='asyncio'),

    'asyncio.constants':
        PythonModule(min_version=(3, 4), internal=True, deps='asyncio'),

    'asyncio.coroutines': (
        PythonModule(min_version=(3, 4, 2), max_version=(3, 4, 3),
                internal=True,
                deps=('asyncio', 'asyncio.events', 'asyncio.futures',
                        'asyncio.log', 'functools', 'inspect', 'opcode', 'os',
                        'traceback', 'types')),
        PythonModule(min_version=(3, 4, 4), internal=True,
                deps=('asyncio', 'asyncio.compat', 'asyncio.events',
                        'asyncio.futures', 'asyncio.log', 'collections.abc',
                        'functools', 'inspect', 'opcode', 'os', 'traceback',
                        'types'))),

    'asyncio.events': (
        PythonModule(min_version=(3, 4, 0), max_version=(3, 4, 1),
                internal=True,
                deps=('asyncio', 'socket', 'subprocess', 'threading')),
        PythonModule(min_version=(3, 4, 2), max_version=(3, 4, 3),
                internal=True,
                deps=('asyncio', 'functools', 'inspect', 'reprlib', 'socket',
                        'subprocess', 'threading', 'traceback')),
        PythonModule(min_version=(3, 4, 4), internal=True,
                deps=('asyncio', 'asyncio.compat', 'functools', 'inspect',
                        'reprlib', 'socket', 'subprocess', 'threading',
                        'traceback'))),

    'asyncio.futures': (
        PythonModule(min_version=(3, 4, 0), max_version=(3, 4, 1),
                internal=True,
                deps=('asyncio', 'asyncio.events', 'concurrent.futures._base',
                        'logging', 'traceback')),
        PythonModule(min_version=(3, 4, 2), max_version=(3, 4, 3),
                internal=True,
                deps=('asyncio', 'asyncio.events', 'concurrent.futures._base',
                        'logging', 'reprlib', 'traceback')),
        PythonModule(min_version=(3, 4, 4), internal=True,
                deps=('asyncio', 'asyncio.compat', 'asyncio.events',
                        'concurrent.futures._base', 'logging', 'reprlib',
                        'traceback'))),

    'asyncio.locks': (
        PythonModule(min_version=(3, 4, 0), max_version=(3, 4, 1),
                internal=True,
                deps=('asyncio', 'asyncio.events', 'asyncio.futures',
                        'asyncio.tasks', 'collections')),
        PythonModule(min_version=(3, 4, 2), max_version=(3, 4, 3),
                internal=True,
                deps=('asyncio', 'asyncio.coroutines', 'asyncio.events',
                        'asyncio.futures', 'collections')),
        PythonModule(min_version=(3, 4, 4), internal=True,
                deps=('asyncio', 'asyncio.compat', 'asyncio.coroutines',
                        'asyncio.events', 'asyncio.futures', 'collections'))),

    'asyncio.log':
        PythonModule(min_version=(3, 4), internal=True,
                deps=('asyncio', 'logging')),

    'asyncio.proactor_events': (
        PythonModule(min_version=(3, 4, 0), max_version=(3, 4, 2),
                internal=True,
                deps=('asyncio', 'asyncio.base_events', 'asyncio.constants',
                        'asyncio.futures', 'asyncio.log', 'asyncio.transports',
                        'socket')),
        PythonModule(min_version=(3, 4, 3), max_version=(3, 4, 3),
                internal=True,
                deps=('asyncio', 'asyncio.base_events', 'asyncio.constants',
                        'asyncio.futures', 'asyncio.log', 'asyncio.sslproto',
                        'asyncio.transports', 'socket', 'warnings')),
        PythonModule(min_version=(3, 4, 4), internal=True,
                deps=('asyncio', 'asyncio.base_events', 'asyncio.compat',
                        'asyncio.constants', 'asyncio.futures', 'asyncio.log',
                        'asyncio.sslproto', 'asyncio.transports', 'socket',
                        'warnings'))),

    'asyncio.protocols':
        PythonModule(min_version=(3, 4), internal=True, deps='asyncio'),

    'asyncio.queues': (
        PythonModule(min_version=(3, 4), max_version=(3, 4, 3), internal=True,
                deps=('asyncio', 'asyncio.events', 'asyncio.futures',
                        'asyncio.locks', 'asyncio.tasks', 'collections',
                        'heapq')),
        PythonModule(min_version=(3, 4, 4), internal=True,
                deps=('asyncio', 'asyncio.compat', 'asyncio.coroutines',
                        'asyncio.events', 'asyncio.futures', 'asyncio.locks',
                        'collections', 'heapq'))),

    'asyncio.selector_events': (
        PythonModule(min_version=(3, 4, 0), max_version=(3, 4, 1),
                internal=True,
                deps=('asyncio', 'asyncio.base_events', 'asyncio.constants',
                        'asyncio.events', 'asyncio.futures', 'asyncio.log',
                        'asyncio.transports', 'collections', 'errno',
                        'selectors', 'socket', '?ssl')),
        PythonModule(version=(3, 4, 2), internal=True,
                deps=('asyncio', 'asyncio.base_events', 'asyncio.constants',
                        'asyncio.events', 'asyncio.futures', 'asyncio.log',
                        'asyncio.transports', 'collections', 'errno',
                        'functools', 'selectors', 'socket', '?ssl')),
        PythonModule(version=(3, 4, 3), internal=True,
                deps=('asyncio', 'asyncio.base_events', 'asyncio.constants',
                        'asyncio.coroutines', 'asyncio.events',
                        'asyncio.futures', 'asyncio.log', 'asyncio.sslproto',
                        'asyncio.transports', 'collections', 'errno',
                        'functools', 'selectors', 'socket', '?ssl',
                        'warnings')),
        PythonModule(min_version=(3, 4, 4), internal=True,
                deps=('asyncio', 'asyncio.base_events', 'asyncio.compat',
                        'asyncio.constants', 'asyncio.coroutines',
                        'asyncio.events', 'asyncio.futures', 'asyncio.log',
                        'asyncio.sslproto', 'asyncio.transports',
                        'collections', 'errno', 'functools', 'selectors',
                        'socket', '?ssl', 'warnings'))),

    'asyncio.sslproto': (
        PythonModule(version=(3, 4, 3), internal=True,
                deps=('asyncio', 'asyncio.log', 'asyncio.protocols',
                        'asyncio.transports', 'collections', '?ssl',
                        'warnings')),
        PythonModule(min_version=(3, 4, 4), internal=True,
                deps=('asyncio', 'asyncio.compat', 'asyncio.log',
                        'asyncio.protocols', 'asyncio.transports',
                        'collections', '?ssl', 'warnings'))),

    'asyncio.streams': (
        PythonModule(min_version=(3, 4, 0), max_version=(3, 4, 1),
                internal=True,
                deps=('asyncio', 'asyncio.events', 'asyncio.futures',
                        'asyncio.protocols', 'asyncio.tasks', 'socket')),
        PythonModule(min_version=(3, 4, 2), max_version=(3, 4, 3),
                internal=True,
                deps=('asyncio', 'asyncio.coroutines', 'asyncio.events',
                        'asyncio.futures', 'asyncio.log', 'asyncio.protocols',
                        'socket')),
        PythonModule(min_version=(3, 4, 4), internal=True,
                deps=('asyncio', 'asyncio.compat', 'asyncio.coroutines',
                        'asyncio.events', 'asyncio.futures', 'asyncio.log',
                        'asyncio.protocols', 'socket'))),

    'asyncio.subprocess': (
        PythonModule(min_version=(3, 4, 0), max_version=(3, 4, 1),
                internal=True,
                deps=('asyncio', 'asyncio.events', 'asyncio.futures',
                        'asyncio.protocols', 'asyncio.streams',
                        'asyncio.tasks', 'collections', 'subprocess')),
        PythonModule(min_version=(3, 4, 2), max_version=(3, 4, 3),
                internal=True,
                deps=('asyncio', 'asyncio.coroutines', 'asyncio.events',
                        'asyncio.futures', 'asyncio.log', 'asyncio.protocols',
                        'asyncio.streams', 'asyncio.tasks', 'collections',
                        'subprocess')),
        PythonModule(min_version=(3, 4, 4), internal=True,
                deps=('asyncio', 'asyncio.coroutines', 'asyncio.events',
                        'asyncio.log', 'asyncio.protocols', 'asyncio.streams',
                        'asyncio.tasks', 'subprocess'))),

    'asyncio.tasks': (
        PythonModule(min_version=(3, 4, 0), max_version=(3, 4, 1),
                internal=True,
                deps=('asyncio', 'asyncio.events', 'asyncio.futures',
                        'asyncio.log', 'asyncio.queues', 'asyncio.tasks',
                        'concurrent.futures', 'functools', 'inspect',
                        'linecache', 'os', 'traceback', 'weakref')),
        PythonModule(min_version=(3, 4, 2), max_version=(3, 4, 3),
                internal=True,
                deps=('asyncio', 'asyncio.coroutines', 'asyncio.events',
                        'asyncio.futures', 'asyncio.queues', 'asyncio.tasks',
                        'concurrent.futures', 'functools', 'inspect',
                        'linecache', 'traceback', 'weakref')),
        PythonModule(min_version=(3, 4, 4), internal=True,
                deps=('asyncio', 'asyncio.compat', 'asyncio.coroutines',
                        'asyncio.events', 'asyncio.futures', 'asyncio.queues',
                        'asyncio.tasks', 'concurrent.futures', 'functools',
                        'inspect', 'linecache', 'traceback', 'warnings',
                        'weakref'))),

    'asyncio.transports': (
        PythonModule(min_version=(3, 4), max_version=(3, 4, 3), internal=True,
                deps='asyncio'),
        PythonModule(min_version=(3, 4, 4), internal=True,
                deps=('asyncio', 'asyncio.compat'))),

    'asyncio.unix_events': (
        PythonModule(min_version=(3, 4, 0), max_version=(3, 4, 1),
                internal=True, scope='!win32',
                deps=('asyncio', 'asyncio.base_events',
                        'asyncio.base_subprocess', 'asyncio.constants',
                        'asyncio.events', 'asyncio.log',
                        'asyncio.selector_events', 'asyncio.tasks',
                        'asyncio.transports', 'errno', 'fcntl', 'os', 'signal',
                        'socket', 'stat', 'subprocess', 'threading')),
        PythonModule(version=(3, 4, 2), internal=True, scope='!win32',
                deps=('asyncio', 'asyncio.base_events',
                        'asyncio.base_subprocess', 'asyncio.coroutines',
                        'asyncio.constants', 'asyncio.events', 'asyncio.log',
                        'asyncio.selector_events', 'asyncio.transports',
                        'errno', 'fcntl', 'os', 'signal', 'socket', 'stat',
                        'subprocess', 'threading')),
        PythonModule(version=(3, 4, 3), internal=True, scope='!win32',
                deps=('asyncio', 'asyncio.base_events',
                        'asyncio.base_subprocess', 'asyncio.coroutines',
                        'asyncio.constants', 'asyncio.events',
                        'asyncio.futures', 'asyncio.log',
                        'asyncio.selector_events', 'asyncio.transports',
                        'errno', 'fcntl', 'os', 'signal', 'socket', 'stat',
                        'subprocess', 'threading', 'warnings')),
        PythonModule(min_version=(3, 4, 4), internal=True, scope='!win32',
                deps=('asyncio', 'asyncio.base_events',
                        'asyncio.base_subprocess', 'asyncio.compat',
                        'asyncio.coroutines', 'asyncio.constants',
                        'asyncio.events', 'asyncio.futures', 'asyncio.log',
                        'asyncio.selector_events', 'asyncio.transports',
                        'errno', 'fcntl', 'os', 'signal', 'socket', 'stat',
                        'subprocess', 'threading', 'warnings'))),

    'asyncio.windows_events': (
        PythonModule(min_version=(3, 4, 0), max_version=(3, 4, 1),
                internal=True, scope='win32',
                deps=('asyncio', 'asyncio.events', 'asyncio.base_subprocess',
                        'asyncio.log', 'asyncio.proactor_events',
                        'asyncio.selector_events', 'asyncio.tasks',
                        'asyncio.windows_utils', 'errno', 'math', 'socket',
                        'struct', 'weakref', '_winapi')),
        PythonModule(min_version=(3, 4, 2), internal=True, scope='win32',
                deps=('asyncio', 'asyncio.events', 'asyncio.base_subprocess',
                        'asyncio.coroutines', 'asyncio.log',
                        'asyncio.proactor_events', 'asyncio.selector_events',
                        'asyncio.tasks', 'asyncio.windows_utils', 'errno',
                        'math', 'socket', 'struct', 'weakref', '_winapi'))),

    'asyncio.windows_utils': (
        PythonModule(min_version=(3, 4), max_version=(3, 4, 2),
                internal=True, scope='win32',
                deps=('asyncio', 'itertools', 'msvcrt', 'os', 'socket',
                        'subprocess', 'tempfile', '_winapi')),
        PythonModule(min_version=(3, 4, 3), internal=True, scope='win32',
                deps=('asyncio', 'itertools', 'msvcrt', 'os', 'socket',
                        'subprocess', 'tempfile', 'warnings', '_winapi'))),

    '_bisect':
        ExtensionModule(internal=True, source='_bisectmodule.c'),

    '_bootlocale':
        PythonModule(min_version=(3, 4), internal=True, deps='_locale'),

    'bsddb.db':
        PythonModule(version=2, internal=True, deps=('bsddb', '_bsddb')),

    'bsddb.dbutils':
        PythonModule(version=2, internal=True,
                deps=('bsddb', 'bsddb.db', 'time')),

    '_bsddb':
        ExtensionModule(version=2, internal=True, source='_bsddb.c',
                xlib='bsddb', pyd='_bsddb.pyd'),

    '_bz2':
        ExtensionModule(version=3, internal=True, source='_bz2module.c',
                xlib='bz2', pyd='_bz2.pyd'),

    'cl':
        ExtensionModule(version=2, internal=True, source='clmodule.c'),

    '_codecs':
        CoreExtensionModule(internal=True),

    '_codecs_cn':
        ExtensionModule(internal=True, source='cjkcodecs/_codecs_cn.c'),

    '_codecs_hk':
        ExtensionModule(internal=True, source='cjkcodecs/_codecs_hk.c'),

    '_codecs_iso2022':
        ExtensionModule(internal=True, source='cjkcodecs/_codecs_iso2022.c'),

    '_codecs_jp':
        ExtensionModule(internal=True, source='cjkcodecs/_codecs_jp.c'),

    '_codecs_kr':
        ExtensionModule(internal=True, source='cjkcodecs/_codecs_kr.c'),

    '_codecs_tw':
        ExtensionModule(internal=True, source='cjkcodecs/_codecs_tw.c'),

    '_collections': (
        ExtensionModule(version=2, internal=True,
                source='_collectionsmodule.c'),
        CoreExtensionModule(version=3, internal=True)),

    '_collections_abc':
        PythonModule(min_version=(3, 4), internal=True, deps='abc'),

    '_compat_pickle':
        PythonModule(version=3, internal=True),

    '_compression':
        PythonModule(min_version=(3, 5), internal=True, deps='io'),

    'concurrent.futures._base':
        PythonModule(version=3, internal=True,
                deps=('concurrent.futures', 'collections', 'logging',
                        'threading', 'time')),

    'concurrent.futures.process': (
        PythonModule(min_version=3, max_version=(3, 4), internal=True,
                deps=('concurrent.futures', 'atexit',
                        'concurrent.futures._base', 'multiprocessing',
                        'multiprocessing.connection', 'multiprocessing.queues',
                        'os', 'queue', 'threading', 'weakref')),
        PythonModule(min_version=(3, 5), internal=True,
                deps=('concurrent.futures', 'atexit',
                        'concurrent.futures._base', 'functools', 'itertools',
                        'multiprocessing', 'multiprocessing.connection',
                        'multiprocessing.queues', 'os', 'queue', 'threading',
                        'traceback', 'weakref'))),

    'concurrent.futures.thread': (
        PythonModule(min_version=3, max_version=(3, 4), internal=True,
                deps=('concurrent.futures', 'atexit',
                        'concurrent.futures._base', 'queue', 'threading',
                        'weakref')),
        PythonModule(min_version=(3, 5), internal=True,
                deps=('concurrent.futures', 'atexit',
                        'concurrent.futures._base', 'os', 'queue', 'threading',
                        'weakref'))),

    '_crypt':
        ExtensionModule(version=3, internal=True, scope='!win32',
                source='_cryptmodule.c'),

    '_csv':
        ExtensionModule(internal=True, source='_csv.c'),

    '_ctypes':
        ExtensionModule(internal=True,
                source=('_ctypes/_ctypes.c', '_ctypes/callbacks.c',
                        '_ctypes/callproc.c', '_ctypes/stgdict.c',
                        '_ctypes/cfield.c',
                        'macx#_ctypes/malloc_closure.c',
                        'macx#_ctypes/darwin/dlfcn_simple.c',
                        'macx#_ctypes/libffi_osx/ffi.c',
                        'macx#_ctypes/libffi_osx/x86/darwin64.S',
                        'macx#_ctypes/libffi_osx/x86/x86-darwin.S',
                        'macx#_ctypes/libffi_osx/x86/x86-ffi_darwin.c',
                        'macx#_ctypes/libffi_osx/x86/x86-ffi64.c',
                        'win32#_ctypes/malloc_closure.c',
                        'win32#_ctypes/libffi_msvc/prep_cif.c',
                        'win32#_ctypes/libffi_msvc/ffi.c',
                        'win32_x86#_ctypes/libffi_msvc/win32.c',
                        'win32_x64#_ctypes/libffi_msvc/win64.asm'),
                defines='macx#MACOSX',
                includepath=('_ctypes',
                        'macx#_ctypes/darwin',
                        'macx#_ctypes/libffi_osx/include',
                        'win32#_ctypes/libffi_msvc'),
                libs='linux-*#-lffi',
                pyd='_ctypes.pyd'),

    'ctypes._endian':
        PythonModule(internal=True, deps='ctypes'),

    'ctypes.macholib':
        PythonModule(internal=True, scope='macx', deps='ctypes',
                modules=('ctypes.macholib.dyld', 'ctypes.macholib.dylib',
                        'ctypes.macholib.framework')),

    'ctypes.macholib.dyld':
        PythonModule(internal=True, scope='macx',
                deps=('ctypes.macholib', 'ctypes.macholib.dylib',
                        'ctypes.macholib.framework', 'itertools', 'os')),

    'ctypes.macholib.dylib':
        PythonModule(internal=True, scope='macx',
                deps=('ctypes.macholib', 're')),

    'ctypes.macholib.framework':
        PythonModule(internal=True, scope='macx',
                deps=('ctypes.macholib', 're')),

    'curses.has_key':
        PythonModule(internal=True, scope='!win32',
                deps=('curses', '_curses')),

    'curses.wrapper':
        PythonModule(version=2, internal=True, scope='!win32', deps='curses'),

    '_curses':
        ExtensionModule(internal=True, scope='!win32',
                source='_cursesmodule.c', xlib='curses'),

    '_curses_panel':
        ExtensionModule(internal=True, scope='!win32',
                source='_curses_panel.c', xlib='panel'),

    '_datetime':
        ExtensionModule(version=3, internal=True, source='_datetimemodule.c'),

    '_dbm':
        ExtensionModule(version=3, internal=True, source='_dbmmodule.c',
                defines='HAVE_NDBM_H', xlib='ndbm'),

    'distutils.config': (
        PythonModule(version=2,
                deps=('ConfigParser', 'distutils.cmd', 'os')),
        PythonModule(version=3,
                deps=('cgi', 'configparser', 'distutils.cmd', 'os'))),

    'distutils.msvc9compiler': (
        PythonModule(version=2,
                deps=('distutils.ccompiler', 'distutils.errors',
                        'distutils.log', 'distutils.util', 'os', 're',
                        'subprocess', '_winreg')),
        PythonModule(version=3,
                deps=('distutils.ccompiler', 'distutils.errors',
                        'distutils.log', 'distutils.util', 'os', 're',
                        'subprocess', 'winreg'))),

    'distutils._msvccompiler':
        PythonModule(min_version=(3, 5),
                deps=('distutils.ccompiler', 'distutils.errors',
                        'distutils.log', 'distutils.util', 'itertools', 'os',
                        'shutil', 'stat', 'subprocess', 'winreg')),

    'distutils.versionpredicate':
        PythonModule(
                deps=('distutils.version', 'operator', 're')),

    '_elementtree': (
        ExtensionModule(version=2, internal=True,
                source='_elementtree.c',
                defines=('win32#COMPILED_FROM_DSP',
                        '!win32#HAVE_EXPAT_CONFIG_H', 'USE_PYEXPAT_CAPI'),
                deps='pyexpat', pyd='_elementtree.pyd'),
        ExtensionModule(version=3, internal=True,
                source='_elementtree.c',
                defines=('win32#COMPILED_FROM_DSP',
                        '!win32#HAVE_EXPAT_CONFIG_H', 'USE_PYEXPAT_CAPI'),
                deps=('copy', 'pyexpat', 'xml.etree.ElementPath'),
                pyd='_elementtree.pyd')),

    'email.base64mime': (
        PythonModule(version=2, internal=True,
                deps=('email', 'binascii', 'email.utils')),
        PythonModule(version=3, internal=True,
                deps=('email', 'base64', 'binascii'))),

    'email._encoded_words':
        PythonModule(version=3, internal=True,
                deps=('email', 'base64', 'binascii', 'email.errors',
                        'functools', 're', 'string')),

    'email.feedparser': (
        PythonModule(version=2, internal=True,
                deps=('email', 'email.errors', 'email.message', 're')),
        PythonModule(min_version=3, max_version=(3, 4), internal=True,
                deps=('email', 'email.errors', 'email.message',
                        'email._policybase', 're')),
        PythonModule(min_version=(3, 5), internal=True,
                deps=('email', 'collections', 'email.errors', 'email.message',
                        'email._policybase', 're'))),

    'email._header_value_parser': (
        PythonModule(min_version=3, max_version=(3, 4, 3), internal=True,
                deps=('email', 'collections', 'email._encoded_words',
                        'email.errors', 'email.utils', 're', 'string',
                        'urllib')),
        PythonModule(min_version=(3, 4, 4), internal=True,
                deps=('email', 'collections', 'email._encoded_words',
                        'email.errors', 'email.utils', 'operator', 're',
                        'string', 'urllib'))),

    'email._parseaddr':
        PythonModule(internal=True, deps=('email', 'calendar', 'time')),

    'email._policybase':
        PythonModule(version=3, internal=True,
                deps=('email', 'abc', 'email.charset', 'email.header',
                        'email.utils')),

    'email.quoprimime': (
        PythonModule(version=2, internal=True,
                deps=('email', 'email.utils', 're', 'string')),
        PythonModule(version=(3, 3), internal=True,
                deps=('email', 'io', 're', 'string')),
        PythonModule(min_version=(3, 4), internal=True,
                deps=('email', 're', 'string'))),

    'encodings.aliases': (
        PythonModule(version=2, internal=True, deps='encodings'),
        CorePythonModule(version=3, internal=True, deps='encodings')),

    '_functools': (
        ExtensionModule(version=2, internal=True, source='_functoolsmodule.c'),
        CoreExtensionModule(version=3, internal=True)),

    '_gdbm':
        ExtensionModule(version=3, internal=True, source='_gdbmmodule.c',
                xlib='gdbm'),

    'genericpath':
        PythonModule(internal=True, deps=('os', 'stat')),

    'gestalt':
        ExtensionModule(version=2, internal=True, scope='macx',
                source='../Mac/Modules/gestaltmodule.c'),

    '_gestalt':
        ExtensionModule(version=(3, 3), internal=True, scope='macx',
                source='_gestalt.c'),

    '_hashlib':
        ExtensionModule(internal=True, source='_hashopenssl.c', xlib='ssl',
                pyd='_hashlib.pyd'),

    '_heapq':
        ExtensionModule(internal=True, source='_heapqmodule.c'),

    '_hotshot':
        ExtensionModule(version=2, internal=True, source='_hotshotmodule.c'),

    'hotshot.log':
        PythonModule(version=2, internal=True,
                deps=('hotshot', '_hotshot', 'os', 'parser', 'symbol')),

    '_imp':
        CoreExtensionModule(version=3, internal=True),

    'importlib._bootstrap':
        CorePythonModule(version=3, internal=True, builtin=True,
                deps='importlib'),

    'importlib._bootstrap_external':
        CorePythonModule(min_version=(3, 5), internal=True, builtin=True,
                deps='importlib'),

    '_io': (
        ExtensionModule(version=2, internal=True,
                source=('_io/bufferedio.c', '_io/bytesio.c', '_io/fileio.c',
                        '_io/iobase.c', '_io/_iomodule.c', '_io/stringio.c',
                        '_io/textio.c'),
                includepath='_io'),
        CoreExtensionModule(version=(3, 3), internal=True),
        CoreExtensionModule(min_version=(3, 4), internal=True,
                deps='_bootlocale')),

    '_json':
        ExtensionModule(internal=True, source='_json.c'),

    'json.decoder': (
        PythonModule(version=2, internal=True,
                deps=('json', 'json.scanner', '_json', 're', 'struct')),
        PythonModule(version=(3, 3), internal=True,
                deps=('json', 'binascii', 'json.scanner', '_json', 're',
                        'struct')),
        PythonModule(min_version=(3, 4), internal=True,
                deps=('json', 'json.scanner', '_json', 're'))),

    'json.encoder':
        PythonModule(internal=True, deps=('json', '_json', 're')),

    'json.scanner':
        PythonModule(internal=True, deps=('_json', 're')),

    '_locale': (
        ExtensionModule(version=2, internal=True, source='_localemodule.c'),
        CoreExtensionModule(version=3, internal=True)),

    '_lsprof':
        ExtensionModule(internal=True, source=('_lsprof.c', 'rotatingtree.c')),

    '_LWPCookieJar':
        PythonModule(version=2, internal=True,
                deps=('cookielib', 're', 'time')),

    '_lzma':
        ExtensionModule(version=3, internal=True, source='_lzmamodule.c',
                xlib='lzma', pyd='_lzma.pyd'),

    'markupbase':
        PythonModule(version=2, internal=True, deps='re'),

    '_markupbase':
        PythonModule(version=3, internal=True, deps='re'),

    '_md5': (
        ExtensionModule(version=2, internal=True,
                source=('md5module.c', 'md5.c')),
        ExtensionModule(version=3, internal=True, source='md5module.c')),

    '_MozillaCookieJar':
        PythonModule(version=2, internal=True,
                deps=('cookielib', 're', 'time')),

    '_msi':
        ExtensionModule(internal=True, scope='win32', source='../PC/_msi.c',
                libs=('-lfci', '-lmsi', '-lrpcrt4'), pyd='_msi.pyd'),

    '_multibytecodec':
        ExtensionModule(internal=True, source='cjkcodecs/multibytecodec.c'),

    '_multiprocessing': (
        ExtensionModule(version=2, internal=True,
                source=('_multiprocessing/multiprocessing.c',
                        'win32#_multiprocessing/pipe_connection.c',
                        '_multiprocessing/semaphore.c',
                        '_multiprocessing/socket_connection.c',
                        'win32#_multiprocessing/win32_functions.c'),
                libs=('win32#-lws2_32', 'linux-*#-lrt'),
                includepath='_multiprocessing',
                pyd='_multiprocessing.pyd'),
        ExtensionModule(version=3, internal=True,
                source=('_multiprocessing/multiprocessing.c',
                        '_multiprocessing/semaphore.c'),
                includepath='_multiprocessing',
                pyd='_multiprocessing.pyd')),

    'multiprocessing.context':
        PythonModule(min_version=(3, 4), internal=True,
                deps=('multiprocessing', 'multiprocessing.connection',
                        'multiprocessing.forkserver',
                        'multiprocessing.managers', 'multiprocessing.pool',
                        'multiprocessing.popen_fork',
                        'multiprocessing.popen_forkserver',
                        'multiprocessing.popen_spawn_posix',
                        'multiprocessing.popen_spawn_win32',
                        'multiprocessing.process',
                        'multiprocessing.queues',
                        'multiprocessing.sharedctypes',
                        'multiprocessing.spawn',
                        'multiprocessing.synchronize',
                        'multiprocessing.util', 'os', 'threading')),

    'multiprocessing.dummy.connection': (
        PythonModule(version=2, internal=True,
                deps=('multiprocessing.dummy', 'Queue')),
        PythonModule(version=3, internal=True,
                deps=('multiprocessing.dummy', 'queue'))),

    'multiprocessing.forking': (
        PythonModule(version=2, internal=True,
                deps=('multiprocessing', 'errno', 'functools', 'imp',
                        'multiprocessing.process', 'multiprocessing.util',
                        'msvcrt', 'os', 'pickle', 'signal', '_subprocess',
                        'thread', 'time')),
        PythonModule(version=(3, 3), internal=True,
                deps=('multiprocessing', 'copyreg', 'errno', 'functools',
                        'imp', 'multiprocessing.connection',
                        'multiprocessing.process', 'multiprocessing.util',
                        'msvcrt', 'os', 'pickle', 'signal', '_thread', 'time',
                        '_winapi'))),

    'multiprocessing.forkserver':
        PythonModule(min_version=(3, 4), internal=True,
                deps=('multiprocessing', 'errno', 'multiprocessing.connection',
                        'multiprocessing.process', 'multiprocessing.reduction',
                        'multiprocessing.semaphore_tracker',
                        'multiprocessing.spawn', 'multiprocessing.util', 'os',
                        'selectors', 'signal', 'socket', 'struct',
                        'threading')),

    'multiprocessing.heap': (
        PythonModule(version=2, internal=True,
                deps=('multiprocessing', 'bisect', 'itertools',
                        '_multiprocessing', 'multiprocessing.forking',
                        'multiprocessing.util', 'mmap', 'tempfile', 'os',
                        'threading')),
        PythonModule(version=(3, 3), internal=True,
                deps=('multiprocessing', 'bisect', 'itertools',
                        '_multiprocessing', 'multiprocessing.forking',
                        'multiprocessing.util', 'mmap', 'tempfile', 'os',
                        'threading', '_winapi')),
        PythonModule(min_version=(3, 4), internal=True,
                deps=('multiprocessing', 'bisect', 'multiprocessing.context',
                        'multiprocessing.reduction', 'multiprocessing.util',
                        'mmap', 'tempfile', 'os', 'threading', '_winapi'))),

    'multiprocessing.popen_fork': (
        PythonModule(version=(3, 4), internal=True,
                deps=('multiprocessing', 'errno', 'multiprocessing.connection',
                        'multiprocessing.util', 'os', 'signal')),
        PythonModule(min_version=(3, 5), internal=True,
                deps=('multiprocessing', 'multiprocessing.connection',
                        'multiprocessing.util', 'os', 'signal'))),

    'multiprocessing.popen_forkserver':
        PythonModule(min_version=(3, 4), internal=True,
                deps=('multiprocessing', 'io', 'multiprocessing.connection',
                        'multiprocessing.context',
                        'multiprocessing.forkserver',
                        'multiprocessing.popen_fork',
                        'multiprocessing.reduction',
                        'multiprocessing.spawn', 'multiprocessing.util',
                        'os')),

    'multiprocessing.popen_spawn_posix':
        PythonModule(min_version=(3, 4), internal=True,
                deps=('multiprocessing', 'io', 'multiprocessing.context',
                        'multiprocessing.popen_fork',
                        'multiprocessing.reduction',
                        'multiprocessing.semaphore_tracker',
                        'multiprocessing.spawn',
                        'multiprocessing.util', 'os')),

    'multiprocessing.popen_spawn_win32':
        PythonModule(min_version=(3, 4), internal=True, scope='win32',
                deps=('multiprocessing', 'msvcrt', 'multiprocessing.context',
                        'multiprocessing.reduction', 'multiprocessing.spawn',
                        'multiprocessing.util', 'os', 'signal', '_winapi')),

    'multiprocessing.process': (
        PythonModule(version=2, internal=True,
                deps=('multiprocessing', 'itertools',
                        'multiprocessing.forking', 'multiprocessing.util',
                        'os', 'signal', 'traceback')),
        PythonModule(version=(3, 3), internal=True,
                deps=('multiprocessing', 'itertools',
                        'multiprocessing.forking', 'multiprocessing.util',
                        'os', 'signal', 'traceback', '_weakrefset')),
        PythonModule(min_version=(3, 4), internal=True,
                deps=('multiprocessing', 'itertools',
                        'multiprocessing.context', 'multiprocessing.util',
                        'os', 'signal', 'traceback', '_weakrefset'))),

    'multiprocessing.queues': (
        PythonModule(version=2, internal=True,
                deps=('multiprocessing', 'atexit', 'collections',
                        '_multiprocessing', 'multiprocessing.forking',
                        'multiprocessing.synchronize', 'multiprocessing.util',
                        'os', 'Queue', 'threading', 'time', 'traceback',
                        'weakref')),
        PythonModule(version=(3, 3), internal=True,
                deps=('multiprocessing', 'collections', 'errno',
                        '_multiprocessing', 'multiprocessing.connection',
                        'multiprocessing.forking',
                        'multiprocessing.synchronize', 'multiprocessing.util',
                        'os', 'queue', 'threading', 'time', 'traceback',
                        'weakref')),
        PythonModule(min_version=(3, 4), max_version=(3, 4, 3), internal=True,
                deps=('multiprocessing', 'collections', 'errno',
                        '_multiprocessing', 'multiprocessing.connection',
                        'multiprocessing.context', 'multiprocessing.reduction',
                        'multiprocessing.util', 'os', 'queue', 'threading',
                        'time', 'traceback', 'weakref')),
        PythonModule(min_version=(3, 4, 4), internal=True,
                deps=('multiprocessing', 'collections', 'errno',
                        '_multiprocessing', 'multiprocessing.connection',
                        'multiprocessing.context', 'multiprocessing.reduction',
                        'multiprocessing.synchronize', 'multiprocessing.util',
                        'os', 'queue', 'threading', 'time', 'traceback',
                        'weakref'))),

    'multiprocessing.reduction': (
        PythonModule(version=2, internal=True,
                deps=('multiprocessing', '_multiprocessing',
                        'multiprocessing.connection',
                        'multiprocessing.forking', 'multiprocessing.util',
                        'os', 'socket', '_subprocess', 'threading',
                        'traceback')),
        PythonModule(version=(3, 3), internal=True,
                deps=('multiprocessing', 'multiprocessing.connection',
                        'multiprocessing.util', 'os', 'signal', 'socket',
                        'struct', 'threading', 'traceback', '_winapi')),
        PythonModule(min_version=(3, 4), internal=True,
                deps=('multiprocessing', 'array', 'copyreg', 'functools', 'io',
                        'multiprocessing.context',
                        'multiprocessing.resource_sharer', 'os', 'pickle',
                        'socket', '_winapi'))),

    'multiprocessing.resource_sharer':
        PythonModule(min_version=(3, 4), internal=True,
                deps=('multiprocessing', 'multiprocessing.connection',
                        'multiprocessing.process', 'multiprocessing.reduction',
                        'multiprocessing.util', 'os', 'signal', 'socket',
                        'threading')),

    'multiprocessing.semaphore_tracker':
        PythonModule(min_version=(3, 4), internal=True,
                deps=('multiprocessing', '_multiprocessing',
                        'multiprocessing.spawn', 'multiprocessing.util', 'os',
                        'signal', 'threading', 'warnings')),

    'multiprocessing.spawn':
        PythonModule(min_version=(3, 4), internal=True,
                deps=('multiprocessing', 'msvcrt', 'multiprocessing.process',
                        'multiprocessing.reduction',
                        'multiprocessing.semaphore_tracker',
                        'multiprocessing.util', 'os', 'pickle', 'runpy',
                        'types')),

    'multiprocessing.synchronize': (
        PythonModule(version=2, internal=True,
                deps=('multiprocessing', '_multiprocessing',
                        'multiprocessing.forking', 'multiprocessing.process',
                        'multiprocessing.util', 'os', 'threading', 'time')),
        PythonModule(version=(3, 3), internal=True,
                deps=('multiprocessing', '_multiprocessing',
                        'multiprocessing.forking', 'multiprocessing.process',
                        'multiprocessing.util', 'threading', 'time')),
        PythonModule(min_version=(3, 4), internal=True,
                deps=('multiprocessing', '_multiprocessing',
                        'multiprocessing.context', 'multiprocessing.heap',
                        'multiprocessing.process',
                        'multiprocessing.semaphore_tracker',
                        'multiprocessing.util', 'struct', 'threading', 'time',
                        'tempfile'))),

    'multiprocessing.util': (
        PythonModule(version=2, internal=True,
                deps=('multiprocessing', 'atexit', 'itertools', 'logging',
                        'multiprocessing.process', 'os', 'shutil',
                        'subprocess', 'tempfile', 'threading', 'traceback',
                        'weakref')),
        PythonModule(version=(3, 3), internal=True,
                deps=('multiprocessing', 'atexit', 'functools', 'itertools',
                        'logging', 'multiprocessing.process', 'os', 'shutil',
                        'subprocess', 'tempfile', 'threading', 'traceback',
                        'weakref')),
        PythonModule(min_version=(3, 4), internal=True,
                deps=('multiprocessing', 'atexit', 'itertools', 'logging',
                        'multiprocessing.process', 'os', '_posixsubprocess',
                        'shutil', 'subprocess', 'tempfile', 'threading',
                        'traceback', 'weakref'))),

    'nt':
        CoreExtensionModule(internal=True, scope='win32'),

    'ntpath':
        PythonModule(internal=True, scope='win32',
                deps=('genericpath', 'nt', 'os', 'stat', 'string',
                        'warnings')),

    'nturl2path': (
        PythonModule(version=2, internal=True, scope='win32',
                deps=('string', 'urllib')),
        PythonModule(version=3, internal=True, scope='win32',
                deps=('string', 'urllib.parse'))),

    'opcode': (
        PythonModule(max_version=(3, 3), internal=True),
        PythonModule(min_version=(3, 4), internal=True, deps='_opcode')),

    '_opcode':
        ExtensionModule(min_version=(3, 4), internal=True, source='_opcode.c'),

    '_operator':
        CoreExtensionModule(min_version=(3, 4), internal=True),

    '_osx_support':
        PythonModule(internal=True, deps=('contextlib', 'os', 're'),
                scope='macx'),

    '_pickle':
        ExtensionModule(version=3, internal=True, source='_pickle.c'),

    'posixpath':
        PythonModule(internal=True, scope='!win32',
                deps=('genericpath', 'os', 'pwd', 're', 'stat', 'warnings')),

    '_posixsubprocess':
        ExtensionModule(version=3, internal=True, scope='!win32',
                source='_posixsubprocess.c'),

    '_pydecimal':
        PythonModule(min_version=(3, 5), internal=True,
                deps=('collections', 'itertools', 'locale', 'math', 'numbers',
                        're', 'threading')),

    'pyexpat':
        ExtensionModule(internal=True,
                source=('expat/xmlparse.c', 'expat/xmlrole.c',
                        'expat/xmltok.c', 'pyexpat.c'),
                defines=('XML_STATIC', 'win32#COMPILED_FROM_DSP',
                        '!win32#HAVE_EXPAT_CONFIG_H'),
                includepath='expat',
                pyd='pyexpat.pyd'),

    '_random':
        ExtensionModule(internal=True, source='_randommodule.c'),

    '_scproxy': (
        ExtensionModule(version=2, internal=True, scope='macx',
                source='../Mac/Modules/_scproxy.c'),
        ExtensionModule(version=3, internal=True, scope='macx',
                source='_scproxy.c')),

    '_sha':
        ExtensionModule(version=2, internal=True, source='shamodule.c'),

    '_sha1':
        ExtensionModule(version=3, internal=True, source='sha1module.c'),

    '_sha256':
        ExtensionModule(internal=True, source='sha256module.c'),

    '_sha512':
        ExtensionModule(internal=True, source='sha512module.c'),

    '_signal':
        CoreExtensionModule(min_version=(3, 5)),

    '_socket': (
        ExtensionModule(version=2, internal=True,
                source=('socketmodule.c', 'timemodule.c'), pyd='_socket.pyd'),
        ExtensionModule(version=3, internal=True, source='socketmodule.c',
                pyd='_socket.pyd')),

    '_sqlite3':
        ExtensionModule(internal=True,
                source=('_sqlite/cache.c', '_sqlite/connection.c',
                        '_sqlite/cursor.c', '_sqlite/microprotocols.c',
                        '_sqlite/module.c', '_sqlite/prepare_protocol.c',
                        '_sqlite/row.c', '_sqlite/statement.c',
                        '_sqlite/util.c'),
                defines=('MODULE_NAME=\\\\\\"sqlite3\\\\\\"',
                        'SQLITE_OMIT_LOAD_EXTENSION'),
                includepath='_sqlite', xlib='sqlite3', pyd='_sqlite3.pyd',
                dlls='sqlite3.dll'),

    '_sre':
        CoreExtensionModule(internal=True),

    'sre_compile': (
        PythonModule(max_version=(3, 4, 2), internal=True,
                deps=('array', '_sre', 'sre_constants', 'sre_parse')),
        PythonModule(min_version=(3, 4, 3), internal=True,
                deps=('_sre', 'sre_constants', 'sre_parse'))),

    'sre_constants':
        PythonModule(internal=True, deps='_sre'),

    'sre_parse': (
        PythonModule(max_version=(2, 7, 9), internal=True,
                deps='sre_constants'),
        PythonModule(min_version=(2, 7, 10), max_version=2, internal=True,
                deps=('sre_constants', 'warnings')),
        PythonModule(version=3, internal=True,
                deps=('sre_constants', 'warnings'))),

    '_ssl':
        ExtensionModule(internal=True, source='_ssl.c', xlib='ssl',
                pyd='_ssl.pyd'),

    '_stat':
        CoreExtensionModule(min_version=(3, 4), internal=True),

    '_string':
        CoreExtensionModule(version=3, internal=True),

    'strop':
        ExtensionModule(version=2, internal=True, source='stropmodule.c'),

    '_strptime': (
        PythonModule(version=2, internal=True,
                deps=('calendar', 'datetime', 'locale', 're', 'thread',
                        'time')),
        PythonModule(version=3, internal=True,
                deps=('calendar', 'datetime', 'locale', 're', '_thread',
                        'time'))),

    # For Python v3.4 and later assume that the source code is compiled in
    # elsewhere (eg. by using the python.org Python library, or by using a
    # static Python library configured by pyqtdeploy).  This is because it
    # cannot be linked separately on Windows (because of the
    # PyVarObject_HEAD_INIT() problem).  This is probably a Python bug.
    '_struct': (
        ExtensionModule(max_version=(3, 3), internal=True, source='_struct.c'),
        ExtensionModule(min_version=(3, 4), internal=True,
                source='!win32#_struct.c')),

    '_subprocess':
        ExtensionModule(version=2, internal=True, scope='win32',
                source='../PC/_subprocess.c'),

    '_symtable':
        CoreExtensionModule(internal=True),

    '_sysconfigdata':
        PythonModule(internal=True),

    '_tracemalloc':
        CoreExtensionModule(min_version=(3, 4), internal=True),

    '_warnings':
        CoreExtensionModule(internal=True),

    '_weakref':
        CoreExtensionModule(internal=True),

    '_weakrefset':
        PythonModule(internal=True, deps='_weakref'),

    '_winapi':
        ExtensionModule(version=3, internal=True, scope='win32',
                source='_winapi.c'),

    'xml.dom.domreg': (
        PythonModule(version=2, internal=True,
                deps=('xml.dom', 'os', 'xml.dom.minicompat')),
        PythonModule(version=3, internal=True, deps=('xml.dom', 'os'))),

    'xml.dom.expatbuilder':
        PythonModule(internal=True,
                deps=('xml.dom', 'xml.dom.minicompat', 'xml.dom.minidom',
                        'xml.parsers.expat')),

    'xml.dom.minicompat':
        PythonModule(internal=True, deps='xml.dom'),

    'xml.dom.xmlbuilder': (
        PythonModule(version=2, internal=True,
                deps=('xml.dom', 'copy', 'posixpath', 'urllib2', 'urlparse',
                        'xml.dom.expatbuilder')),
        PythonModule(min_version=3, max_version=(3, 4), internal=True,
                deps=('xml.dom', 'copy', 'posixpath', 'urllib.parse',
                        'urllib.request', 'xml.dom.expatbuilder')),
        PythonModule(min_version=(3, 5), internal=True,
                deps=('xml.dom', 'copy', 'posixpath', 'urllib.parse',
                        'urllib.request', 'warnings',
                        'xml.dom.expatbuilder'))),

    'xml.etree.ElementPath':
        PythonModule(internal=True, deps=('xml.etree', 're')),

    'xml.sax._exceptions':
        PythonModule(internal=True, deps='xml.sax'),
}


# Meta-data is read-only so we cache and re-use it if possible.
_metadata_cache = {}


def get_python_metadata(version):
    """ Return the dict of StdlibModule instances for a particular version of
    Python.  It is assumed that the version is valid.
    """

    nr = _version_from_tuple(version)

    # Use the cached value if there is one.
    version_metadata = _metadata_cache.get(nr)
    if version_metadata is not None:
        return version_metadata

    _metadata_cache[nr] = version_metadata = {}

    for name, versions in _metadata.items():
        if not isinstance(versions, tuple):
            versions = (versions, )

        for versioned_module in versions:
            min_nr = _version_from_tuple(versioned_module.min_version)

            if nr >= min_nr:
                max_nr = _version_from_tuple(versioned_module.max_version)

                if nr <= max_nr:
                    version_metadata[name] = versioned_module.module
                    break

    return version_metadata


def _version_from_tuple(version):
    """ Convert a 3-tuple version to an integer. """

    return (version[0] << 16) + (version[1] << 8) + version[2]


if __name__ == '__main__':

    def check_modules(names, metadata, unused):
        """ Sanity check a list of module names. """

        for name in names:
            if name[0] in '?!':
                name = name[1:]

            module = metadata.get(name)
            if module is None:
                print("Unknown module '{0}'".format(name))
                continue

            try:
                del unused[name]
            except KeyError:
                pass

    def check_version(major, minor, patch=0):
        """ Carry out sanity checks for a particular version of Python. """

        print("Checking Python v{0}.{1}.{2}...".format(major, minor, patch))

        # Get the meta-data for this version.
        version_metadata = {}

        for name, versions in _metadata.items():
            if not isinstance(versions, tuple):
                versions = (versions, )

            # Check the version numbers.
            nr = _version_from_tuple((major, minor, patch))
            matches = []
            for module in versions:
                min_nr = _version_from_tuple(module.min_version)
                max_nr = _version_from_tuple(module.max_version)

                if min_nr > max_nr:
                    print("Module '{0}' version numbers are swapped".format(name))

                if nr >= min_nr and nr <= max_nr:
                    matches.append(module)

            nr_matches = len(matches)

            if nr_matches != 1:
                if nr_matches > 1:
                    print("Module '{0}' has overlapping versions".format(name))

                continue

            version_metadata[name] = matches[0]

        # Check all the dependencies and sub-modules exist.
        unused = version_metadata.copy()

        for name, versioned_module in version_metadata.items():
            module = versioned_module.module

            check_modules(module.deps, version_metadata, unused)

            if isinstance(module, PythonModule) and module.modules is not None:
                check_modules(module.modules, version_metadata, unused)

        # See if there are any internal, non-core modules that are unused.
        for name, versioned_module in unused.items():
            module = versioned_module.module

            if module.internal and not module.core:
                print("Unused module '{0}'".format(name))

    # Check each supported version.
    check_version(2, 7, 0)
    check_version(2, 7, 9)
    check_version(2, 7, 10)
    check_version(2, 7, 11)
    check_version(3, 3)
    check_version(3, 4, 0)
    check_version(3, 4, 1)
    check_version(3, 4, 2)
    check_version(3, 4, 3)
    check_version(3, 4, 4)
    check_version(3, 5, 0)
    check_version(3, 5, 1)
