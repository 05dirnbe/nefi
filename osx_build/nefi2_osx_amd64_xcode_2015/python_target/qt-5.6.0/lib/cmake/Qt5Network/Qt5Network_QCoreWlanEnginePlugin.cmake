
add_library(Qt5::QCoreWlanEnginePlugin MODULE IMPORTED)

_populate_Network_plugin_properties(QCoreWlanEnginePlugin RELEASE "bearer/libqcorewlanbearer.a")

list(APPEND Qt5Network_PLUGINS Qt5::QCoreWlanEnginePlugin)
