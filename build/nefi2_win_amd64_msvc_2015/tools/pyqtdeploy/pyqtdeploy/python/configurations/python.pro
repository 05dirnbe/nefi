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


PY_MAJOR_VERSION = @PY_MAJOR_VERSION@
PY_MINOR_VERSION = @PY_MINOR_VERSION@
PY_PATCH_VERSION = @PY_PATCH_VERSION@
PY_DYNAMIC_LOADING = @PY_DYNAMIC_LOADING@

!defined(SYSROOT, var) {
    error("SYSROOT must be defined on the qmake command line")
}

TEMPLATE = lib

win32 {
    TARGET = python$${PY_MAJOR_VERSION}$${PY_MINOR_VERSION}
} else {
    TARGET = python$${PY_MAJOR_VERSION}.$${PY_MINOR_VERSION}
}

CONFIG -= qt
CONFIG += warn_off staticlib

# Work around QTBUG-39300.
CONFIG -= android_install

OBJECTS_DIR = .obj

DEFINES += NDEBUG Py_BUILD_CORE

INCLUDEPATH += . Include

win32 {
    INCLUDEPATH += PC
} else {
    QMAKE_CFLAGS_RELEASE = -O3
    QMAKE_CFLAGS += -fwrapv

    !greaterThan(PY_MAJOR_VERSION, 2) {
        QMAKE_CFLAGS += -fno-strict-aliasing
    }
}

win32 {
    DEFINES += PLATFORM=\\\"win32\\\"
}

macx {
    DEFINES += PLATFORM=\\\"darwin\\\"
}

unix:!macx {
    DEFINES += PLATFORM=\\\"linux\\\"
}

target.path = $$SYSROOT/lib

