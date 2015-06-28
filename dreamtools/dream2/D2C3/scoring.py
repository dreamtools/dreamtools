
import os
from dreamtools.core.challenge import Challenge
import pandas as pd
from dreamtools.core.rocs import D3D4ROC


class D2C3(Challenge, D3D4ROC):
    """A class dedicated to D2C3 challenge


    ::

        from dreamtools import D2C3
        s = D2C3()
        filename = s.download_template() 
        s.score(filename) 

    There are 12 gold standards and therefore 12 possible submissions.
    6 for the chip case and 6 for the qPCR. Those should be scored independently.
    THere is no sub-challenge per se. 

    This class works for the DIRECTED-SIGNED_EXCITATORY_chip case only but implementation
    for other cases is straightforward.

    """
    def __init__(self):
        """.. rubric:: constructor"""
        super(D2C3, self).__init__('D2C3')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self._init()
        self.sub_challenges = []

    def _init(self):
        # should download files from synapse if required.
        pass

    def download_goldstandard(self, subname=None):
        print("This is just one instance amongst 12 other filenames to be found in the same directory")
        gold = self._pj([self._path2data, 'goldstandard', 
            'D2C3_goldstandard_DIRECTED-SIGNED_EXCITATORY_chip.txt'])
        return gold

    def download_template(self, subname=None):
        print("This is just one instance amongst 12 other filenames to be found in the same directory")
        filename = 'D2C3_templates_DIRECTED-SIGNED_EXCITATORY_chip.txt'
        return self._pj([self._path2data, 'templates', filename])

    def score(self, filename, subname=None, goldstandard=None):
        if goldstandard is None:
            raise ValueError("GS must be provided with --goldstandard")

        self.gold_edges =  pd.read_csv(goldstandard, sep='\t', header=None)
        self.prediction =  pd.read_csv(filename, sep='\t', header=None)
        newtest = pd.merge(self.prediction, self.gold_edges, how='inner', on=[0,1])

        test = list(newtest['2_x'])
        gold_index = list(newtest['2_y'])

        AUC, AUROC, prec, rec, tpr, fpr = self.get_statistics(self.gold_edges, 
            self.prediction, gold_index)

        results = {'AUPR':AUC, 'AUROC':AUROC}

        # specific precision values
        P = self.gold_edges[2].sum()
        spec_prec = {}
                                                          
        for x in [1, 2, 5]:
            if x > P:
                break
            rec0 = x / float(P)
            i = rec.index(rec0)
            spec_prec[x] = rec[i]
        results['precision a nth correct prediction'] = spec_prec

        return results
