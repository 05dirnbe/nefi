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

from ..user_exception import UserException


class FileDiff:
    """ Encapsulate the diff for a single file. """

    def __init__(self, file_name):
        """ Initialise the object.  file_name is the name of the file relative
        to the source directory using native path separators.
        """

        self.file_name = file_name
        self.hunks = []


class Hunk:
    """ Encapsulate a hunk. """

    def __init__(self, old_start):
        """ Initialise the object.  old_start is the number of the first line
        of the old content to replace.
        """

        self.old_start = old_start
        self.old_lines = []
        self.new_lines = []


def parse_diffs(diff):
    """ Parse a diff and return a list of FileDiff instances. """

    WANT_DIFF, WANT_OLD, WANT_NEW, WANT_RANGES, WANT_BODY = range(5)

    want = WANT_DIFF
    old_length = new_length = 0

    diffs = []

    if diff.endsWith(b'\n'):
        diff.chop(1)

    if diff.isEmpty():
        return diffs

    for line_nr, line in enumerate(diff.split('\n')):
        line = line.data().decode('latin1')
        words = line.split()

        if want == WANT_DIFF:
            if len(words) == 0 or words[0] != 'diff':
                raise _DiffException(line_nr, "diff command line expected")

            want = WANT_OLD
        elif want == WANT_OLD:
            if len(words) < 3 or words[0] != '---':
                raise _DiffException(line_nr, "--- line expected")

            # Remove the root directory from the name of the file being
            # patched.  We assume we won't have a diff with paths containing
            # spaces.
            parts = words[1].split('/')[1:]
            diffs.append(FileDiff(os.path.join(*parts)))

            want = WANT_NEW
        elif want == WANT_NEW:
            if len(words) < 3 or words[0] != '+++':
                raise _DiffException(line_nr, "+++ line expected")

            want = WANT_RANGES
        elif want == WANT_RANGES:
            old_length, new_length = _parse_hunk_header(diffs, words, line_nr)

            want = WANT_BODY
        elif want == WANT_BODY:
            hunk = diffs[-1].hunks[-1]

            if len(words) != 0:
                if words[0] == 'diff':
                    _check_hunk_lengths(hunk, old_length, new_length, line_nr)
                    want = WANT_OLD
                    continue

                if words[0] == '@@':
                    _check_hunk_lengths(hunk, old_length, new_length, line_nr)
                    old_length, new_length = _parse_hunk_header(diffs, words,
                            line_nr)
                    continue

            line += '\n'

            if line.startswith('-'):
                line = line[1:]
                hunk.old_lines.append(line)
            elif line.startswith('+'):
                line = line[1:]
                hunk.new_lines.append(line)
            else:
                if line.startswith(' '):
                    line = line[1:]

                hunk.old_lines.append(line)
                hunk.new_lines.append(line)

    if want != WANT_BODY:
        raise _DiffException(line_nr, "diff seems to be truncated")

    _check_hunk_lengths(diffs[-1].hunks[-1], old_length, new_length, line_nr)

    return diffs


def _parse_hunk_header(diffs, words, line_nr):
    """ Parse a hunk header line and add it to the current diff.  Return a
    2-tuple of the length of the old part and the length of the new part.
    """

    if len(words) != 4 or words[0] != '@@' or words[3] != '@@':
        raise _DiffException(line_nr, "hunk header line expected")

    old_start, old_length = _parse_range(words[1], '-')
    if old_start == 0:
        raise _DiffException(line_nr, "invalid -range")

    new_start, new_length = _parse_range(words[2], '+')
    if new_start == 0:
        raise _DiffException(line_nr, "invalid +range")

    diffs[-1].hunks.append(Hunk(old_start))

    return old_length, new_length


def _check_hunk_lengths(hunk, old_length, new_length, line_nr):
    """ Sanity check the expected lengths of a hunk with the actual lengths.
    """

    if len(hunk.old_lines) != old_length:
        raise _DiffException(line_nr,
                "found {0} old lines, expected {1}".format(len(hunk.old_lines),
                        old_length))

    if len(hunk.new_lines) != new_length:
        raise _DiffException(line_nr,
                "found {0} new lines, expected {1}".format(len(hunk.new_lines),
                        new_length))


def _parse_range(range_str, prefix):
    """ Parse a hunk range and return a 2-tuple of the line number and number
    of lines.  The line number will be 0 if there was an error.
    """

    if range_str[0] != prefix:
        return 0, 0

    line_nr, nr_lines = range_str[1:].split(',', maxsplit=1)

    try:
        line_nr = int(line_nr)
    except ValueError:
        return 0, 0

    try:
        nr_lines = int(nr_lines)
    except ValueError:
        return 0, 0

    return (line_nr, nr_lines)


class _DiffException(UserException):
    """ A UserException specifically related to an unexpected diff file format.
    """

    def __init__(self, line_nr, detail):
        """ Initialise the object. """

        super().__init__("Unexpected diff format",
                "line {0}: {1}".format(line_nr + 1, detail))
