/* Generated automatically from ./Modules/config.c.in by makesetup. */
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
   See create_builtin() in import.c. */

#include "Python.h"

#ifdef __cplusplus
extern "C" {
#endif


extern PyObject* PyInit__thread(void);
extern PyObject* PyInit__signal(void);
extern PyObject* PyInit_posix(void);
extern PyObject* PyInit_errno(void);
extern PyObject* PyInit_pwd(void);
extern PyObject* PyInit__sre(void);
extern PyObject* PyInit__codecs(void);
extern PyObject* PyInit__weakref(void);
extern PyObject* PyInit__functools(void);
extern PyObject* PyInit__operator(void);
extern PyObject* PyInit__collections(void);
extern PyObject* PyInit_itertools(void);
extern PyObject* PyInit_atexit(void);
extern PyObject* PyInit__stat(void);
extern PyObject* PyInit_time(void);
extern PyObject* PyInit__locale(void);
extern PyObject* PyInit__io(void);
extern PyObject* PyInit_zipimport(void);
extern PyObject* PyInit_faulthandler(void);
extern PyObject* PyInit__tracemalloc(void);
extern PyObject* PyInit__symtable(void);
extern PyObject* PyInit_readline(void);
extern PyObject* PyInit_array(void);
extern PyObject* PyInit_math(void);
extern PyObject* PyInit__struct(void);
extern PyObject* PyInit__random(void);
extern PyObject* PyInit__elementtree(void);
extern PyObject* PyInit__pickle(void);
extern PyObject* PyInit__datetime(void);
extern PyObject* PyInit__bisect(void);
extern PyObject* PyInit__heapq(void);
extern PyObject* PyInit_unicodedata(void);
extern PyObject* PyInit_fcntl(void);
extern PyObject* PyInit_grp(void);
extern PyObject* PyInit_select(void);
extern PyObject* PyInit_mmap(void);
extern PyObject* PyInit__csv(void);
extern PyObject* PyInit_xxsubtype(void);
/* -- ADDMODULE MARKER 1 -- */

extern PyObject* PyMarshal_Init(void);
extern PyObject* PyInit_imp(void);
extern PyObject* PyInit_gc(void);
extern PyObject* PyInit__ast(void);
extern PyObject* _PyWarnings_Init(void);
extern PyObject* PyInit__string(void);

struct _inittab _PyImport_Inittab[] = {

{"_thread", PyInit__thread},
{"_signal", PyInit__signal},
{"posix", PyInit_posix},
{"errno", PyInit_errno},
{"pwd", PyInit_pwd},
{"_sre", PyInit__sre},
{"_codecs", PyInit__codecs},
{"_weakref", PyInit__weakref},
{"_functools", PyInit__functools},
{"_operator", PyInit__operator},
{"_collections", PyInit__collections},
{"itertools", PyInit_itertools},
{"atexit", PyInit_atexit},
{"_stat", PyInit__stat},
{"time", PyInit_time},
{"_locale", PyInit__locale},
{"_io", PyInit__io},
{"zipimport", PyInit_zipimport},
{"faulthandler", PyInit_faulthandler},
{"_tracemalloc", PyInit__tracemalloc},
{"_symtable", PyInit__symtable},
{"readline", PyInit_readline},
{"array", PyInit_array},
{"math", PyInit_math},
{"_struct", PyInit__struct},
{"_random", PyInit__random},
{"_elementtree", PyInit__elementtree},
{"_pickle", PyInit__pickle},
{"_datetime", PyInit__datetime},
{"_bisect", PyInit__bisect},
{"_heapq", PyInit__heapq},
{"unicodedata", PyInit_unicodedata},
{"fcntl", PyInit_fcntl},
{"grp", PyInit_grp},
{"select", PyInit_select},
{"mmap", PyInit_mmap},
{"_csv", PyInit__csv},
{"xxsubtype", PyInit_xxsubtype},
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
