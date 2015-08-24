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
        """.. rubric:: constructor"""
        super(D8C2, self).__init__('D8C2')
        self.sub_challenges = ['sc1', 'sc2']

    def score(self, filename, subname):
        """Scoring functions for the 2 sub challenges"""
        if subname == 'sc1':
            df = self.score_sc1(filename)
            return df
        elif subname == 'sc2':
            df = self.score_sc2(filename)
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
            filename = self.getpath_data('test_sc1.csv')
            return filename
        elif sub_challenge == 'sc2':
            filename = self.getpath_data('test_sc2.csv')
            return filename
        else:
            ValueError("Invalid sub challenge. Use one of %s" % self.sub_challenges)

    def download_goldstandard(self, subname):
        raise NotImplementedError






