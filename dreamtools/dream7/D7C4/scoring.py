"""


Original code for challenge B translted from  Mukesh Bansal
Sub challenge A is currently a wrapping of a perl code provided by Jim Costello

"""

import os
import math
import random

from dreamtools.core.challenge import Challenge
from easydev import shellcmd
import pandas as pd


import numpy as np

class D7C4(Challenge):
    """A class dedicated to D7C4 challenge

    ::

        from dreamtools import D7C4
        s = D7C4()
        filename = s.download_template()
        s.score(filename)

    Data and templates are downloaded from Synapse. You must have a login.

    ::

        # columns represent the probabilistic c-index of the given team for
          each drug.
        # following the columns of teams are 5 columns which are used for
          calculating the overall team score
        # |-> Test_data = the probabilistic c-index for the experimentally
          determined test data scored against itself
        # |-> Mean Null Distribution = a set of 10,000 random predictions
          were scored to create the null distribution, of which this column
          represents the mean
        # |-> SD Null Distribution = a set of 10,000 random predictions
          were scored to create the null distribution, of which this column
          represents the standard deviation
        # |-> z-score of test data to null = score of the test data minus
          the mean of the null distribution divided by the standard deviation
          of the null distribution
        # |-> weight of drug (normalized z-score) = the z-score normalized
          by the largest z-score across all 31 drugs.
        # to calculate your team overall score, simply mulitple the score
          of all drugs by the corresponding weight.  Divide the sum of these
          weighted scores by the sum of the weights


    """
    def __init__(self):
        """.. rubric:: constructor

        This challenge uses PERL script that requires the

        It can be installed using a tool such as cpanm

        Project URL : http://search.cpan.org/dist/App-cpanminus/

        Download the perl package available in  ./misc

        This should work out of the box under Fedora::

            sudo cpanm install Math::Libm
            sudo cpanm install Algorithm::Pair::Best2
            sudo cpanm install Digest::SHA1
            sudo cpanm install Tk
            sudo cpanm install Games::Go::AGATourn
            #sudo cpanm install Games::Go::goPair

        Then, untar file in ./misc
        cd to the directory and type:;

            perl Makefile.PL
            make
            sudo make install


        """
        super(D7C4, self).__init__('D7C4')
        self.sub_challenges = ['A', 'B']

    def _check_subname(self, subname):
        from easydev import check_param_in_list
        check_param_in_list(subname, self.sub_challenges)

    def download_template(self, subname):
        self._check_subname(subname)
        if subname == 'A':
            filename = self.getpath_template('D7C4_template.csv')
        elif subname == 'B':
            filename = self.getpath_template('D7C4_template_B.csv')
        return filename

    def score(self, filename, subname):
        self._check_subname(subname)
        if subname == 'A':
            return self.score_A(filename)
        elif subname == 'B':
            return self.score_B(filename)

    def download_goldstandard(self, subname):
        self._check_subname(subname)
        if subname == 'A':
            filename = self._pj([self.classpath, 'templates',
                    'D7C4_template.csv'])
        elif subname == 'B':
            filename = self.getpath_gs('D7C4_B_synergy_IC20.tsv')
        return filename

    def score_A(self, filename):
        from easydev import TempFile
        fh = TempFile()
        script = self._pj([self.classpath,
            'weighted_average_concordance_index.pl'])
        datadir = self._pj([self.classpath, 'data'])
        cmd = "perl %s %s %s %s"
        cmd = cmd % (script, filename, datadir , fh.name)

        shellcmd(cmd, verbose=True, ignore_errors=True)
        df = pd.read_csv(fh.name, sep='\t', header=None)
        df.columns = ['DrugID', 'probabilistic c-index',
        'weighted probabilistic c-index', 'zscores']
        df = df.set_index('DrugID')
        fh.delete()

        ws = (df.sum() / df.sum().ix['zscores'])
        ws = ws.ix['weighted probabilistic c-index']

        results = df.mean()
        results['weight average probabilistic c-index'] = ws

        del results['zscores']

        # Finally compute pvalues based on precomputed scores
        precomp = pd.read_csv(self._pj([self.classpath, 'data',
            'DREAM7_DrugSensitivity1_drug_zscores.txt']), sep='\t',
            skiprows=6,  header=None)

        overall_mean = precomp.ix[31][1]
        overall_var = precomp.ix[31][2]

        pval = 1 -  (.5 * (math.erf((ws - overall_mean)/(math.sqrt(2*overall_var))) + 1))

        results['weight average probabilistic c-index p-value'] = pval

        return {'Results': results}

    def score_B(self, filename):
        gs_filename = self.download_goldstandard('B')
        gold = pd.read_csv(gs_filename, sep='\t')
        gold.columns = [x.strip() for x in gold.columns]

        unique_drugs = list(set(gold['Cmpd A']))

        # build a new columns
        pairs = gold['Cmpd A'] + "_" + gold['Cmpd B']
        gold['pairs'] = pairs

        # sort by excess of over Bliss
        gold = gold.sort(columns=['Excess over Bliss'])

        self.p_matrix = self._probability_matrix(gold['Excess over Bliss'], gold['SEM'])

        # noew read the predicition. Note that here it has to be comma separated
        # There are 91 rows + 1 . THe lsat gives the
        # The 93rd row (i.e., the last row after the header line and the 91 pairs) should report the
        # first compound pair in the ranked list whose predicted activity is not deemed to have a
        # significant synergistic effect, i.e. excess over Bliss close to 0 (see Scoring Metrics section
        # for the definition of excess over Bliss).
        prediction = pd.read_csv(filename, sep=',')
        # we rename first column to agree with gold for a later merge
        prediction.columns = ['pairs', 'Rank']
        #skip last row
        prediction = prediction.ix[0:90]

        #In the submission, drugs already within a single column where drug A and B are seprated by a & sign.
        # let us replace the & by a _ like in the gold standard
        newnames = prediction['pairs'].apply(lambda x : "_".join([y.strip() for y in x.split("&")]))
        newnames = list(newnames)
        prediction['pairs'] = newnames

        # not that the fold is sorted so it should be first
        self.merged = pd.merge(gold, prediction, how='inner', on=['pairs'])

        N = 91
        ranks = self.merged['Rank'].values.astype(float)
        weighted_cindex = self._concordance(ranks, range(0,N), self.p_matrix)

        Nmax = 10000
        cindex_nulldist =np.zeros(Nmax)
        for i in range(0, Nmax):
            randx = range(N)
            random.shuffle(randx) # in place
            cindex_nulldist[i] = self._concordance(randx, range(0,N), self.p_matrix)

        pvalues = sum(cindex_nulldist>= weighted_cindex)/float(Nmax)

        results = pd.TimeSeries()
        results['weighted cindex'] = weighted_cindex
        results['pvalue'] = pvalues

        return {'Results': results}

    def _probability_matrix(self, x, x_std):
        from scipy.special import erf
        N = len(x)
        X = np.repeat(np.array(x),N).reshape(N,N)
        X = X - X.transpose()
        X_std = np.repeat(np.array(x_std),N).reshape(N,N)
        X_std = np.sqrt(X_std**2+X_std.transpose()**2)
        p_matrix = 0.5*(1 + erf(X/X_std))
        return p_matrix

    def _concordance(self, x, y, p_matrix):
        N = len(x)
        X = np.repeat(np.array(x),N).reshape(N, N)
        Y = np.repeat(np.array(y),N).reshape(N, N)

        C = np.sign(X - X.transpose()) == np.sign(Y - Y.transpose())
        C = C * (1 - p_matrix.transpose()) + (1-C) * p_matrix.transpose()

        C = sum(sum(np.tril(C, -1))) / float(N) / (N - 1.) * 2
        return C

