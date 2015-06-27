
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

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D2C3, self).__init__('D2C3')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self._init()
        self.sub_challenges = []

    def _init(self):
        # should download files from synapse if required.
        pass

    def score(self, prediction_file):
        raise NotImplementedError

    def download_goldstandard(self):
        # should return full path to a gold standard file
        raise NotImplementedError

    def download_template(self):
        filename = 'D2C3_templates_DIRECTED-SIGNED_EXCITATORY_FiveGene_chip.txt'
        return self._pj([self._path2data, 'templates', filename])

    def score(self, filename):
        gold = self._pj([self._path2data, 'goldstandard', 
            'GoldStandard_DIRECTED-SIGNED_EXCITATORY_FiveGene_chip.txt'])
        prediction = filename

        self.gold_edges =  pd.read_csv(gold, sep='\t', header=None)
        self.prediction =  pd.read_csv(prediction, sep='\t', header=None)
        newtest = pd.merge(self.prediction, self.gold_edges, how='inner', on=[0,1])

        test = list(newtest['2_x'])
        gold_index = list(newtest['2_y'])

        AUC, AUROC, prec, rec, tpr, fpr = self.get_statistics(self.gold_edges, 
            self.prediction, gold_index)

        #p_auroc = self._probability(self.pdf_data['auroc_X'][0], 
        #    self.pdf_data['auroc_Y'][0], AUROC)
                                                
        #p_aupr = self._probability(self.pdf_data['aupr_X'][0], 
        #    self.pdf_data['aupr_Y'][0], AUC)

        #return AUC, AUROC, prec, rec, tpr, fpr
        #p_auroc, p_aupr

        results = {'AUPR':AUC, 'AUROC':AUROC}

        return results
