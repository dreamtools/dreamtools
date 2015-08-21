#!/usr/bin/env python
# -*- python -*-
#
#  This file is part of DREAMTools software
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
import numpy as np
from sklearn.utils import shuffle
from sklearn.metrics import roc_curve, auc, precision_recall_curve

from dreamtools import Challenge


def __get_blockWise_stats(sub_stats):
    """
    calculate stats for each block of belief scores
    """
    #group to calculate group wise stats for each block
    grouped = sub_stats.groupby(['predict'], sort=False)
    #instantiate a pandas dataframe to store the results for each group (tied values)

    result = pandas.DataFrame.from_dict({'block':xrange(len(grouped)),
                                         'block_numElements'  : np.nan,
                                         'block_truePos_density' : np.nan,
                                         'block_truePos'      : np.nan,
                                         'blockValue'   : np.nan
                                         })

    for block,grp in enumerate(grouped):
        name,grp = grp[0],grp[1]
        truePositive = sum(grp.truth == 1)
        grp_truePositive_density = truePositive / float(len(grp))
        idxs = result.block == block
        result.loc[idxs,'block_truePos_density'] = grp_truePositive_density
        result.loc[idxs,'block_numElements'] = len(grp)
        result.loc[idxs,'block_truePos'] = truePositive
        result.loc[idxs,'blockValue'] = grp.predict.unique()
    result.block = result.block + 1
    result['cum_numElements'] = result.block_numElements.cumsum()
    result['cum_truePos'] = result.block_truePos.cumsum()
    return(result)

def get_precision_recall_fpr(y_predict, y_true):
    
    sub_stats = pandas.DataFrame.from_dict({'predict':y_predict, 'truth':y_true}, dtype='float64')
    sub_stats = sub_stats.sort(['predict'],ascending=False)

    blockWise_stats = __get_blockWise_stats(sub_stats)
    grouped = sub_stats.groupby(['predict'],sort=False)
    sub_stats = grouped.apply(__nonlinear_interpolated_evalStats,blockWise_stats)
    precision, recall,  fpr, threshold = sub_stats.precision, sub_stats.recall, sub_stats.fpr, sub_stats.predict 
    return(precision, recall, fpr, threshold)


def __nonlinear_interpolated_evalStats(block_df, blockWise_stats):
    """
    // given a block* of submitted belief score and blockwise statistics (see:__get_blockWise_stats)
    calculates the Precision, Recall & False Positive Rate
    
    *A block by definition should have the same belief score
   

    """
    blockValue = block_df.predict.unique()
    if len(blockValue) != 1:
        raise Exception("grouping by predict column doesnt yield unique predict vals per group..WIERD")
    blockValue = blockValue[0]
    blockStats = blockWise_stats[blockWise_stats.blockValue == blockValue].squeeze() #squeeze will convert one row df to series
    
    block_precision = []
    block_recall = []
    block_fpr = []
    total_elements = blockWise_stats.cum_numElements.max()
    total_truePos = blockWise_stats.cum_truePos.max()
    total_trueNeg = total_elements - total_truePos
    
    for block_depth,row in enumerate(block_df.iterrows()):
        block_depth += 1  #increase block depth by 1 
        row = row[1]
        #calculate the cumulative true positives seen till the last block from the current active block
        # and the total number of elements(cumulative) seen till the last block
        if blockStats.block == 1: #no previous obviously
            cum_truePos_till_lastBlock = 0
            cum_numElements_till_lastBlock = 0
            cum_trueNeg_till_lastBlock = 0
        elif blockStats.block > 1:
            last_blockStats = blockWise_stats[blockWise_stats.block == (blockStats.block-1)].squeeze()
            cum_truePos_till_lastBlock = last_blockStats['cum_truePos']
            cum_numElements_till_lastBlock = last_blockStats['cum_numElements']
            cum_trueNeg_till_lastBlock = cum_numElements_till_lastBlock - cum_truePos_till_lastBlock
            
        truePos = cum_truePos_till_lastBlock + (blockStats.block_truePos_density*block_depth)
        falsePos = cum_trueNeg_till_lastBlock + ((1 - blockStats.block_truePos_density ) * block_depth)
        
        #precision
        interpolated_precision = truePos /(cum_numElements_till_lastBlock+block_depth)
        block_precision.append(interpolated_precision)
        #recall == true positive rate
        interpolated_recall = truePos /total_truePos
        block_recall.append(interpolated_recall)
        #fpr == false positive rate
        interpolated_fpr = falsePos / total_trueNeg
        block_fpr.append(interpolated_fpr)
    
    block_df['precision'] = block_precision
    block_df['recall'] = block_recall
    block_df['fpr'] = block_fpr
    block_df['block_depth'] = np.arange(1,block_df.shape[0]+1)
    block_df['block'] = blockStats.block
    
    return(block_df)



