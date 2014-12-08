# -*- python -*-
#
#  This file is part of dreamtools software
#
#  Copyright (c) 2011-2014 - EBI-EMBL
#
#  File author(s): Thomas Cokelaer <cokelaer@ebi.ac.uk>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  website: http://github.com/dreamtools
#
##############################################################################
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

include_dirs = []
ext_modules = [Extension("cython_scoring", ["cython_scoring.pyx"], include_dirs)
              ]

setup(
  name = 'optimisation cython',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)


