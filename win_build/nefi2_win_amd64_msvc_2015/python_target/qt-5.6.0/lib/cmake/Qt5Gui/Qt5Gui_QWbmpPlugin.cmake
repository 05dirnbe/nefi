
add_library(Qt5::QWbmpPlugin MODULE IMPORTED)

_populate_Gui_plugin_properties(QWbmpPlugin RELEASE "imageformats/qwbmp.lib")

list(APPEND Qt5Gui_PLUGINS Qt5::QWbmpPlugin)
