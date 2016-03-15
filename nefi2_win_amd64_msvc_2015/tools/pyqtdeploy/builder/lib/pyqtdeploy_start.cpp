// Copyright (c) 2015, Riverbank Computing Limited
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
// 
// 1. Redistributions of source code must retain the above copyright notice,
//    this list of conditions and the following disclaimer.
// 
// 2. Redistributions in binary form must reproduce the above copyright notice,
//    this list of conditions and the following disclaimer in the documentation
//    and/or other materials provided with the distribution.
// 
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
// ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
// LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
// CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
// SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
// INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
// CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
// ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
// POSSIBILITY OF SUCH DAMAGE.


#include <stdio.h>

#include <Python.h>

#include <QByteArray>
#include <QDir>
#include <QString>
#include <QRegExp>
#include <QTextCodec>

#include "frozen_bootstrap.h"

#if PY_VERSION_HEX >= 0x03050000
#include "frozen_bootstrap_external.h"
#endif

#if defined(PYQTDEPLOY_FROZEN_MAIN)
#include "frozen_main.h"
#endif


#if PY_MAJOR_VERSION >= 3

#define BOOTSTRAP_MODULE            "_frozen_importlib"
#define BOOTSTRAP_EXTERNAL_MODULE   "_frozen_importlib_external"
#define PDYTOOLS_INIT               PyInit_pdytools
#define CONST_CAST(s)               s
extern "C" PyObject *PyInit_pdytools(void);

#if defined(Q_OS_WIN)
#define WIDE_ARGV
#endif

#else

#define BOOTSTRAP_MODULE    "__bootstrap__"
#define PDYTOOLS_INIT       initpdytools
#define CONST_CAST(s)       const_cast<char *>(s)
extern "C" void initpdytools(void);

#endif


// The internal API.
void pdytools_init_executable_dir(const QString &argv0);
const QDir &pdytools_get_executable_dir();


// We use Qt as the source of the locale information, partly because it
// officially supports Android.
static QTextCodec *locale_codec;


// Foward declarations.
static int handle_exception();
static int append_path_dirs(PyObject *list, const char **path_dirs);
#if PY_MAJOR_VERSION < 3
static PyObject *string_from_qstring(const QString &qs);
#endif


#if defined(WIDE_ARGV)
int pyqtdeploy_start(int argc, wchar_t **w_argv,
        struct _inittab *extension_modules, const char *main_module,
        const char *entry_point, const char **path_dirs)
#else
int pyqtdeploy_start(int argc, char **argv,
        struct _inittab *extension_modules, const char *main_module,
        const char *entry_point, const char **path_dirs)
