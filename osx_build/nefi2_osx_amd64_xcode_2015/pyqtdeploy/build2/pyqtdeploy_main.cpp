#include <Python.h>
#include <QtGlobal>

#if PY_MAJOR_VERSION >= 3
extern "C" PyObject *PyInit_sip(void);
extern "C" PyObject *PyInit_QtPrintSupport(void);
extern "C" PyObject *PyInit_QtGui(void);
extern "C" PyObject *PyInit_Qt(void);
extern "C" PyObject *PyInit_QtWidgets(void);
extern "C" PyObject *PyInit_QtCore(void);
#if defined(Q_OS_ANDROID)
extern "C" PyObject *PyInit__struct(void);
extern "C" PyObject *PyInit_syslog(void);
extern "C" PyObject *PyInit_zlib(void);
extern "C" PyObject *PyInit__lsprof(void);
extern "C" PyObject *PyInit__codecs_kr(void);
extern "C" PyObject *PyInit__dbm(void);
extern "C" PyObject *PyInit__gdbm(void);
extern "C" PyObject *PyInit__opcode(void);
extern "C" PyObject *PyInit_audioop(void);
extern "C" PyObject *PyInit__datetime(void);
extern "C" PyObject *PyInit__curses_panel(void);
extern "C" PyObject *PyInit_mmap(void);
extern "C" PyObject *PyInit__csv(void);
extern "C" PyObject *PyInit__codecs_iso2022(void);
extern "C" PyObject *PyInit__codecs_jp(void);
extern "C" PyObject *PyInit__codecs_cn(void);
extern "C" PyObject *PyInit__multibytecodec(void);
extern "C" PyObject *PyInit_pyexpat(void);
extern "C" PyObject *PyInit__multiprocessing(void);
extern "C" PyObject *PyInit_time(void);
extern "C" PyObject *PyInit__sha1(void);
extern "C" PyObject *PyInit_readline(void);
extern "C" PyObject *PyInit__curses(void);
extern "C" PyObject *PyInit__elementtree(void);
extern "C" PyObject *PyInit_spwd(void);
extern "C" PyObject *PyInit__bisect(void);
extern "C" PyObject *PyInit_resource(void);
extern "C" PyObject *PyInit__crypt(void);
extern "C" PyObject *PyInit__bz2(void);
extern "C" PyObject *PyInit_binascii(void);
extern "C" PyObject *PyInit__heapq(void);
extern "C" PyObject *PyInit_select(void);
extern "C" PyObject *PyInit_unicodedata(void);
extern "C" PyObject *PyInit_zipimport(void);
extern "C" PyObject *PyInit__posixsubprocess(void);
extern "C" PyObject *PyInit_parser(void);
extern "C" PyObject *PyInit__ctypes(void);
extern "C" PyObject *PyInit__lzma(void);
extern "C" PyObject *PyInit__sqlite3(void);
extern "C" PyObject *PyInit_grp(void);
extern "C" PyObject *PyInit__random(void);
extern "C" PyObject *PyInit_array(void);
extern "C" PyObject *PyInit__sha512(void);
extern "C" PyObject *PyInit__md5(void);
extern "C" PyObject *PyInit_nis(void);
extern "C" PyObject *PyInit__pickle(void);
extern "C" PyObject *PyInit_math(void);
extern "C" PyObject *PyInit_termios(void);
extern "C" PyObject *PyInit__codecs_hk(void);
extern "C" PyObject *PyInit_ossaudiodev(void);
extern "C" PyObject *PyInit__sha256(void);
extern "C" PyObject *PyInit__json(void);
extern "C" PyObject *PyInit_fcntl(void);
extern "C" PyObject *PyInit__socket(void);
extern "C" PyObject *PyInit_cmath(void);
extern "C" PyObject *PyInit__codecs_tw(void);
extern "C" PyObject *PyInit__ssl(void);
#endif

