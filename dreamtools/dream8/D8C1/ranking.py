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

        report = [sub['substatus']['report'] for sub in self.submissions]
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
        df['Final Rank'] = df.index
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

        # now, you can add a new submission and compute the new ranking
        # !!! this is different from original version but due to rounded errors at 1e-16
        # Pandas works as expected actually
        # df2 = df.rank(ascending=False, method='min').mean(axis=1)
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

    def __init__(self):
        pass

    def get_ranking(self, rsc1a, rsc1b):
        # Here we want to replace values that are not between 1 and N
        # into integer from 1 to N so that it can be compared to df1b
        df1a = rsc1a.get_ranking()
        N = len(df1a)
        df1a = pd.DataFrame(range(1, N+1), index=df1a.index)

        # df1a has already values from 1 to N
        df1b = rsc1b.get_ranking()

        df = pd.concat([df1a, df1b], axis=1).fillna(1e6) #.rank(ascending=False, method='min')
        df.columns = ['SC1A', 'SC1B']
        df['mean'] = df.mean(axis=1)
        df.sort(columns='mean', inplace=True)

        ranks = df['mean'].rank(ascending=True, method='min')
        df['aggregate rank'] = ranks

        return df


