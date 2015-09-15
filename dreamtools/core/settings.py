# -*- python -*-
# -*- coding: utf-8 -*-
#
#  This file is part of DREAMTools software
#
#  Copyright (c) 2015, DREAMTools Development Team
#  All rights reserved
#
#  Distributed under the BSD 3-Clause License.
#  See accompanying file LICENSE distributed with this software
#
#  File author(s): Thomas Cokelaer <cokelaer@ebi.ac.uk>
#
#  website: http://github.com/dreamtools
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
