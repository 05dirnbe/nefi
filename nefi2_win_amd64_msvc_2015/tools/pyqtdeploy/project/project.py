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
from xml.etree.ElementTree import Element, ElementTree, SubElement

from PyQt5.QtCore import QDir, QFileInfo, QObject, pyqtSignal

from ..metadata import get_latest_supported_python_version, get_python_metadata
from ..user_exception import UserException


class Project(QObject):
    """ The encapsulation of a project. """

    # The minimum supported project version.  At the moment a project will be
    # automatically updated to the current version when saved.
    min_version = 4

    # The current project version.
    version = 6

    # Emitted when the modification state of the project changes.
    modified_changed = pyqtSignal(bool)

    @property
    def modified(self):
        """ The modified property getter. """

        return self._modified

    @modified.setter
    def modified(self, value):
        """ The modified property setter. """

        if self._modified != value:
            self._modified = value
            self.modified_changed.emit(value)

    # Emitted when the name of the project changes.
    name_changed = pyqtSignal(str)

    @property
    def name(self):
        """ The name property getter. """

        # Use absoluteFilePath() because the file might not exist.
        return self._name.absoluteFilePath() if self._name is not None else ''

    @name.setter
    def name(self, value):
        """ The name property setter. """

        if self._name is None or self._name.absoluteFilePath() != value:
            self._name = QFileInfo(value)
            self.name_changed.emit(value)

    def __init__(self, name=''):
        """ Initialise the project. """

        super().__init__()

        # Initialise the project meta-data.
        self._modified = False
        self._name = QFileInfo(name) if name != '' else None

        # Initialise the project data.
        self.application_name = ''
        self.application_is_pyqt5 = True
        self.application_is_console = False
        self.application_use_py_dll = False
        self.application_is_bundle = True
        self.application_package = QrcPackage()
        self.application_script = ''
        self.application_entry_point = ''
        self.build_dir = 'build'
        self.external_libraries = []
        self.other_extension_modules = []
        self.other_packages = []
        self.pyqt_modules = []
        self.python_host_interpreter = ''
        self.python_use_platform = ['win32']
        self.python_source_dir = '$SYSROOT/src/Python-$PDY_PY_MAJOR.$PDY_PY_MINOR.$PDY_PY_MICRO'
        self.python_ssl = False
        self.python_target_include_dir = '$SYSROOT/include/python$PDY_PY_MAJOR.$PDY_PY_MINOR'
        self.python_target_library = '$SYSROOT/lib/libpython$PDY_PY_MAJOR.$PDY_PY_MINOR.a'
        self.python_target_stdlib_dir = '$SYSROOT/lib/python$PDY_PY_MAJOR.$PDY_PY_MINOR'
        self.python_target_version = get_latest_supported_python_version()
        self.qmake = ''
        self.qmake_configuration = ''
        self.standard_library = []
        self.sys_path = ''

    def path_to_user(self, path):
        """ Convert a file name to one that is relative to the project name if
        possible and uses native separators.
        """

        if self._name is not None:
            rel = self._name.dir().relativeFilePath(path)
            if not rel.startswith('..'):
                path = rel

        return QDir.toNativeSeparators(path)

    def path_from_user(self, user_path):
        """ Convert the name of a file or directory specified by the user to
        the standard Qt format (ie. an absolute path using UNIX separators).  A
        user path may be relative to the name of the project and may contain
        environment variables.
        """

        fi = self._fileinfo_from_user(user_path)

        # Use the canonical name if possible (ie. when the file exists) and
        # fall back to the absolute name.
        path = fi.canonicalFilePath()
        if path == '':
            path = fi.absoluteFilePath()

        return path

    def get_executable_basename(self):
        """ Return the basename of the application executable (i.e. with no
        path or extension.
        """

        if self.application_name != '':
            return self.application_name

        name = self.application_script
        if name == '':
            name = self.application_package.name
            if name == '':
                return ''

        return self._fileinfo_from_user(name).completeBaseName()

    def expandvars(self, path):
        """ Call os.path.expandvars() after expanding some internal values. """

        major, minor, micro = self.python_target_version
        major = str(major)
        minor = str(minor)
        micro = str(micro)

        path = path.replace('$PDY_PY_MAJOR', major)
        path = path.replace('${PDY_PY_MAJOR}', major)

        path = path.replace('$PDY_PY_MINOR', minor)
        path = path.replace('${PDY_PY_MINOR}', minor)

        path = path.replace('$PDY_PY_MICRO', micro)
        path = path.replace('${PDY_PY_MICRO}', micro)

        return os.path.expandvars(path)

    def _fileinfo_from_user(self, user_path):
        """ Convert the name of a file or directory specified by the user to a
        QFileInfo instance.  A user path may be relative to the name of the
        project and may contain environment variables.
        """

        fi = QFileInfo(self.expandvars(user_path.strip()))

        if fi.isRelative():
            fi = QFileInfo(self._name.canonicalPath() + '/' + fi.filePath())

        return fi

    def get_stdlib_requirements(self, include_hidden=False):
        """ Return a 2-tuple of the required Python standard library modules
        and the required external libraries.  The modules are a dict with the
        module name as the key and a bool as the value.  The bool is True if
        the module is explicitly required and False if it is implicitly
        required.  The libraries are a set of well known library names.
        """

        # Work out the dependencies.
        metadata = get_python_metadata(self.python_target_version)
        all_modules = {name: _DepState(module)
                for name, module in metadata.items()}

        visit = 0
        for name in all_modules.keys():
            self._set_dependency_state(all_modules, name, visit)
            visit += 1

        # Extract the required modules and libraries.
        required_modules = {}
        required_libraries = set()

        for name, dep_state in all_modules.items():
            if dep_state.explicit:
                explicit = True
            elif dep_state.implicit:
                explicit = False
            else:
                continue

            # Handle any hidden dependencies if required.
            if include_hidden:
                for hidden_dep in dep_state.module.hidden_deps:
                    if hidden_dep not in required_modules:
                        required_modules[hidden_dep] = False

            required_modules[name] = explicit

            if dep_state.module.xlib is not None:
                required_libraries.add(dep_state.module.xlib)

        return required_modules, required_libraries

    def _set_dependency_state(self, all_modules, name, visit, is_dep=False):
        """ Set a module's dependency state. """

        dep_state = all_modules[name]

        if dep_state.visit == visit:
            return

        dep_state.visit = visit

        if dep_state.module.builtin:
            # This will mean that the explicit and implicit states will remain
            # None and so the module will be omitted from the list.
            return

        dep_state.explicit = (name in self.standard_library)

        if dep_state.module.core or is_dep:
            dep_state.implicit = True

        for dep in dep_state.module.deps:
            # If the first character of the module is '?' then it should be
            # excluded if SSL support is disabled.  If the first character is
            # '!' then it should be excluded if SSL support is enabled.
            if dep[0] == '?':
                if not self.python_ssl:
                    continue

                dep = dep[1:]
            elif dep[0] == '!':
                if self.python_ssl:
                    continue

                dep = dep[1:]

            self._set_dependency_state(all_modules, dep, visit,
                    (dep_state.explicit or dep_state.implicit))

    @classmethod
    def load(cls, file_name):
        """ Return a new project loaded from the given file.  Raise a
        UserException if there was an error.
        """

        fi = QFileInfo(file_name)

        tree = ElementTree()

        try:
            root = tree.parse(QDir.toNativeSeparators(fi.canonicalFilePath()))
        except Exception as e:
            raise UserException(
                "There was an error reading the project file.", str(e))

        cls._assert(root.tag == 'Project',
                "Unexpected root tag '{0}', 'Project' expected.".format(
                        root.tag))

        # Check the project version number.
        version = root.get('version')
        cls._assert(version is not None, "Missing 'version' attribute.")

        try:
            version = int(version)
        except:
            version = None

        cls._assert(version is not None, "Invalid 'version'.")

        if version < cls.min_version:
            raise UserException("The project's format is no longer supported.")

        if version > cls.version:
            raise UserException(
                    "The project's format is version {0} but only version {1} is supported.".format(version, cls.version))

        # Create the project and populate it.
        project = cls()
        project._name = fi

        # The Python specific configuration.
        python = root.find('Python')
        cls._assert(python is not None, "Missing 'Python' tag.")

        project.python_host_interpreter = python.get('hostinterpreter', '')

        # This was added in version 5.
        project.python_use_platform = python.get('platformpython', '').split()

        project.python_source_dir = python.get('sourcedir', '')
        project.python_ssl = cls._get_bool(python, 'ssl', 'Python')
        project.python_target_include_dir = python.get('targetincludedir', '')
        project.python_target_library = python.get('targetlibrary', '')
        project.python_target_stdlib_dir = python.get('targetstdlibdir', '')

        major = cls._get_int(python, 'major', 'Python')
        minor = cls._get_int(python, 'minor', 'Python')
        patch = cls._get_int(python, 'patch', 'Python', default=0)
        project.python_target_version = (major, minor, patch)

        # The application specific configuration.
        application = root.find('Application')
        cls._assert(application is not None, "Missing 'Application' tag.")

        project.application_entry_point = application.get('entrypoint', '')
        project.application_is_pyqt5 = cls._get_bool(application, 'ispyqt5',
                'Application')
        project.application_is_console = cls._get_bool(application,
                'isconsole', 'Application')

        project.application_is_bundle = cls._get_bool(application, 'isbundle',
                'Application')
        project.application_name = application.get('name', '')
        project.application_script = application.get('script', '')
        project.sys_path = application.get('syspath', '')

        # Any qmake configuration. This was added in version 5.
        qmake_configuration = application.find('QMakeConfiguration')

        if qmake_configuration is not None:
            project.qmake_configuration = qmake_configuration.text

        # Any application package.
        app_package = application.find('Package')

        if app_package is not None:
            project.application_package = cls._load_package(app_package)
        else:
            project.application_package = QrcPackage()

        # Any PyQt modules.
        for pyqt_m in root.iterfind('PyQtModule'):
            name = pyqt_m.get('name', '')
            cls._assert(name != '',
                    "Missing or empty 'PyQtModule.name' attribute.")
            project.pyqt_modules.append(name)

        # Any standard library modules.
        for stdlib_module_element in root.iterfind('StdlibModule'):
            name = stdlib_module_element.get('name')
            cls._assert(name is not None,
                    "Missing 'StdlibModule.name' attribute.")

            project.standard_library.append(name)

        # Any external C libraries.
        for external_lib_element in root.iterfind('ExternalLib'):
            name = external_lib_element.get('name')
            cls._assert(name is not None,
                    "Missing 'ExternalLib.name' attribute.")

            defines = external_lib_element.get('defines', '')
            includepath = external_lib_element.get('includepath', '')
            libs = external_lib_element.get('libs', '')

            project.external_libraries.append(
                    ExternalLibrary(name, defines, includepath, libs))

        # Any other Python packages.
        project.other_packages = [cls._load_package(package)
                for package in root.iterfind('Package')]

        # Any other extension module.
        for extension_module_element in root.iterfind('ExtensionModule'):
            name = extension_module_element.get('name')
            cls._assert(name is not None,
                    "Missing 'ExtensionModule.name' attribute.")

            qt = extension_module_element.get('qt', '')
            config = extension_module_element.get('config', '')
            sources = extension_module_element.get('sources', '')
            defines = extension_module_element.get('defines', '')
            includepath = extension_module_element.get('includepath', '')
            libs = extension_module_element.get('libs', '')

            project.other_extension_modules.append(
                    ExtensionModule(name, qt, config, sources, defines,
                            includepath, libs))

        # The other configuration.
        others = root.find('Others')
        if others is not None:
            project.build_dir = others.get('builddir', '')
            project.qmake = others.get('qmake', '')

        return project

    def save(self):
        """ Save the project.  Raise a UserException if there was an error. """

        self._save_project(self.name)

    def save_as(self, file_name):
        """ Save the project to the given file and make the file the
        destination of subsequent saves.  Raise a UserException if there was an
        error.
        """

        self._save_project(file_name)

        # Only do this after the project has been successfully saved.
        self.name = file_name

    @classmethod
    def _load_package(cls, package_element):
        """ Return a populated QrcPackage instance. """

        package = QrcPackage()

        package.name = package_element.get('name')
        cls._assert(package.name is not None,
                "Missing 'Package.name' attribute.")

        package.contents = cls._load_mfs_contents(package_element)

        package.exclusions = []
        for exclude_element in package_element.iterfind('Exclude'):
            name = exclude_element.get('name', '')
            cls._assert(name != '',
                    "Missing or empty 'Package.Exclude.name' attribute.")
            package.exclusions.append(name)

        return package

    @classmethod
    def _load_mfs_contents(cls, mfs_element):
        """ Return a list of contents for a memory-filesystem container. """

        contents = []

        for content_element in mfs_element.iterfind('PackageContent'):
            isdir = cls._get_bool(content_element, 'isdirectory',
                    'Package.PackageContent')

            name = content_element.get('name', '')
            cls._assert(name != '',
                    "Missing or empty 'Package.PackageContent.name' attribute.")

            included = cls._get_bool(content_element, 'included',
                    'Package.PackageContent')

            content = QrcDirectory(name, included) if isdir else QrcFile(name, included)

            if isdir:
                content.contents = cls._load_mfs_contents(content_element)

            contents.append(content)

        return contents

    @classmethod
    def _get_bool(cls, element, name, context, default=None):
        """ Get a boolean attribute from an element. """

        value = element.get(name)
        try:
            value = int(value)
        except:
            value = default

        cls._assert(value is not None,
                "Missing or invalid boolean value of '{0}.{1}'.".format(
                        context, name))

        return bool(value)

    @classmethod
    def _get_int(cls, element, name, context, default=None):
        """ Get an integer attribute from an element. """

        value = element.get(name)
        try:
            value = int(value)
        except:
            value = default

        cls._assert(value is not None,
                "Missing or invalid integer value of '{0}.{1}'.".format(
                        context, name))

        return value

    def _save_project(self, file_name):
        """ Save the project to the given file.  Raise a UserException if there
        was an error.
        """

        root = Element('Project', attrib={
            'version': str(self.version)})

        SubElement(root, 'Python', attrib={
            'hostinterpreter': self.python_host_interpreter,
            'platformpython': ' '.join(self.python_use_platform),
            'sourcedir': self.python_source_dir,
            'ssl': str(int(self.python_ssl)),
            'targetincludedir': self.python_target_include_dir,
            'targetlibrary': self.python_target_library,
            'targetstdlibdir': self.python_target_stdlib_dir,
            'major': str(self.python_target_version[0]),
            'minor': str(self.python_target_version[1]),
            'patch': str(self.python_target_version[2])})

        application = SubElement(root, 'Application', attrib={
            'entrypoint': self.application_entry_point,
            'ispyqt5': str(int(self.application_is_pyqt5)),
            'isconsole': str(int(self.application_is_console)),
            'isbundle': str(int(self.application_is_bundle)),
            'name': self.application_name,
            'script': self.application_script,
            'syspath': self.sys_path})

        if self.qmake_configuration != '':
            SubElement(application, 'QMakeConfiguration').text = self.qmake_configuration

        if self.application_package.name is not None:
            self._save_package(application, self.application_package)

        for pyqt_module in self.pyqt_modules:
            SubElement(root, 'PyQtModule', attrib={
                'name': pyqt_module})

        for stdlib_module in self.standard_library:
            SubElement(root, 'StdlibModule', attrib={
                'name': stdlib_module})

        for external_lib in self.external_libraries:
            SubElement(root, 'ExternalLib', attrib={
                'name': external_lib.name,
                'defines': external_lib.defines,
                'includepath': external_lib.includepath,
                'libs': external_lib.libs})

        for package in self.other_packages:
            self._save_package(root, package)

        for extension_module in self.other_extension_modules:
            SubElement(root, 'ExtensionModule', attrib={
                'name': extension_module.name,
                'qt': extension_module.qt,
                'config': extension_module.config,
                'sources': extension_module.sources,
                'defines': extension_module.defines,
                'includepath': extension_module.includepath,
                'libs': extension_module.libs})

        SubElement(root, 'Others', attrib={
            'builddir': self.build_dir,
            'qmake': self.qmake})

        tree = ElementTree(root)

        try:
            tree.write(QDir.toNativeSeparators(file_name), encoding='utf-8',
                    xml_declaration=True)
        except Exception as e:
            raise UserException(
                    "There was an error writing the project file.", str(e))

        self.modified = False

    @classmethod
    def _save_package(cls, container, package):
        """ Save a package in a container element. """

        package_element = SubElement(container, 'Package', attrib={
            'name': package.name})

        cls._save_mfs_contents(package_element, package.contents)

        for exclude in package.exclusions:
            SubElement(package_element, 'Exclude', attrib={
                'name': exclude})

    @classmethod
    def _save_mfs_contents(cls, container, contents):
        """ Save the contents of a memory-filesystem container. """

        for content in contents:
            isdir = isinstance(content, QrcDirectory)

            subcontainer = SubElement(container, 'PackageContent', attrib={
                'name': content.name,
                'included': str(int(content.included)),
                'isdirectory': str(int(isdir))})

            if isdir:
                cls._save_mfs_contents(subcontainer, content.contents)

    @staticmethod
    def _assert(ok, detail):
        """ Validate an assertion and raise a UserException if it failed. """

        if not ok:
            raise UserException("The project file is invalid.", detail)


