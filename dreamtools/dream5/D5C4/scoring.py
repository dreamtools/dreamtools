"""

Based on original matlab code from Gustavo A. Stolovitzky and Robert Prill


"""
import os
from dreamtools.core.challenge import Challenge
import pandas as pd
from dreamtools.core.rocs import D3D4ROC


class D5C4(Challenge, D3D4ROC):
    """A class dedicated to D5C4 challenge


    ::

        from dreamtools import D5C4
        s = D5C4()
        filename = s.download_template() 
        s.score(filename) 

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D5C4, self).__init__('D5C4')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self._init()
        self.sub_challenges = []

    def _init(self):
        # should download files from synapse if required.
        pass
        # Get goldstandard and unpack zipped files
        self._download_data('D5C4_goldstandard.zip', 'syn4564722')
        self.unzip('D5C4_goldstandard.zip')

        # the probabilities
        self._download_data('D5C4_probabilities.zip', 'syn4564719')
        self.unzip('D5C4_probabilities.zip')
        
        # the templates
        self._download_data('D5C4_templates.zip', 'syn4564726')
        self.unzip('D5C4_templates.zip')

    def _load_network(self, filename):
        df = pd.read_csv(filename, header=None, sep='[ \t]', engine='python')
        df[0] = df[0].apply(lambda x: x.replace('g','').replace('G',''))
        df[1] = df[1].apply(lambda x: x.replace('g','').replace('G',''))
        df = df.astype(float) # imoprtant for later to check for equality
        return df

    def download_template(self):
        # should return full path to a template file
        filenames = []
        for tag in [1,3,4]:
            filename = "DREAM5_NetworkInference_myteam_Network%s.txt" % tag
            filenames.append(self.get_pathname(filename))
        return filenames

    def download_goldstandard(self):
        # should return full path to a gold standard file
        filenames = []
        for tag in [1,3,4]:
            filename = "DREAM5_NetworkInference_Edges_Network%s.tsv" % tag
            filenames.append(self.get_pathname(filename))
        return filenames
    
    def score(self, filename):
        #goldfile = self.get_pathname('DREAM5_NetworkInference_Edges_Network1.tsv')
        goldfile = self.get_pathname('DREAM5_NetworkInference_Edges_Network1.tsv')

        # predicted edges
        #predictionfile = self.get_pathname('DREAM5_NetworkInference_myteam_Network1.txt')
        #predictionfile = 'templates/DREAM5_NetworkInference_myteam_Network1.txt'
        predictionfile = filename

        # precomputed probability densities for various metrics
        #pdffile_aupr  = self.get_pathname('A100_Network1_AUPR.mat')
        #pdffile_auroc = self.get_pathname('A100_Network1_AUROC.mat')
        pdffile_aupr  = self.get_pathname('Network1_AUPR.mat')
        pdffile_auroc = self.get_pathname('Network1_AUROC.mat')

        # load gold standard
        self.gold_edges = self._load_network(goldfile)

        # load predictions
        self.prediction = self._load_network(predictionfile)

        # load probability densities
        self.pdf_aupr  = self.loadmat(pdffile_aupr)
        self.pdf_auroc = self.loadmat(pdffile_auroc)

        newtest = pd.merge(self.prediction, self.gold_edges, how='inner', on=[0,1])

        test = list(newtest['2_x'])
        gold_index = list(newtest['2_y'])

        AUC, AUROC, prec, rec, tpr, fpr = self.get_statistics(self.gold_edges, 
                                        self.prediction, gold_index)

        p_auroc = self._probability(self.pdf_data['auroc_X'][0], 
                self.pdf_data['auroc_Y'][0], AUROC)
                
        p_aupr = self._probability(self.pdf_data['aupr_X'][0], 
                self.pdf_data['aupr_Y'][0], AUC)

        return AUC, AUROC, prec, rec, tpr, fpr, p_auroc, p_aupr
