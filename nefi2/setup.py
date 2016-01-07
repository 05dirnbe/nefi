#!/usr/bin/env python3
"""
Setup script for NEFI2

Usage:
    python setup.py install
    
"""
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    windows=['nefi2.py'],
    console = ['nefi2.py'],
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
            'Dennis Groß',
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

    # What does your project relate to?
    keywords='graph extraction',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'unittests']),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['thinning>=1.2.3', 'numpy>=1.9.1', 'networkx>=1.9.1'],

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    #package_data={
    #    'example_images': [''],
    #},
)
