# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from Cython.Build import cythonize


_MAJOR               = 0
_MINOR               = 11
_MICRO               = 0
version              = '%d.%d.%d' % (_MAJOR, _MINOR, _MICRO)
release              = '%d.%d' % (_MAJOR, _MINOR)



metainfo = {
    'authors': {
        'Cokelaer':('Thomas Cokelaer','cokelaer@gmail.com'),
        'Eduati': ('Federica Eduati', 'eduati@ebi.ac.uk')
        },
    'version': version,
    'license' : 'BSD',
    'download_url' : ['http://pypi.python.org/pypi/dreamtools'],
    'url' : ['https://github.com/dreamtools/dreamtools'],
    'description':'Scoring functions for the dream / sage challenges' ,
    'platforms' : ['Linux', 'Unix', 'MacOsX', 'Windows'],
    'keywords' : ['DREAM challenges', 'DREAM', 'System Biology', 
        'Leaderboard', 'ROC', 'scoring', 'synapse','statistics' ],
    'bugtrack_url': 'https://github.com/dreamtools/issues',
    'classifiers' : [
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Topic :: Scientific/Engineering :: Mathematics',
          'Topic :: Scientific/Engineering :: Physics']
    }


with open('README.rst') as f:
    readme = f.read()


setup(
    name             = 'dreamtools',
    version          = version,
    maintainer       = metainfo['authors']['Cokelaer'][0],
    maintainer_email = metainfo['authors']['Cokelaer'][1],
    author           = metainfo['authors']['Cokelaer'][0],
    author_email     = metainfo['authors']['Cokelaer'][1],
    long_description = readme,
    keywords         = metainfo['keywords'],
    description = metainfo['description'],
    license          = metainfo['license'],
    platforms        = metainfo['platforms'],
    url              = metainfo['url'],
    download_url     = metainfo['download_url'],
    classifiers      = metainfo['classifiers'],

    zip_safe=False,
    packages = find_packages(),
    # package installation

    include_package_data = True,
    # (you can provide an exclusion dictionary named exclude_package_data to 
    # remove parasites). alternatively to global inclusion, list the file 
    # to include
    package_data = {
        '' : ['*.pl', '*.txt', '*xls', '*.pyx', '*.so', '*.zip', '*.csv', 
            '*.ini', '*.R', 'README.rst'],
        },

    install_requires = ['cython', 'numpy', 'matplotlib', 'pandas', 'appdirs',
        'easydev>=0.8.7', 'fitter', 'synapseclient', 'tabulate', 'scipy',
        'xlrd'],

    ext_modules = cythonize(["dreamtools/dream8/D8C1/*.pyx"]),

    entry_points = {
        'console_scripts': [
            'dreamtools=dreamtools.core.scoring:scoring',
            'dreamtools-scoring=dreamtools.core.scoring:scoring',
            'dreamtools-layout=dreamtools.core.layout:layout',
        ]
    },
)

#using cythonize command gets the compiled cython code into the .egg
#post_process()
