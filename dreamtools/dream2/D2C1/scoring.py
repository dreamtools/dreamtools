"""


Based on matlab code from
Gustavo A. Stolovitzky, Ph.D.
Bernd Jagla, Ph.D.

"""
import pandas as pd
import numpy as np
import os
from dreamtools.core.challenge import Challenge


class D2C1(Challenge):
    def __init__(self):
        super(D2C1, self).__init__('D2C1')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self.decoys = pd.read_excel(self.get_data("BCL6_targets_and_decoys.xls"))

    def get_data(self, filename):
        filename = self._path2data + os.sep + "data" + os.sep +"BCL6_targets_and_decoys.xls"
        return filename

    def _create_templates(self, filename='test_BCL6targets.txt'):
        templates = self.decoys.copy()
        templates['scores'] = np.random.random(200)
        df = templates[['Entrez GeneID', 'scores']]

        df = df.sort(columns=['scores'], ascending=[False])
        df.to_csv(filename, sep='\t', header=None, index=False)

    def download_template(self):
        return self._pj([self._path2data, 'templates', 'D2C1_template.tsv'])

    def score(self, filename):
        # SEE one of later challenges. Same methodology!
        # gold standard edges only
        goldfile = self.get_pathname('DREAM5_SysGenA100_Edges_Network1.tsv')

        # predicted edges
        #predictionfile = self.get_pathname('DREAM5_SysGenA100_myteam_Network1.txt')
        #predictionfile = filename

        # precomputed probability densities for various metrics
        pdffile_aupr  = self.get_pathname('A100_Network1_AUPR.mat')
        pdffile_auroc = self.get_pathname('A100_Network1_AUROC.mat')

        # load gold standard
        self.gold_edges = self._load_network(goldfile)

        # load predictions
        self.prediction = self._load_network(predictionfile)

        # load probability densities
        self.pdf_aupr  = self.loadmat(pdffile_aupr)
        self.pdf_auroc = self.loadmat(pdffile_auroc)

        # 
        newtest = pd.merge(self.prediction, self.gold_edges, how='inner', on=[0,1])




















        
