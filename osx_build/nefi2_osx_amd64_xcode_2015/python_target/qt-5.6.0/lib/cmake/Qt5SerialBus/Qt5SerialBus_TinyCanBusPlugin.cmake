
add_library(Qt5::TinyCanBusPlugin MODULE IMPORTED)

_populate_SerialBus_plugin_properties(TinyCanBusPlugin RELEASE "canbus/libqttinycanbus.a")

list(APPEND Qt5SerialBus_PLUGINS Qt5::TinyCanBusPlugin)
