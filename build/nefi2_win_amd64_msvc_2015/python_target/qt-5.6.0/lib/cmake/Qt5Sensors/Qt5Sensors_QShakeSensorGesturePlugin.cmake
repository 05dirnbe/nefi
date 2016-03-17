
add_library(Qt5::QShakeSensorGesturePlugin MODULE IMPORTED)

_populate_Sensors_plugin_properties(QShakeSensorGesturePlugin RELEASE "sensorgestures/qtsensorgestures_shakeplugin.lib")

list(APPEND Qt5Sensors_PLUGINS Qt5::QShakeSensorGesturePlugin)