#endif
{
    // The replacement table of frozen modules.
    static struct _frozen modules[] = {
        {
            CONST_CAST(BOOTSTRAP_MODULE),
            frozen_pyqtdeploy_bootstrap,
            sizeof (frozen_pyqtdeploy_bootstrap)
        },
#if PY_VERSION_HEX >= 0x03050000
        {
            CONST_CAST(BOOTSTRAP_EXTERNAL_MODULE),
            frozen_pyqtdeploy_bootstrap_external,
            sizeof (frozen_pyqtdeploy_bootstrap_external)
        },
#endif
#if defined(PYQTDEPLOY_FROZEN_MAIN)
        {
            CONST_CAST("__main__"),
            frozen_pyqtdeploy_main,
            sizeof (frozen_pyqtdeploy_main)
        },
#endif
        {NULL, NULL, 0}
    };

    // Get the codec for the locale.
    locale_codec = QTextCodec::codecForLocale();

    if (!locale_codec)
    {
#if defined(WIDE_ARGV)
        fwprintf(stderr, L"%s: no locale codec found\n", w_argv[0]);
#else
        fprintf(stderr, "%s: no locale codec found\n", argv[0]);
#endif
        return 1;
    }

    // Initialise some Python globals.
    Py_FrozenFlag = 1;
    Py_NoSiteFlag = 1;
    Py_IgnoreEnvironmentFlag = 1;
#if defined(PYQTDEPLOY_OPTIMIZED)
    Py_OptimizeFlag = 1;
#endif

#if PY_MAJOR_VERSION >= 3
    if (!Py_FileSystemDefaultEncoding)
    {
        // Python doesn't have a platform default so get it from Qt.  However
        // if Qt isn't specific then let Python have a go later.

        static QByteArray locale_codec_name;

        locale_codec_name = locale_codec->name();
        if (locale_codec_name != "System")
        {
            Py_FileSystemDefaultEncoding = locale_codec_name.data();
            Py_HasFileSystemDefaultEncoding = 1;
        }
    }
#endif

    PyImport_FrozenModules = modules;

    // Add the importer to the table of builtins.
    if (PyImport_AppendInittab("pdytools", PDYTOOLS_INIT) < 0)
    {
#if defined(WIDE_ARGV)
        fwprintf(stderr, L"%s: PyImport_AppendInittab() failed\n", w_argv[0]);
#else
        fprintf(stderr, "%s: PyImport_AppendInittab() failed\n", argv[0]);
#endif
        return 1;
    }

    // Add any extension modules.
    if (extension_modules != NULL)
        if (PyImport_ExtendInittab(extension_modules) < 0)
        {
#if defined(WIDE_ARGV)
            fwprintf(stderr, L"%s: PyImport_ExtendInittab() failed\n", w_argv[0]);
#else
            fprintf(stderr, "%s: PyImport_ExtendInittab() failed\n", argv[0]);
#endif
            return 1;
        }

#if PY_MAJOR_VERSION >= 3
#if !defined(WIDE_ARGV)
    // Convert the argument list to wide characters using the locale codec.
    wchar_t **w_argv = new wchar_t *[argc + 1];

    for (int i = 0; i < argc; i++)
    {
        QString qs_arg = locale_codec->toUnicode(argv[i]);

        wchar_t *w_arg = new wchar_t[qs_arg.length() + 1];

        w_arg[qs_arg.toWCharArray(w_arg)] = 0;

        w_argv[i] = w_arg;
    }

    w_argv[argc] = NULL;
#endif

    // Initialise the Python v3 interpreter.
    Py_SetProgramName(w_argv[0]);
    Py_Initialize();
    PySys_SetArgvEx(argc, w_argv, 0);
#else
    // Initialise the Python v2 interpreter.
    Py_SetProgramName(argv[0]);
    Py_Initialize();
    PySys_SetArgvEx(argc, argv, 0);

    // Initialise the path hooks.
    if (PyImport_ImportFrozenModule(CONST_CAST(BOOTSTRAP_MODULE)) < 0)
        return handle_exception();
#endif

    // Set sys.frozen.
    if (PySys_SetObject("frozen", Py_True) < 0)
        return handle_exception();

    // Initialise the directory containing the executable.
#if PY_MAJOR_VERSION >= 3
    pdytools_init_executable_dir(QString::fromWCharArray(w_argv[0]));
#else
    pdytools_init_executable_dir(locale_codec->toUnicode(argv[0]));
#endif

    // Configure sys.path.
    if (path_dirs != NULL)
    {
        PyObject *py_path = PySys_GetObject(CONST_CAST("path"));

        if (py_path)
        {
            if (append_path_dirs(py_path, path_dirs) < 0)
                return handle_exception();
        }
    }

#if defined(PYQTDEPLOY_FROZEN_MAIN)
    Q_UNUSED(entry_point)

    // Set the __file__ attribute of the main module.
    PyObject *mod, *mod_dict, *py_filename;

    if ((mod = PyImport_AddModule(main_module)) == NULL)
        return handle_exception();

    mod_dict = PyModule_GetDict(mod);

#if PY_MAJOR_VERSION >= 3
    py_filename = PyUnicode_FromString(":/__main__.pyo");
#else
    py_filename = PyString_FromString(":/__main__.pyo");
#endif

    if (py_filename == NULL)
        return handle_exception();

    if (PyDict_SetItemString(mod_dict, "__file__", py_filename) < 0)
        return handle_exception();

    Py_DECREF(py_filename);

    // Import the main module.
    if (PyImport_ImportFrozenModule(CONST_CAST(main_module)) < 0)
        return handle_exception();
#else
    // Import the main module.
    PyObject *mod, *main_module_obj;

#if PY_MAJOR_VERSION >= 3
    main_module_obj = PyUnicode_FromString(main_module);
#else
    main_module_obj = string_from_qstring(QString::fromUtf8(main_module));
#endif

    if (main_module_obj == NULL)
        return handle_exception();

    mod = PyImport_Import(main_module_obj);
    if (!mod)
        return handle_exception();

    // Call the entry point.
    if (!PyObject_CallMethod(mod, CONST_CAST(entry_point), NULL))
        return handle_exception();
#endif

    // Tidy up.
    Py_Finalize();

    return 0;
}


