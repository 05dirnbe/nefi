:::::::::::::::::::::::::::::::
:: Installing NEFI dependencies
:::::::::::::::::::::::::::::::
:: Install numpy, networkx, opencv
pip install numpy
pip install networkx
pip install opencv_python-2.4.12-cp27-none-win32.whl

:: Install thinning
CALL mingw-get-setup.exe
mingw-get install mingw32-base
mingw-get install mingw32-gcc-g++
SET PATH=%PATH%;C:\MinGW\bin
:: Good user always installs Python where told
COPY distutils.cfg C:\Python27\Lib\distutils\
pip install thinning
DEL C:\Python27\Lib\distutils\distutils.cfg

:: Install PyQt5
::CALL PyQt5-5.5.1-gpl-Py3.4-Qt5.5.1-x64.exe
