# -*- python -*-
# -*- coding: utf-8 -*-
#
#  This file is part of dreamtools software
#
#  Copyright (c) 2013-2015 - EBI-EMBL
#
#  File author(s): Thomas Cokelaer <cokelaer@ebi.ac.uk>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  website: http://github.com/dreamtools
#
##############################################################################
"""This is a standlone ranking independent of synapse that may be used in the
future"""
import json
import pandas as pd
from dreamtools.dream8.D8C1 import submissions
from dreamtools.dream8.D8C1 import scoring


from dreamtools import LocalData


class Ranking(LocalData):

    def __init__(self, name):
        super(Ranking, self).__init__()
        self.name = name
        self.yours = 'YOUR_SUBMISSION'

    def _getdata(self, filename):
        return self.getpath_data(filename)

    def add_team(self):
        raise NotImplementedError

    def check_submissions(self):
        if getattr(self, 'submissions') is False:
            print("Call load_data_from_synapse() first. You 'll need synapse access as admin")

    def load_data_from_synapse(self):
        if self.name == 'SC1A':
            subs = submissions.SC1ASubmissions()
        elif self.name == 'SC1B':
            subs = submissions.SC1BSubmissions()
        elif self.name == 'SC2A':
            subs = submissions.SC2ASubmissions()
        elif self.name == 'SC2B':
            subs = submissions.SC2BSubmissions()
        subs.load_submissions()
        self.submissions = subs.submissions

    def get_ranked_df(self):
        df = self.ranked_df.copy()
        df = self._sort_df(df)
        return df

    def _sort_df(self, df):
        raise NotImplementedError

    def get_rank_your_submission(self):
        try:
            return list(self.get_ranking().index).index(self.yours) + 1
        except:
            print("Are we here?")
            try:
                return self.get_ranking().ix[self.yours].values[0]
            except:
                print("Use append_submission() method to add your submission")
                return 99

    def __str__(self):
        return self.get_ranked_df().to_string()


class SC1A_ranking(Ranking):
    """


    """
    def __init__(self, version=None):
        super(SC1A_ranking, self).__init__('SC1A')
        self.aucs = pd.read_json(self._getdata("SC1A_aucs.json"))
        self.ranked_df = pd.read_json(self._getdata("SC1A_results.json"))
        self.version = version

    def _sort_df(self, df):
        df.sort('Mean Rank', inplace=True)
        df = df[['Final Rank', 'Team Name', 'Team Id', 'Submission Id',
                 'Entity Id', 'Mean AUC', 'Mean Rank']]
        df = df.reset_index(drop=True)
        df['Final Rank'] = [1+x for x in df.index]
        return df

    def get_aucs(self):
        return self.aucs

    def get_ranked_df_from_submission(self):
        """No need to be used. Just for admin to recreate SC1A_results.json"""
        self.check_submissions()

        submitterAlias = [sub['submitterAlias'] for sub in self.submissions]
        subId = [sub['substatus']['id'] for sub in self.submissions]
        entityId = [sub['substatus']['entityId'] for sub in self.submissions]
        userId = [sub['userId'] for sub in self.submissions]
        auc = [sub['mean_aucs'] for sub in self.submissions]
        ranking = [sub['ranking'] for sub in self.submissions]

        submitterAlias = [sub.replace("ChaosLab", "FreiburgBiossX") for sub in submitterAlias]

        df = pd.DataFrame({
            'Final Rank': ranking,
            'Team Name': submitterAlias,
            'Team Id': userId,
            'Submission Id': subId,
            'Entity Id': entityId,
            'Mean AUC': auc,
            'Mean Rank':ranking
        })
        df = self._sort_df(df)
        return df

    def get_aucs_from_submissions(self):
        """No need to be used. Just for admin to recreate SC1A_aucs.json"""
        self.check_submissions()
        df = self.get_ranked_df_from_submissions()
        data = [json.loads(this['substatus']['report']) for this in self.submissions]

        columns = [k1+"_"+k2 for k1 in data[0].keys() for k2 in data[0][k1].keys()]
        aucs = [[datum[k1][k2] for k1 in datum.keys() for k2 in datum[k1].keys()] for datum in data]

        #indices = df['Team Name']
        indices = [sub['submitterAlias'] for sub in self.submissions]
        indices = [this.replace("ChaosLab", "FreiburgBiossX") for this in indices]
        aucs = pd.DataFrame(aucs, columns=columns, index=indices)

        return aucs

    def get_ranking(self):
        aucs = self.get_aucs().copy()  # copy is essnetial since we then delete columns
        # some combo were removed in the final LB

        del aucs['BT549_NRG1']
        del aucs['BT20_Insulin']

        df = aucs.rank(ascending=False, method='min').mean(axis=1)
        try:
            df.sort_values(inplace=True)
        except:
            df.sort(inplace=True)
        return df

    def __str__(self):
        return self.get_ranked_df().to_string()

    def append_submission(self, res):
        try:
            res = scoring.HPNScoringNetwork(res)
            res.compute_all_aucs()
        except Exception:
            if getattr(res, 'aucs') is False:
                raise Exception

        self.aucs.ix[self.yours] = [1] * 32
        #now replace the values as expected; s.auc is a 4 by  8 matrix
        for cell in res.auc.keys():
            for stim in res.auc[cell].keys():
                self.aucs.ix[self.yours][cell + "_" + stim] = res.auc[cell][stim]