// Handle an exception and return the error code to immediately pass back to
// the operating system.
static int handle_exception()
{
    int exit_code;

    if (PyErr_ExceptionMatches(PyExc_SystemExit))
    {
        PyObject *exc, *value, *tb;

        PyErr_Fetch(&exc, &value, &tb);
        PyErr_NormalizeException(&exc, &value, &tb);

        if (!value || value == Py_None)
        {
            exit_code = 0;
        }
        else
        {
            PyObject *code = PyObject_GetAttrString(value, "code");

            if (code)
            {
#if PY_MAJOR_VERSION >= 3
                if (PyLong_Check(code))
                {
                    exit_code = (int)PyLong_AsLong(code);
                    Py_DECREF(code);
                }
#else
                if (PyInt_Check(code))
                {
                    exit_code = (int)PyInt_AsLong(code);
                    Py_DECREF(code);
                }
#endif
                else
                {
                    exit_code = 1;
                }
            }
            else
            {
                exit_code = 1;
            }
        }

        PyErr_Restore(exc, value, tb);
        PyErr_Clear();
    }
    else
    {
        PyErr_Print();
        exit_code = 1;
    }

    Py_Finalize();

    return exit_code;
}


// Extend a list with an array of UTF-8 encoded path directory names.  Return
// -1 if there was an error.
static int append_path_dirs(PyObject *list, const char **path_dirs)
{
    const char *path_dir_utf8;

    while ((path_dir_utf8 = *path_dirs++) != NULL)
    {
        // Convert to a QString.
        QString path_dir(QString::fromUtf8(path_dir_utf8));

        // Expand any (locale encoded) environment variables.
        QRegExp env_var_name_re("\\$([A-Za-z0-9_]+)");

        int i;

        while ((i = env_var_name_re.indexIn(path_dir)) != -1)
        {
            QByteArray name(locale_codec->fromUnicode(env_var_name_re.cap(1)));
            QByteArray value(qgetenv(name.data()));

            path_dir.replace(i, env_var_name_re.matchedLength(),
                    locale_codec->toUnicode(value));
        }

        // Make sure the path is absolute.
        if (QDir::isRelativePath(path_dir))
        {
            const QDir &exec_dir = pdytools_get_executable_dir();
            path_dir = exec_dir.filePath(path_dir);
        }

        // Convert to the native format.  (Note that we don't resolve symbolic
        // links.)
        path_dir = QDir::toNativeSeparators(QDir::cleanPath(path_dir));

        // Convert to a Python string.
        PyObject *py_path_dir;

#if PY_MAJOR_VERSION >= 3
        QByteArray utf8(path_dir.toUtf8());
        py_path_dir = PyUnicode_FromStringAndSize(utf8.data(), utf8.length());
#else
        py_path_dir = string_from_qstring(path_dir);
#endif

        if (!py_path_dir)
            return -1;

        // Append to the list.
        int rc = PyList_Append(list, py_path_dir);
        Py_DECREF(py_path_dir);

        if (rc < 0)
            return -1;
    }

    return 0;
}


#if PY_MAJOR_VERSION < 3
// Convert a QString to a Python v2 locale encoded str object.
static PyObject *string_from_qstring(const QString &qs)
{
    QByteArray locale_s(locale_codec->fromUnicode(qs));

    return PyString_FromStringAndSize(locale_s, locale_s.length());
}
#endif
