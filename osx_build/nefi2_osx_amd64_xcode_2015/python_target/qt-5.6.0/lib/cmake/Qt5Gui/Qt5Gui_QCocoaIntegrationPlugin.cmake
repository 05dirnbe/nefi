
add_library(Qt5::QCocoaIntegrationPlugin MODULE IMPORTED)

_populate_Gui_plugin_properties(QCocoaIntegrationPlugin RELEASE "platforms/libqcocoa.a")

list(APPEND Qt5Gui_PLUGINS Qt5::QCocoaIntegrationPlugin)