class SC1B_ranking(Ranking):

    def __init__(self, version=None):
        super(SC1B_ranking, self).__init__('SC1B')
        self.ranked_df = pd.read_json(self._getdata("SC1B_results.json"))
        self.version = version # does not matter. to have same API

    def _sort_df(self, df):
        try:
            df.sort_values(by='AUC', inplace=True, ascending=False)
        except:
            df.sort('AUC', inplace=True, ascending=False)

        df = df.reset_index(drop=True)
        df['Final Rank'] = df.index
        df = df[['Final Rank', 'Team Name', 'Team Id', 'Submission Id',
                 'Entity Id', 'AUC', 'zscore']]
        return df

    def get_ranked_df_from_submissions(self):
        self.check_submissions()
        report = [sub['substatus']['report'] for sub in self.submissions]
        submitterAlias = [sub['submitterAlias'] for sub in self.submissions]
        subId = [sub['substatus']['id'] for sub in self.submissions]
        entityId = [sub['substatus']['entityId'] for sub in self.submissions]
        userId = [sub['userId'] for sub in self.submissions]

        auc = [sub['auc'] for sub in self.submissions]
        zscore = [json.loads(sub['substatus']['report'])['score'] for sub in self.submissions]

        submitterAlias = [sub.replace("ChaosLab", "FreiburgBiossX") for sub in submitterAlias]

        df = pd.DataFrame({
            'Team Name': submitterAlias,
            'Team Id': userId,
            'Submission Id': subId,
            'Entity Id': entityId,
            'AUC': auc,
            'zscore': zscore,
        })
        df = self._sort_df(df)
        return df

    def get_ranking(self):
        df = self.get_ranked_df()
        df = df[['Team Name', 'AUC']]
        df.set_index('Team Name', inplace=True)
        df = df.rank(ascending=False, method='min')
        return df

    def append_submission(self, res):
        try:
            res = scoring.HPNScoringNetworkInsilico(res, self.version)
            res.compute_score()
        except:
            print('Failed to score submission')

        ts = self.ranked_df.ix[0].copy()
        ts.name = 99
        ts['AUC'] = res.auc
        ts['Team Name'] = self.yours
        self.ranked_df = self._sort_df(self.ranked_df.append(ts))


class SC2A_ranking(Ranking):
    """

    """
    # 375805/alphabeta is a test from TC
    # 1991105/sakev from week 5 has different id from sakev week 6. renmove
    #      week5 that has a lower score anyway
    # 1971259/HD systems see SC1A function docstring
    userIds_toremove =  ["375805", "1991105", "1971259"]
    def __init__(self, version=1):
        super(SC2A_ranking, self).__init__('SC2A')
        self.version = version

        # Those files are created using the submissions module calling
        # save_rmse_to_json anda save_df_to_json
        if self.version == 1:
            self.rmses = pd.read_json(self._getdata("SC2A_rmses_v1.json"))
            self.ranked_df = pd.read_json(self._getdata("SC2A_results_v1.json"))
        elif version == 2:
            self.rmses = pd.read_json(self._getdata("SC2A_rmses_v2.json"))
            self.ranked_df = pd.read_json(self._getdata("SC2A_results_v2.json"))

    def _sort_df(self, df):
        try:
            df.sort_by_values(by='Mean Rank', inplace=True)
        except:
            df.sort('Mean Rank', inplace=True)

        df = df[['Final Rank', 'Team Name', 'Team Id', 'Submission Id',
                 'Entity Id', 'Mean RMSE', 'Mean Rank']]
        df = df.reset_index(drop=True)
        df['Final Rank'] = [1+x for x in df.index]
        return df

    def get_rmses(self):
        return self.rmses.copy()

    def get_ranking(self):
        rmses = self.get_rmses()
        # Here we use ascending True because we have RMSE (lower=better)
        df = rmses.rank(ascending=True, method='min').mean(axis=1)
        try:
            df.sort_values(inplace=True)
        except:
            df.sort(inplace=True)
        return df

    def append_submission(self, res):
        try:
            res = scoring.HPNScoringPrediction(res, version=self.version)
            res.compute_all_rmse()
        except:
            pass

        self.rmses.ix[self.yours] = [1] * 162
        #now replace the values as expected; s.auc is a 4 by  8 matrix
        for cell in res.rmse.keys():
            for stim in res.rmse[cell].keys():
                self.rmses.ix[self.yours][cell + "_" + stim] = res.rmse[cell][stim]