static struct _inittab extension_modules[] = {
    {"sip", PyInit_sip},
    {"PyQt5.QtPrintSupport", PyInit_QtPrintSupport},
    {"PyQt5.QtGui", PyInit_QtGui},
    {"PyQt5.Qt", PyInit_Qt},
    {"PyQt5.QtWidgets", PyInit_QtWidgets},
    {"PyQt5.QtCore", PyInit_QtCore},
#if defined(Q_OS_ANDROID)
    {"_struct", PyInit__struct},
    {"syslog", PyInit_syslog},
    {"zlib", PyInit_zlib},
    {"_lsprof", PyInit__lsprof},
    {"_codecs_kr", PyInit__codecs_kr},
    {"_dbm", PyInit__dbm},
    {"_gdbm", PyInit__gdbm},
    {"_opcode", PyInit__opcode},
    {"audioop", PyInit_audioop},
    {"_datetime", PyInit__datetime},
    {"_curses_panel", PyInit__curses_panel},
    {"mmap", PyInit_mmap},
    {"_csv", PyInit__csv},
    {"_codecs_iso2022", PyInit__codecs_iso2022},
    {"_codecs_jp", PyInit__codecs_jp},
    {"_codecs_cn", PyInit__codecs_cn},
    {"_multibytecodec", PyInit__multibytecodec},
    {"pyexpat", PyInit_pyexpat},
    {"_multiprocessing", PyInit__multiprocessing},
    {"time", PyInit_time},
    {"_sha1", PyInit__sha1},
    {"readline", PyInit_readline},
    {"_curses", PyInit__curses},
    {"_elementtree", PyInit__elementtree},
    {"spwd", PyInit_spwd},
    {"_bisect", PyInit__bisect},
    {"resource", PyInit_resource},
    {"_crypt", PyInit__crypt},
    {"_bz2", PyInit__bz2},
    {"binascii", PyInit_binascii},
    {"_heapq", PyInit__heapq},
    {"select", PyInit_select},
    {"unicodedata", PyInit_unicodedata},
    {"zipimport", PyInit_zipimport},
    {"_posixsubprocess", PyInit__posixsubprocess},
    {"parser", PyInit_parser},
    {"_ctypes", PyInit__ctypes},
    {"_lzma", PyInit__lzma},
    {"_sqlite3", PyInit__sqlite3},
    {"grp", PyInit_grp},
    {"_random", PyInit__random},
    {"array", PyInit_array},
    {"_sha512", PyInit__sha512},
    {"_md5", PyInit__md5},
    {"nis", PyInit_nis},
    {"_pickle", PyInit__pickle},
    {"math", PyInit_math},
    {"termios", PyInit_termios},
    {"_codecs_hk", PyInit__codecs_hk},
    {"ossaudiodev", PyInit_ossaudiodev},
    {"_sha256", PyInit__sha256},
    {"_json", PyInit__json},
    {"fcntl", PyInit_fcntl},
    {"_socket", PyInit__socket},
    {"cmath", PyInit_cmath},
    {"_codecs_tw", PyInit__codecs_tw},
    {"_ssl", PyInit__ssl},
#endif
    {NULL, NULL}
};
#else
extern "C" void initsip(void);
extern "C" void initQtPrintSupport(void);
extern "C" void initQtGui(void);
extern "C" void initQt(void);
extern "C" void initQtWidgets(void);
extern "C" void initQtCore(void);
#if defined(Q_OS_ANDROID)
extern "C" void init_struct(void);
extern "C" void initsyslog(void);
extern "C" void initzlib(void);
extern "C" void init_lsprof(void);
extern "C" void init_codecs_kr(void);
extern "C" void init_dbm(void);
extern "C" void init_gdbm(void);
extern "C" void init_opcode(void);
extern "C" void initaudioop(void);
extern "C" void init_datetime(void);
extern "C" void init_curses_panel(void);
extern "C" void initmmap(void);
extern "C" void init_csv(void);
extern "C" void init_codecs_iso2022(void);
extern "C" void init_codecs_jp(void);
extern "C" void init_codecs_cn(void);
extern "C" void init_multibytecodec(void);
extern "C" void initpyexpat(void);
extern "C" void init_multiprocessing(void);
extern "C" void inittime(void);
extern "C" void init_sha1(void);
extern "C" void initreadline(void);
extern "C" void init_curses(void);
extern "C" void init_elementtree(void);
extern "C" void initspwd(void);
extern "C" void init_bisect(void);
extern "C" void initresource(void);
extern "C" void init_crypt(void);
extern "C" void init_bz2(void);
extern "C" void initbinascii(void);
extern "C" void init_heapq(void);
extern "C" void initselect(void);
extern "C" void initunicodedata(void);
extern "C" void initzipimport(void);
extern "C" void init_posixsubprocess(void);
extern "C" void initparser(void);
extern "C" void init_ctypes(void);
extern "C" void init_lzma(void);
extern "C" void init_sqlite3(void);
extern "C" void initgrp(void);
extern "C" void init_random(void);
extern "C" void initarray(void);
extern "C" void init_sha512(void);
extern "C" void init_md5(void);
extern "C" void initnis(void);
extern "C" void init_pickle(void);
extern "C" void initmath(void);
extern "C" void inittermios(void);
extern "C" void init_codecs_hk(void);
extern "C" void initossaudiodev(void);
extern "C" void init_sha256(void);
extern "C" void init_json(void);
extern "C" void initfcntl(void);
extern "C" void init_socket(void);
extern "C" void initcmath(void);
extern "C" void init_codecs_tw(void);
extern "C" void init_ssl(void);
#endif

