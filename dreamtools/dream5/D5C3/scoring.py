"""

Based on DREAM5_Challenge3A_Evaluation().
from Gustavo A. Stolovitzky,  Robert Prill, Ph.D.
sub challenge B original code in R from A. de la Fuente

"""
import os
import random
from dreamtools.core.challenge import Challenge
import pandas as pd
import numpy as np
from dreamtools.core.rocs import D3D4ROC

class D5C3(Challenge, D3D4ROC):
    """A class dedicated to D5C3 challenge


    ::

        from dreamtools import D5C3
        s = D5C3()
        filename = s.download_template() 
        s.score(filename) 

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D5C3, self).__init__('D5C3')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self._init()
        self.sub_challenges = []
        self.N_pvalues = 10

    def _init(self):
        # should download files from synapse if required.
        # The templates
        self._download_data('DREAM5_SysGenA100_myteam_Network1.txt', 'syn4561478')
        self._download_data('DREAM5_SysGenA100_myteam_Network2.txt', 'syn4561482')
        self._download_data('DREAM5_SysGenA100_myteam_Network3.txt', 'syn4561486')
        self._download_data('DREAM5_SysGenA100_myteam_Network4.txt', 'syn4561489')
        self._download_data('DREAM5_SysGenA100_myteam_Network5.txt', 'syn4561493')

        # Get goldstandard and unpack zipped files
        self._download_data('D5C3_goldstandard.zip', 'syn4561554')
        self.unzip('D5C3_goldstandard.zip')

        # the probabilities
        self._download_data('D5C3_probabilities.zip', 'syn4562041')
        self.unzip('D5C3_probabilities.zip')
        
    def download_template(self, subname):
        # should return full path to a template file
        if subname == 'A':
            print('There were 15 combo of network and number of RILS.')
            print('Here is one of them for 100 RILS and network 1. ')
            print('Other files are in the same directory')
            return self.get_pathname('DREAM5_SysGenA100_myteam_Network1.txt')
        elif subname == 'B':
            filenames = [] 
            for tag in [1, 2, 3]:
                filename = 'DREAM5_SysGenB%s_your_Predictions.txt' % tag
                filename = self._pj([self._path2data, 'templates', filename])
                filenames.append(filename)
            return filenames
        else: 
            raise ValueError('Sub challenge must be either A or B')

    def download_goldstandard(self, subname):
        # should return full path to a gold standard file
        raise NotImplementedError

    def _load_network(self, filename):
        df = pd.read_csv(filename, header=None, sep='[ \t]', engine='python')
        df[0] = df[0].apply(lambda x: x.replace('g','').replace('G',''))
        df[1] = df[1].apply(lambda x: x.replace('g','').replace('G',''))
        df = df.astype(float) # imoprtant for later to check for equality
        return df

    def score(self, filename, subchallenge):
        if subchallenge == 'A':
            return self.score_challengeA(filename)
        elif subchallenge == 'B':
            return self.score_challengeB(filename)
        else:
            raise ValueError('Sub challenge must be either A or B')

    def score_challengeA(self, filename):
        raise NotImplementedError
        # gold standard edges only
        goldfile = self.get_pathname('DREAM5_SysGenA100_Edges_Network1.tsv')

        # predicted edges
        predictionfile = self.get_pathname('DREAM5_SysGenA100_myteam_Network1.txt')
        predictionfile = filename

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

        test = list(newtest['2_x'])
        gold_index = list(newtest['2_y'])

        AUC, AUROC, prec, rec, tpr, fpr = self.get_statistics(self.gold_edges, 
                                        self.prediction, gold_index)

        p_auroc = self._probability(self.pdf_data['auroc_X'][0], 
                self.pdf_data['auroc_Y'][0], AUROC)
                
        p_aupr = self._probability(self.pdf_data['aupr_X'][0], 
                self.pdf_data['aupr_Y'][0], AUC)

        return AUC, AUROC, prec, rec, tpr, fpr, p_auroc, p_aupr

    def score_challengeB(self, filenames):
        # Ideally provide 3 filenames but if only 1 is given, try
        # to infer the names of the 2 others
        cor_pheno1 = []
        cor_pheno2 = []
        pval_pheno1 = []
        pval_pheno2 = []
        scores = []
        from dreamtools.core.rtools import RTools
        rtool = RTools(verboseR=False)

        assert len(filenames) == 3, "Must provide 3 files"

        self.golds = []
        self.preds = []
        for tag in [1,2,3]:
            filename = 'DREAM5_SysGenB%s_TestPhenotypeData.txt' % tag
            filename = self._pj([self._path2data, 'goldstandard', filename])
            gold = pd.read_csv(filename, sep='[ \t]', engine='python')
            self.golds.append(gold)

            #filename = 'DREAM5_SysGenB%s_your_Predictions.txt' % tag
            #filename = self._pj([self._path2data, 'data', filename])
            filename = filenames[tag-1]
            pred1 = pd.read_csv(filename, sep='[ \t]', engine='python')
            self.preds.append(pred1)

            # correlation gs versus predicted
            rtool.session.t = pred1.ix[0].values
            rtool.session.g = gold.ix[0].values
            rtool.session.run("results = cor.test(t, g, method='spearman', alternative='greater')")
            T1 = rtool.session.results.copy()
    
            rtool.session.t = pred1.ix[1].values
            rtool.session.g = gold.ix[1].values
            rtool.session.run("results = cor.test(t, g, method='spearman', alternative='greater')")
            T2 = rtool.session.results.copy()
            cor_pheno1.append(T1['estimate'])
            cor_pheno2.append(T2['estimate'])
            pval_pheno1.append(T1['p.value'])
            pval_pheno2.append(T2['p.value'])

            score = -(np.log(T1['p.value']) + np.log(T2['p.value']))
            scores.append(score)

        self.corp1 = cor_pheno1
        self.corp2 = cor_pheno2
        self.pval1 = pval_pheno1
        self.pval2 = pval_pheno2
        self.scores = scores


        # This part now compute the pvalues using random prediction
        random_scores = {0:[],1:[],2:[]}

        from easydev import Progress
        pb = Progress(self.N_pvalues, interval=1)
        
        for ii in range(1, self.N_pvalues):
            for tag in [0,1,2]:
                #generate random coordinates
                coord = random.sample(['RIL%s' % i for i in range(1,31)], 30)
                coord2 = random.sample(['RIL%s' % i for i in range(1,31)], 30)

                # Obtaining random scores
                rtool.session.t = self.preds[tag].ix[0].ix[coord].values
                rtool.session.g = self.golds[tag].ix[0].values
                rtool.session.run("results = cor.test(t, g, method='spearman', alternative='greater')")
                T1 = rtool.session.results.copy()
                rtool.session.t = self.preds[tag].ix[1].ix[coord2].values
                rtool.session.g = self.golds[tag].ix[1].values
                rtool.session.run("results = cor.test(t, g, method='spearman', alternative='greater')")
                T2 = rtool.session.results.copy()

                random_scores[tag].append(-(np.log(T1['p.value']) + np.log(T2['p.value'])))
            pb.animate(ii+1)
        self.random_scores = random_scores 
        #Obtaining p-values
        pvals = [sum(self.random_scores[k]>= self.scores[k])/float(self.N_pvalues) for k in [0,1,2]]
        self.pvals = pvals


        df = pd.DataFrame({'scores':self.scores, 
            'correlation_phenotype1':cor_pheno1,
            'correlation_phenotype2':cor_pheno2,
            'pvalues_phenotype1':pval_pheno1,
            'pvalues_phenotype2':pval_pheno2,
            'pvalues':self.pvals})
        df= df.T
        df.columns = ['SysGenB1', 'SysGenB2', 'SysGenB3']

        return df
