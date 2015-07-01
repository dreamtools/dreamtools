"""D2C2 scoring function

:Title: DREAM2 - BCL6 Transcriptional Target Prediction
:Nickname: D2C1
:Summary: Predict the genes for transcription factor binding.
:SubChallenges: None
:Synapse page: https://www.synapse.org/#!Synapse:syn3034857

Implementation in Python based on a MATLAB code from
Gustavo A. Stolovitzky and Bernd Jagla.

"""
import pandas as pd
import numpy as np
import os
from dreamtools.core.challenge import Challenge
from dreamtools.core.rocs import D3D4ROC, DREAM2


class D2C1(Challenge, D3D4ROC, DREAM2):
    def __init__(self):
        super(D2C1, self).__init__('D2C1')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]

        filename = [self._path2data, "data", "BCL6_targets_and_decoys.xls"]
        filename = self._pj(filename)
        self.decoys = pd.read_excel(filename)

    def _create_templates(self, filename='test_BCL6targets.txt'):
        templates = self.decoys.copy()
        templates['scores'] = np.random.random(200)
        df = templates[['Entrez GeneID', 'scores']]

        df = df.sort(columns=['scores'], ascending=[False])
        df.to_csv(filename, sep='\t', header=None, index=False)

    def download_template(self):
        return self._pj([self._path2data, 'templates', 'D2C1_template.tsv'])

    def download_goldstandard(self):
        return  self._pj([self._path2data, 'goldstandard',
                             'D2C1_goldstandard.tsv'])

    def score(self, filename):
        """Returns statistics (e.g. AUROC)

        :param str filename: a valid filename as returned by
            :meth:`download_template`

        """
        # SEE one of later challenges. Same methodology!
        # gold standard edges only
        gold = self.download_goldstandard()

        # load predictions

        self.gold_edges = pd.read_csv(gold, sep='\t', header=None)
        self.prediction = pd.read_csv(filename,  sep='\t', header=None)

        #
        newtest = pd.merge(self.prediction, self.gold_edges,
                how='inner', on=[0])

        test = list(newtest['1_x'])
        gold_index = list(newtest['1_y'])

        AUC, AUROC, prec, rec, tpr, fpr = self.get_statistics(self.gold_edges,
                                            self.prediction, gold_index)

        # specific precision values
        P = self.gold_edges[1].sum()
        spec_prec = self.compute_specific_precision_values(P, rec)

        # for plotting
        self.metrics = {'AUPR':AUC, 'AUROC':AUROC ,
            'tpr':  tpr, 'fpr':  fpr,
            'rec':  rec, 'prec':  prec,
            'precision at nth correct prediction':  spec_prec}

        results = {'AUPR':AUC, 'AUROC':AUROC }

        results['precision at nth correct prediction'] = spec_prec

        return results






















