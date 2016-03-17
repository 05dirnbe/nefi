
add_library(Qt5::QTcpServerConnectionFactory MODULE IMPORTED)

_populate_Qml_plugin_properties(QTcpServerConnectionFactory RELEASE "qmltooling/qmldbg_tcp.lib")

list(APPEND Qt5Qml_PLUGINS Qt5::QTcpServerConnectionFactory)
