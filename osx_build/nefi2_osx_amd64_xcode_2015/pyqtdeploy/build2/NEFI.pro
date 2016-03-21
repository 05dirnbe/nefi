TEMPLATE = app

CONFIG += warn_off
QT += widgets printsupport

RESOURCES = \
    resources/pyqtdeploy0.qrc \
    resources/pyqtdeploy1.qrc \
    resources/pyqtdeploy2.qrc \
    resources/pyqtdeploy3.qrc \
    resources/pyqtdeploy4.qrc \
    resources/pyqtdeploy5.qrc \
    resources/pyqtdeploy6.qrc \
    resources/pyqtdeploy7.qrc \
    resources/pyqtdeploy8.qrc \
    resources/pyqtdeploy9.qrc \
    resources/pyqtdeploy10.qrc \
    resources/pyqtdeploy11.qrc \
    resources/pyqtdeploy12.qrc \
    resources/pyqtdeploy13.qrc \
    resources/pyqtdeploy14.qrc \
    resources/pyqtdeploy15.qrc \
    resources/pyqtdeploy16.qrc \
    resources/pyqtdeploy17.qrc \
    resources/pyqtdeploy18.qrc \
    resources/pyqtdeploy19.qrc \
    resources/pyqtdeploy20.qrc \
    resources/pyqtdeploy21.qrc \
    resources/pyqtdeploy22.qrc \
    resources/pyqtdeploy23.qrc \
    resources/pyqtdeploy24.qrc \
    resources/pyqtdeploy25.qrc \
    resources/pyqtdeploy26.qrc \
    resources/pyqtdeploy27.qrc \
    resources/pyqtdeploy28.qrc \
    resources/pyqtdeploy29.qrc \
    resources/pyqtdeploy30.qrc \
    resources/pyqtdeploy31.qrc \
    resources/pyqtdeploy32.qrc \
    resources/pyqtdeploy33.qrc \
    resources/pyqtdeploy34.qrc \
    resources/pyqtdeploy35.qrc \
    resources/pyqtdeploy36.qrc \
    resources/pyqtdeploy37.qrc \
    resources/pyqtdeploy38.qrc \
    resources/pyqtdeploy39.qrc \
    resources/pyqtdeploy40.qrc \
    resources/pyqtdeploy41.qrc \
    resources/pyqtdeploy42.qrc \
    resources/pyqtdeploy43.qrc \
    resources/pyqtdeploy44.qrc \
    resources/pyqtdeploy45.qrc \
    resources/pyqtdeploy46.qrc \
    resources/pyqtdeploy47.qrc \
    resources/pyqtdeploy48.qrc \
    resources/pyqtdeploy49.qrc \
    resources/pyqtdeploy50.qrc \
    resources/pyqtdeploy51.qrc \
    resources/pyqtdeploy52.qrc \
    resources/pyqtdeploy53.qrc \
    resources/pyqtdeploy54.qrc \
    resources/pyqtdeploy55.qrc \
    resources/pyqtdeploy56.qrc \
    resources/pyqtdeploy57.qrc \
    resources/pyqtdeploy58.qrc \
    resources/pyqtdeploy59.qrc \
    resources/pyqtdeploy60.qrc \
    resources/pyqtdeploy61.qrc \
    resources/pyqtdeploy62.qrc \
    resources/pyqtdeploy63.qrc \
    resources/pyqtdeploy64.qrc \
    resources/pyqtdeploy65.qrc \
    resources/pyqtdeploy66.qrc \
    resources/pyqtdeploy67.qrc \
    resources/pyqtdeploy68.qrc \
    resources/pyqtdeploy69.qrc \
    resources/pyqtdeploy70.qrc \
    resources/pyqtdeploy71.qrc \
    resources/pyqtdeploy72.qrc \
    resources/pyqtdeploy73.qrc \
    resources/pyqtdeploy74.qrc \
    resources/pyqtdeploy75.qrc \
    resources/pyqtdeploy76.qrc \
    resources/pyqtdeploy77.qrc \
    resources/pyqtdeploy78.qrc \
    resources/pyqtdeploy79.qrc \
    resources/pyqtdeploy80.qrc \
    resources/pyqtdeploy81.qrc \
    resources/pyqtdeploy82.qrc \
    resources/pyqtdeploy83.qrc \
    resources/pyqtdeploy84.qrc \
    resources/pyqtdeploy85.qrc \
    resources/pyqtdeploy86.qrc \
    resources/pyqtdeploy87.qrc \
    resources/pyqtdeploy88.qrc \
    resources/pyqtdeploy89.qrc \
    resources/pyqtdeploy90.qrc \
    resources/pyqtdeploy91.qrc \
    resources/pyqtdeploy92.qrc \
    resources/pyqtdeploy93.qrc \
    resources/pyqtdeploy94.qrc \
    resources/pyqtdeploy95.qrc \
    resources/pyqtdeploy96.qrc \
    resources/pyqtdeploy97.qrc \
    resources/pyqtdeploy98.qrc