headers.path = $$SYSROOT/include/python$${PY_MAJOR_VERSION}.$${PY_MINOR_VERSION}
headers.files = pyconfig.h Include/*.h

stdlib.path = $$SYSROOT/lib/python$${PY_MAJOR_VERSION}.$${PY_MINOR_VERSION}
stdlib.files = Lib/*

INSTALLS += target headers stdlib

PARSER_SOURCES = \
    Parser/acceler.c \
    Parser/grammar1.c \
    Parser/listnode.c \
    Parser/node.c \
    Parser/parser.c \
    Parser/bitset.c \
    Parser/metagrammar.c \
    Parser/firstsets.c \
    Parser/grammar.c \
    Parser/pgen.c \
    Parser/myreadline.c Parser/parsetok.c Parser/tokenizer.c

OBJECT_SOURCES = \
    Objects/abstract.c \
    Objects/boolobject.c \
    Objects/bytes_methods.c \
    Objects/bytearrayobject.c \
    Objects/cellobject.c \
    Objects/classobject.c \
    Objects/codeobject.c \
    Objects/complexobject.c \
    Objects/descrobject.c \
    Objects/enumobject.c \
    Objects/exceptions.c \
    Objects/genobject.c \
    Objects/fileobject.c \
    Objects/floatobject.c \
    Objects/frameobject.c \
    Objects/funcobject.c \
    Objects/iterobject.c \
    Objects/listobject.c \
    Objects/longobject.c \
    Objects/dictobject.c \
    Objects/memoryobject.c \
    Objects/methodobject.c \
    Objects/moduleobject.c \
    Objects/object.c \
    Objects/obmalloc.c \
    Objects/capsule.c \
    Objects/rangeobject.c \
    Objects/setobject.c \
    Objects/sliceobject.c \
    Objects/structseq.c \
    Objects/tupleobject.c \
    Objects/typeobject.c \
    Objects/unicodeobject.c \
    Objects/unicodectype.c \
    Objects/weakrefobject.c

greaterThan(PY_MAJOR_VERSION, 2) {
    OBJECT_SOURCES += \
        Objects/accu.c \
        Objects/bytesobject.c \
        Objects/namespaceobject.c

    greaterThan(PY_MINOR_VERSION, 4) {
        OBJECT_SOURCES += \
            Objects/odictobject.c
    }
} else {
    OBJECT_SOURCES += \
        Objects/bufferobject.c \
        Objects/cobject.c \
        Objects/intobject.c \
        Objects/stringobject.c
}

PYTHON_SOURCES = \
    Python/_warnings.c \
    Python/Python-ast.c \
    Python/asdl.c \
    Python/ast.c \
    Python/bltinmodule.c \
    Python/ceval.c \
    Python/compile.c \
    Python/codecs.c \
    Python/errors.c \
    Python/frozenmain.c \
    Python/future.c \
    Python/getargs.c \
    Python/getcompiler.c \
    Python/getcopyright.c \
    Python/getplatform.c \
    Python/getversion.c \
    Python/graminit.c \
    Python/import.c \
    Python/importdl.c \
    Python/marshal.c \
    Python/modsupport.c \
    Python/mystrtoul.c \
    Python/mysnprintf.c \
    Python/peephole.c \
    Python/pyarena.c \
    Python/pyfpe.c \
    Python/pymath.c \
    Python/pystate.c \
    Python/pythonrun.c \
    Python/structmember.c \
    Python/symtable.c \
    Python/sysmodule.c \
    Python/traceback.c \
    Python/getopt.c \
    Python/pystrcmp.c \
    Python/pystrtod.c \
    Python/formatter_unicode.c \
    Python/thread.c

greaterThan(PY_MAJOR_VERSION, 2) {
    PYTHON_SOURCES += \
        Python/pyctype.c \
        Python/pytime.c \
        Python/random.c \
        Python/dtoa.c \
        Python/fileutils.c

    greaterThan(PY_MINOR_VERSION, 3) {
        PYTHON_SOURCES += \
            Python/pyhash.c
    }

    greaterThan(PY_MINOR_VERSION, 4) {
        PYTHON_SOURCES += \
            Python/dynamic_annotations.c \
            Python/pylifecycle.c \
            Python/pystrhex.c
    }
} else {
    PYTHON_SOURCES += \
        Python/formatter_string.c \
        Python/pyctype.c \
        Python/random.c \
        Python/dtoa.c
}

equals(PY_DYNAMIC_LOADING, "enabled") {
    DEFINES += SOABI=\\\"cpython-$${PY_MAJOR_VERSION}$${PY_MINOR_VERSION}\\\"

    win32 {
        PYTHON_SOURCES += Python/dynload_win.c
    } else {
        PYTHON_SOURCES += Python/dynload_shlib.c
    }
}

MODULE_SOURCES = \
    Modules/config.c \
    Modules/main.c \
    Modules/gcmodule.c

greaterThan(PY_MAJOR_VERSION, 2) {
    MOD_SOURCES = \
        Modules/_threadmodule.c \
        Modules/signalmodule.c \
        Modules/posixmodule.c \
        Modules/errnomodule.c \
        Modules/_sre.c \
        Modules/_codecsmodule.c \
        Modules/_weakref.c \
        Modules/_functoolsmodule.c \
        Modules/_collectionsmodule.c \
        Modules/itertoolsmodule.c \
        Modules/atexitmodule.c \
        Modules/_localemodule.c \
        Modules/_io/_iomodule.c \
        Modules/_io/iobase.c \
        Modules/_io/fileio.c \
        Modules/_io/bytesio.c \
        Modules/_io/bufferedio.c \
        Modules/_io/textio.c \
        Modules/_io/stringio.c \
        Modules/faulthandler.c \
        Modules/symtablemodule.c \

    greaterThan(PY_MINOR_VERSION, 3) {
        MOD_SOURCES += \
            Modules/_operator.c \
            Modules/_stat.c \
            Modules/_tracemalloc.c \
            Modules/hashtable.c

        win32 {
            # Work around the PyVarObject_HEAD_INIT() problem in Python v3.4.
            MOD_SOURCES += Modules/_struct.c
        }
    }
} else {
    MOD_SOURCES = \
        Modules/threadmodule.c \
        Modules/signalmodule.c \
        Modules/posixmodule.c \
        Modules/errnomodule.c \
        Modules/_sre.c \
        Modules/_codecsmodule.c \
        Modules/symtablemodule.c \
        Modules/_weakref.c
}

win32 {
    MOD_SOURCES += \
        PC/getpathp.c

    greaterThan(PY_MAJOR_VERSION, 2) {
        MOD_SOURCES += \
            PC/winreg.c
    }
} else {
    MOD_SOURCES += \
        Modules/getpath.c \
        Modules/pwdmodule.c
}

SOURCES = Modules/getbuildinfo.c Python/frozen.c
SOURCES += $$PARSER_SOURCES
SOURCES += $$OBJECT_SOURCES
SOURCES += $$PYTHON_SOURCES
SOURCES += $$MODULE_SOURCES
SOURCES += $$MOD_SOURCES
