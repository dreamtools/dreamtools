"""D6C3 scoring function

Based on Pablo's Meyer Matlab code.
"""
import os
from dreamtools.core.challenge import Challenge
import pandas as pd
import numpy as np
import glob

class D6C3(Challenge):
    """A class dedicated to D6C3 challenge

    ::

        from dreamtools import D6C3
        s = D6C3()
        filename = s.download_template()
        s.score(filename)

    Absolute score in the Pearson coeff but other scores such as
    chi-square and rank are based on the 21st participants.

    Pearson and spearman gives same values as in final LB but X2 and R2
    are slightly different. Same results as in the original matlab scripts
    so the different with the LB is probably coming fron a different
    set of predictions files, which is stored in ./data/predictions
    and was found in http://genome.cshlp.org/content/23/11/1928/suppl/DC1

    The final score in the official leaderboard computed the p-values for
    each score (chi-square, r-square, spearman and pearson correlation
    coefficient) and took -0.25 log ( product of p-values) as the final score.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D6C3, self).__init__('D6C3')
        self.sub_challenges = []

    def score(self, filename):

        self.read_all_participants()

        gs_filename = self.download_goldstandard()
        self.goldstandard = pd.read_csv(gs_filename, sep='\t', header=None)
        self.goldstandard.set_index(0, inplace=True)

        self.prediction = pd.read_csv(filename, sep='\t', header=None)
        self.prediction.set_index(0, inplace=True)

        # some aliaes
        pred = self.prediction
        gs = self.goldstandard
        Spred = self.prediction.sum()
        Sgs = self.goldstandard.sum()

        # Compute the Pearson coeff
        d1 = ((pred - Spred/53.)**2).sum()  # variance participant
        d2 = ((gs - Sgs/53.)**2).sum()      # variance GS
        Cp = (pred * gs).sum() - Spred * Sgs / 53.
        Cp /= np.sqrt(d1*d2)
        Cp = Cp.values[0]

        # using Scipy gives also the p-values
        # scipy.stats.pearsonr(s.prediction, s.goldstandard)
        import scipy.stats
        Sp = scipy.stats.spearmanr(pred, gs)[0]
        # could replace code above to compute pearson by this code:
        #Cp2 = scipy.stats.pearsonr(pred,gs)[0][0]

        # The ChiSqaure
        # Same results as Kelly's score but different from LB on synapse
        chi = 0
        for j in range(0,53):
            num = (pred.ix[j] - gs.ix[j])**2
            denom = np.mean((self.alldata.ix[j] - gs.ix[j].values)**2)
            chi += num / denom

        tiedrank = self.goldstandard.rank()   # if tied, average ranks

        # R-square
        r2 = 0
        pt = 21
        allranks = self.alldata.rank()
        for i in range(0, 53):
            indx = pred.rank()
            rn1 = indx.ix[i] - tiedrank.ix[i]
            rs2 = 0
            for j in range(0, pt):
                rd1 = allranks.ix[i,j] - tiedrank.ix[i]
                rs2 = rs2 + rd1*rd1
            rs2 = rs2 / float(pt)
            r2 = r2 + (rn1*rn1) / rs2

        results = pd.TimeSeries()
        results['chi2'] = chi.values[0]
        results['R-square'] = r2.values[0]
        results['Spearman(Sp)'] = Sp
        results['Pearson(Cp)'] = Cp
        return {'results':results}

    def read_all_participants(self):
        path = self._pj([self.classpath, 'data', 'predictions'])
        filenames = glob.glob(path + os.sep + '*txt')
        assert len(filenames) == 21
        data = [pd.read_csv(filenames[i], sep='\t', header=None)[1] for
            i in range(0,21)]
        self.alldata = pd.DataFrame(data).T
        self.alldata.columns = range(0,21)

    def download_template(self):
        return self.getpath_template('D6C3_template.txt')

    def download_goldstandard(self):
        return self.getpath_gs('D6C3_goldstandard.txt')

