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

from ..file_utilities import create_file, open_file, read_embedded_file
from ..user_exception import UserException

from .diff_parser import parse_diffs


def apply_diffs(diff_file, patch_dir, message_handler):
    """ Apply an embedded diff file to a directory. """

    diffs = read_embedded_file(diff_file)

    for diff in parse_diffs(diffs):
        _apply_diff(diff, patch_dir, message_handler)


def _apply_diff(diff, patch_dir, message_handler):
    """ Apply a single diff. """

    # Note that (at the moment) we don't support a fuzz factor and the old
    # lines of a hunk must be found at the expected line.  If it turns out that
    # we would significantly reduce the need for new patches for later versions
    # of Python by supporting a fuzz factor then we will do so.

    src_file_name = os.path.join(patch_dir, diff.file_name)
    dst_file_name = src_file_name + '.new'

    message_handler.progress_message("Patching {0}".format(src_file_name))

    src_file = open_file(src_file_name)
    dst_file = create_file(dst_file_name)

    src_line_nr = 1

    for hunk in diff.hunks:
        # Copy the old lines before the hunk.
        while src_line_nr < hunk.old_start:
            line = src_file.readline()
            src_line_nr += 1

            dst_file.write(line)

        # Skip the old lines while checking they are as expected.
        for hunk_line in hunk.old_lines:
            line = src_file.readline()
            src_line_nr += 1

            if hunk_line != line:
                raise UserException(
                        "{0}:{1}: line does not match diff context".format(
                                src_file_name, src_line_nr))

        # Write the new lines.
        for line in hunk.new_lines:
            dst_file.write(line)

    # Copy the remaining lines.
    for line in src_file.readlines():
        dst_file.write(line)

    src_file.close()
    dst_file.close()

    # Rename the files.
    os.rename(src_file_name, src_file_name + '.orig')
    os.rename(dst_file_name, src_file_name)
