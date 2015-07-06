"""

Implementation in Python from Thomas Cokelaer.
Original code in matlab (Gustavo Stolovitzky and Robert Prill, Bernd Jagla).

"""
import os
from dreamtools.core.challenge import Challenge
import pandas as pd
from dreamtools.core.rocs import D3D4ROC


class D3C4(Challenge, D3D4ROC):
    """A class dedicated to D3C4 challenge


    ::

        from dreamtools import D3C4
        s = D3C4()
        filename = s.download_template() 
        s.score(filename) 


    .. note:: AUROC/AUPR and p-values are returned for a 
        given sub-challenge. In the DREAM LB, the 5 networks 
        are combined together. We should have same implemntatin
        as in D4C2

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D3C4, self).__init__('D3C4')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self._init()

        self.sub_challenges = []
        for x in ['10', '100', '50']:
            for y in ['Yeast3', 'Yeast1', 'Yeast2', 'Ecoli2', 'Ecoli1']:
                self.sub_challenges.append(x + '_' + y)

    def _init(self):
        # should download files from synapse if required.
        # First the PDF
        #TODO create a zip on synapse to simplify the follwoing?
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
        tag = "DREAM3GoldStandard"
        self._download_data('%s_InSilicoSize100_Ecoli1.txt' % tag, 'syn4558558')
        self._download_data('%s_InSilicoSize100_Ecoli2.txt' % tag, 'syn4558560')
        self._download_data('%s_InSilicoSize100_Yeast1.txt' % tag, 'syn4558562')
        self._download_data('%s_InSilicoSize100_Yeast2.txt' % tag, 'syn4558564')
        self._download_data('%s_InSilicoSize100_Yeast3.txt' % tag, 'syn4558565')

        self._download_data('%s_InSilicoSize10_Ecoli1.txt' % tag, 'syn4558540')
        self._download_data('%s_InSilicoSize10_Ecoli2.txt' % tag, 'syn4558542')
        self._download_data('%s_InSilicoSize10_Yeast1.txt' % tag, 'syn4558544')
        self._download_data('%s_InSilicoSize10_Yeast2.txt' % tag, 'syn4558545')
        self._download_data('%s_InSilicoSize10_Yeast3.txt' % tag, 'syn4558547')

        self._download_data('%s_InSilicoSize50_Ecoli1.txt' % tag, 'syn4558549')
        self._download_data('%s_InSilicoSize50_Ecoli2.txt' % tag, 'syn4558551')
        self._download_data('%s_InSilicoSize50_Yeast1.txt' % tag, 'syn4558553')
        self._download_data('%s_InSilicoSize50_Yeast2.txt' % tag, 'syn4558554')
        self._download_data('%s_InSilicoSize50_Yeast3.txt' % tag, 'syn4558556')

    def score(self, filename, subname=None):
        name1, name2 = self._check_subname(subname)
        results =  self.score_prediction(filename, subname)
        AUC, AUROC, prec, rec, tpr, fpr, p_auroc, p_aupr = results
        return {'AUROC': AUROC, 'AUC':AUC, 'p_auroc':p_auroc, 'p_aupr':p_aupr}

    def _check_subname(self, subname):
        name1, name2 = subname.split("_")
        names = ['Ecoli1', 'Ecoli2', 'Yeast1', 'Yeast2', 'Yeast3']
        error = "The sub challenge name must be X_Y where X is in 10 50 100"
        error += "\nand Y is in  %s" % names
        if name1 not in ['100', '10', '50']:
            raise ValueError(error)
        if name2 not in names:
            raise ValueError(error)
        return name1, name2

    def download_template(self, subname):
        name1, name2 = self._check_subname(subname)
        if name1 == '10':
            filename = self._pj([self._path2data, 'templates',
                'example_InSilicoSize%s_%s.txt' % (name1, name2)])
        else:
            # no template/examples for those cases were provided
            filename = self.download_goldstandard(subname)
        return filename

    def download_goldstandard(self, subname):
        name1, name2 = self._check_subname(subname)
        return self.get_pathname('DREAM3GoldStandard_InSilicoSize%s_%s.txt' % (name1, name2))

    def _load_network(self, filename):
        df = pd.read_csv(filename, header=None, sep='[ \t]', engine='python')
        df[0] = df[0].apply(lambda x: x.replace('g','').replace('G',''))
        df[1] = df[1].apply(lambda x: x.replace('g','').replace('G',''))
        df = df.astype(float) # imoprtant for later to check for equality
        return df

    def score_prediction(self, filename, subname):
        """

        :param filename:
        :param size:
        :param name:
        :return:

        """
        name1, name2 = self._check_subname(subname)
        gs_filename = self.download_goldstandard(subname)
        pdf_filename = self.get_pathname("PDF_InSilicoSize%s_%s.mat" % (name1, name2))

        self.gold_data = self._load_network(gs_filename)
        self.test_data = self._load_network(filename)
        self.pdf_data = self.loadmat(pdf_filename)

        # we want to remove all entries for test that are not in GS
        # This can be done with a merge !
        newtest = pd.merge(self.test_data, self.gold_data, how='inner', on=[0,1])
        #test = list(newtest['2_x'])
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
