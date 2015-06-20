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
import os
from dreamtools.core.challenge import Challenge


class D8C2(Challenge):
    """A class dedicated to D8C2 challenge

    ::

        from dreamtools import D8C2
        s = D8C2()
        filename = s.download_template() 
        s.score(filename) 

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D8C2, self).__init__('D8C2')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self.sub_challenges = ['sc1', 'sc2']

    def score(self, filename, sub_challenge_name):
        """Scoring functions for the 2 sub challenges"""
        if sub_challenge_name == 'sc1':
            df = self.score_sc1(filename)
            return df
        elif sub_challenge_name == 'sc2':
            df = self.score_sc1(filename)
            return df
        else:
            ValueError("Invalid sub challenge. Use one of %s" % self.sub_challenges)
        
    def score_sc1(self, filename):
        """See :class:`~dreamtools.dream8.D8C2.sc1.D8C2_sc1` class for details"""
        from dreamtools.dream8.D8C2.sc1 import D8C2_sc1
        s = D8C2_sc1(filename)
        df = s.run()
        return df

    def score_sc2(self, filename):
        """See :class:`~dreamtools.dream8.D8C2.sc1.D8C2_sc2` class for details"""
        from dreamtools.dream8.D8C2.sc2 import D8C2_sc2
        s = D8C2_sc2(filename)
        df = s.run()
        return df

    def download_template(self, sub_challenge):
        """Download template 

        :param sub_challenge: sc1 or sc2 string
        """
        if sub_challenge == 'sc1':
            filename = os.sep.join([self._path2data, 'data', 'test_sc1.csv'])
            return filename
        elif sub_challenge == 'sc2':
            filename = os.sep.join([self._path2data, 'data', 'test_sc2.csv'])
            return filename
        else:
            ValueError("Invalid sub challenge. Use one of %s" % self.sub_challenges)








