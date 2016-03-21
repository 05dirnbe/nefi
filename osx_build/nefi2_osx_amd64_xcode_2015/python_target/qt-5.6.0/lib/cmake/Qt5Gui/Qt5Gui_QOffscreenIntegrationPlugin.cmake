
add_library(Qt5::QOffscreenIntegrationPlugin MODULE IMPORTED)

_populate_Gui_plugin_properties(QOffscreenIntegrationPlugin RELEASE "platforms/libqoffscreen.a")

list(APPEND Qt5Gui_PLUGINS Qt5::QOffscreenIntegrationPlugin)