class SC2B_ranking(Ranking):
    """

    subs = submissions.SC1ASubmissions()
    subs.load_submissions()

    ranking = SC2B_ranking(subs.submissions)

    """
    # 375805/alphabeta is a test from TC
    # 1991105/sakev from week 5 has different id from sakev week 6. renmove
    #      week5 that has a lower score anyway
    # 1971259/HD systems see SC1A function docstring
    userIds_toremove =  ["375805", "1991105"]
    def __init__(self, version=1):
        super(SC2B_ranking, self).__init__('SC2B')
        # Those files are created using the submissions module calling
        # save_rmse_to_json anda save_df_to_json
        if version == 1:
            self.rmses = pd.read_json(self._getdata("SC2B_rmses_v1.json"))
            self.ranked_df = pd.read_json(self._getdata("SC2B_results_v1.json"))
        elif version == 2:
            self.rmses = pd.read_json(self._getdata("SC2B_rmses_v2.json"))
            self.ranked_df = pd.read_json(self._getdata("SC2B_results_v2.json"))
        self.version = version

    def _sort_df(self, df):
        try:
            df.sort_values(by='Mean Rank', inplace=True)
        except:
            df.sort('Mean Rank', inplace=True)
        df = df[['Final Rank', 'Team Name', 'Team Id', 'Submission Id',
                 'Entity Id', 'Mean RMSE', 'Mean Rank']]

        df = df.reset_index(drop=True)
        df['Final Rank'] = [1+x for x in df.index]
        return df

    def get_rmses(self):
         return self.rmses.copy()

    def get_ranking(self):
        #I check on the old/wrong  GS network that we retrieve the rank and mean RMSE from the
        # LB so this code is correct. Using the new correct GS network, we of course
        # get different results but the results should be correct.
        rmses = self.get_rmses()
        # Here we use ascending True because we have RMSE (lower=better)
        df = rmses.rank(ascending=True, method='min').mean(axis=1)
        try:
            df.sort_values(inplace=True)
        except:
            df.sort(inplace=True)
        return df

    def append_submission(self, res):
        try:
            res = scoring.HPNScoringPredictionInsilico(res, version=self.version)
            res.compute_all_rmse()
        except:
            pass

        self.rmses.ix[self.yours] = [1] * 231
        #now replace the values as expected; s.auc is a 4 by  8 matrix
        for cell in res.rmse.keys():
            for stim in res.rmse[cell].keys():
                self.rmses.ix[self.yours][cell + "_" + stim] = res.rmse[cell][stim]



class CombinedRanking(object):
    """Combined Ranking for SC1 and SC2 challenge

    ::

        >>> a = ranking.SC1A_ranking()
        >>> b = ranking.SC1B_ranking()
        >>> aggr = CombinedRanking(a, b, 'SC1')
        >>> aggr.get_ranking()

    """
    def __init__(self, rsca, rscb, name):
        """

        :param rsca: an instance of SC1A_ranking or SC2A_ranking
        :param rscb: an instance of SC1B_ranking or SC2B_ranking
        :param name: SC1 or SC2

        """
        self.rsca = rsca
        self.rscb = rscb
        assert name in ['SC1', 'SC2']
        self.name = name

    def get_ranking(self):
        fillna = 1e6
        # Here we want to replace values that are not between 1 and N
        # into integer from 1 to N so that it can be compared to df1b
        dfa = self.rsca.get_ranking()
        N = len(dfa)
        dfa = pd.DataFrame(range(1, N+1), index=dfa.index)

        dfb = self.rscb.get_ranking()
        N2 = len(dfb)
        dfb = pd.DataFrame(range(1, N2+1), index=dfb.index)

        df = pd.concat([dfa, dfb], axis=1).fillna(fillna)
        df.columns = [self.name +'A', self.name +'B']
        df['mean'] = df.mean(axis=1)
        df.sort(columns='mean', inplace=True)

        ranks = df['mean'].rank(ascending=True, method='min')
        df['aggregate rank'] = ranks

        df['aggregate rank'][df['mean']>(fillna-1)/2] = None
        return df

    def __str__(self):
        df = self.get_ranking()
        from dreamtools.core.wikitools import dataframe_towiki
        print(dataframe_towiki(df))
