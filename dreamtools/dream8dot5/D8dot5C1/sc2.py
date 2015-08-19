# -*- python -*-
#
#  This file is part of DreamTools software
#
#  Copyright (c) 2014-2015 - Sage Bionetworks
#
#  File author(s): Abhishek Pratap <apratap@sagebase.org>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  website: http://github.org/dreamtools
#
##############################################################################
from dreamtools.core.challenge import Challenge
import os


class D8dot5C1_sc1(Challenge, RTools):
    """Scoring class for D8dot5C1 sub challenge 1

    ::

        from dreamtools impoty D8dot5C1
        s = D8dot5C1_sc1(filename)
        s.run()
        s.df

    """

    def __init__(self, filename, verboseR=True):
        Challenge.__init__(self, challenge_name='D8dot5C1')
        self.filename = filename
        self._path2data = os.path.split(os.path.abspath(__file__))[0]

    def run(self):
        """Compute the score and populates :attr:`df` attribute with results

        """

        return self.df

