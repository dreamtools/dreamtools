"""

original code in MATLAB by gustavo Stolovitzky

"""
import os
from dreamtools.core.challenge import Challenge
import pandas as pd
from dreamtools.core.rocs import D3D4ROC, DREAM2


class D2C4(Challenge, D3D4ROC, DREAM2):
    """A class dedicated to D2C4 challenge


    ::

        from dreamtools import D2C4
        s = D2C4()
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
        super(D2C4, self).__init__('D2C4')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self._init()

        # although there is no sub challenges per se,
        # 12 different GS were used to score 12 types
        # of network. We use those TAGS 
        self.sub_challenges = []
        for name in ['InSilico1', 'InSilico2', 'InSilico3']:
            self.sub_challenges.append('DIRECTED-UNSIGNED_%s' %name)
            self.sub_challenges.append('UNDIRECTED-UNSIGNED_%s' %name)
            self.sub_challenges.append('UNDIRECTED-SIGNED_EXCITATORY_%s' %name)
            self.sub_challenges.append('UNDIRECTED-SIGNED_INHIBITORY_%s' %name)
            self.sub_challenges.append('DIRECTED-SIGNED_EXCITATORY_%s' %name)
            self.sub_challenges.append('DIRECTED-SIGNED_INHIBITORY_%s' %name)

    def _init(self):
        # should download files from synapse if required.
        self._download_data('D2C4_goldstandard.zip', 'syn4565570')
        self.unzip('D2C4_goldstandard.zip')

    def download_goldstandard(self, subname=None):
        self._check_subname(subname)
        gold = self.get_pathname('D2C4_goldstandard_%s.txt' % subname)
        return gold

    def download_template(self, subname=None):
        # not template found when developing this code.
        # We will use the GS instead
        msg = "! Note that there is no template per se. Here is the "
        msg += "goldstandard that would work as well."
        print(msg)

        self._check_subname(subname)
        return self.download_goldstandard(subname)

    def score(self, filename, subname=None, goldstandard=None):
        if goldstandard is None:
            goldstandard = self.download_goldstandard(subname)

        self.gold_edges =  pd.read_csv(goldstandard, sep='\t', header=None)
        self.prediction =  pd.read_csv(filename, sep='\t', header=None)
        newtest = pd.merge(self.prediction, self.gold_edges, how='inner', on=[0,1])

        test = list(newtest['2_x'])
        gold_index = list(newtest['2_y'])

        AUC, AUROC, prec, rec, tpr, fpr = self.get_statistics(self.gold_edges, 
            self.prediction, gold_index)

        P = self.gold_edges[2].sum()
        spec_prec = self.compute_specific_precision_values(P, rec)

        # for plotting
        self.metrics = {'AUPR':AUC, 'AUROC':AUROC ,
            'tpr':  tpr, 'fpr':  fpr,
            'rec':  rec, 'prec':  prec,
            'precision at nth correct prediction': spec_prec}

        results = {'AUPR':AUC, 'AUROC':AUROC }
        results['precision at nth correct prediction'] =spec_prec
        return results

