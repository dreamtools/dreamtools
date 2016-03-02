# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


try:
    from Cython.Build import cythonize
except ImportError:
    print("-----------------------------------------------------------")
    print("DREAMTools installation:: **cython** package not found")
    print("-----------------------------------------------------------")
    print("You can try to install it using **pip** as follows::")
    print("")
    print("    pip install cython")
    print("")
    exit()

# On travis, Cython compilation hangs forever.
# We will skip the D8C1 tests where cython is required.
# On travis, we create a variable called  __TRAVIS_DREAMTOOLS
#if os.environ.get('__TRAVIS_DREAMTOOLS'):
#    ext_modules = []
#else:
ext_modules = cythonize(["dreamtools/dream8/D8C1/*.pyx"])

#ext_modules = []


_MAJOR               = 1
_MINOR               = 2
_MICRO               = 6
version              = '%d.%d.%d' % (_MAJOR, _MINOR, _MICRO)
release              = '%d.%d' % (_MAJOR, _MINOR)



metainfo = {
    'authors': {
        'Cokelaer':('Thomas Cokelaer','cokelaer@gmail.com'),
        },
    'version': version,
    'license' : 'BSD',
    'download_url' : ['http://pypi.python.org/pypi/dreamtools'],
    'url' : ['https://github.com/dreamtools/dreamtools'],
    'description':'Scoring functions for the DREAM / SAGE challenges' ,
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

packages = find_packages()
# exclude test (somehow prevent conda recipes to work properly since test is
# considered as an independent package)
packages = [this for this in packages if this.startswith('test') is False]


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
    packages = packages,
    # package installation

    include_package_data = True,
    # (you can provide an exclusion dictionary named exclude_package_data to 
    # remove parasites). alternatively to global inclusion, list the file 
    # to include
    package_data = {
        '' : ['*.pl', '*.txt', '*xls', '*.pyx', '*.so', '*.zip', '*.csv', 
            '*.ini', '*.R', 'README.rst'],
        },

    install_requires = ['cython', 'numpy', 'matplotlib', 'pandas', 
        'easydev>=0.9.11', 'fitter', 'synapseclient>=1.5', 'tabulate', 'scipy',
        'biokit','xlrd', 'numexpr', 'scikit-learn'],

    ext_modules = ext_modules,

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
