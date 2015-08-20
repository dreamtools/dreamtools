"""


Original scoring function: Kelly Norel
"""
import os
from dreamtools.core.challenge import Challenge
import pandas as pd


__all__ = ['D6C4']


class D6C4(Challenge):
    """A class dedicated to D6C4 challenge


    ::

        from dreamtools import D6C4
        s = D6C4()
        filename = s.download_template()
        s.score(filename)

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self):
        """.. rubric:: constructor"""
        super(D6C4, self).__init__('D6C4')
        self._init()
        self.sub_challenges = []

    def download_template(self):
        # should return full path to a template file
        filename = self.getpath_template('D6C4_template.txt')
        return filename

    def download_goldstandard(self):
        # should return full path to a gold standard file
        filename = self.getpath_gs('D6C4_goldstandard.txt')
        return filename

    def _init(self):

        # Reads the test file with missing values
        df = pd.read_csv(self._pj([self.classpath, 'data', 'AMLTraining.csv']),
                index_col=0)
        df.fillna('none', inplace=True)

        testset = df.SampleNumber[df.Label == 'none'].unique()

        testsetIndex = [df.SampleNumber[df.SampleNumber == x].index[0] for x in
                testset]


        # Read the test with all values
        # let us set the index with first column (FCSFileName)
        filename = self._pj([self.classpath, 'goldstandard', 'AML.csv'])
        gs = pd.read_csv(filename, index_col=0, 
                sep=',')
        # let us keep only the relevant data (test set)
        gs = gs.ix[testsetIndex]
        assert sum(gs.Label == 'aml') == 20

        # we can drop the tube number
        gs = gs[['SampleNumber', 'Label']]
        gs = gs.replace('normal', 0)
        gs = gs.replace('aml', 1)
        self.gs = gs

    def _read_submission(self, filename):
        sub = pd.read_csv(filename, sep='\t', header=None,
                names=['SampleNumber', 'Label'])
        return sub

    def score(self, filename):

        sub = self._read_submission(filename)
        df = pd.merge(self.gs, sub, on='SampleNumber')
        df.drop(['SampleNumber'], axis=1, inplace=True)

        # Label_x is the class vector
        # label_y is the score vector

        self.df = df

        results = {}
        results['pearson'] = df.corr()['Label_x']['Label_y']

        # The Precision of the predictions, defined as the
        # fraction of correct AML patients amongst the first 20 predictions.
        prec = df.sort('Label_y', ascending=False)['Label_x'][0:20]
        results['precision'] = sum(prec)/20.

        # The Recall of the predictions, defined as the proportion of AML
        # patients in the first 20 predictions out of all the AML 
        # patients in the cohort.

        # TODO seems to be identicl to prec
        # at least on the official LB
        # https://www.synapse.org/#!Synapse:syn2887788/wiki/72181
        results['recall'] = sum(prec)/20.

        #MCC: The Matthews Correlation Coefficient is a measure of the quality
        #of binary classifications. It takes into account true and false
        #positives and negatives and is generally regarded as a balanced measure
        #which can be used even if the classes are of very different sizes. For
        #its mathematical definition see
        #http://en.wikipedia.org/wiki/Matthews_correlation_coefficient
        from dreamtools.core.rocs import MCC
        N = 180
        T = 20
        TP = sum(prec)
        FP = T - TP
        FN = FP  # symmetric
        TN = N - T - FP
        results['MCC'] = MCC(TP, TN, FP, FN)


        # Finally the JSC (jaccard)
        try:
            from sklearn.metrics import jaccard_similarity_score as JSC
            true = df.sort('Label_y', ascending=False)['Label_x'].values
            pred = df.sort('Label_y', ascending=False)['Label_y'].values
            results['JSC'] = JSC(true[0:20], pred.round()[0:20])
            # TODO: this is not exactly the same as in the LB
        except:
            print('Install scikit-learn for the Jaccard similarity')

        return results











