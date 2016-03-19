# Copyright (c) 2014, Riverbank Computing Limited
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

from ..file_utilities import (copy_embedded_file, get_embedded_dir,
        get_embedded_dir_names)
from ..targets import normalised_target
from ..user_exception import UserException


# The mapping of supported main targets to Python platforms.
_TARGET_PYPLATFORM_MAP = {
    'linux':    'linux',
    'win':      'win32',
    'osx':      'darwin',
    'ios':      'darwin',
    'android':  'linux'
}


def configure_package(package, target, output):
    """ Write a configuration file for a particular package and target. """

    # Get the package directory and check it is valid.
    package_dir = get_embedded_dir(__file__, 'configurations', package)

    if package_dir is None:
        raise UserException(
                "'{0}' is not a supported package.".format(package))

    # Get the main target platform.
    target, _ = normalised_target(target).split('-', maxsplit=1)
    py_platform = _TARGET_PYPLATFORM_MAP[target]

    # Make sure we have a name to write to.
    if output is None:
        output = _get_configuration_name(package, target)

    # See if there is a target-specific file.
    name = _get_configuration_name(package, target)
    if not package_dir.exists(name):
        name = _get_configuration_name(package)
        if not package_dir.exists(name):
            raise UserException(
                    "There is no configuration file for target '{0}'.".format(
                            target))

    # Copy the configuration file.
    copy_embedded_file(package_dir.absoluteFilePath(name), output,
            macros={'@PY_PLATFORM@': py_platform})


def get_supported_packages():
    """ Return the list of supported packages. """

    packages = [os.path.basename(name)
            for name in get_embedded_dir_names(__file__, 'configurations')]
    packages.append('python')

    return packages


def show_packages():
    """ Write the list of packages for which configuration files exist to
    stdout.
    """

    for package in sorted(get_supported_packages()):
        print(package)


def _get_configuration_name(package, target=None):
    """ Return the name of a configuration file for a platform and optional
    target.
    """

    if target is None:
        return '{0}.cfg'.format(package)

    return '{0}-{1}.cfg'.format(package, target)
