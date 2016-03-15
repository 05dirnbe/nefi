# Copyright (c) 2015, Riverbank Computing Limited
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


# The supported versions.
_supported_versions = (
    ((3, 5, 1), "3.5.1 and later"),
    ((3, 5, 0), "3.5.0"),
    ((3, 4, 4), "3.4.4"),
    ((3, 4, 3), "3.4.3"),
    ((3, 4, 2), "3.4.2"),
    ((3, 4, 1), "3.4.1"),
    ((3, 4, 0), "3.4.0"),
    ((3, 3, 0), "3.3.x"),
    ((2, 7, 11), "2.7.11"),
    ((2, 7, 10), "2.7.10"),
    ((2, 7, 9), "2.7.9"),
    ((2, 7, 0), "2.7 to 2.7.8"))


def get_supported_python_versions():
    """ Return the sequence of strings describing each supported version. """

    return [text for _, text in _supported_versions]


def get_supported_python_version_index(version):
    """ Return the index of a particular version. """

    for idx, (v, _) in enumerate(_supported_versions):
        if v == version:
            return idx

    # This should never happen.
    raise ValueError('invalid version {0}'.format(version))


def get_supported_python_version(idx):
    """ Return the version corresponding to a particular index. """

    return _supported_versions[idx][0]


def get_latest_supported_python_version():
    """ Return the latest version. """

    return _supported_versions[0][0]
