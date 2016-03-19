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


import os

from PyQt5.QtCore import QDir, QFile, QFileInfo, QIODevice

from .user_exception import UserException


def get_embedded_dir(root, *subdirs):
    """ Return a QDir corresponding to an embedded directory.  root is the root
    directory and will be the __file__ attribute of a pyqtdeploy module.
    subdirs is a sequence of sub-directories from the root.  Return None if no
    such directory exists.
    """

    qdir = QFileInfo(root).absoluteDir()

    for subdir in subdirs:
        if not qdir.cd(subdir):
            return None

    return qdir


def get_embedded_dir_names(root, *subdirs):
    """ Return a list of absolute directory names in an embedded directory.
    root is the root directory and will be the __file__ attribute of a
    pyqtdeploy module.  subdirs is a sequence of sub-directories from the root.
    The directory is assumed to exist.
    """

    qdir = get_embedded_dir(root, *subdirs)

    return [qdir.absoluteFilePath(name)
            for name in qdir.entryList(QDir.Dirs|QDir.NoDotAndDotDot)]


def get_embedded_file_names(root, *subdirs):
    """ Return a list of absolute file names in an embedded directory.  root is
    the root directory and will be the __file__ attribute of a pyqtdeploy
    module.  subdirs is a sequence of sub-directories from the root.  The
    directory is assumed to exist.
    """

    qdir = get_embedded_dir(root, *subdirs)

    return [qdir.absoluteFilePath(name) for name in qdir.entryList(QDir.Files)]


def read_embedded_file(src_name):
    """ Return the contents of an embedded source file as a QByteArray.
    src_name is the name of the source file.  A UserException is raised if
    there was an error.
    """

    src_file = QFile(src_name)

    if not src_file.open(QIODevice.ReadOnly|QIODevice.Text):
        raise UserException(
                "Unable to open file {0}.".format(src_file.fileName()),
                src_file.errorString())

    contents = src_file.readAll()
    src_file.close()

    return contents


def copy_embedded_file(src_name, dst_name, macros={}):
    """ Copy an embedded source file to a destination file.  src_name is the
    name of the source file.  dst_name is the name of the destination file.
    macros is an optional dictionary of key/value string macros and instances
    of each key are replaced by the corresponding value.  A UserException is
    raised if there was an error.
    """

    contents = read_embedded_file(src_name)

    for key, value in macros.items():
        contents.replace(bytes(key, encoding='ascii'),
                bytes(value, encoding='ascii'))

    dst_file = QFile(dst_name)

    if not dst_file.open(QIODevice.WriteOnly|QIODevice.Text):
        raise UserException(
                "Unable to create file {0}.".format(dst_file.fileName()),
                dst_file.errorString())

    if dst_file.write(contents) < 0:
        raise UserException(
                "Unable to write to file {0}.".format(dst_file.fileName()),
                dst_file.errorString())

    dst_file.close()


def create_file(file_name):
    """ Create a text file.  file_name is the name of the file. """

    try:
        return open(file_name, 'wt', encoding='UTF-8')
    except Exception as e:
        raise UserException("Unable to create file {0}".format(file_name),
                str(e))


def open_file(file_name):
    """ Open a text file.  file_name is the name of the file. """

    try:
        return open(file_name, 'rt')
    except Exception as e:
        raise UserException("Unable to open file {0}".format(file_name),
                str(e))


def get_embedded_file_for_version(version, root, *subdirs):
    """ Return the absolute file name in an embedded directory of a file that
    is the most appropriate for a particular version.  version is the encoded
    version.  root is the root directory and will be the __file__ attribute of
    a pyqtdeploy module.  subdirs is a sequence of sub-directories from the
    root.  An empty string is returned if the version is not supported.
    """

    best_version = 0
    best_name = ''

    for name in get_embedded_file_names(root, *subdirs):
        this_version = extract_version(name)

        if this_version <= version and this_version > best_version:
            best_version = this_version
            best_name = name

    return best_name


def extract_version(name):
    """ Return an encoded version number from the name of a file or directory.
    name is the name of the file or directory.  0 is returned if a version
    number could not be extracted.
    """

    name = os.path.basename(name)

    for version_str in name.split('-'):
        if len(version_str) != 0 and version_str[0].isdigit():
            break
    else:
        return 0

    while not version_str[-1].isdigit():
        version_str = version_str[:-1]

    return parse_version(version_str)


def parse_version(version_str):
    """ Return an encoded version number from a string.  version_str is the
    string.  0 is returned if a version number could not be extracted.
    """

    version_parts = version_str.split('.')

    while len(version_parts) < 3:
        version_parts.append('0')

    version = 0

    if len(version_parts) == 3:
        for part in version_parts:
            try:
                part = int(part)
            except ValueError:
                version = 0
                break

            version = (version << 8) + part

    return version
