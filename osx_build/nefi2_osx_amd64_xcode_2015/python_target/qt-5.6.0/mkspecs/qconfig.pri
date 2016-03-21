#configuration
CONFIG +=  static qpa no_mocdepend release qt_no_framework
host_build {
    QT_ARCH = x86_64
    QT_TARGET_ARCH = x86_64
} else {
    QT_ARCH = x86_64
    QMAKE_DEFAULT_LIBDIRS = /lib /usr/lib
    QMAKE_DEFAULT_INCDIRS = /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1 /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/clang/7.0.2/include /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.11.sdk/usr/include
}
QT_CONFIG +=  minimal-config small-config medium-config large-config full-config no-pkg-config c++11 c++14 c++1z accessibility opengl static qpa reduce_exports getaddrinfo ipv6ifname getifaddrs jpeg png gif freetype harfbuzz system-zlib nis cups iconv dbus ssl securetransport rpath corewlan concurrent audio-backend release

#versioning
QT_VERSION = 5.6.0
QT_MAJOR_VERSION = 5
QT_MINOR_VERSION = 6
QT_PATCH_VERSION = 0

#namespaces
QT_LIBINFIX = 
QT_NAMESPACE = 

QT_EDITION = OpenSource

QT_DEFAULT_QPA_PLUGIN = qcocoa

QT_COMPILER_STDCXX = 199711
QT_APPLE_CLANG_MAJOR_VERSION = 7
QT_APPLE_CLANG_MINOR_VERSION = 0
