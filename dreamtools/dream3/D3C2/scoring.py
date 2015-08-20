"""D3C2 scoring function

Implemented after an original MATLAB code from Gustavo Stolovitzky and 
Robert Prill.

"""
from dreamtools.core.challenge import Challenge
import pandas as pd


class D3C2(Challenge):
    """A class dedicated to D3C2 challenge

    ::

        from dreamtools import D3C2
        s = D3C2()
        filename = s.download_template('cytokine')
        s.score(filename, 'cytokine')

        filename = s.download_template('phospho')
        s.score(filename, 'phospho')

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D3C2, self).__init__('D3C2')
        self.sub_challenges = ['phospho', 'cytokine']
        self._init()

    def _init(self):
        self._download_data('D3C2_proba_cytokine.mat', 'syn4555587')
        self._download_data('D3C2_proba_phospho.mat', 'syn4555588')

    def _check_sub_challenge_name(self, name):
        assert name in self.sub_challenges

    def download_template(self, name):
        self._check_sub_challenge_name(name)
        filename = self._pj([self.classpath, 'templates', 
            'D3C2_template_%s.txt' % name])
        return filename

    def download_goldstandard(self, subname):
        gs_filename = self._pj([self.classpath, 'goldstandard', 
            'D3C2_goldstandard_%s.txt' % subname])
        return gs_filename

    def score(self, filename, subname):
        """Returns score of a prediction"""
        self._check_sub_challenge_name(subname)

        gs_filename = self.download_goldstandard(subname)

        pdf_filename = self.get_pathname('D3C2_proba_%s.mat' % subname)
        # Read the probability density function that we computed 
        # (empirically) elsewhere
        # NOTE: This loads: X, Y, and C, where C is a constant that 
        # scales the pdf to the histogram
        temp = self.loadmat(pdf_filename)
        X = temp['X'][0]
        Y = temp['Y'][0]

        G = self._read_challenge_file(gs_filename)
        T = self._read_challenge_file(filename)

        # %% perform calculations
        score = self._performance_score(G,T)
        pval = self._probability(X, Y, score)

        return {'score':score, 'pvalue':pval}

    def _read_challenge_file(self, filename):
        df = pd.read_csv(filename, sep='\t')
        #ignore the cell type, stimulus, inhibitor and prediction time
        df = df[df.columns[4:]]
        return df

    def _probability(self, X, Y, x):
        return sum(Y[X <= x]) * (X[1] - X[0])

    def _performance_score(self, G, T):
        ACC = 300       # accuracy of the dector (lower limit of detection)
        GAMMA = 0.08    # coeff of variation (gamma) due to biological error

        numer = (G - T)**2
        denom = ACC**2 + (GAMMA * G)**2
        score = (numer/denom).sum().sum()
        return score

