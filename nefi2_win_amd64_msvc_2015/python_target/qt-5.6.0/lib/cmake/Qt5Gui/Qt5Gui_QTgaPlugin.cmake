
add_library(Qt5::QTgaPlugin MODULE IMPORTED)

_populate_Gui_plugin_properties(QTgaPlugin RELEASE "imageformats/qtga.lib")

list(APPEND Qt5Gui_PLUGINS Qt5::QTgaPlugin)
