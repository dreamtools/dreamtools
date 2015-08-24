"""D4C1 scoring function

Based on an original matlab code from
Gustavo A. Stolovitzky, and Robert Prill.

"""
import StringIO
from dreamtools.core.challenge import Challenge

import scipy.io
import numpy as np
import pandas as pd


class D4C1(Challenge):
    """A class dedicated to D4C1 challenge

    ::

        from dreamtools import D4C1
        s = D4C1()
        filename = s.download_template()
        s.score(filename)

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D4C1, self).__init__('D4C1')

        self._indices_sh3 = [0, 1, 2, 4]  # gold standard for 3 was not ready
        self._indices_kinases = [5, 6, 7]
        self._indices_pdz = [8, 9, 10, 11, 12]

        self._init()

        self._load_golddata()
        self.results = {'kinase': {}, 'pdz': {}, 'sh3': {}}

    def score(self, filename):
        self._load_prediction(filename)
        self.score_kinases()
        self.score_pdz()
        self.score_sh3()
        return self.results

    def _load_golddata(self):
        filename = self._pj([self.classpath, 'goldstandard',
            'D4C1_goldstandard.txt'])
        data = open(filename).read()
        # in principle, the file contains 13 matrices with an empty
        # line in between (hence the \n\n and there is a line before
        # each matrix that is not a header hence header=None
        self.golddata = []
        for i in range(0, 13):
            df = pd.read_csv(StringIO.StringIO(data.split("\n\n")[i]),
                    header=None, sep='\t', skiprows=1, index_col=0)
            self.golddata.append(df)

    def _load_prediction(self, filename):
        data = open(filename).read()
        # in principle, the file contains 13 matrices with an empty
        # line in between (hence the \n\n and there is a line before
        # each matrix that is not a header hence header=None
        self.prediction = []
        for i in range(0, 13):
            df = pd.read_csv(StringIO.StringIO(data.split("\n\n")[i]),
                    header=None, sep='\t', skiprows=1, index_col=0)

            if all(df.apply(lambda x: abs(x.sum()-1) < 1e-12)) is False:
                print all(df.apply(lambda x: abs(x.sum()-1) < 1e-12))
                print('WARNING In Matrix %s, the sum over a column is not equal to 1!!' % (i+1))
                print df.sum()
            self.prediction.append(df)

    def download_template(self):
        filename = self._pj([self.classpath, 'templates',
            'D4C1_templates.txt'])
        return filename

    def download_goldstandard(self):
        return  self._pj([self.classpath, 'goldstandard',
            'D4C1_goldstandard.txt'])

    def _probability(self, X, Y, x):
        dx = X[1]-X[0]
        P = sum(Y[X <= x])*dx
        return P

    def _load_probability(self, tag):
        filename = self._pj([self.directory, 'pdf_%s.mat' % str(tag)])
        pdffile = scipy.io.loadmat(filename)
        return pdffile

    def score_kinases(self):

        pvals = {}
        mydists = {}
        for i in self._indices_kinases:
            # i+1 since the original matlab file starts at 1 (not 0)
            pdffile = self._load_probability(i+1)

            X = pdffile['X'][0]
            Y = pdffile['Y'][0]
            mydist = self._frobenius_norm()[i]
            pval = self._probability(X, Y, mydist)
            mydists[i] = mydist
            pvals[i] = pval

        self.results['kinase']['overall_score'] = -np.mean(np.log10(pvals.values()))
        self.results['kinase']['pvals'] = pvals
        self.results['kinase']['distances'] = mydists

    def score_pdz(self):

        pvals = {}
        mydists = {}
        for i in self._indices_pdz:
            # i+1 since the original matlab file starts at 1 (not 0)
            pdffile = self._load_probability(i+1)

            X = pdffile['X'][0]
            Y = pdffile['Y'][0]
            mydist = self._frobenius_norm()[i]
            pval = self._probability(X, Y, mydist)
            if pval < 1e-100:
                pval = 1e-100
            mydists[i] = mydist
            pvals[i] = pval

        self.results['pdz']['overall_score'] = -np.mean(np.log10(pvals.values()))
        self.results['pdz']['pvals'] = pvals
        self.results['pdz']['distances'] = mydists

    def score_sh3(self):
        all_pvals = []
        all_offsets = []
        for i in self._indices_sh3:
            # i+1 since the original matlab file starts at 1 (not 0)
            pdffile = self._load_probability(i+1)

            XX = pdffile['XX']
            YY = pdffile['YY']
            G = self.golddata[i]
            T = self.prediction[i]
            scores, offsets = self._slide(G, T)

            pvals = []
            for k, score in enumerate(scores):
                X = XX[:, k]
                Y = YY[:, k]

                pval = self._probability(X, Y, score)
                if pval < 1e-100:
                    pval = 1e-100
                pvals.append(pval)

            index = np.argmin(pvals)
            all_offsets.append(offsets[index])
            all_pvals.append(pvals[index])

        self.results['sh3']['overall_score'] = -np.mean(np.log10(all_pvals))
        self.results['sh3']['pvals'] = all_pvals
        self.results['sh3']['offset'] = all_offsets

    def _frobenius_norm(self):
        return [np.linalg.norm(self.golddata[i]-self.prediction[i])
                for i in range(0, 13)]

    def _init(self):
        self._download_data('pdf_1.mat', 'syn4552308')
        self._download_data('pdf_2.mat', 'syn4552309')
        self._download_data('pdf_3.mat', 'syn4552310')
        self._download_data('pdf_4.mat', 'syn4552311')
        self._download_data('pdf_5.mat', 'syn4552312')
        self._download_data('pdf_6.mat', 'syn4552313')
        self._download_data('pdf_7.mat', 'syn4552314')
        self._download_data('pdf_8.mat', 'syn4552315')
        self._download_data('pdf_9.mat', 'syn4552316')
        self._download_data('pdf_10.mat', 'syn4552317')
        self._download_data('pdf_11.mat', 'syn4552318')
        self._download_data('pdf_12.mat', 'syn4552319')
        self._download_data('pdf_13.mat', 'syn4552320')

    def _slide(self, G, T):
        # FIXME: this code could be simplified (two loops into 1 ?)
        # slide T relative to G
        #Here we manipulate the dataframe. The columns are labelled 1 to 10
        score = []
        offset = []
        t_stop = 10
        g_start = 1
        for t_start in [6, 5, 4, 3, 2, 1]:
            g_stop = 10 - t_start + 1

            idx_t = range(t_start, t_stop+1)
            idx_g = range(g_start, g_stop+1)

            # matrix of element distances
            d = G[idx_g].values - T[idx_t].values

            # frob norm
            f = np.linalg.norm(d)

            # %% number of overlapping rows
            overlap = len(idx_t)

            # remember realtive position
            offset.append(g_start - t_start)

            # remember score
            score.append(f)

        # last position is complete overlap

        # continue sliding T relative to G
        t_start = 1
        g_stop = 10
        for t_stop in range(9, 5-1, -1):
            g_start = 10 - t_stop + 1

            idx_t = range(t_start, t_stop+1)
            idx_g = range(g_start, g_stop+1)

            # matrix of element distances
            d = G[idx_g].values - T[idx_t].values

            # frob norm
            f = np.linalg.norm(d)

            # number of overlapping rows
            overlap = len(idx_t)

            # remember realtive position
            offset.append(g_start - t_start)

            # remember score
            score.append(f)

        return score, offset

