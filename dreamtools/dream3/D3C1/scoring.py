"""
% Gustavo A. Stolovitzky, Ph.D.
% Robert Prill, Ph.D.
%
"""
import os
import numpy as np
from dreamtools.core.challenge import Challenge
import pandas as pd

__all__ = ["D3C1"]


class D3C1(Challenge):
    """D3C1 scoring function to evaluate the accuracy of a prediction 
    
    
    This is a Python implementation of the matlab code from  Gustavo A. Stolovitzky, Ph.D.
    Robert Prill, Ph.D. here
    https://www.synapse.org/#!Synapse:syn3033068/files/.
    The gold standard and example are provided within the D3C1 directory in
    dreamtools.


    ::

        from dreamtools import D3C1
        s = D3C1()
        filename = s.download_template()
        s.score(filename)
    """

    def __init__(self):
        Challenge.__init__(self, "D3C1")
        self._path2data = os.path.split(os.path.abspath(__file__))[0]

        # read data required for the scoring.
        self._load_proba()
        goldfile = "DREAM3GoldStandard_SignalingCascadeChallenge.txt"
        goldfile = self._path2data + os.sep + 'goldstandard' + os.sep + goldfile
        self.G = self.read_challenge1_file(goldfile)

    def score(self, filename):
        """

        :return: tuple with first element being the number of correct
            predictions and second element being the pvalue

        """
        data = self.read_challenge1_file(filename)
        #  add-up the correct predictions
        num_correct = np.logical_and(self.G == 1, data==1).sum().sum()
        pval = self.probability(num_correct)
        return num_correct, pval

    def read_challenge1_file(self, filename):
        d = pd.read_csv(filename, sep="\t", index_col=0)
    	assert d.shape == (4, 7), 'Problem parsing file'
        return d

    def _load_proba(self):
        """load the probability density (really a prob mass function for this
        challenge)"""
        # There is a matlab file called data/PDF_SignalingCascadeChallenge.mat
        # but it appears to be very simple so it is hardcoded here below
        # from scipy.io import loadmat;  temp = loadmat(pdffile)
        self.X = np.array([0,1,2,3,4])
        self.Y = np.array([0.55357143,  0.33809524,  0.09285714,  0.01428571,
            0.00119048])

    def probability(self,x):
    	dx = self.X[2] - self.X[1]
        P = sum( np.double(self.X>=x) * self.Y * dx )
        return P

    def get_template(self):
        """Return filename of a template to be used for testing"""
        filename = self._path2data + os.sep + 'templates' + os.sep 
        filename += 'example_SignalingCascadeChallenge.txt'
        return filename


