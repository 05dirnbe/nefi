#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import nefi2_prototype.nefi2
import pytest
import sys


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


full_description = read('README.md')


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


setup(
    name = 'nefi2_prototype',
    version = nefi2_prototype.__version__,
    url = 'ssh://git@se.st.cs.uni-saarland.de/towards-nefi-2-0.git',
    license = 'BSD',
    author = '',
    tests_require = ['pytest'],
    install_requires = ['numpy>=1.9.1',
                        'networkx>=1.9.1',
                        'thinning>=1.2.3',
                        'OpenCV>=2.4.10'
                       ],
    cmdclass = {'test': PyTest},
    author_email = '',
    description = 'NEFI is an extensible tool for extracting graphs from \
                   images of networks.',
    long_description = full_description,
    packages = ['nefi2_prototype'],
    include_package_data = True,
    platforms = 'any',
    test_suite = 'tests',
    classifiers = [''],
    extras_require = {
                     'testing': ['pytest'],
                     }
)
