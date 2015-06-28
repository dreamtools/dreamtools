"""

Implementation in Python from Thomas Cokelaer.
Original code in matlab (Gustavo Stolovitzky and Robert Prill, Bernd Jagla).

"""
import os
from dreamtools.core.challenge import Challenge
import pandas as pd
import numpy as np
from dreamtools.core.rocs import D3D4ROC

class D3C4(Challenge, D3D4ROC):
    """A class dedicated to D3C4 challenge


    ::

        from dreamtools import D3C4
        s = D3C4()
        filename = s.download_template() 
        s.score(filename) 

    Data and templates are downloaded from Synapse. You must have a login.

    Insilico size 10 Ecoli1 gives 0.3295

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D3C4, self).__init__('D3C4')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self._init()
        self.sub_challenges = [10,50,100]

    def _init(self):
        # should download files from synapse if required.
        # First the PDF
        self._download_data('PDF_InSilicoSize100_Ecoli1.mat', 'syn4558484')
        self._download_data('PDF_InSilicoSize100_Ecoli2.mat', 'syn4558485')
        self._download_data('PDF_InSilicoSize100_Yeast1.mat', 'syn4558486')
        self._download_data('PDF_InSilicoSize100_Yeast2.mat', 'syn4558487')
        self._download_data('PDF_InSilicoSize100_Yeast3.mat', 'syn4558488')

        self._download_data('PDF_InSilicoSize10_Ecoli1.mat', 'syn4558474')
        self._download_data('PDF_InSilicoSize10_Ecoli2.mat', 'syn4558475')
        self._download_data('PDF_InSilicoSize10_Yeast1.mat', 'syn4558476')
        self._download_data('PDF_InSilicoSize10_Yeast2.mat', 'syn4558477')
        self._download_data('PDF_InSilicoSize10_Yeast3.mat', 'syn4558478')

        self._download_data('PDF_InSilicoSize50_Ecoli1.mat', 'syn4558479')
        self._download_data('PDF_InSilicoSize50_Ecoli2.mat', 'syn4558480')
        self._download_data('PDF_InSilicoSize50_Yeast1.mat', 'syn4558481')
        self._download_data('PDF_InSilicoSize50_Yeast1.mat', 'syn4558482')
        self._download_data('PDF_InSilicoSize50_Yeast1.mat', 'syn4558483')
        # Then, the gold standard
        self._download_data('DREAM3GoldStandard_InSilicoSize100_Ecoli1.txt', 'syn4558558')
        self._download_data('DREAM3GoldStandard_InSilicoSize100_Ecoli2.txt', 'syn4558560')
        self._download_data('DREAM3GoldStandard_InSilicoSize100_Yeast1.txt', 'syn4558562')
        self._download_data('DREAM3GoldStandard_InSilicoSize100_Yeast2.txt', 'syn4558564')
        self._download_data('DREAM3GoldStandard_InSilicoSize100_Yeast3.txt', 'syn4558565')

        self._download_data('DREAM3GoldStandard_InSilicoSize10_Ecoli1.txt', 'syn4558540')
        self._download_data('DREAM3GoldStandard_InSilicoSize10_Ecoli2.txt', 'syn4558542')
        self._download_data('DREAM3GoldStandard_InSilicoSize10_Yeast1.txt', 'syn4558544')
        self._download_data('DREAM3GoldStandard_InSilicoSize10_Yeast2.txt', 'syn4558545')
        self._download_data('DREAM3GoldStandard_InSilicoSize10_Yeast3.txt', 'syn4558547')

        self._download_data('DREAM3GoldStandard_InSilicoSize50_Ecoli1.txt', 'syn4558549')
        self._download_data('DREAM3GoldStandard_InSilicoSize50_Ecoli2.txt', 'syn4558551')
        self._download_data('DREAM3GoldStandard_InSilicoSize50_Yeast1.txt', 'syn4558553')
        self._download_data('DREAM3GoldStandard_InSilicoSize50_Yeast2.txt', 'syn4558554')
        self._download_data('DREAM3GoldStandard_InSilicoSize50_Yeast3.txt', 'syn4558556')

    def score(self, filename, size):
        print('Your filename must end with the batch name that is Ecoli1, Ecoli2, Yeast1, Yeast2, Yeast3 ')
        print('E.G. template_Ecoli1.txt')
        vals = os.path.split(filename)[-1].split('.')[0].split("_")
        results =  self.score_prediction(filename, size, vals[-1])
        AUC, AUROC, prec, rec, tpr, fpr, p_auroc, p_aupr = results
        return {'AUROC': AUROC, 'AUC':AUC, 'p_auroc':p_auroc, 'p_aupr':p_aupr}


    def _check_sub_challenge_size(self, name):
        assert name in [100, '100', 10, '10', '50', 50]

    def _check_sub_challenge_name(self, name):
        assert name in ['Ecoli1', 'Ecoli2', 'Yeast1', 'Yeast2', 'Yeast3']

    def download_template(self, size, name):
        self._check_sub_challenge_size(size)
        self._check_sub_challenge_name(name)
        subname = str(size)
        filename = self._pj([self._path2data, 'templates',
            'example_InSilicoSize%s_%s.txt' % (subname, name)])
        return filename

    def download_goldstandard(self, size, name):
        self._check_sub_challenge_size(size)
        self._check_sub_challenge_name(name)
        subname = str(size)
        return self.get_pathname('DREAM3GoldStandard_InSilicoSize%s_%s.txt' % (subname, name))

    def _load_network(self, filename):
        df = pd.read_csv(filename, header=None, sep='[ \t]', engine='python')
        df[0] = df[0].apply(lambda x: x.replace('g','').replace('G',''))
        df[1] = df[1].apply(lambda x: x.replace('g','').replace('G',''))
        df = df.astype(float) # imoprtant for later to check for equality
        return df

    def score_prediction(self, filename, size, name):
        """


        :param filename:
        :param size:
        :param name:
        :return:


        .. todo:: merge this function with the one from D4C2
        """
        gs_filename = self.download_goldstandard(size, name)
        pdf_filename = self.get_pathname("PDF_InSilicoSize%s_%s.mat" % (size, name))

        self.gold_data = self._load_network(gs_filename)
        self.test_data = self._load_network(filename)
        self.pdf_data = self.loadmat(pdf_filename)


        # we want to remove all entries for test that are not in GS
        # This can be done with a merge !
        newtest = pd.merge(self.test_data, self.gold_data, how='inner', on=[0,1])
        test = list(newtest['2_x'])
        gold_index = list(newtest['2_y'])

        AUC, AUROC, prec, rec, tpr, fpr = self.get_statistics(self.gold_data, self.test_data, gold_index)
        p_auroc = self._probability(self.pdf_data['x_auroc'][0], self.pdf_data['y_auroc'][0], AUROC)
        p_aupr = self._probability(self.pdf_data['x_aupr'][0], self.pdf_data['y_aupr'][0], AUC)

        return AUC, AUROC, prec, rec, tpr, fpr, p_auroc, p_aupr

    def _probability(self, X, Y, x):
        dx = X[2] - X[1]
        P = sum( Y[X>=x] * dx )
        return P

    def plot(self, filename, size, batch):
        aupr, auroc, prec, rec, tpr, fpr, p_auroc, p_aupr = self.score_prediction(filename, size, batch)
        super(D3C4, self).plot(metrics={'prec':prec, 'rec':rec, 'tpr':tpr, 'fpr':fpr})
