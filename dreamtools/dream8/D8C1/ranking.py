import pandas as pd
import json



class Ranking(object):
    pass



class SC1A_ranking(Ranking):
    """

    subs = submissions.SC1ASubmissions()
    subs.load_submissions()

    ranking = SC1A_ranking(subs.submissions)

    """
    def __init__(self, submissions):
        super(SC1A_ranking, self).__init__()
        self.submissions = submissions

    def get_ranked_df(self):

        # report = [sub['substatus']['report'] for sub in self.submissions]
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
        df.sort('Mean Rank', inplace=True)
        df = df[['Final Rank', 'Team Name', 'Team Id', 'Submission Id',
                 'Entity Id', 'Mean AUC', 'Mean Rank']]

        df = df.reset_index(drop=True)
        df['Final Rank'] = [1+x for x in df.index]
        return df

    def get_aucs(self):

        df = self.get_ranked_df()

        data = [json.loads(this['substatus']['report']) for this in self.submissions]


        columns = [k1+"_"+k2 for k1 in data[0].keys() for k2 in data[0][k1].keys()]
        aucs = [[datum[k1][k2] for k1 in datum.keys() for k2 in datum[k1].keys()] for datum in data]

        #indices = df['Team Name']
        indices = [sub['submitterAlias'] for sub in self.submissions]
        indices = [this.replace("ChaosLab", "FreiburgBiossX") for this in indices]


        aucs = pd.DataFrame(aucs, columns=columns, index=indices)


        return aucs

    def get_ranking(self):
        aucs = self.get_aucs()
        # some combo were removed:
        del aucs['BT549_NRG1']
        del aucs['BT20_Insulin']
        df = aucs.rank(ascending=False, method='min').mean(axis=1)
        df.sort()

        return df


    def __str__(self):
        return self.get_df().to_string()

class SC1B_ranking(Ranking):

    def __init__(self, submissions):
        super(SC1B_ranking, self).__init__()
        self.submissions = submissions


    def get_ranked_df(self):
        report = [sub['substatus']['report'] for sub in self.submissions]
        submitterAlias = [sub['submitterAlias'] for sub in self.submissions]
        subId = [sub['substatus']['id'] for sub in self.submissions]
        entityId = [sub['substatus']['entityId'] for sub in self.submissions]
        userId = [sub['userId'] for sub in self.submissions]

        auc = [sub['auc'] for sub in self.submissions]
        zscore = [json.loads(sub['substatus']['report'])['score'] for sub in self.submissions]

        submitterAlias = [sub.replace("ChaosLab", "FreiburgBiossX") for sub in submitterAlias]

        df = pd.DataFrame({
            #'Final Rank': ,
            'Team Name': submitterAlias,
            'Team Id': userId,
            'Submission Id': subId,
            'Entity Id': entityId,
            'AUC': auc,
            'zscore':zscore,
        })
        df.sort('AUC', inplace=True, ascending=False)
        df = df.reset_index(drop=True)
        df['Final Rank'] = df.index
        df = df[['Final Rank', 'Team Name', 'Team Id', 'Submission Id',
                 'Entity Id', 'AUC', 'zscore']]

        return df

    def get_ranking(self):
        df = self.get_ranked_df()
        df = df[['Team Name', 'AUC']]
        df.set_index('Team Name', inplace=True)
        df = df.rank(ascending=False, method='min')
        return df


