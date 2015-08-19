#!/usr/bin/env python

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






import os
import sys
import warnings
import pandas
#also turning off the warning
#./eval_submissions_ra_challenge.py:295: SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame.
#Try using .loc[row_index,col_indexer] = value instead
#leaderboard_df_selectedCol['submissionTeamName'] = leaderboard_df_selectedCol.submissionTeamName.apply(lambda x: "```%s```" % x)
#ref this link : https://stackoverflow.com/questions/20625582/how-to-deal-with-this-pandas-warning 
pandas.options.mode.chained_assignment = None
import synapseclient
import argparse
import numpy as np
import collections
import shutil
from scipy.stats.stats import pearsonr
import tempfile
from sklearn.utils import shuffle
from sklearn.metrics import roc_curve, auc, precision_recall_curve

#RA challenge specific code
import synLeaderboard
import metrics
import dreamchallenge
import ra_challenge
import ra_message_templates

