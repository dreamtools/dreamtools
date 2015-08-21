"""D5C1 scoring function

From an original matlab code from Gustavo A. Stolovitzky, Robert Prill

"""
from dreamtools.core.challenge import Challenge
import pandas as pd
import numpy as np


__all__ = ["D5C1"]


class D5C1(Challenge):
    """A class dedicated to D5C1 challenge

    ::

        from dreamtools import D5C1
        s = D5C1()
        filename = s.download_template()
        s.score(filename)

    """
    def __init__(self):
        """.. rubric:: constructor"""
        super(D5C1, self).__init__('D5C1')
        self._init()
        self.sub_challenges = []

    def _init(self):
        # should download files from synapse if required.
        self._download_data('AUPR.mat', 'syn4560154')
        self._download_data('AUROC.mat', 'syn4560158')
        self._download_data('DREAM5_EAR_GoldStandard.tsv', 'syn4560182')
        self._download_data('DREAM5_EAR_myteam_Predictions.txt', 'syn4560167')

    def download_template(self):
        # should return full path to a template file
        return self.get_pathname('DREAM5_EAR_myteam_Predictions.txt')

    def download_goldstandard(self):
        # should return full path to a gold standard file
        return self.get_pathname('DREAM5_EAR_GoldStandard.tsv')

    def _load_proba(self):
        import scipy.io
        self.auroc = scipy.io.loadmat(self.get_pathname("AUROC.mat"))
        self.aupr = scipy.io.loadmat(self.get_pathname("AUPR.mat"))

    def score(self, filename):
        """

        :return: dictionay with AUC/AUPR metrics and score.


        """
        self._load_proba()
        prediction = pd.read_csv(filename, sep='[ \t]', engine='python', header=None)
        gold = pd.read_csv(self.download_goldstandard(), sep='[ \t]',
                engine='python', header=None)
        prediction.columns = ['sequence', 'value']
        gold.columns = ['sequence', 'value']

        # merge the prediction and gold based on the sequence.
        data = pd.merge(prediction, gold, how='inner', on=['sequence'],
                suffixes=['_pred', '_gold'])
        # sory by prediction
        data.sort(columns=['value_pred'], ascending=False, inplace=True)
        data.columns = ['Sequence', 'prediction_values', 'prediction']

        self.data = data

        from dreamtools.core.rocs import ROCDiscovery
        self.roc = ROCDiscovery(self.data['prediction'])
        self.roc.get_statistics()
        auroc = self.roc.compute_auc()
        aupr = self.roc.compute_aupr()

        P_AUPR = self._probability(self.aupr['X'][0], self.aupr['Y'][0], aupr)
        P_AUROC = self._probability(self.auroc['X'][0], self.auroc['Y'][0], auroc)

        score = np.mean(-np.log10([P_AUROC, P_AUPR]))

        return {'auroc':auroc, 'aupr':aupr, 'pval_aupr': P_AUPR,
                'pval_auroc':P_AUROC, 'score':score}

    def _probability(self, X, Y, x):
        dx = X[2] - X[1]
        return  sum( Y[X>=x] * dx )