class SC1Aggregate():

    def __init__(self, rsc1a, rsc1b):
        """

        :param rsc1a:
        :param rsc1b:
        :return:
        """
        self.rsc1a = rsc1a
        self.rsc1b = rsc1b

    def get_ranking(self):
        # Here we want to replace values that are not between 1 and N
        # into integer from 1 to N so that it can be compared to df1b
        df1a = self.rsc1a.get_ranking()
        N = len(df1a)
        df1a = pd.DataFrame(range(1, N+1), index=df1a.index)

        # df1a has already values from 1 to N
        df1b = self.rsc1b.get_ranking()

        df = pd.concat([df1a, df1b], axis=1).fillna(1e6) #.rank(ascending=False, method='min')
        df.columns = ['SC1A', 'SC1B']
        df['mean'] = df.mean(axis=1)
        df.sort(columns='mean', inplace=True)

        ranks = df['mean'].rank(ascending=True, method='min')
        df['aggregate rank'] = ranks

        return df

    def __str__(self):
        df = self.get_ranking()
        return df.to_string()



class SC2A_ranking(Ranking):
    """

    subs = submissions.SC1ASubmissions()
    subs.load_submissions()

    ranking = SC1A_ranking(subs.submissions)

    """


    # 375805/alphabeta is a test from TC
    # 1991105/sakev from week 5 has different id from sakev week 6. renmove
    #      week5 that has a lower score anyway
    # 1971259/HD systems see SC1A function docstring
    userIds_toremove =  ["375805", "1991105", "1971259"]
    def __init__(self, submissions):
        super(SC2A_ranking, self).__init__()
        self.submissions = submissions

        self.phosphos_to_exclude = {
                'MCF7': ['TAZ_pS89', 'FOXO3a_pS318_S321', 'mTOR_pS2448'],
                'UACC812': ['TAZ_pS89','mTOR_pS2448'],
                'BT20': ['TAZ_pS89', 'FOXO3a_pS318_S321', 'mTOR_pS2448'],
                'BT549': ['TAZ_pS89','mTOR_pS2448']
        }


    def get_ranked_df(self):

        #report = [sub['substatus']['report'] for sub in self.submissions]

        submitterAlias = [sub['submitterAlias'] for sub in self.submissions]
        subId = [sub['substatus']['id'] for sub in self.submissions]
        entityId = [sub['substatus']['entityId'] for sub in self.submissions]
        userId = [sub['userId'] for sub in self.submissions]
        rmse = [sub['mean_rmse'] for sub in self.submissions]
        ranking = [sub['ranking'] for sub in self.submissions]


        df = pd.DataFrame({
            'Final Rank': ranking,
            'Team Name': submitterAlias,
            'Team Id': userId,
            'Submission Id': subId,
            'Entity Id': entityId,
            'Mean RMSE': rmse,
            'Mean Rank':ranking
        })
        df.sort('Mean Rank', inplace=True)
        df = df[['Final Rank', 'Team Name', 'Team Id', 'Submission Id',
                 'Entity Id', 'Mean RMSE', 'Mean Rank']]

        df = df.reset_index(drop=True)
        df['Final Rank'] = [1+x for x in df.index]
        return df

    def get_rmses(self):

        df = self.get_ranked_df()

        data = [this['rmses'] for this in self.submissions]
        columns = [k1+"_"+k2 for k1 in data[0].keys() for k2 in data[0][k1].keys()]
        rmses = [[datum[k1][k2] for k1 in datum.keys() for k2 in datum[k1].keys()] for datum in data]
        indices = [sub['submitterAlias'] for sub in self.submissions]
        rmses = pd.DataFrame(rmses, columns=columns, index=indices)
        # recompute the mean RMSEs gives same results as in get_ranked_df
        # self.get_rmses().mean(axis=1)
        return rmses

    def get_ranking(self):
        rmses = self.get_rmses()
        # Here we use ascending True because we have RMSE (lower=better)
        df = rmses.rank(ascending=True, method='min').mean(axis=1)
        df.sort()
        return df

    def __str__(self):
        return self.get_ranked_df().to_string()




