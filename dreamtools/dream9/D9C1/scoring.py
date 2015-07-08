
"""

Based on https://github.com/Sage-Bionetworks/DREAM9_Broad_Challenge_Scoring/
and instructions and communications from Mehmet Gonen.

Original code in R. Translated to Python by Thomas Cokelaer

"""
import os
import StringIO

from dreamtools.core.challenge import Challenge
import pandas as pd

class D9C1(Challenge):
    """A class dedicated to D9C1 challenge


    ::

        from dreamtools import D9C1
        s = D9C1()
        filename = s.download_template() 
        s.score(filename) 


    For consistency, all gene essentiality and genomic data files will be given in 
    the same gct file format.

    Briefly, this means:

    The first and second lines contains the version string and numbers indicating the 
    size of the data table that is contained in the remainder of the file::

        #1.2
        (# of data rows) (tab) (# of data columns)

    The third line contains a list of identifiers for the samples associated with 
    each of the columns in the remainder of the file::
    
        Name (tab) Description (tab) (sample 1 name) (tab) (sample 2 name) (tab) ... (sample N name)

     And the remainder of the data file contains data for each of the genes. 
     There is one line for each gene and one column for each of the samples. 
     The first two fields in the line contain name and descriptions for the genes 
     (names and descriptions can contain spaces since fields are separated by tabs). 
     The number of lines should agree with the number of data rows specified on line 2.:

        (gene name) (tab) (gene description) (tab) (col 1 data) (tab) (col 2 data) (tab) ... (col N data)


    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D9C1, self).__init__('D9C1')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self._init()
        self.sub_challenges = ['sc1','sc3','sc2']

    def _read_gct(self, filename):
        gct = pd.read_csv(filename, sep='[ \t]',  skiprows=2, engine='python')
        gct.drop(['Description'], axis=1, inplace=True)
        gct.set_index('Name', inplace=True)
        gct.columns = [x.strip() for x in gct.columns]
        return gct


    def _init(self):
        # should download files from synapse if required.
        self._download_data('D9C1_goldstandard.gct.zip', 'syn4595275')

        # now unzip and read the gs on the go
        from dreamtools.core.ziptools import ZIP
        z = ZIP()
        z.loadZIPFile(self.get_pathname('D9C1_goldstandard.gct.zip'))
        data = z.read('D9C1_goldstandard.gct')
        self.goldstandard = pd.read_csv(StringIO.StringIO(data), sep='[ \t]', 
                skiprows=2, engine='python')
        self.goldstandard.drop(['Description'], axis=1, inplace=True)
        self.goldstandard.set_index('Name', inplace=True)
        self.goldstandard.columns = [x.strip() for x in self.goldstandard.columns]

        # get template for SC1A
        self._download_data('D9C1_template_sc1.gct.zip', 'syn4595283')
        self.unzip('D9C1_template_sc1.gct.zip')

        filename = self._pj([self._path2data, 'goldstandard', 'D9C1_goldstandard_sc2.txt'])
        self.gs_priority = pd.read_csv(filename, sep='\t', header=None)

    def _read_feature(self, filename):
        return pd.read_csv(filename, sep='\t', header=None)

    def score(self, filename, subname=None):
        self._check_subname(subname)
        if subname == 'sc1':
            return self._score_sc1(filename)
        elif subname == 'sc2':
            return self._score_sc2(filename)
        elif subname == 'sc3':
            return self._score_sc3(filename)

    def _score_sc1(self, filename):
        self.prediction = self._read_gct(filename)
        assert all(self.goldstandard.columns == self.prediction.columns)
        assert self.goldstandard.shape == self.prediction.shape

        scores = []
        # two aliases
        df1 = self.goldstandard
        df2 = self.prediction
        N = len(df1)

        # a bit slow (10 seconds)
        scores = [df1.ix[i].corr(df2.ix[i], method='spearman') for i in range(0, N)]

        final_score = sum(scores)/float(len(scores))
        return {'score': final_score}

    def _score_sc2(self, filename):
        self.prediction = self._read_gct(filename)
        assert all(self.goldstandard.columns == self.prediction.columns)
        assert self.goldstandard.shape == self.prediction.shape

        # in SC2, only a subset of predictive features (2647 out of 17.000) are used
        df1 = self.goldstandard.ix[s.gs_priority[0]

        scores = []
        df2 = self.prediction
        N = len(df1)
        
        scores = [df1.ix[i].corr(df2.ix[i], method='spearman') for i in range(0, N)]

        final_score = sum(scores)/float(len(scores))
        return {'score': final_score}


        #0.003495996

    def _score_sc3(self, filename):
        raise NotImplementedError

    def download_template(self, subname=None):
        # should return full path to a template file
        self._check_subname(subname)
        if subname == 'sc1':
            return self.get_pathname('D9C1_template_sc1.gct')

    def download_goldstandard(self, subname=None):
        # should return full path to a gold standard file
        return self.get_pathname('D9C1_goldstandard.gct.zip')










