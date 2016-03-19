/*
 * Copyright (c) 2015, Riverbank Computing Limited
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 * 
 * 1. Redistributions of source code must retain the above copyright notice,
 *    this list of conditions and the following disclaimer.
 * 
 * 2. Redistributions in binary form must reproduce the above copyright notice,
 *    this list of conditions and the following disclaimer in the documentation
 *    and/or other materials provided with the distribution.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */


/* -*- C -*- ***********************************************
Copyright (c) 2000, BeOpen.com.
Copyright (c) 1995-2000, Corporation for National Research Initiatives.
Copyright (c) 1990-1995, Stichting Mathematisch Centrum.
All rights reserved.

See the file "Misc/COPYRIGHT" for information on usage and
redistribution of this file, and for a DISCLAIMER OF ALL WARRANTIES.
******************************************************************/

/* Module configuration */

/* !!! !!! !!! This file is edited by the makesetup script !!! !!! !!! */

/* This file contains the table of built-in modules.
   See init_builtin() in import.c. */

#include "Python.h"

#ifdef __cplusplus
extern "C" {
#endif


extern PyObject* PyInit__thread(void);
#if PY_MINOR_VERSION >= 5
extern PyObject* PyInit__signal(void);
#else
extern PyObject* PyInit_signal(void);
#endif
#if defined(MS_WINDOWS)
extern PyObject* PyInit_nt(void);
extern PyObject* PyInit_winreg(void);
#else
extern PyObject* PyInit_posix(void);
#endif
extern PyObject* PyInit_errno(void);
#if !defined(MS_WINDOWS)
extern PyObject* PyInit_pwd(void);
#endif
extern PyObject* PyInit__sre(void);
extern PyObject* PyInit__codecs(void);
extern PyObject* PyInit__weakref(void);
extern PyObject* PyInit__functools(void);
#if PY_MINOR_VERSION >= 4
extern PyObject* PyInit__operator(void);
#else
extern PyObject* PyInit_operator(void);
#endif
extern PyObject* PyInit__collections(void);
extern PyObject* PyInit_itertools(void);
#if PY_MINOR_VERSION >= 4
extern PyObject* PyInit_atexit(void);
#endif
#if PY_MINOR_VERSION >= 4
extern PyObject* PyInit__stat(void);
#endif
extern PyObject* PyInit__locale(void);
extern PyObject* PyInit__io(void);
extern PyObject* PyInit_faulthandler(void);
#if PY_MINOR_VERSION >= 4
extern PyObject* PyInit__tracemalloc(void);
#endif
extern PyObject* PyInit__symtable(void);

/* -- ADDMODULE MARKER 1 -- */

extern PyObject* PyMarshal_Init(void);
extern PyObject* PyInit_imp(void);
extern PyObject* PyInit_gc(void);
extern PyObject* PyInit__ast(void);
extern PyObject* _PyWarnings_Init(void);
extern PyObject* PyInit__string(void);

struct _inittab _PyImport_Inittab[] = {

	{"_thread", PyInit__thread},
#if PY_MINOR_VERSION >= 5
	{"_signal", PyInit__signal},
#else
	{"signal", PyInit_signal},
#endif
#if defined(MS_WINDOWS)
	{"nt", PyInit_nt},
	{"winreg", PyInit_winreg},
#else
	{"posix", PyInit_posix},
#endif
	{"errno", PyInit_errno},
#if !defined(MS_WINDOWS)
	{"pwd", PyInit_pwd},
#endif
	{"_sre", PyInit__sre},
	{"_codecs", PyInit__codecs},
	{"_weakref", PyInit__weakref},
	{"_functools", PyInit__functools},
#if PY_MINOR_VERSION >= 4
	{"_operator", PyInit__operator},
#else
	{"operator", PyInit_operator},
#endif
	{"_collections", PyInit__collections},
	{"itertools", PyInit_itertools},
#if PY_MINOR_VERSION >= 4
	{"atexit", PyInit_atexit},
#endif
#if PY_MINOR_VERSION >= 4
	{"_stat", PyInit__stat},
#endif
	{"_locale", PyInit__locale},
	{"_io", PyInit__io},
	{"faulthandler", PyInit_faulthandler},
#if PY_MINOR_VERSION >= 4
	{"_tracemalloc", PyInit__tracemalloc},
#endif
	{"_symtable", PyInit__symtable},

/* -- ADDMODULE MARKER 2 -- */

    /* This module lives in marshal.c */
    {"marshal", PyMarshal_Init},

    /* This lives in import.c */
    {"_imp", PyInit_imp},

    /* This lives in Python/Python-ast.c */
    {"_ast", PyInit__ast},

    /* These entries are here for sys.builtin_module_names */
    {"builtins", NULL},
    {"sys", NULL},

    /* This lives in gcmodule.c */
    {"gc", PyInit_gc},

    /* This lives in _warnings.c */
    {"_warnings", _PyWarnings_Init},

    /* This lives in Objects/unicodeobject.c */
    {"_string", PyInit__string},

    /* Sentinel */
    {0, 0}
};


#ifdef __cplusplus
}
#endif