static struct _inittab extension_modules[] = {
    {"sip", initsip},
    {"PyQt5.QtPrintSupport", initQtPrintSupport},
    {"PyQt5.QtGui", initQtGui},
    {"PyQt5.Qt", initQt},
    {"PyQt5.QtWidgets", initQtWidgets},
    {"PyQt5.QtCore", initQtCore},
#if defined(Q_OS_ANDROID)
    {"_struct", init_struct},
    {"syslog", initsyslog},
    {"zlib", initzlib},
    {"_lsprof", init_lsprof},
    {"_codecs_kr", init_codecs_kr},
    {"_dbm", init_dbm},
    {"_gdbm", init_gdbm},
    {"_opcode", init_opcode},
    {"audioop", initaudioop},
    {"_datetime", init_datetime},
    {"_curses_panel", init_curses_panel},
    {"mmap", initmmap},
    {"_csv", init_csv},
    {"_codecs_iso2022", init_codecs_iso2022},
    {"_codecs_jp", init_codecs_jp},
    {"_codecs_cn", init_codecs_cn},
    {"_multibytecodec", init_multibytecodec},
    {"pyexpat", initpyexpat},
    {"_multiprocessing", init_multiprocessing},
    {"time", inittime},
    {"_sha1", init_sha1},
    {"readline", initreadline},
    {"_curses", init_curses},
    {"_elementtree", init_elementtree},
    {"spwd", initspwd},
    {"_bisect", init_bisect},
    {"resource", initresource},
    {"_crypt", init_crypt},
    {"_bz2", init_bz2},
    {"binascii", initbinascii},
    {"_heapq", init_heapq},
    {"select", initselect},
    {"unicodedata", initunicodedata},
    {"zipimport", initzipimport},
    {"_posixsubprocess", init_posixsubprocess},
    {"parser", initparser},
    {"_ctypes", init_ctypes},
    {"_lzma", init_lzma},
    {"_sqlite3", init_sqlite3},
    {"grp", initgrp},
    {"_random", init_random},
    {"array", initarray},
    {"_sha512", init_sha512},
    {"_md5", init_md5},
    {"nis", initnis},
    {"_pickle", init_pickle},
    {"math", initmath},
    {"termios", inittermios},
    {"_codecs_hk", init_codecs_hk},
    {"ossaudiodev", initossaudiodev},
    {"_sha256", init_sha256},
    {"_json", init_json},
    {"fcntl", initfcntl},
    {"_socket", init_socket},
    {"cmath", initcmath},
    {"_codecs_tw", init_codecs_tw},
    {"_ssl", init_ssl},
#endif
    {NULL, NULL}
};
#endif

static const char *path_dirs[] = {
    "./nefi2",
    "./nefi2/model",
    "./nefi2/model/categories",
    "./nefi2/model/algorithms",
    "./nefi2/view",
    NULL
};


#if defined(Q_OS_WIN) && PY_MAJOR_VERSION >= 3
#include <windows.h>

extern int pyqtdeploy_start(int argc, wchar_t **w_argv,
        struct _inittab *extension_modules, const char *main_module,
        const char *entry_point, const char **path_dirs);

int main(int argc, char **)
{
    LPWSTR *w_argv = CommandLineToArgvW(GetCommandLineW(), &argc);

    return pyqtdeploy_start(argc, w_argv, extension_modules, "__main__", NULL, path_dirs);
}
#else
extern int pyqtdeploy_start(int argc, char **argv,
        struct _inittab *extension_modules, const char *main_module,
        const char *entry_point, const char **path_dirs);

int main(int argc, char **argv)
{
    return pyqtdeploy_start(argc, argv, extension_modules, "__main__", NULL, path_dirs);
}
#endif