SOURCES = pyqtdeploy_main.cpp pyqtdeploy_start.cpp pdytools_module.cpp
DEFINES += PYQTDEPLOY_FROZEN_MAIN PYQTDEPLOY_OPTIMIZED
HEADERS = pyqtdeploy_version.h frozen_bootstrap.h frozen_bootstrap_external.h frozen_main.h

INCLUDEPATH += /Users/philipp/NetworkExtractionFromImages/osx_build/nefi2_osx_amd64_xcode_2015/python_target/include/python3.5m
LIBS += -L/Users/philipp/NetworkExtractionFromImages/osx_build/nefi2_osx_amd64_xcode_2015/python_target/lib/python3.5/site-packages -lsip
LIBS += -L/Users/philipp/NetworkExtractionFromImages/osx_build/nefi2_osx_amd64_xcode_2015/python_target/lib/python3.5/site-packages/PyQt5 -lQtGui -lQtCore -lQtWidgets -lQt -lQtPrintSupport

!win32 {
    LIBS += -L/Users/philipp/NetworkExtractionFromImages/osx_build/nefi2_osx_amd64_xcode_2015/python_target/lib -lpython3.5m
}

android {
    DEFINES += USE_PYEXPAT_CAPI
    DEFINES += HAVE_EXPAT_CONFIG_H
    DEFINES += MODULE_NAME=\\\"sqlite3\\\"
    DEFINES += Py_BUILD_CORE
    DEFINES += SQLITE_OMIT_LOAD_EXTENSION
    DEFINES += HAVE_NDBM_H
    DEFINES += XML_STATIC
    INCLUDEPATH += /Users/philipp/Downloads/Python-3.5.1/Modules
    INCLUDEPATH += /Users/philipp/Downloads/Python-3.5.1/Modules/_ctypes
    INCLUDEPATH += /Users/philipp/Downloads/Python-3.5.1/Modules/_multiprocessing
    INCLUDEPATH += /Users/philipp/Downloads/Python-3.5.1/Modules/expat
    INCLUDEPATH += /Users/philipp/Downloads/Python-3.5.1/Modules/_sqlite
    LIBS += -lz
    LIBS += -lpanel
    LIBS += -lbz2
    LIBS += -lnsl
    LIBS += -lreadline
    LIBS += -lsqlite3
    LIBS += -ltermcap
    LIBS += -llzma
    LIBS += -lcrypto
    LIBS += -lcurses
    LIBS += -lssl
    LIBS += -lgdbm
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/cjkcodecs/_codecs_kr.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/selectmodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_curses_panel.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/pyexpat.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_ctypes/cfield.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_sqlite/statement.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_math.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_randommodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_gdbmmodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_heapqmodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/termios.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/socketmodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_lsprof.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_cursesmodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_sqlite/microprotocols.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_sqlite/module.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/unicodedata.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/audioop.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/cmathmodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_sqlite/prepare_protocol.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_sqlite/row.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/syslogmodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/expat/xmltok.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/mathmodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/expat/xmlrole.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_opcode.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/nismodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/cjkcodecs/_codecs_hk.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/binascii.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_bisectmodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_ctypes/callproc.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_sqlite/cursor.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_sqlite/cache.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_csv.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_lzmamodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_multiprocessing/multiprocessing.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/arraymodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/parsermodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/md5module.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/readline.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_sqlite/util.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/cjkcodecs/_codecs_cn.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_posixsubprocess.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_ctypes/_ctypes.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/ossaudiodev.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/resource.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/fcntlmodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/cjkcodecs/_codecs_tw.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/mmapmodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/expat/xmlparse.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_multiprocessing/semaphore.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/cjkcodecs/_codecs_iso2022.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_ctypes/stgdict.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_elementtree.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/zlibmodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_pickle.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/sha256module.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_bz2module.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/sha512module.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/grpmodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/rotatingtree.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/timemodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/cjkcodecs/multibytecodec.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_ctypes/callbacks.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_json.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_ssl.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_dbmmodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/zipimport.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/spwdmodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_struct.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/cjkcodecs/_codecs_jp.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/sha1module.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_datetimemodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_cryptmodule.c
    SOURCES += /Users/philipp/Downloads/Python-3.5.1/Modules/_sqlite/connection.c
}

win32 {
    LIBS += -L/Users/philipp/NetworkExtractionFromImages/osx_build/nefi2_osx_amd64_xcode_2015/python_target/lib -lpython35m
}

