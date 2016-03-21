
add_library(Qt5::QGeoPositionInfoSourceFactoryCL MODULE IMPORTED)

_populate_Positioning_plugin_properties(QGeoPositionInfoSourceFactoryCL RELEASE "position/libqtposition_cl.a")

list(APPEND Qt5Positioning_PLUGINS Qt5::QGeoPositionInfoSourceFactoryCL)
