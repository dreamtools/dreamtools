import os
from dreamtools.core.challenge import Challenge
from easydev import shellcmd
import pandas as pd


class D7C4(Challenge):
    """A class dedicated to D7C4 challenge

    ::

        from dreamtools import D7C4
        s = D7C4()
        filename = s.download_template() 
        s.score(filename) 

    Data and templates are downloaded from Synapse. You must have a login.

    ::

        # columns represent the probablisitic c-index of the given team for each drug.
        # following the columns of teams are 5 columns which are used for calculating the overall team score
        # |-> Test_data = the probabalistic c-index for the experimentally determined test data scored against itself
        # |-> Mean Null Distribution = a set of 10,000 random predictions were scored to create the null distribution, of which this column represents the mean
        # |-> SD Null Distribution = a set of 10,000 random predictions were scored to create the null distribution, of which this column represents the standard deviation
        # |-> z-score of test data to null = score of the test data minus the mean of the null distribution divided by the standard deviation of the null distribution
        # |-> weight of drug (normalized z-score) = the z-score normalized by the largest z-score across all 31 drugs.
        # to calculate your team overall score, simply mulitple the score of all drugs by the corresponding weight.  Divide the sum of these weighted scores by the sum of the weights


    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D7C4, self).__init__('D7C4')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]

    def download_template(self):
        filename = self._pj([self._path2data, 'templates', 'D7C4_template.csv'])
        return filename

    def score(self, filename):
        from easydev import TempFile
        fh = TempFile()
        script = self._pj([self._path2data, 'weighted_average_concordance_index.pl'])
        datadir = self._pj([self._path2data, 'data'])
        cmd = "perl %s %s %s %s"
        cmd = cmd % (script, filename, datadir , fh.name)

        shellcmd(cmd, verbose=True, ignore_errors=True)
        df = pd.read_csv(fh.name, sep='\t', header=None)
        df.columns = ['DrugID','probabalistic c-index',	'weighted probabalistic c-index']
        df = df.set_index('DrugID')
        fh.delete()
        return {'c-index': df.mean()}