win32 {
    PDY_DLL = /Users/philipp/NetworkExtractionFromImages/osx_build/nefi2_osx_amd64_xcode_2015/python_target/lib/DLLs3.5/python35.dll
    exists($$PDY_DLL) {
        CONFIG(debug, debug|release) {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &
        } else {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &
        }
    }

    PDY_DLL = /Users/philipp/NetworkExtractionFromImages/osx_build/nefi2_osx_amd64_xcode_2015/python_target/lib/DLLs3.5/vcruntime140.dll
    exists($$PDY_DLL) {
        CONFIG(debug, debug|release) {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &
        } else {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &
        }
    }

    PDY_DLL = /Users/philipp/NetworkExtractionFromImages/osx_build/nefi2_osx_amd64_xcode_2015/python_target/lib/DLLs3.5/_lzma.pyd
    exists($$PDY_DLL) {
        CONFIG(debug, debug|release) {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &
        } else {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &
        }
    }

    PDY_DLL = /Users/philipp/NetworkExtractionFromImages/osx_build/nefi2_osx_amd64_xcode_2015/python_target/lib/DLLs3.5/unicodedata.pyd
    exists($$PDY_DLL) {
        CONFIG(debug, debug|release) {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &
        } else {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &
        }
    }

    PDY_DLL = /Users/philipp/NetworkExtractionFromImages/osx_build/nefi2_osx_amd64_xcode_2015/python_target/lib/DLLs3.5/_bz2.pyd
    exists($$PDY_DLL) {
        CONFIG(debug, debug|release) {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &
        } else {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &
        }
    }

    PDY_DLL = /Users/philipp/NetworkExtractionFromImages/osx_build/nefi2_osx_amd64_xcode_2015/python_target/lib/DLLs3.5/_sqlite3.pyd
    exists($$PDY_DLL) {
        CONFIG(debug, debug|release) {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &
        } else {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &
        }
    }

    PDY_DLL = /Users/philipp/NetworkExtractionFromImages/osx_build/nefi2_osx_amd64_xcode_2015/python_target/lib/DLLs3.5/sqlite3.dll
    exists($$PDY_DLL) {
        CONFIG(debug, debug|release) {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &
        } else {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &
        }
    }

    PDY_DLL = /Users/philipp/NetworkExtractionFromImages/osx_build/nefi2_osx_amd64_xcode_2015/python_target/lib/DLLs3.5/_ctypes.pyd
    exists($$PDY_DLL) {
        CONFIG(debug, debug|release) {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &
        } else {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &
        }
    }

    PDY_DLL = /Users/philipp/NetworkExtractionFromImages/osx_build/nefi2_osx_amd64_xcode_2015/python_target/lib/DLLs3.5/_ssl.pyd
    exists($$PDY_DLL) {
        CONFIG(debug, debug|release) {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &
        } else {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &
        }
    }

    PDY_DLL = /Users/philipp/NetworkExtractionFromImages/osx_build/nefi2_osx_amd64_xcode_2015/python_target/lib/DLLs3.5/select.pyd
    exists($$PDY_DLL) {
        CONFIG(debug, debug|release) {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &
        } else {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &
        }
    }

    PDY_DLL = /Users/philipp/NetworkExtractionFromImages/osx_build/nefi2_osx_amd64_xcode_2015/python_target/lib/DLLs3.5/pyexpat.pyd
    exists($$PDY_DLL) {
        CONFIG(debug, debug|release) {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &
        } else {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &
        }
    }

    PDY_DLL = /Users/philipp/NetworkExtractionFromImages/osx_build/nefi2_osx_amd64_xcode_2015/python_target/lib/DLLs3.5/_multiprocessing.pyd
    exists($$PDY_DLL) {
        CONFIG(debug, debug|release) {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &
        } else {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &
        }
    }

    PDY_DLL = /Users/philipp/NetworkExtractionFromImages/osx_build/nefi2_osx_amd64_xcode_2015/python_target/lib/DLLs3.5/_elementtree.pyd
    exists($$PDY_DLL) {
        CONFIG(debug, debug|release) {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &
        } else {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &
        }
    }

    PDY_DLL = /Users/philipp/NetworkExtractionFromImages/osx_build/nefi2_osx_amd64_xcode_2015/python_target/lib/DLLs3.5/_socket.pyd
    exists($$PDY_DLL) {
        CONFIG(debug, debug|release) {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &
        } else {
            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &
        }
    }
}

cython.name = Cython compiler
cython.input = CYTHONSOURCES
cython.output = ${QMAKE_FILE_BASE}.c
cython.variable_out = GENERATED_SOURCES
cython.commands = cython ${QMAKE_FILE_IN} -o ${QMAKE_FILE_OUT}

QMAKE_EXTRA_COMPILERS += cython

linux-* {
    LIBS += -lutil -ldl
}

win32 {
    masm.input = MASMSOURCES
    masm.output = ${QMAKE_FILE_BASE}.obj

    contains(QMAKE_TARGET.arch, x86_64) {
        masm.name = MASM64 compiler
        masm.commands = ml64 /Fo ${QMAKE_FILE_OUT} /c ${QMAKE_FILE_IN}
    } else {
        masm.name = MASM compiler
        masm.commands = ml /Fo ${QMAKE_FILE_OUT} /c ${QMAKE_FILE_IN}
    }

    QMAKE_EXTRA_COMPILERS += masm

    LIBS += -ladvapi32 -lshell32 -luser32 -lws2_32 -lole32 -loleaut32
    DEFINES += MS_WINDOWS _WIN32_WINNT=Py_WINVER NTDDI_VERSION=Py_NTDDI WINVER=Py_WINVER

    # This is added from the qmake spec files but clashes with _pickle.c.
    DEFINES -= UNICODE
}

macx {
    LIBS += -framework SystemConfiguration -framework CoreFoundation
}
