# -*- python -*-
#
#  This file is part of DREAMTools software
#
#  Copyright (c) 2014-2015 - EBI-EMBL
#
#  File author(s): Thomas Cokelaer <cokelaer@ebi.ac.uk>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  website: http://github.org/dreamtools
#
##############################################################################
"""Tools to handle a configuration file."""
import os

from easydev import CustomConfig


__all__ = ["DREAMToolsConfig"]


class DREAMToolsConfig(CustomConfig):

    def __init__(self, verbose=False):
        super(DREAMToolsConfig, self).__init__("dreamtools", verbose)
        if self.verbose is True:
            print("Welcome to DREAMTools")
            print("=====================")
            print("\nUsage example:")
            print(" >>> from dreamtools import D2C1")
            print(" >>> c = D2C1()")
            print(" >>> filename = c.download_template()")
            print(" >>> c.score(filename)\n")
            print(" Any issues/suggestions ? Visit http://github.com/dreamtools/\n\n")





