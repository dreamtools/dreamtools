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
import os
import pandas as pd


'''
def sanity_check_userSubmission(goldStandard, user_predicted_response,
                                expected_columnNames = None):

    #making sure the column names are exactly same as expected
    if expected_columnNames:
        expected_columnNames = set(expected_columnNames)
        recvd_columnNames = set(user_predicted_response.columns).difference(set(['index'])) #to remove 'index' if blank df is present
        if(len(expected_columnNames.difference(recvd_columnNames)) !=0):
            submissionResult.error=True
            submissionResult.error_message='Expected column names: (%s) not found in the submission file colnames:(%s) \n' % (', '.join(expected_columnNames),
                                                                                              ', '.join(recvd_columnNames))
            return

    #making sure all the sampleIDs are present in the user submitted response
    user_submitted_ids = set(user_predicted_response.ID)
    testSamples_id = set(goldStandard.ID)
    if(len(user_submitted_ids.difference(testSamples_id)) !=0 or len(testSamples_id.difference(user_submitted_ids)) != 0 ):
       print 'missing rows(IDs) in the submission'
       return

    #check for missing values in any of the rows
    if(sum(pandas.isnull(user_predicted_response).any(axis=1)) > 0):
        submissionResult.error=True
        submissionResult.error_message='NA/missing values found in the submission'
        return
'''





class D8dot5C1():
    """A class dedicated to D8dot5C1 challenge

    ::

        from dreamtools import D8dot5C1
        s = D8dot5C1()
        filename = s.download_template() 
        s.score(filename) 

    Data and templates are downloaded from Synapse. You must have a login.
    """
    def __init__(self):
        """.. rubric:: constructor
        """
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self.sub_challenges = ['sc1', 'sc2']

    

    def score(self, filename, sub_challenge_name):
        """Scoring functions for the 2 sub challenges"""
        if sub_challenge_name == 'sc1':
            df = self.score_sc1(filename)
            return df
        elif sub_challenge_name == 'sc2':
            df = self.score_sc2(filename)
            return df
        else:
            ValueError("Invalid sub challenge. Use one of %s" % self.sub_challenges)

    def score_sc1(self, filename):
        """See :class:`~dreamtools.dream8dot5.D8dot5C1.sc1.D8dot5C1_sc1` class for details"""
        from dreamtools.dream8dot5.D8dot5C1.sc1 import D8dot5C1_sc1
        s = D8dot5C1_sc1(filename)
        df = s.run()
        return df

    '''
    def score_sc2(self, filename):
        """See :class:`~dreamtools.dream8.D8C2.sc1.D8C2_sc2` class for details"""
        from dreamtools.dream8.D8dot5C1.sc2 import D8dot5C1_sc2
        s = D8dot5C1_sc2(filename)
        df = s.run()
        return df
    '''


    def download_template(self, sub_challenge):
        """Download template 
        """
        if sub_challenge == 'sc1':
            filename = os.sep.join([self._path2data, 'data', 'dummy_template_sc1.csv'])
            return filename
        elif sub_challenge == 'sc2':
            filename = os.sep.join([self._path2data, 'data', 'dummy_template_sc2.csv'])
            return filename
        else:
            ValueError("Invalid sub challenge. Use one of %s" % self.sub_challenges)







