
add_library(Qt5::AVFServicePlugin MODULE IMPORTED)

_populate_Multimedia_plugin_properties(AVFServicePlugin RELEASE "mediaservice/libqavfcamera.a")

list(APPEND Qt5Multimedia_PLUGINS Qt5::AVFServicePlugin)
