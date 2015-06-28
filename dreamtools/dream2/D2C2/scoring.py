"""

The algorithm was developed by Gustavo Stolovitzky and originally implemented by Bernd Jagla in Matlab.

"""
import os
from dreamtools.core.challenge import Challenge
import pandas as pd
from dreamtools.core.rocs import D3D4ROC


class D2C2(Challenge, D3D4ROC):
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

    def download_template(self):
        return self._pj([self._path2data, 'templates', 'D2C2_template.txt'])

    def score(self, filename, subname=None, goldstandard=None):
        gold = self._pj([self._path2data, 'goldstandard', 'D2C2_goldstandard.txt'])
        prediction = filename

        self.gold_edges =  pd.read_csv(gold, sep='\t', header=None)
        self.prediction =  pd.read_csv(prediction, sep='\t', header=None)
        newtest = pd.merge(self.prediction, self.gold_edges, how='inner', on=[0,1])

        test = list(newtest['2_x'])
        gold_index = list(newtest['2_y'])

        AUC, AUROC, prec, rec, tpr, fpr = self.get_statistics(self.gold_edges, 
            self.prediction, gold_index)

        results = {'AUPR':AUC, 'AUROC':AUROC }

        # specific precision values
        P = self.gold_edges[2].sum()
        spec_prec = {}
        
        for x in [1, 2, 3, 20]:
            if x > P:
                break
            rec0 = x / float(P)
            i = rec.index(rec0)
            spec_prec[x] = rec[i]
        
        results['precision a nth correct prediction'] = spec_prec
        return results





