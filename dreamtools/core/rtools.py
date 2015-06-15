# -*- python -*-
#
#  This file is part of DreamTools software
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
"""Simple class to handld R packages

"""
from biokit.rtools import RSession


__all__ = ['RTools']


class RTools(object):
    """A base class to handle the R session and its verbosity"""
    def __init__(self, verboseR):
        assert verboseR in [True, False]
        self._verboseR = verboseR
        self.session = RSession(verbose=self.verboseR)
       
    def _get_verboseR(self):
        return self._verboseR
    def _set_verboseR(self, value):
        assert value in [True, False]
        self._verboseR = value
        self.session.dump_stdout = value
    verboseR = property(_get_verboseR, _set_verboseR)

