#!/usr/bin/env python3
"""
Setup script for NEFI2

Usage:
    python3.4 setup.py install

"""
import os
import subprocess as sb
from setuptools import setup, find_packages
from setuptools.command.install import install


HERE = os.path.abspath(os.path.dirname(__file__))


class DepsInstall(install):
    """Install dependencies"""
    def run(self):
        install.run(self)
        script_path = os.path.join(os.getcwd(), 'deps_install.sh')
        sb.call([script_path])


# Get the long description from the README file
with open(os.path.join(HERE, 'README.md')) as f:
    LONG = f.read()

setup(
    name='NEFI2',
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='2.0.0',
    description='NEFI2 -- graph extractor from images',
    long_description=LONG,
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
        # Development Status :: 4 - Beta
        # Development Status :: 5 - Production/Stable
        # Development Status :: 6 - Mature
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Visualization',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3 :: Only'
    ],

    keywords='graph extraction',

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'nefi2 = nefi2.main:gui_mode',
        ],
    },

    install_requires=['numpy>=1.10.4',
                      'networkx>=1.11',
                      'demjson>=2.2.4',
                      'QDarkStyle>=2.1'],

    #cmdclass={'install': DepsInstall},

    #package_data={
    #    '.': ['data/default_pipelines/*.json',
    #              'icons/*.png',
    #              'icons/*.ico'],
    #}
)
