CONFIG+= release static rtti no_plugin_manifest directwrite qpa
host_build {
    QT_ARCH = x86_64
    QT_TARGET_ARCH = x86_64
} else {
    QT_ARCH = x86_64
}
QT_CONFIG += minimal-config small-config medium-config large-config full-config release static zlib angle gif jpeg png freetype harfbuzz accessibility opengl opengles2 egl dbus audio-backend directwrite native-gestures qpa concurrent
#versioning 
QT_VERSION = 5.6.0
QT_MAJOR_VERSION = 5
QT_MINOR_VERSION = 6
QT_PATCH_VERSION = 0

QT_EDITION = OpenSource
QT_DEFAULT_QPA_PLUGIN = qwindows
