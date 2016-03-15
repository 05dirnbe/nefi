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


import argparse
import os
import sys


def main():
    """ The entry point for the setuptools generated CLI wrapper. """

    # Parse the command line.
    parser = argparse.ArgumentParser()

    parser.add_argument('action',
            help="the action to perform",
            choices=('build', 'configure', 'install', 'show-packages',
                    'show-targets', 'show-version'))
    parser.add_argument('--disable-patches',
            help="disable the patching of the Python source code (configure)",
            action='store_true')
    parser.add_argument('--enable-dynamic-loading',
            help="enable the dynamic loading of modules (configure)",
            action='store_true')
    parser.add_argument('--include-dir',
            help="the target Python include directory (build)", metavar="DIR")
    parser.add_argument('--interpreter',
            help="the host interpreter executable (build)",
            metavar="EXECUTABLE")
    parser.add_argument('--opt',
            help="the optimisation level where 0 is none, 1 is no asserts, 2 "
                    "is no asserts or docstrings (build) [default: 2]",
            metavar="LEVEL", type=int, choices=range(3), default=2),
    parser.add_argument('--output',
            help="the name of the output file or directory (configure, build)",
            metavar="OUTPUT")
    parser.add_argument('--package',
            help="the package name (configure, install)",
            metavar="PACKAGE")
    parser.add_argument('--project', help="the project file (build)",
            metavar="FILE")
    parser.add_argument('--python-library',
            help="the target Python library (build)", metavar="LIB")
    parser.add_argument('--resources',
            help="the number of .qrc resource files to generate (build) "
                    "[default: 1]",
            metavar="NUMBER", type=int, default=1),
    parser.add_argument('--source-dir',
            help="the Python source code directory (build)", metavar="DIR")
    parser.add_argument('--standard-library-dir',
            help="the target Python standard library directory (build)",
            metavar="DIR")
    parser.add_argument('--sysroot',
            help="the system image root directory (install)",
            metavar="DIR")
    parser.add_argument('--system-python',
            help="use the system installed Python (install)",
            metavar="VERSION")
    parser.add_argument('--target',
            help="the target platform (configure, install)",
            metavar="TARGET")
    parser.add_argument('--quiet', help="disable progress messages (build)",
            action='store_true')
    parser.add_argument('--verbose',
            help="enable verbose progress messages (configure, build)",
            action='store_true')

    args = parser.parse_args()

    # Handle the specific actions.
    if args.action == 'build':
        rc = build(args)
    elif args.action == 'configure':
        rc = configure(args)
    elif args.action == 'install':
        rc = install(args)
    elif args.action == 'show-packages':
        rc = show_packages(args)
    elif args.action == 'show-targets':
        rc = show_targets(args)
    elif args.action == 'show-version':
        rc = show_version(args)
    else:
        # This should never happen.
        rc = 1

    return rc


def build(args):
    """ Perform the build action. """

    if args.project is None:
        missing_argument('--project')
        return 2

    if args.resources < 1:
        print(
                "{0}: error: argument --resources: number must be at least 1".format(
                        os.path.basename(sys.argv[0])),
                file=sys.stderr)
        return 2

    from . import Builder, MessageHandler, Project, UserException

    message_handler = MessageHandler(args.quiet, args.verbose)

    try:
        builder = Builder(Project.load(args.project), message_handler)
        builder.build(args.opt, args.resources, build_dir=args.output,
                include_dir=args.include_dir, interpreter=args.interpreter,
                python_library=args.python_library, source_dir=args.source_dir,
                standard_library_dir=args.standard_library_dir)
    except UserException as e:
        handle_exception(e, args.verbose)
        return 1

    return 0


def configure(args):
    """ Perform the configure action. """

    if args.package is None:
        missing_argument('--package')
        return 2

    if args.package == 'python':
        from . import configure_python, MessageHandler, UserException

        message_handler = MessageHandler(args.quiet, args.verbose)

        try:
            configure_python(args.target, args.output,
                    args.enable_dynamic_loading, not args.disable_patches,
                    message_handler)
        except UserException as e:
            handle_exception(e, args.verbose)
            return 1
    else:
        from . import configure_package, UserException

        try:
            configure_package(args.package, args.target, args.output)
        except UserException as e:
            handle_exception(e, args.verbose)
            return 1

    return 0


def install(args):
    """ Perform the install action. """

    # Note that the intent is to support the installation of all supported
    # packages into sysroot in a future version.  For now we just handle the
    # Windows version of Python installed from the official installers.

    if args.package is None:
        missing_argument('--package')
        return 2

    if args.sysroot is None:
        missing_argument('--sysroot')
        return 2

    if args.package == 'python':
        from . import install_python, MessageHandler, UserException

        message_handler = MessageHandler(args.quiet, args.verbose)

        try:
            install_python(args.target, args.sysroot, args.system_python,
                    message_handler)
        except UserException as e:
            handle_exception(e, args.verbose)
            return 1
    else:
        error("install only supports the python package at the moment.")
        return 1

    return 0


def show_packages(args):
    """ Perform the show-packages action. """

    from . import get_supported_packages, UserException

    try:
        packages = get_supported_packages()
    except UserException as e:
        handle_exception(e, args.verbose)
        return 1

    show(packages)

    return 0


def show_targets(args):
    """ Perform the show-targets action. """

    from . import get_supported_targets, UserException

    try:
        targets = get_supported_targets()
    except UserException as e:
        handle_exception(e, args.verbose)
        return 1

    show(targets)

    return 0


def show_version(args):
    """ Perform the show-version action. """

    from . import PYQTDEPLOY_RELEASE

    print(PYQTDEPLOY_RELEASE)


def show(items):
    """ Show an unsorted list of items on stdout. """

    for item in sorted(items):
        print(item)


def missing_argument(name):
    """ Tell the user about a missing argument. """

    # Mimic the argparse message.
    error("error: the following arguments are required: {0}".format(name))


def handle_exception(e, verbose):
    """ Tell the user about an exception. """

    if verbose and e.detail != '':
        error("{0}: {1}".format(e.text, e.detail))
    else:
        error(e.text)


def error(message):
    """ Tell the user about an error. """

    print("{0}: {1}".format(os.path.basename(sys.argv[0]), message),
            file=sys.stderr)
