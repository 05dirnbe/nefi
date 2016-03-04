:::::::::::::::::::::::::::::::
:: Installing NEFI dependencies
:::::::::::::::::::::::::::::::
:: NET SEND %ComputerName% This is a popup message.

:: NET SEND %ComputerName%
:: error: you already have a python interpreter installed on your system.
:: Unfortunatly the interpreter version is not compatible with the project.
:: You may consider to remove your python interpreter in, so the installer is able to install the proper Python version!"


:: if exist C:\Python34
::     GOTO RESOURCES
::     GOTO INTERPRETERCHECK

:: :INTERPRETERCHECK
:: IF DEFINED Python
::     GOTO MALPYTHONINSTALLATION
::     GOTO INSTALLPYTHON

:: :MALPYTHONINSTALLATION
:: echo your python interpreter is not matching the project resources
:: start "" /wait cmd /c "echo error: you already have a python
:: interpreter installed on your system.
:: Unfortunatly the interpreter version is not compatible with
:: the project. You may consider to remove your python interpreter in
:: , so the installer is able to install the proper Python version!&echo(&pause"

:: :INSTALLPYTHON
:: echo the installer takes care on a fresh python interpreter installation
:: call python-3.4.4.msi

:RESOURCES
:: echo interpreter installed, we now take care on the project resources
easy_install demjson-2.2.4-py3.4.egg
pip install decorator-4.0.6-py2.py3-none-any.whl
pip install networkx-1.10.tar.gz
pip install opencv_python-3.1.0-cp34-none-win32.whl
pip install numpy-1.10.4+mkl-cp34-none-win32.whl
easy_install thinning-1.2.3-py3.4-win32.egg
start PyQt5-5.5.1-gpl-Py3.4-Qt5.5.1-x32.exe
pip install Sphinx-1.2-py33-none-any.whl
easy_install QDarkStyle-2.1-py3.4.egg
pip install sip-4.17.zip
call PyQt5-5.5.1-gpl-Py3.4-Qt5.5.1-x32.exe



