
"""

Based on https://github.com/Sage-Bionetworks/DREAM9_Broad_Challenge_Scoring/
and instructions and communications from Mehmet Gonen.

Original code in R. Translated to Python by Thomas Cokelaer

"""
import os
import StringIO

from dreamtools.core.challenge import Challenge
from dreamtools.core.ziptools import ZIP

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
        self._init()
        self.sub_challenges = ['sc1','sc3','sc2']

    def _init(self):
        # should download files from synapse if required.
        self._download_data('D9C1_goldstandard.gct.zip', 'syn4595275')

        # now unzip and read the gs on the go
        z = ZIP()
        z.loadZIPFile(self.get_pathname('D9C1_goldstandard.gct.zip'))
        data = z.read('D9C1_goldstandard.gct')
        self.goldstandard = pd.read_csv(StringIO.StringIO(data), sep='[ \t]',
                skiprows=2, engine='python')
        self.goldstandard.drop(['Description'], axis=1, inplace=True)
        self.goldstandard.set_index('Name', inplace=True)
        self.goldstandard.columns = [x.strip() for x in self.goldstandard.columns]

        # get template for SC1, SC2, SC3
        self._download_data('D9C1_template_sc1.gct.zip', 'syn4595283')
        self.unzip('D9C1_template_sc1.gct.zip')
        self._download_data('D9C1_template_sc2.zip', 'syn4595587')
        self._download_data('D9C1_template_sc3.zip', 'syn4595588')

        # download gold standard for sc2
        filename = self.getpath_gs( 'D9C1_goldstandard_sc2.txt')
        self.gs_priority = pd.read_csv(filename, sep='\t', header=None)

    def _read_gct(self, filename):
        if os.path.exists(filename):
            gct = pd.read_csv(filename, sep='[ \t]',  skiprows=2, engine='python')
        else:
            gct = pd.read_csv(StringIO.StringIO(filename),
                              sep='[ \t]',  skiprows=2, engine='python')
        gct.drop(['Description'], axis=1, inplace=True)
        gct.set_index('Name', inplace=True)
        gct.columns = [x.strip() for x in gct.columns]
        return gct

    def _read_feature(self, filename):
        if os.path.exists(filename):
            return pd.read_csv(filename, sep='\t', header=None)
        else:
            return pd.read_csv(StringIO.StringIO(filename),
                               sep='\t', header=None)

    def score(self, filename, subname=None):
        self._check_subname(subname)
        if subname == 'sc1':
            return self._score_sc1(filename)
        elif subname == 'sc2':
            return self._score_sc2_sc3(filename)
        elif subname == 'sc3':
            return self._score_sc2_sc3(filename)

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

    def _score_sc2_sc3(self, filename):
        # looks like exactly same function in sc2/sc3
        # feature file is not used either in original code ?!

        # this should be a zip file with 2 files.
        z = ZIP()
        z.loadZIPFile(filename)
        # there should be 2 files, one ending in gct one in txt
        assert len(z.filenames) == 2, "There should be 2 files in the zip archive"

        for filename in z.filenames:
            if filename.endswith('gct'):
                prediction = z.read(filename)
                prediction = self._read_gct(prediction)
            elif filename.endswith('txt'):
                feature = z.read(filename)
                feature = self._read_feature(feature)
                # first column should be the names
                feature.set_index(0, inplace=True)
            else:
                raise ValueError("there should be only 2 files. \n" +
                        "One ending with gct extension (prediction)\n" +
                        "One ending with txt extension (feature)")

        #assert feature.shape == (2647,10)
        assert prediction.shape == (2647,44)
        self.prediction = prediction
        self.feature = feature

        # in SC2, only a subset of predictive features (2647 out of 17.000) are used
        df1 = self.goldstandard.ix[self.gs_priority[0]]
        self.df1 = df1
        scores = []
        df2 = self.prediction
        N = len(df1)
        scores = [df2.ix[i].corr(df1.ix[i], method='spearman') for i in range(0, N)]
        self.scores = scores
        final_score = sum(scores)/float(len(scores))
        return {'score': final_score}


    def download_template(self, subname=None):
        # should return full path to a template file
        self._check_subname(subname)
        if subname == 'sc1':
            return self.get_pathname('D9C1_template_sc1.gct')
        elif subname == 'sc2':
            return self.get_pathname('D9C1_template_sc2.zip')
        elif subname == 'sc3':
            return self.get_pathname('D9C1_template_sc3.zip')

    def download_goldstandard(self, subname=None):
        # should return full path to a gold standard file
        return self.get_pathname('D9C1_goldstandard.gct.zip')


