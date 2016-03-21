
add_library(Qt5::QQmlDebuggerServiceFactory MODULE IMPORTED)

_populate_Qml_plugin_properties(QQmlDebuggerServiceFactory RELEASE "qmltooling/libqmldbg_debugger.a")

list(APPEND Qt5Qml_PLUGINS Qt5::QQmlDebuggerServiceFactory)
