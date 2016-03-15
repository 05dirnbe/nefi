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


import struct
import sys

from .user_exception import UserException


def get_supported_targets():
    """ Return the sequence of supported targets. """

    return ('android-32', 'ios-64', 'linux-32', 'linux-64', 'osx-64', 'win-32',
            'win-64')


def normalised_target(target):
    """ Return a string which is the normalised version of a target.  If target
    is None then the host target is returned with '-32' or '-64' appended.  A
    UserException is raised if the target is unsupported.
    """

    if target is None:
        if sys.platform.startswith('linux'):
            main_target = 'linux'
        elif sys.platform == 'win32':
            main_target = 'win'
        elif sys.platform == 'darwin':
            main_target = 'osx'
        else:
            # This will fail.
            main_target = sys.platform

        target = '{0}-{1}'.format(main_target, 8 * struct.calcsize('P'))

    if target not in get_supported_targets():
        raise UserException("'{0}' is not a supported target.".format(target))

    return target
