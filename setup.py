#!/usr/bin/env python3
"""
Setup script for NEFI2

Usage:
    python3.4 setup.py install

"""
import os
import subprocess as sb
from distutils.core import setup
# To use a consistent encoding
import codecs
from os import path
from setuptools.command.install import install
from setuptools import find_packages

HERE = path.abspath(path.dirname(__file__))


class post_install(install):
    def run(self):
        """Run default install with pos-install script"""
        install.run(self)
        script_path = os.path.join(os.getcwd(), 'post_install.sh')
        sb.call([script_path])


# Get the long description from the README file
with open(path.join(HERE, 'README.md')) as f:
    long_description = f.read()

setup(
    name='NEFI2',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='2.0.0',

    description='NEFI2 -- graph extractor from images',
    long_description=long_description,

    # The project's main homepage.
    url='http://nefi.mpi-inf.mpg.de/index.html',

    # Author details
    author=[
            'Andreas Firczynski',
            'Dennis Gross',
            'Martino Bruni',
            'Pavel Shkadzko',
            'Philipp Reichert',
            'Sebastian Schattner'
        ],

    author_email=[
                  's9anfirc@stud.uni-saarland.de',
                  's9dsgros@stud.uni-saarland.de',
                  's8mobrun@stud.uni-saarland.de',
                  'p.shkadzko@gmail.com',
                  'prei@me.com',
                  's9sescat@stud.uni-saarland.de'
                ],

    # Choose your license
    license='BSD',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        # Development Status :: 3 - Alpha
        # Development Status :: 4 - Beta
        # Development Status :: 5 - Production/Stable
        # Development Status :: 6 - Mature
        'Development Status :: 3 - Alpha',
        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Visualization',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: BSD License',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.4 :: Only'
    ],

    keywords='graph extraction',
    packages=['nefi2'],

    #packages=find_packages(exclude=["doc", "unittests", "tests"]),

    install_requires=['numpy>=1.9.1',
                      'networkx>=1.9.1',
                      'sip>=4.17',
                      'demjson>=2.2.4',
                      'QDarkStyle>=2.1'],

    #scripts=['nefi2/nefi2'],

    cmdclass={'install': post_install},

    package_data={
        'nefi2': ['data/default_pipelines/*.json'],
    }
)