class SC2B_ranking(Ranking):
    """

    subs = submissions.SC1ASubmissions()
    subs.load_submissions()

    ranking = SC1A_ranking(subs.submissions)

    """


    # 375805/alphabeta is a test from TC
    # 1991105/sakev from week 5 has different id from sakev week 6. renmove
    #      week5 that has a lower score anyway
    # 1971259/HD systems see SC1A function docstring
    userIds_toremove =  ["375805", "1991105"]
    def __init__(self, submissions):
        super(SC2B_ranking, self).__init__()
        self.submissions = submissions

    def get_ranked_df(self):

        #report = [sub['substatus']['report'] for sub in self.submissions]

        submitterAlias = [sub['submitterAlias'] for sub in self.submissions]
        subId = [sub['substatus']['id'] for sub in self.submissions]
        entityId = [sub['substatus']['entityId'] for sub in self.submissions]
        userId = [sub['userId'] for sub in self.submissions]
        rmse = [sub['mean_rmse'] for sub in self.submissions]
        ranking = [sub['ranking'] for sub in self.submissions]


        df = pd.DataFrame({
            'Final Rank': ranking,
            'Team Name': submitterAlias,
            'Team Id': userId,
            'Submission Id': subId,
            'Entity Id': entityId,
            'Mean RMSE': rmse,
            'Mean Rank':ranking
        })
        df.sort('Mean Rank', inplace=True)
        df = df[['Final Rank', 'Team Name', 'Team Id', 'Submission Id',
                 'Entity Id', 'Mean RMSE', 'Mean Rank']]

        df = df.reset_index(drop=True)
        df['Final Rank'] = [1+x for x in df.index]
        return df

    def get_rmses(self):

        df = self.get_ranked_df()

        data = [this['rmses'] for this in self.submissions]
        columns = [k1+"_"+k2 for k1 in data[0].keys() for k2 in data[0][k1].keys()]
        rmses = [[datum[k1][k2] for k1 in datum.keys() for k2 in datum[k1].keys()] for datum in data]
        indices = [sub['submitterAlias'] for sub in self.submissions]
        rmses = pd.DataFrame(rmses, columns=columns, index=indices)
        # recompute the mean RMSEs gives same results as in get_ranked_df
        # self.get_rmses().mean(axis=1)
        return rmses

    def get_ranking(self):
        #I check on the old/wrong  GS network that we retrieve the rank and mean RMSE from the
        # LB so this code is correct. Using the new correct GS network, we of course
        # get different results but the results should be correct.
        rmses = self.get_rmses()
        # Here we use ascending True because we have RMSE (lower=better)
        df = rmses.rank(ascending=True, method='min').mean(axis=1)
        df.sort()
        return df

    def __str__(self):
        return self.get_ranked_df().to_string()


class Aggregate():
    """
    sc2a =
    sc2b =
    sc2a.load_submissions()
    sc2b.load_submissions()
    rsc2a =
    rsc2b =
    aggr = SCA

    """

    def __init__(self, rsc2a, rsc2b):
        """

        :param rsc1a:
        :param rsc1b:
        :return:
        """
        self.rsc2a = rsc2a
        self.rsc2b = rsc2b

    def get_ranking(self):
        fillna = 1e6
        # Here we want to replace values that are not between 1 and N
        # into integer from 1 to N so that it can be compared to df1b
        df2a = self.rsc2a.get_ranking()
        N = len(df2a)
        df2a = pd.DataFrame(range(1, N+1), index=df2a.index)



        df2b = self.rsc2b.get_ranking()
        N2 = len(df2b)
        df2b = pd.DataFrame(range(1, N2+1), index=df2b.index)

        df = pd.concat([df2a, df2b], axis=1).fillna(fillna)
        df.columns = ['SC2A', 'SC2B']
        df['mean'] = df.mean(axis=1)
        df.sort(columns='mean', inplace=True)

        ranks = df['mean'].rank(ascending=True, method='min')
        df['aggregate rank'] = ranks


        df['aggregate rank'][df['mean']>(fillna-1)/2] = None

        return df

    def __str__(self):
        df = self.get_ranking()
        return df.to_string()
