CONFIG +=  compile_examples qpa largefile precompile_header sse2 sse3 ssse3 sse4_1 sse4_2 avx avx2 pcre
QT_BUILD_PARTS += libs tools
QT_NO_DEFINES =  ALSA CLOCK_MONOTONIC EGL EGLFS EGL_X11 EVDEV EVENTFD FONTCONFIG GLIB INOTIFY LIBPROXY MREMAP OPENSSL OPENVG POSIX_FALLOCATE PULSEAUDIO STYLE_GTK TSLIB XRENDER ZLIB
QT_QCONFIG_PATH = 
host_build {
    QT_CPU_FEATURES.x86_64 =  cx16 mmx sse sse2 sse3 ssse3
} else {
    QT_CPU_FEATURES.x86_64 =  cx16 mmx sse sse2 sse3 ssse3
}
QT_COORD_TYPE = double
QT_LFLAGS_ODBC   = -lodbc
styles += mac fusion windows
DEFINES += QT_NO_MTDEV
DEFINES += QT_NO_LIBUDEV
DEFINES += QT_NO_EVDEV
DEFINES += QT_NO_TSLIB
DEFINES += QT_NO_LIBINPUT
sql-drivers = 
sql-plugins =  sqlite