def get_AUC_PR_N_ROC_curve(truth, pred):
    
    #only use the cases present in the truth dataset
    pred_flt = pred[pred.ID.isin(truth.ID)]
    
    #making sure the patients IDs have the same row order on both truth and pred data frames
    #else the computations will be messed up
    #Also imp to order the final dataframe by the same order as participants entered
    #so keep pred_flt first in the data frame merge
    temp_merged_df = pandas.merge(pred_flt, truth, how="outer", left_on="ID", right_on="ID")
    
    true_y_response = temp_merged_df.binary_class
    predicted_belief_gen = temp_merged_df.belief_gen
    predicted_belief_gen_N_clin = temp_merged_df.belief_clin_gen
    
    #1. For genetics
    #ROC curve AUC
    precision_gen, recall_gen, fpr_gen, threshold_gen = get_precision_recall_fpr(predicted_belief_gen,true_y_response)
    tpr_gen = recall_gen #(Recall and True positive rates are same)
    roc_auc_gen = auc(fpr_gen, tpr_gen,reorder=True)
    #PR curve AUC
    PR_curve_auc_gen = auc(recall_gen, precision_gen,reorder=True)
    
    #2. For genetics + clinical
    #ROC curve AUC
    precision_gen_N_clin, recall_gen_N_clin, fpr_gen_N_clin, thresholds_gen_N_clin = get_precision_recall_fpr(predicted_belief_gen_N_clin,
                                                                                                                      true_y_response)
    tpr_gen_N_clin = recall_gen_N_clin #(Recall and True positive rates are same)
    roc_auc_gen_N_clin = auc(fpr_gen_N_clin, tpr_gen_N_clin,reorder=True)
    #PR curve AUC
    PR_curve_auc_gen_N_clin = auc(recall_gen_N_clin, precision_gen_N_clin,reorder=True)
    
    results = (roc_auc_gen, PR_curve_auc_gen, roc_auc_gen_N_clin, PR_curve_auc_gen_N_clin)
    results = [ round(x,4) for x in results ]
    return(results)



class D8dot5C1_sc2(Challenge):
    """Scoring class for D8dot5C1 sub challenge 2

    ::
        from dreamtools impoty D8dot5C2
        s = D8dot5C1_sc2(filename)
        s.run()
        s.df

    """

    def __init__(self, filename):
        super(D8dot5C1_sc2, self).__init__('D8dot5C1')
        self.filename = filename

    def load_gold_standard(self):
        filename = self.getpath_gs('dummy_goldStandard.csv')
        df = pandas.read_csv(filename)
        self.goldstandard = df.copy()

    def load_user_prediction(self):
        df = pandas.read_csv(self.filename)
        self.prediction = df.copy()

    def run(self):
        """Compute the score and populates :attr:`result` attribute with results

        """ 
        self.load_user_prediction()
        self.load_gold_standard()

        result = get_AUC_PR_N_ROC_curve(self.goldstandard,self.prediction)

        df = pandas.DataFrame({'ROC_auc_gen' : result[0] ,'ROC_auc_gen+clin' : result[1], 
                               'PR_auc_gen' :  result[2] , 'PR_auc_gen+clin'  :  result[3]}, index=xrange(1))

        return df
