"""

The algorithm was developed by Gustavo Stolovitzky and originally implemented by Bernd Jagla in Matlab.

"""
import os
from dreamtools.core.challenge import Challenge
import pandas as pd
from dreamtools.core.rocs import D3D4ROC, DREAM2


class D2C2(Challenge, D3D4ROC, DREAM2):
    """A class dedicated to D2C2 challenge

    ::

        from dreamtools import D2C2
        s = D2C2()
        filename = s.download_template() 
        s.score(filename) 

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D2C2, self).__init__('D2C2')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self._init()
        self.sub_challenges = []

    def _init(self):
        # should download files from synapse if required.
        pass

    def download_template(self, subname=None):
        return self._pj([self._path2data, 'templates', 'D2C2_template.txt'])

    def download_goldstandard(self, subname=None):
        return  self._pj([self._path2data, 'goldstandard', 
            'D2C2_goldstandard.txt'])

    def score(self, filename, subname=None):
        gold = self.download_goldstandard(subname)
        prediction = filename

        self.gold_edges =  pd.read_csv(gold, sep='\t', header=None)
        self.prediction =  pd.read_csv(prediction, sep='\t', header=None)
        newtest = pd.merge(self.prediction, self.gold_edges, how='inner', on=[0,1])


        test = list(newtest['2_x'])
        gold_index = list(newtest['2_y'])

        AUC, AUROC, prec, rec, tpr, fpr = self.get_statistics(self.gold_edges, 
            self.prediction, gold_index)

        # specific precision values
        P = self.gold_edges[2].sum()
        spec_prec = self.compute_specific_precision_values(P, rec)

        # for plotting
        self.metrics = {'AUPR':AUC, 'AUROC':AUROC ,
            'tpr':  tpr, 'fpr':  fpr,
            'rec':  rec, 'prec':  prec,
            'precision at nth correct prediction':  spec_prec}

        results = {'AUPR':AUC, 'AUROC':AUROC }
        results['precision at nth correct prediction'] = spec_prec

        return results





