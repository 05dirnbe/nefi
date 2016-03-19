
add_library(Qt5::QLocalClientConnectionFactory MODULE IMPORTED)

_populate_Qml_plugin_properties(QLocalClientConnectionFactory RELEASE "qmltooling/qmldbg_local.lib")

list(APPEND Qt5Qml_PLUGINS Qt5::QLocalClientConnectionFactory)
