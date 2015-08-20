"""D3C1 scoring function


Original matlab code from Gustavo A. Stolovitzky and Robert Prill.

"""
import numpy as np
from dreamtools.core.challenge import Challenge
import pandas as pd

__all__ = ["D3C1"]


class D3C1(Challenge):
    """D3C1 scoring function to evaluate the accuracy of a prediction

    ::

        from dreamtools import D3C1
        s = D3C1()
        filename = s.download_template()
        s.score(filename)
    """

    def __init__(self):
        Challenge.__init__(self, "D3C1")
        # read data required for the scoring.
        self._init()

    def _init(self):
        self._load_proba()
        self.G = self._read_challenge1_file(self.download_goldstandard())

    def download_goldstandard(self):
        filename = "D3C1_goldstandard.txt"
        filename = self._pj([self.classpath, 'goldstandard', filename])
        return filename

    def score(self, filename):
        """Scoring function

        :return: tuple with first element being the number of correct
            predictions and second element being the pvalue

        """
        data = self._read_challenge1_file(filename)
        #  add-up the correct predictions
        num_correct = np.logical_and(self.G == 1, data==1).sum().sum()
        pval = self.probability(num_correct)
        return num_correct, pval

    def _read_challenge1_file(self, filename):
        d = pd.read_csv(filename, sep="\t", index_col=0)
        assert d.shape == (4, 7), 'Problem parsing file'
        return d

    def _load_proba(self):
        """load the probability density (really a prob mass function for this
        challenge)"""
        # There is a matlab file called data/PDF_SignalingCascadeChallenge.mat
        # but it appears to be very simple so it is hardcoded here below
        self.X = np.array([0, 1, 2, 3, 4])
        self.Y = np.array([0.55357143,  0.33809524,  0.09285714,  0.01428571,
            0.00119048])
        # 4 proteins, 7 assignements. P(4 correct) = 1/ (7*6*5*4)
        # P3 = C^4_1, P2 = C^4_2, P1 = C^4_3, P0 = ...

    def probability(self, x):
        dx = self.X[2] - self.X[1]
        return sum( np.double(self.X>=x) * self.Y * dx )

    def download_template(self):
        """Return filename of a template to be used for testing"""
        filename = self._pj([self.classpath, 'templates', 'D3C1_template.txt'])
        return filename

