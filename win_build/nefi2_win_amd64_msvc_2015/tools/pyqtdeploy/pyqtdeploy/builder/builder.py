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


import csv
import os
import shlex
import shutil
import sys

from PyQt5.QtCore import (QByteArray, QCoreApplication, QDir, QFile,
        QFileDevice, QFileInfo, QProcess, QTemporaryDir, QTextCodec)

from ..file_utilities import (create_file, get_embedded_dir,
        get_embedded_file_for_version, read_embedded_file)
from ..metadata import (external_libraries_metadata, get_python_metadata,
        PLATFORM_SCOPES, pyqt4_metadata, pyqt5_metadata)
from ..project import QrcDirectory
from ..python import get_windows_install_path
from ..user_exception import UserException
from ..version import PYQTDEPLOY_HEXVERSION


# The sequence of all platform scopes.
ALL_SCOPES = tuple((scope for scope, platform, subscopes in PLATFORM_SCOPES))


class Builder():
    """ The builder for a project. """

    def __init__(self, project, message_handler):
        """ Initialise the builder for a project. """

        super().__init__()

        self._project = project
        self._message_handler = message_handler

    def build(self, opt, nr_resources, build_dir=None, clean=False, include_dir=None, interpreter=None, python_library=None, source_dir=None, standard_library_dir=None):
        """ Build the project in a given directory.  Raise a UserException if
        there is an error.
        """

        project = self._project

        py_major, py_minor, py_patch = project.python_target_version

        # Create a temporary directory which will be removed automatically when
        # this function's objects are garbage collected.
        temp_dir = QTemporaryDir()
        if not temp_dir.isValid():
            raise UserException(
                    "There was an error creating a temporary directory")

        # Get the names of the required Python modules, extension modules and
        # libraries.
        metadata = get_python_metadata(project.python_target_version)
        required_modules, required_libraries = project.get_stdlib_requirements(
                include_hidden=True)

        required_py = {}
        required_ext = {}
        for name in required_modules.keys():
            module = metadata[name]

            if module.source is None:
                required_py[name] = module
            elif not module.core:
                required_ext[name] = module

        # Initialise and check we have the information we need.
        if len(required_ext) != 0:
            if source_dir is None:
                if project.python_source_dir == '':
                    raise UserException(
                            "The name of the Python source directory has not "
                            "been specified")

                source_dir = project.path_from_user(project.python_source_dir)

        if project.get_executable_basename() == '':
            raise UserException("The name of the application has not been "
                    "specified and cannot be inferred")

        if project.application_script == '':
            if project.application_entry_point == '':
                raise UserException("Either the application script name or "
                        "the entry point must be specified")
            elif len(project.application_entry_point.split(':')) != 2:
                raise UserException("An entry point must be a module name and "
                        "a callable separated by a colon.")
        elif project.application_entry_point != '':
            raise UserException("Either the application script name or the "
                    "entry point must be specified but not both")

        # Get other directories from the project that may be overridden.
        if include_dir is None:
            include_dir = project.path_from_user(
                    project.python_target_include_dir)

        if interpreter is None:
            if project.python_host_interpreter != '':
                # Note that we assume a relative filename is on PATH rather
                # than being relative to the project file.
                interpreter = project.expandvars(
                        project.python_host_interpreter)
            elif sys.platform == 'win32':
                interpreter = get_windows_install_path(py_major, py_minor) + 'python'
            else:
                interpreter = 'python{0}.{1}'.format(py_major, py_minor)

        if python_library is None:
            python_library = project.path_from_user(
                    project.python_target_library)

        if standard_library_dir is None:
            standard_library_dir = project.path_from_user(
                    project.python_target_stdlib_dir)

        # Get the name of the build directory.
        if build_dir is None:
            build_dir = project.build_dir
            if build_dir == '':
                build_dir = '.'

            build_dir = project.path_from_user(build_dir)

        # Remove any build directory if required.
        if clean:
            native_build_dir = QDir.toNativeSeparators(build_dir)
            self._message_handler.progress_message(
                    "Cleaning {0}".format(native_build_dir))
            shutil.rmtree(native_build_dir, ignore_errors=True)

        # Now start the build.
        self._create_directory(build_dir)

        # Create the job file and writer.
        job_filename = QDir.toNativeSeparators(temp_dir.path() + '/jobs.csv')
        job_file = open(job_filename, 'w', newline='')
        job_writer = csv.writer(job_file)

        # Freeze the bootstrap.  Note that from Python v3.5 the modified part
        # is in _bootstrap_external.py and _bootstrap.py is unchanged from the
        # original source.  However we continue to use a local copy of
        # _bootstrap.py for now in case the structure changes again.
        py_version = (py_major << 16) + (py_minor << 8) + py_patch

        self._freeze_bootstrap('bootstrap', py_version, build_dir, temp_dir,
                job_writer)

        if py_version >= 0x030500:
            self._freeze_bootstrap('bootstrap_external', py_version, build_dir,
                    temp_dir, job_writer)

        # Freeze any main application script.
        if project.application_script != '':
            self._freeze(job_writer, build_dir + '/frozen_main.h',
                    project.path_from_user(project.application_script),
                    'pyqtdeploy_main', as_c=True)

        # Create the pyqtdeploy module version file.
        version_f = self._create_file(build_dir + '/pyqtdeploy_version.h')
        version_f.write(
                '#define PYQTDEPLOY_HEXVERSION %s\n' % hex(
                        PYQTDEPLOY_HEXVERSION))
        version_f.close()

        # Generate the application resource.
        resource_names = self._generate_resource(build_dir + '/resources',
                required_py, standard_library_dir, job_writer, nr_resources)

        # Write the .pro file.
        self._write_qmake(py_version, build_dir, required_ext,
                required_libraries, include_dir, python_library,
                standard_library_dir, job_writer, opt, resource_names)

        # Run the freeze jobs.
        job_file.close()

        # The odd naming of Python source files is to prevent them from being
        # frozen if we deploy ourself.
        freeze = self._copy_lib_file(self._get_lib_file_name('freeze.python'),
                temp_dir.path(), dst_file_name='freeze.py')

        self._run_freeze(freeze, interpreter, job_filename, opt)

    def _freeze_bootstrap(self, name, py_version, build_dir, temp_dir, job_writer):
        """ Freeze a version dependent bootstrap script. """

        bootstrap_src = get_embedded_file_for_version(py_version, __file__,
                'lib', name)
        bootstrap = self._copy_lib_file(bootstrap_src, temp_dir.path(),
                dst_file_name=name + '.py')
        self._freeze(job_writer, build_dir + '/frozen_' + name + '.h',
                bootstrap, 'pyqtdeploy_' + name, as_c=True)

    def _generate_resource(self, resources_dir, required_py, standard_library_dir, job_writer, nr_resources):
        """ Generate the application resource. """

        project = self._project

        self._create_directory(resources_dir)
        resource_contents = []

        # Handle any application package.
        if project.application_package.name is not None:
            fi = QFileInfo(project.path_from_user(
                    project.application_package.name))

            package_src_dir = fi.canonicalFilePath()

            package_name = project.application_package.name
            if package_name != '':
                package_name = fi.completeBaseName()

            self._write_package(resource_contents, resources_dir, package_name,
                    project.application_package, package_src_dir, job_writer)

        # Handle the Python standard library.
        self._write_stdlib_py(resource_contents, resources_dir, required_py,
                standard_library_dir, job_writer)

        # Handle any additional packages.
        for package in project.other_packages:
            self._write_package(resource_contents, resources_dir, '', package,
                    project.path_from_user(package.name), job_writer)

        # Handle the PyQt package.
        if len(project.pyqt_modules) != 0:
            pyqt_subdir = 'PyQt5' if project.application_is_pyqt5 else 'PyQt4'
            pyqt_dst_dir = resources_dir + '/' +  pyqt_subdir
            pyqt_src_dir = standard_library_dir + '/site-packages/' + pyqt_subdir

            self._create_directory(pyqt_dst_dir)

            self._freeze(job_writer, pyqt_dst_dir + '/__init__.pyo',
                    pyqt_src_dir + '/__init__.py',
                    pyqt_subdir + '/__init__.py')

            resource_contents.append(pyqt_subdir + '/__init__.pyo')

            # Handle the PyQt.uic package.
            if 'uic' in project.pyqt_modules:
                skip_dirs = ['__pycache__']
                if project.python_target_version[0] == 3:
                    skip_dirs.append('port_v2')
                else:
                    skip_dirs.append('port_v3')

                def copy_freeze(src, dst):
                    for skip in skip_dirs:
                        if skip in src:
                            break
                    else:
                        if dst.endswith('.py'):
                            src = QDir.fromNativeSeparators(src)
                            dst = QDir.fromNativeSeparators(dst)
                            rel_dst = dst[len(resources_dir) + 1:]

                            self._freeze(job_writer, dst + 'o', src, rel_dst)

                            resource_contents.append(rel_dst)

                shutil.copytree(QDir.toNativeSeparators(pyqt_src_dir + '/uic'),
                        QDir.toNativeSeparators(pyqt_dst_dir + '/uic'),
                        copy_function=copy_freeze)

        # Write the .qrc files.
        if nr_resources == 1:
            resource_names = [self._write_resource(resources_dir,
                    resource_contents)]
        else:
            resource_names = []

            nr_files = len(resource_contents)

            if nr_resources > nr_files:
                nr_resources = nr_files

            per_resource = (nr_files + nr_resources - 1) // nr_resources
            start = 0

            for r in range(nr_resources):
                end = start + per_resource
                if end > nr_files:
                    end = nr_files

                resource_names.append(
                        self._write_resource(resources_dir,
                                resource_contents[start:end], r))
                start += per_resource

        return resource_names

    def _write_resource(self, resources_dir, resource_contents, nr=-1):
        """ Write a single resource file and return its basename. """

        suffix = '' if nr < 0 else str(nr)
        basename = 'pyqtdeploy{0}.qrc'.format(suffix)

        f = self._create_file(resources_dir + '/' + basename)

        f.write('''<!DOCTYPE RCC>
<RCC version="1.0">
    <qresource>
''')

        for content in resource_contents:
            f.write('        <file>{0}</file>\n'.format(content))

        f.write('''    </qresource>
</RCC>
''')

        f.close()

        return basename

    def _write_stdlib_py(self, resource_contents, resources_dir, required_py, standard_library_dir, job_writer):
        """ Write the required parts of the Python standard library that are
        implemented in Python.
        """

        project = self._project

        # By sorting the names we ensure parents are handled before children.
        for name in sorted(required_py.keys()):
            name_path = name.replace('.', '/')

            if required_py[name].modules is None:
                in_file = name_path + '.py'
                out_file = name_path + '.pyo'
            else:
                in_file = name_path + '/__init__.py'
                out_file = name_path + '/__init__.pyo'
                self._create_directory(resources_dir + '/' + name_path)

            self._freeze(job_writer, resources_dir + '/' + out_file,
                    standard_library_dir + '/' + in_file, in_file)

            resource_contents.append(out_file)

    # The map of non-C/C++ source extensions to qmake variable.
    _source_extensions = {
        '.asm':     'MASMSOURCES',
        '.h':       'HEADERS',
        '.java':    'JAVASOURCES',
        '.l':       'LEXSOURCES',
        '.pyx':     'CYTHONSOURCES',
        '.y':       'YACCSOURCES',
    }

    def _write_qmake(self, py_version, build_dir, required_ext, required_libraries, include_dir, python_library, standard_library_dir, job_writer, opt, resource_names):
        """ Create the .pro file for qmake. """

        project = self._project

        f = self._create_file(build_dir + '/' +
                project.get_executable_basename() + '.pro')

        f.write('TEMPLATE = app\n')

        # Configure the CONFIG and QT values that are project dependent.
        needs_cpp11 = False
        needs_gui = False
        qmake_qt4 = set()
        qmake_config4 = set()
        qmake_qt5 = set()
        qmake_config5 = set()

        for pyqt_m in project.pyqt_modules:
            metadata = self._get_pyqt_module_metadata(pyqt_m)

            if metadata.cpp11:
                needs_cpp11 = True

            if metadata.gui:
                needs_gui = True

            qmake_qt4.update(metadata.qt4)
            qmake_config4.update(metadata.config4)
            qmake_qt5.update(metadata.qt5)
            qmake_config5.update(metadata.config5)

        both_qt = qmake_qt4 & qmake_qt5
        qmake_qt4 -= both_qt
        qmake_qt5 -= both_qt

        both_config = qmake_qt4 & qmake_qt5
        qmake_config4 -= both_config
        qmake_config5 -= both_config

        both_config.add('warn_off')

        if project.application_is_console or not needs_gui:
            both_config.add('console')

        if needs_cpp11:
            both_config.add('c++11')

        f.write('\n')
        f.write('CONFIG += {0}\n'.format(' '.join(both_config)))

        if not project.application_is_bundle:
            f.write('CONFIG -= app_bundle\n')

        if not needs_gui:
            f.write('QT -= gui\n')

        if both_qt:
            f.write('QT += {0}\n'.format(' '.join(both_qt)))

        if qmake_config4 or qmake_qt4:
            f.write('\n')
            f.write('lessThan(QT_MAJOR_VERSION, 5) {\n')

            if qmake_config4:
                f.write('    CONFIG += {0}\n'.format(' '.join(qmake_config4)))

            if qmake_qt4:
                f.write('    QT += {0}\n'.format(' '.join(qmake_qt4)))

            f.write('}\n')

        if qmake_config5 or qmake_qt5:
            f.write('\n')
            f.write('greaterThan(QT_MAJOR_VERSION, 4) {\n')

            if qmake_config5:
                f.write('    CONFIG += {0}\n'.format(' '.join(qmake_config5)))

            if qmake_qt5:
                f.write('    QT += {0}\n'.format(' '.join(qmake_qt5)))

            f.write('}\n')

        # Modules can share sources so we need to make sure we don't include
        # them more than once.  We might as well handle the other things in the
        # same way.
        used_qt = {}
        used_config = {}
        used_sources = {}
        used_defines = {}
        used_includepath = {}
        used_libs = {}
        used_inittab = {}
        used_dlls = {}

        # Handle any static PyQt modules.
        if len(project.pyqt_modules) > 0:
            site_packages = standard_library_dir + '/site-packages'
            pyqt_version = 'PyQt5' if project.application_is_pyqt5 else 'PyQt4'

            l_libs = []
            for pyqt in self._get_all_pyqt_modules():
                # The sip module is always needed (implicitly or explicitly) if
                # we have got this far.  We handle it separately as it is in a
                # different directory.
                if pyqt == 'sip':
                    continue

                # The uic module is pure Python.
                if pyqt == 'uic':
                    continue

                self._add_value_for_scopes(used_inittab,
                        pyqt_version + '.' + pyqt)

                lib_name = pyqt
                if self._get_pyqt_module_metadata(pyqt).needs_suffix:
                    # Qt4's qmake thinks -lQtCore etc. always refer to the Qt
                    # libraries so PyQt4 creates static libraries with a
                    # suffix.
                    lib_name += '_s'

                l_libs.append('-l' + lib_name)

            # Add the LIBS value for any PyQt modules to the global scope.
            if len(l_libs) > 0:
                self._add_value_for_scopes(used_libs,
                        '-L{0}/{1} {2}'.format(site_packages, pyqt_version,
                                ' '.join(l_libs)))

            # Add the sip module.
            self._add_value_for_scopes(used_inittab, 'sip')
            self._add_value_for_scopes(used_libs,
                    '-L{0} -lsip'.format(site_packages))

        # Handle any other extension modules.
        for other_em in project.other_extension_modules:
            scopes, value = self._get_scopes_and_value(other_em.name,
                    ALL_SCOPES)
            self._add_value_for_scopes(used_inittab, value, scopes)

            if other_em.qt != '':
                self._add_parsed_scoped_values(used_qt, other_em.qt, False)

            if other_em.config != '':
                self._add_parsed_scoped_values(used_config, other_em.config,
                        False)

            if other_em.sources != '':
                self._add_parsed_scoped_values(used_sources, other_em.sources,
                        True)

            if other_em.defines != '':
                self._add_parsed_scoped_values(used_defines, other_em.defines,
                        False)

            if other_em.includepath != '':
                self._add_parsed_scoped_values(used_includepath,
                        other_em.includepath, True)

            if other_em.libs != '':
                self._add_parsed_scoped_values(used_libs, other_em.libs, False)

        # Configure the target Python interpreter.
        if include_dir != '':
            self._add_value_for_scopes(used_includepath, include_dir)

        if python_library != '':
            fi = QFileInfo(python_library)

            py_lib_dir = fi.absolutePath()
            lib = fi.completeBaseName()

            # This is smart enough to translate the Python library as a UNIX .a
            # file to what Windows needs.
            if lib.startswith('lib'):
                lib = lib[3:]

            if '.' in lib:
                self._add_value_for_scopes(used_libs,
                        '-L{0} -l{1}'.format(py_lib_dir, lib.replace('.', '')),
                        ['win32'])
                self._add_value_for_scopes(used_libs,
                        '-L{0} -l{1}'.format(py_lib_dir, lib), ['!win32'])
            else:
                self._add_value_for_scopes(used_libs,
                        '-L{0} -l{1}'.format(py_lib_dir, lib))
        else:
            py_lib_dir = None

        # Handle any standard library extension modules.
        if len(required_ext) != 0:
            source_dir = project.path_from_user(project.python_source_dir)
            source_scopes = set()

            for name, module in required_ext.items():
                # Get the list of all applicable scopes.
                module_scopes = self._stdlib_scopes(module.scope)

                if len(module_scopes) == 0:
                    # The module is specific to a platform for which we are
                    # using the python.org Python libraries so ignore it
                    # completely.
                    continue

                self._add_value_for_scopes(used_inittab, name, module_scopes)

                for source in module.source:
                    scopes, source = self._get_scopes_and_value(source,
                            module_scopes)
                    source = self._python_source_file(source_dir, source)
                    self._add_value_for_scopes(used_sources, source, scopes)

                    source_scopes.update(scopes)

                if module.defines is not None:
                    for define in module.defines:
                        scopes, define = self._get_scopes_and_value(define,
                                module_scopes)
                        self._add_value_for_scopes(used_defines, define,
                                scopes)

                if module.includepath is not None:
                    for includepath in module.includepath:
                        scopes, includepath = self._get_scopes_and_value(
                                includepath, module_scopes)
                        includepath = self._python_source_file(source_dir,
                                includepath)
                        self._add_value_for_scopes(used_includepath,
                                includepath, scopes)

                if module.libs is not None:
                    for lib in module.libs:
                        scopes, lib = self._get_scopes_and_value(lib,
                                module_scopes)
                        self._add_value_for_scopes(used_libs, lib, scopes)

                if module.pyd is not None:
                    self._add_value_for_scopes(used_dlls, module, ['win32'])

            self._add_value_for_scopes(used_includepath,
                    source_dir + '/Modules', source_scopes)

            if 'win32' not in project.python_use_platform:
                self._add_value_for_scopes(used_includepath,
                        source_dir + '/PC', ['win32'])

        # Handle any required external libraries.
        for required_lib in required_libraries:
            for xlib in project.external_libraries:
                if xlib.name == required_lib:
                    if xlib.defines != '':
                        self._add_parsed_scoped_values(used_defines,
                                xlib.defines, False)

                    if xlib.includepath != '':
                        self._add_parsed_scoped_values(used_includepath,
                                xlib.includepath, True)

                    if xlib.libs != '':
                        self._add_parsed_scoped_values(used_libs, xlib.libs,
                                False)

                    break
            else:
                for xlib in external_libraries_metadata:
                    if xlib.name == required_lib:
                        scopes = self._stdlib_scopes()

                        if len(scopes) != 0:
                            for lib in xlib.libs.split():
                                self._add_value_for_scopes(used_libs, lib,
                                        scopes)

                        break

        # Specify the resource files.
        f.write('\n')
        f.write('RESOURCES = \\\n')
        f.write(' \\\n'.join(['    resources/{0}'.format(n) for n in resource_names]))
        f.write('\n')

        # Specify the source and header files.
        f.write('\n')

        f.write('SOURCES = pyqtdeploy_main.cpp pyqtdeploy_start.cpp pdytools_module.cpp\n')
        self._write_main(build_dir, used_inittab)
        self._copy_lib_file('pyqtdeploy_start.cpp', build_dir)
        self._copy_lib_file('pdytools_module.cpp', build_dir)

        defines = []
        headers = ['pyqtdeploy_version.h', 'frozen_bootstrap.h']

        if py_version >= 0x030500:
            headers.append('frozen_bootstrap_external.h')

        if project.application_script != '':
            defines.append('PYQTDEPLOY_FROZEN_MAIN')
            headers.append('frozen_main.h')

        if opt:
            defines.append('PYQTDEPLOY_OPTIMIZED')

        if len(defines) != 0:
            f.write('DEFINES += {0}\n'.format(' '.join(defines)))

        f.write('HEADERS = {0}\n'.format(' '.join(headers)))

        # Get the set of all scopes used.
        used_scopes = set(used_qt.keys())
        used_scopes.update(used_config.keys())
        used_scopes.update(used_sources.keys())
        used_scopes.update(used_defines.keys())
        used_scopes.update(used_includepath.keys())
        used_scopes.update(used_libs.keys())
        used_scopes.update(used_dlls.keys())

        # Write out grouped by scope.
        for scope in used_scopes:
            f.write('\n')

            if scope == '':
                indent = ''
                tail = None
            elif scope.startswith('win32_'):
                # We could avoid the hardcoded handling by reverting to
                # defining appropriate CONFIG values in a pre_configuration.pro
                # file.
                indent = '        '
                f.write(
                        'win32 {\n    %scontains(QMAKE_TARGET.arch, x86_64) {\n' % ('!' if scope == 'win32_x86' else ''))
                tail = '    }\n}\n'
            else:
                indent = '    '
                f.write('%s {\n' % scope)
                tail = '}\n'

            for qt in used_qt.get(scope, ()):
                f.write('{0}QT += {1}\n'.format(indent, qt))

            for config in used_config.get(scope, ()):
                f.write('{0}CONFIG += {1}\n'.format(indent, config))

            for defines in used_defines.get(scope, ()):
                f.write('{0}DEFINES += {1}\n'.format(indent, defines))

            for includepath in used_includepath.get(scope, ()):
                f.write('{0}INCLUDEPATH += {1}\n'.format(indent, includepath))

            for lib in used_libs.get(scope, ()):
                # A (strictly unnecessary) bit of pretty printing.
                if lib.startswith('"-framework') and lib.endswith('"'):
                    lib = lib[1:-1]

                f.write('{0}LIBS += {1}\n'.format(indent, lib))

            for source in used_sources.get(scope, ()):
                for ext, qmake_var in self._source_extensions.items():
                    if source.endswith(ext):
                        break
                else:
                    qmake_var = 'SOURCES'

                f.write('{0}{1} += {2}\n'.format(indent, qmake_var, source))

            if tail is not None:
                f.write(tail)

        # If we are using the platform Python on Windows then copy in the
        # required DLLs if they can be found.
        if 'win32' in project.python_use_platform and used_dlls and py_lib_dir is not None:
            self._copy_windows_dlls(py_version, py_lib_dir, used_dlls['win32'],
                    f)

        # Add the project independent post-configuration stuff.
        self._write_embedded_lib_file('post_configuration.pro', f)

        # Add any application specific stuff.
        qmake_configuration = project.qmake_configuration.strip()

        if qmake_configuration != '':
            f.write('\n' + qmake_configuration + '\n')

        # All done.
        f.close()

    def _copy_windows_dlls(self, py_version, py_lib_dir, modules, f):
        """ Generate additional qmake commands to install additional Windows
        DLLs so that the application will be able to run.
        """

        py_major = py_version >> 16
        py_minor = (py_version >> 8) & 0xff

        dlls = ['python{0}{1}.dll'.format(py_major, py_minor)]

        if py_version >= 0x030500:
            dlls.append('vcruntime140.dll')

        for module in modules:
            dlls.append(module.pyd)

            if module.dlls is not None:
                dlls.extend(module.dlls)

        f.write('\nwin32 {')

        for name in dlls:
            f.write('\n')
            f.write('    PDY_DLL = %s/DLLs%d.%d/%s\n' % (py_lib_dir, py_major, py_minor, name))
            f.write('    exists($$PDY_DLL) {\n')
            f.write('        CONFIG(debug, debug|release) {\n')
            f.write('            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/debug) &\n')
            f.write('        } else {\n')
            f.write('            QMAKE_POST_LINK += $(COPY_FILE) $$shell_path($$PDY_DLL) $$shell_path($$OUT_PWD/release) &\n')
            f.write('        }\n')
            f.write('    }\n')

        f.write('}\n')

    def _write_embedded_lib_file(self, file_name, f):
        """ Write an embedded file from the lib directory. """

        contents = read_embedded_file(self._get_lib_file_name(file_name))

        f.write('\n')
        f.write(contents.data().decode('latin1'))

    def _stdlib_scopes(self, module_scope=''):
        """ Return the list of scopes for the standard library and, optionally,
        one of its modules.
        """

        # Get the list of all applicable scopes.
        stdlib_scopes = list(ALL_SCOPES)

        if module_scope != '':
            if module_scope.startswith('!'):
                stdlib_scopes.remove(module_scope[1:])
            else:
                stdlib_scopes = [module_scope]

        # Remove those scopes for which we are using the python.org Python
        # libraries.
        for plat_scope in self._project.python_use_platform:
            try:
                stdlib_scopes.remove(plat_scope)
            except ValueError:
                pass

        return stdlib_scopes

    @staticmethod
    def _python_source_file(py_source_dir, rel_path):
        """ Return the absolute name of a file in the Python source tree
        relative to the Modules directory.
        """

        file_path = py_source_dir + '/Modules/' + rel_path

        return QFileInfo(file_path).absoluteFilePath()

    def _add_parsed_scoped_values(self, used_values, raw, isfilename):
        """ Parse a string of space separated possible scoped values and add
        them to a dict of used values indexed by scope.  The values are
        optionally treated as filenames where they are converted to absolute
        filenames with UNIX separators and have environment variables expanded.
        """

        scoped_values = self._parse_scoped_values(raw, isfilename)

        for scope, values in scoped_values.items():
            self._add_value_set_for_scope(used_values, values, scope)

    def _parse_scoped_values(self, raw, isfilename):
        """ Parse a string of space separated possible scoped values and return
        a dict, keyed by scope, of the values for each scope.
        """

        project = self._project

        scoped_value_sets = {}

        for scoped_value in self._split_quotes(raw):
            scopes, value = self._get_scopes_and_value(scoped_value, ALL_SCOPES)

            # Convert potential filenames.
            if isfilename:
                value = project.path_from_user(value)
            elif value.startswith('-L'):
                value = '-L' + project.path_from_user(value[2:])

            self._add_value_for_scopes(scoped_value_sets, value, scopes)

        return scoped_value_sets

    @staticmethod
    def _split_quotes(s):
        """ A generator for a splitting a string allowing for quoted spaces.
        """

        s = s.lstrip()

        while s != '':
            quote_stack = []
            i = 0

            for ch in s:
                if ch in '\'"':
                    if len(quote_stack) == 0 or quote_stack[-1] != ch:
                        quote_stack.append(ch)
                    else:
                        quote_stack.pop()
                elif ch == ' ':
                    if len(quote_stack) == 0:
                        break

                i += 1

            yield s[:i]

            s = s[i:].lstrip()

    @staticmethod
    def _get_scopes_and_value(scoped_value, scopes):
        """ Return the 2-tuple of scopes and value from a (possibly) scoped
        value.
        """

        parts = scoped_value.split('#', maxsplit=1)
        if len(parts) == 2:
            scope, value = parts

            if scope.startswith('!'):
                scope = scope[1:]

                # Make sure we don't modify the original list.
                scopes = [s for s in scopes if s != scope]
            else:
                for s in scopes:
                    # Assume sub-scopes start with the scope.
                    if scope.startswith(s):
                        scopes = [scope]
                        break
                else:
                    scopes = []
        else:
            value = parts[0]

        return scopes, value

    @staticmethod
    def _add_value_for_scopes(used_values, value, scopes=ALL_SCOPES):
        """ Add a value to the set of used values for some scopes. """

        # Make sure we have a fresh list as we may want to modify it.
        scopes = list(scopes)

        # Optimise any sub-scopes.
        for scope, platform, subscopes in PLATFORM_SCOPES:
            if len(subscopes) == 0:
                continue

            if scope in scopes:
                # Remove any redundant sub-scopes.
                for ss in subscopes:
                    try:
                        scopes.remove(ss)
                    except ValueError:
                        pass
            else:
                # Replace all sub-scopes if all are present.
                collapsed = [s for s in scopes if s not in subscopes]

                if len(collapsed) == len(scopes) - len(subscopes):
                    collapsed.append(scope)
                    scopes = collapsed

        if len(scopes) == len(ALL_SCOPES):
            scopes = ['']
        elif len(scopes) == len(ALL_SCOPES) - 1:
            # This usually makes the generated code shorter because non-Windows
            # scopes will be collapsed into one.
            scopes = ['!' + (set(ALL_SCOPES) - set(scopes)).pop()]

        for scope in scopes:
            used_values.setdefault(scope, set()).add(value)

    @staticmethod
    def _add_value_set_for_scope(used_values, values, scope=''):
        """ Add a set of values to the set of used values for a scope. """

        used_values.setdefault(scope, set()).update(values)

    def _get_py_module_metadata(self, name):
        """ Get the meta-data for a Python module. """

        return get_python_metadata(self._project.python_target_version).get(name)

    def _get_pyqt_module_metadata(self, module_name):
        """ Get the meta-data for a PyQt module. """

        if self._project.application_is_pyqt5:
            metadata = pyqt5_metadata
        else:
            metadata = pyqt4_metadata

        return metadata[module_name]

    def _get_all_pyqt_modules(self):
        """ Return the list of all PyQt modules including dependencies. """

        all_modules = []

        for module_name in self._project.pyqt_modules:
            self._get_pyqt_module_dependencies(module_name, all_modules)

            if module_name not in all_modules:
                all_modules.append(module_name)

        return all_modules

    def _get_pyqt_module_dependencies(self, module_name, all_modules):
        """ Update a list of dependencies for a PyQt module. """

        for dep in self._get_pyqt_module_metadata(module_name).deps:
            if dep not in all_modules:
                all_modules.append(dep)

            # Handle sub-dependencies.
            self._get_pyqt_module_dependencies(dep, all_modules)

    def _write_package(self, resource_contents, resources_dir, resource, package, src_dir, job_writer):
        """ Write the contents of a single package and return the list of files
        written relative to the resources directory.
        """

        if resource == '':
            dst_dir = resources_dir
            dir_stack = []
        else:
            dst_dir = resources_dir + '/' + resource
            dir_stack = [resource]

        self._write_package_contents(package.contents, dst_dir, src_dir,
                dir_stack, job_writer, resource_contents)

    def _write_package_contents(self, contents, dst_dir, src_dir, dir_stack, job_writer, resource_contents):
        """ Write the contents of a single package directory. """

        self._create_directory(dst_dir)

        for content in contents:
            if not content.included:
                continue

            if isinstance(content, QrcDirectory):
                dir_stack.append(content.name)

                self._write_package_contents(content.contents,
                        dst_dir + '/' + content.name,
                        src_dir + '/' + content.name, dir_stack, job_writer,
                        resource_contents)

                dir_stack.pop()
            else:
                freeze_file = True
                src_file = content.name
                src_path = src_dir + '/' + src_file

                if src_file.endswith('.py'):
                    dst_file = src_file[:-3] + '.pyo'
                elif src_file.endswith('.pyw'):
                    dst_file = src_file[:-4] + '.pyo'
                else:
                    # Just copy the file.
                    dst_file = src_file
                    freeze_file = False

                dst_path = dst_dir + '/' + dst_file

                file_path = list(dir_stack)
                file_path.append(dst_file)
                file_path = '/'.join(file_path)

                if freeze_file:
                    self._freeze(job_writer, dst_path, src_path,
                            file_path[:-1])
                else:
                    src_path = QDir.toNativeSeparators(src_path)
                    dst_path = QDir.toNativeSeparators(dst_path)

                    try:
                        shutil.copyfile(src_path, dst_path)
                    except FileNotFoundError:
                        raise UserException(
                                "{0} does not seem to exist".format(src_path))

                resource_contents.append(file_path)

    def _write_main(self, build_dir, inittab):
        """ Create the application specific pyqtdeploy_main.cpp file. """

        project = self._project

        f = self._create_file(build_dir + '/pyqtdeploy_main.cpp')

        f.write('''#include <Python.h>
#include <QtGlobal>

''')

        if len(inittab) > 0:
            c_inittab = 'extension_modules'

            f.write('#if PY_MAJOR_VERSION >= 3\n')
            self._write_inittab(f, inittab, c_inittab, py3=True)
            f.write('#else\n')
            self._write_inittab(f, inittab, c_inittab, py3=False)
            f.write('#endif\n\n')
        else:
            c_inittab = 'NULL'

        sys_path = project.sys_path

        if sys_path != '':
            f.write('static const char *path_dirs[] = {\n')

            for dir_name in shlex.split(sys_path):
                f.write('    "{0}",\n'.format(dir_name.replace('"','\\"')))

            f.write('''    NULL
};

''')

        if project.application_script != '':
            main_module = '__main__'
            entry_point = 'NULL'
        else:
            main_module, entry_point = project.application_entry_point.split(
                    ':')
            entry_point = '"' + entry_point + '"'

        path_dirs = 'path_dirs' if sys_path != '' else 'NULL'

        f.write('''
#if defined(Q_OS_WIN) && PY_MAJOR_VERSION >= 3
#include <windows.h>

extern int pyqtdeploy_start(int argc, wchar_t **w_argv,
        struct _inittab *extension_modules, const char *main_module,
        const char *entry_point, const char **path_dirs);

int main(int argc, char **)
{
    LPWSTR *w_argv = CommandLineToArgvW(GetCommandLineW(), &argc);

    return pyqtdeploy_start(argc, w_argv, %s, "%s", %s, %s);
}
#else
extern int pyqtdeploy_start(int argc, char **argv,
        struct _inittab *extension_modules, const char *main_module,
        const char *entry_point, const char **path_dirs);

int main(int argc, char **argv)
{
    return pyqtdeploy_start(argc, argv, %s, "%s", %s, %s);
}
#endif
''' % (c_inittab, main_module, entry_point, path_dirs,
       c_inittab, main_module, entry_point, path_dirs))

        f.close()

    @classmethod
    def _write_inittab(cls, f, inittab, c_inittab, py3):
        """ Write the Python version specific extension module inittab. """

        if py3:
            init_type = 'PyObject *'
            init_prefix = 'PyInit_'
        else:
            init_type = 'void '
            init_prefix = 'init'

        for scope, names in inittab.items():
            if scope != '':
                cls._write_scope_guard(f, scope)

            for name in names:
                base_name = name.split('.')[-1]

                f.write('extern "C" %s%s%s(void);\n' % (init_type, init_prefix,
                        base_name))

            if scope != '':
                f.write('#endif\n')

        f.write('''
static struct _inittab %s[] = {
''' % c_inittab)

        for scope, names in inittab.items():
            if scope != '':
                cls._write_scope_guard(f, scope)

            for name in names:
                base_name = name.split('.')[-1]

                f.write('    {"%s", %s%s},\n' % (name, init_prefix, base_name))

            if scope != '':
                f.write('#endif\n')

        f.write('''    {NULL, NULL}
};
''')

    # The map of scopes to pre-processor symbols.
    _guards = {
        'android':  'Q_OS_ANDROID',
        'linux-*':  'Q_OS_LINUX',
        'macx':     'Q_OS_MAC',
        'win32':    'Q_OS_WIN',
    }

    @classmethod
    def _write_scope_guard(cls, f, scope):
        """ Write the C pre-processor guard for a scope. """

        if scope[0] == '!':
            inv = '!'
            scope = scope[1:]
        else:
            inv = ''

        f.write('#if {0}defined({1})\n'.format(inv, cls._guards[scope]))

    @staticmethod
    def _freeze(job_writer, out_file, in_file, name, as_c=False):
        """ Freeze a Python source file to a C header file or a data file. """

        out_file = QDir.toNativeSeparators(out_file)
        in_file = QDir.toNativeSeparators(in_file)

        if as_c:
            conversion = 'C'
        else:
            name = ':/' + name
            conversion = 'data'

        job_writer.writerow([out_file, in_file, name, conversion])

    def _run_freeze(self, freeze, interpreter, job_filename, opt):
        """ Run the accumlated freeze jobs. """

        # On Windows the interpreter name is simply 'python'.  So in order to
        # make the .pdy file more portable we strip any trailing version
        # number.
        if sys.platform == 'win32':
            for i in range(len(interpreter) - 1, -1, -1):
                if interpreter[i] not in '.0123456789':
                    interpreter = interpreter[:i + 1]
                    break

        argv = [QDir.toNativeSeparators(interpreter)]

        if opt == 2:
            argv.append('-OO')
        elif opt == 1:
            argv.append('-O')

        argv.append(freeze)
        argv.append(job_filename)

        self.run(argv, "Unable to freeze files")

    def run(self, argv, error_message, in_build_dir=False):
        """ Execute a command and capture the output. """

        if in_build_dir:
            project = self._project

            saved_cwd = os.getcwd()
            build_dir = project.path_from_user(project.build_dir)
            build_dir = QDir.toNativeSeparators(build_dir)
            os.chdir(build_dir)
            self._message_handler.verbose_message(
                    "{0} is now the current directory".format(build_dir))
        else:
            saved_cwd = None

        self._message_handler.verbose_message(
                "Running '{0}'".format(' '.join(argv)))

        QCoreApplication.processEvents()

        process = QProcess()

        process.readyReadStandardOutput.connect(
                lambda: self._message_handler.progress_message(
                        QTextCodec.codecForLocale().toUnicode(
                                process.readAllStandardOutput()).strip()))

        stderr_output = QByteArray()
        process.readyReadStandardError.connect(
                lambda: stderr_output.append(process.readAllStandardError()))

        process.start(argv[0], argv[1:])
        finished = process.waitForFinished()

        if saved_cwd is not None:
            os.chdir(saved_cwd)
            self._message_handler.verbose_message(
                    "{0} is now the current directory".format(saved_cwd))

        if not finished:
            raise UserException(error_message, process.errorString())

        if process.exitStatus() != QProcess.NormalExit or process.exitCode() != 0:
            raise UserException(error_message,
                    QTextCodec.codecForLocale().toUnicode(stderr_output).strip())

    @staticmethod
    def _get_lib_file_name(file_name):
        """ Get name of a file in the 'lib' sub-directory. """

        return get_embedded_dir(__file__, 'lib').absoluteFilePath(file_name)

    @classmethod
    def _copy_lib_file(cls, file_name, dir_name, dst_file_name=None):
        """ Copy a library file to a directory and return the full pathname of
        the copy.
        """

        # Note that we use the Qt file operations to support the possibility
        # that pyqtdeploy itself has been deployed as a single executable.

        if dst_file_name is None:
            dst_file_name = file_name
            s_file_name = cls._get_lib_file_name(file_name)
        else:
            s_file_name = file_name

        d_file_name = dir_name + '/' +  dst_file_name

        # Make sure the destination doesn't exist.
        QFile.remove(d_file_name)

        if not QFile.copy(s_file_name, d_file_name):
            raise UserException("Unable to copy file {0}".format(file_name))

        # The file will be read-only if it was embedded.
        QFile.setPermissions(d_file_name,
                QFileDevice.ReadOwner|QFileDevice.WriteOwner)

        return d_file_name

    @staticmethod
    def _create_file(file_name):
        """ Create a text file in the build directory. """

        return create_file(QDir.toNativeSeparators(file_name))

    def _create_directory(self, dir_name):
        """ Create a directory which may already exist. """

        dir_name = QDir.toNativeSeparators(dir_name)

        self._message_handler.verbose_message(
                "Creating directory {0}".format(dir_name))

        try:
            os.makedirs(dir_name, exist_ok=True)
        except Exception as e:
            raise UserException(
                    "Unable to create the '{0}' directory".format(dir_name),
                    str(e))
