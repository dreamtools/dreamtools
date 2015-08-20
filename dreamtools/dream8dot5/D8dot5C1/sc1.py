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
#from dreamtools.core.challenge import Challenge
import os
import pandas
import numpy
from scipy.stats.stats import pearsonr


def get_corrn_true_vs_predicted(truth,pred):
    #caculate correlation for the given drug against both 
    # 1.Genetics and  2.Genetics + Clinical user submitted response
    pred_flt = pred[pred.ID.isin(truth.ID)]
    
    #making sure the patients IDs have the same row order on both truth and pred data frames
    #else the correlations will be messed up
    temp_merged_df = pandas.merge(pred_flt, truth, how="inner", left_on="ID", right_on="ID")

    #calculate  correlation for genetics only AND genetics + clinical
    corrn_genetics = pearsonr(temp_merged_df.deltaDAS, temp_merged_df.pred_gen_facs)
    corrn_genetics_N_clinical = pearsonr(temp_merged_df.deltaDAS, temp_merged_df.pred_clin_gen_facs)
    
    #just return correlation and not the p-value which is also reported
    return (round(corrn_genetics[0],5), round(corrn_genetics_N_clinical[0],5))




class D8dot5C1_sc1():
    """Scoring class for D8dot5C1 sub challenge 1

    ::
        from dreamtools impoty D8dot5C1
        s = D8dot5C1_sc1(filename)
        s.run()
        s.df

    """

    def __init__(self, filename, verboseR=True):
        self.filename = filename
        self._path2data = os.path.split(os.path.abspath(__file__))[0]

    def load_gold_standard(self):
        filename = self._path2data + '/goldstandard/dummy_goldStandard.csv'
        df = pandas.read_csv(filename)
        self.goldstandard = df.copy()

    def load_user_prediction(self):
        df = pandas.read_csv(self.filename)
        self.prediction = df.copy()

    def run(self):
        """Compute the score and populates :attr:`df` attribute with results

        """ 
        self.load_user_prediction()
        self.load_gold_standard()
        result = get_corrn_true_vs_predicted(self.goldstandard, self.prediction)
        result = pandas.DataFrame({'cor_gen' : result[0] , 'cor_gen+clin' : result[1]}, index=xrange(1))
        return(result)

