# Copyright (c) 2016, Riverbank Computing Limited
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


import os
import shutil
import sys

from ..file_utilities import parse_version
from ..targets import normalised_target
from ..user_exception import UserException
from .supported_versions import check_version
from .windows import get_windows_install_path


def install_python(target, sysroot, system_python, message_handler):
    """ Install Python into a sysroot for a particular target. """

    # Validate the target.
    target = normalised_target(target)

    # At the moment we only support Windows Python installed from an official
    # installer.
    if not target.startswith('win') or system_python is None or sys.platform != 'win32':
        raise UserException(
                "install only supports Windows Python installed from an "
                "official installer at the moment.")

    sysroot = os.path.abspath(sysroot)

    py_version = parse_version(system_python)

    if py_version == 0:
        raise UserException(
                "Invalid Python version {0}.".format(system_python))

    check_version(py_version)

    py_major = py_version >> 16
    py_minor = (py_version >> 8) & 0xff

    message_handler.progress_message(
            "Installing Python v{0}.{1} for {2} in {3}".format(
                    py_major, py_minor, target, sysroot))

    _install_windows_system_python(py_major, py_minor, sysroot,
            message_handler)


def _install_windows_system_python(py_major, py_minor, sysroot, message_handler):
    """ Install the Windows system Python. """

    install_path = get_windows_install_path(py_major, py_minor)
    message_handler.progress_message(
            "Found Python v{0}.{1} at {2}".format(py_major, py_minor,
                    install_path))

    # The interpreter library.
    lib_dir = os.path.join(sysroot, 'lib')
    _create_dir(lib_dir, message_handler)

    lib_name = 'python{0}{1}.lib'.format(py_major, py_minor)

    _copy_file(install_path + 'libs\\' + lib_name,
            os.path.join(lib_dir, lib_name), message_handler)

    # The DLLs and extension modules.
    dlls_dir = _clean_dir(lib_dir, 'DLLs{0}.{1}'.format(py_major, py_minor),
            message_handler)
    _copy_dir(install_path + 'DLLs', dlls_dir, message_handler,
            ignore=('*.ico', 'tcl*.dll', 'tk*.dll', '_tkinter.pyd'))

    if py_major == 3 and py_minor >= 5:
        py_dll_dir = install_path

        vc_dll = 'vcruntime140.dll'
        _copy_file(py_dll_dir + vc_dll, os.path.join(dlls_dir, vc_dll),
                message_handler)
    else:
        py_dll_dir = 'C:\\Windows\\System32\\'

    py_dll = 'python{0}{1}.dll'.format(py_major, py_minor)

    _copy_file(py_dll_dir + py_dll, os.path.join(dlls_dir, py_dll),
            message_handler)

    # The standard library.
    py_subdir = 'python{0}.{1}'.format(py_major, py_minor)

    dst_dir = _clean_dir(lib_dir, py_subdir, message_handler)
    _copy_dir(install_path + 'Lib', dst_dir, message_handler,
            ignore=('site-packages', '__pycache__', '*.pyc', '*.pyo'))

    # The header files.
    include_dir = os.path.join(sysroot, 'include')
    dst_dir = _clean_dir(include_dir, py_subdir, message_handler)
    _copy_dir(install_path + 'include', dst_dir, message_handler)


def _clean_dir(parent, name, message_handler):
    """ Ensure that a directory doesn't exist but its parent does.  Return the
    full path of the directory.
    """

    name_path = os.path.join(parent, name)

    _create_dir(parent, message_handler)
    _remove_dir(name_path, message_handler)

    return name_path


def _copy_file(src, dst, message_handler):
    """ Copy a file. """

    message_handler.progress_message("Copying {0} to {1}".format(src, dst))

    try:
        shutil.copy(src, dst)
    except Exception as e:
        raise UserException("Unable to copy {0}.".format(src),
                detail=str(e))


def _copy_dir(src, dst, message_handler, ignore=None):
    """ Copy a directory and its contents. """

    message_handler.progress_message("Copying {0} to {1}".format(src, dst))

    if ignore is not None:
        ignore = shutil.ignore_patterns(*ignore)

    try:
        shutil.copytree(src, dst, ignore=ignore)
    except Exception as e:
        raise UserException("Unable to copy directory {0}.".format(src),
                detail=str(e))


def _create_dir(name, message_handler):
    """ Ensure a directory exists. """

    message_handler.progress_message("Creating {0}".format(name))

    try:
        os.makedirs(name, exist_ok=True)
    except Exception as e:
        raise UserException("Unable to create directory {0}.".format(name),
                detail=str(e))


def _remove_dir(name, message_handler):
    """ Remove a directory and its contents. """

    if os.path.exists(name):
        message_handler.progress_message("Removing {0}".format(name))

        try:
            shutil.rmtree(name)
        except Exception as e:
            raise UserException("Unable to remove directory {0}.".format(name),
                    detail=str(e))
