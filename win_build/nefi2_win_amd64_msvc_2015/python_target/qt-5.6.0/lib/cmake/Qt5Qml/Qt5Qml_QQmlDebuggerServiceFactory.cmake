
add_library(Qt5::QQmlDebuggerServiceFactory MODULE IMPORTED)

_populate_Qml_plugin_properties(QQmlDebuggerServiceFactory RELEASE "qmltooling/qmldbg_debugger.lib")

list(APPEND Qt5Qml_PLUGINS Qt5::QQmlDebuggerServiceFactory)