class QrcPackage():
    """ The encapsulation of a memory-filesystem package. """

    def __init__(self):
        """ Initialise the package. """

        self.name = None
        self.contents = []
        self.exclusions = ['*.pyc', '*.pyd', '*.pyo', '*.pyx', '*.pxi',
                '__pycache__', '*-info', 'EGG_INFO', '*.so']

    def copy(self):
        """ Return a copy of the package. """

        copy = type(self)()

        copy.name = self.name
        copy.contents = [content.copy() for content in self.contents]
        copy.exclusions = list(self.exclusions)

        return copy


class QrcFile():
    """ The encapsulation of a memory-filesystem file. """

    def __init__(self, name, included=True):
        """ Initialise the file. """

        self.name = name
        self.included = included

    def copy(self):
        """ Return a copy of the file. """

        return type(self)(self.name, self.included)


class QrcDirectory(QrcFile):
    """ The encapsulation of a memory-filesystem directory. """

    def __init__(self, name, included=True):
        """ Initialise the directory. """

        super().__init__(name, included)

        self.contents = []

    def copy(self):
        """ Return a copy of the directory. """

        copy = super().copy()

        copy.contents = [content.copy() for content in self.contents]

        return copy


class ExternalLibrary():
    """ The encapsulation of an external library. """

    def __init__(self, name, defines, includepath, libs):
        """ Initialise the external library. """

        self.name = name
        self.defines = defines
        self.includepath = includepath
        self.libs = libs


class ExtensionModule():
    """ The encapsulation of an extension module. """

    def __init__(self, name, qt, config, sources, defines, includepath, libs):
        """ Initialise the extension module. """

        self.name = name
        self.qt = qt
        self.config = config
        self.sources = sources
        self.defines = defines
        self.includepath = includepath
        self.libs = libs


class _DepState:
    """ Encapsulate the state information required when working out module
    dependencies.
    """

    def __init__(self, module):
        """ Initialise the object. """

        self.module = module
        self.explicit = False
        self.implicit = False
        self.visit = -1
