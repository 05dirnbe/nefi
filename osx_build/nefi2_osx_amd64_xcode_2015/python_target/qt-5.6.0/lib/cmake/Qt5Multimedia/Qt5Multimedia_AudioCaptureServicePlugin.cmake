
add_library(Qt5::AudioCaptureServicePlugin MODULE IMPORTED)

_populate_Multimedia_plugin_properties(AudioCaptureServicePlugin RELEASE "mediaservice/libqtmedia_audioengine.a")

list(APPEND Qt5Multimedia_PLUGINS Qt5::AudioCaptureServicePlugin)
