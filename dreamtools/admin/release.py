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
"""

Mechanism to download all required files from Synapse, create a bundle
, post if on github or elsewhere to not rely on synpase connection ?


"""
from dreamtools.admin.download_data import  DREAMToolsBundle


class Release(object):
    """A draft class to handle releases"""
    def __init__(self):
        self.bundle = DREAMToolsBundle()
        self.bundle.create_bundle(output_filename='dreamtools_data.tar.gz')
