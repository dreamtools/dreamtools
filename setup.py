# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from Cython.Build import cythonize


_MAJOR               = 0
_MINOR               = 1
_MICRO               = 0
version              = '%d.%d.%d' % (_MAJOR, _MINOR, _MICRO)
release              = '%d.%d' % (_MAJOR, _MINOR)


## compile cython code
def post_process():
    cwd = os.getcwd()
    os.chdir('dreamtools/dream8/D8C1')
    os.system('python setup.py build_ext --inplace')
    os.chdir(cwd)


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
    'keywords' : ['scoring', 'dream', 'roc', 'leaderboard'],
    'classifiers' : [
          'Development Status :: 1 - Planning',
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
    # (you can provide an exclusion dictionary named exclude_package_data to remove parasites).
    # alternatively to global inclusion, list the file to include
    package_data = {'' : ['*.txt', '*.so', '*.zip', '*.csv', '*.ini', '*.R'],},


    # distutils in rtools.package
    #install_requires = [ 'pandas', 'bioservices', 'colormap>=0.9.3'],
    install_requires = ['numpy', 'matplotlib', 'pandas', 'appdirs',
        'easydev>=0.8.3', 'fitter',
        'synapseclient', 'tabulate', 'cython'],

    ext_modules = cythonize("dreamtools/dream8/D8C1/*.pyx"),


    entry_points = {
        'console_scripts': [
            'dreamtools-scoring=dreamtools.core.scoring:scoring',
        ]
    },
)

#using cythonize command gets the compiled cython code into the .egg
#post_process()
