
add_library(Qt5::AVFMediaPlayerServicePlugin MODULE IMPORTED)

_populate_Multimedia_plugin_properties(AVFMediaPlayerServicePlugin RELEASE "mediaservice/libqavfmediaplayer.a")

list(APPEND Qt5Multimedia_PLUGINS Qt5::AVFMediaPlayerServicePlugin)
