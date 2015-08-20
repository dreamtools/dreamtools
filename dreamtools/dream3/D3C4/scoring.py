"""

Implementation in Python from Thomas Cokelaer.
Original code in matlab (Gustavo Stolovitzky and Robert Prill).

"""
from dreamtools.core.challenge import Challenge
import pandas as pd
from dreamtools.core.rocs import D3D4ROC
import numpy as np


__all__ = ["D3C4"]


class D3C4(Challenge, D3D4ROC):
    """A class dedicated to D3C4 challenge

    ::

        from dreamtools import D3C4
        s = D3C4()
        filename = s.download_template(10)
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
        self._init()

        self.sub_challenges = ['10', '100', '50']
        self.netnames = ['Yeast3', 'Yeast1', 'Yeast2', 'Ecoli2', 'Ecoli1']


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

    def _check_filename(self, filename):
        end = filename[-10:]
        if end[6] != '.':
            raise ValueError("File must end with a suffix of 3 letters e.g. .csv")
        end = end[0:6]

        endings = ['Ecoli1', 'Ecoli2', 'Yeast1', 'Yeast2', 'Yeast3']
        if end not in endings:
             raise ValueError("File must end with a valid batch value in %s" %
                     endings)
        return end

    def score(self, filename, subname):
        subname = str(subname)
        self._check_subname(subname)

        if isinstance(filename, str):
            end = self._check_filename(filename)
            if end not in subname:
                subname += "_"+end
            results =  self.score_prediction(filename, subname)
            del results['tpr']
            del results['fpr']
            del results['rec']
            del results['prec']
            return results
            #{'AUROC': AUROC, 'AUC':AUC, 'p_auroc':p_auroc,
            #            'p_aupr':p_aupr}
        elif isinstance(filename, list):
            assert len(filename) == 5, "if a list of filenames is provide, it must contain 5 names"
            results = {}
            for i, this in enumerate(filename):
                end = self._check_filename(this)
                results['Net%s' % i] = self.score_prediction(this,
                        subname+"_"+end)

            df = pd.DataFrame(results).T
            # get rid of non important data
            df = df[['AUROC', 'AUPR', 'p_aupr', 'p_auroc']]
            df = df.astype('float64')

            final_score =  -np.mean(np.log10(df[['p_auroc', 'p_aupr']]))

            results = {}
            results['AUPR_SCORE'] = final_score['p_aupr']
            results['AUROC_SCORE'] = final_score['p_auroc']
            overall_score = np.mean(final_score)

            for index in df.index:
                results['%s_AUROC' % index] = df.ix[index]['AUROC']
            for index in df.index:
                results['%s_AUPR' % index] = df.ix[index]['AUPR']

            final_score = 10**-(final_score)
            results['AUPR_PVAL'] = final_score['p_aupr']
            results['AUROC_PVAL'] = final_score['p_auroc']

            results['SCORE'] = overall_score
            results = pd.TimeSeries(results)

            results = results[['SCORE', 'AUPR_PVAL', 'AUPR_SCORE', 'AUROC_PVAL',
                'AUROC_SCORE','Net1_AUPR',  'Net2_AUPR', 'Net3_AUPR',
                'Net4_AUPR', 'Net5_AUPR', 'Net1_AUROC', 'Net2_AUROC',
                'Net3_AUROC', 'Net4_AUROC', 'Net5_AUROC']]
            return results

    def _warning(self):
        print("\nNote that 5 networks had to be submitted")
        print("You can score an individual one.")
        print("Or provide a list of 5 filenames.")
        print("You can use a wildcard * or be explicit.")
        print("The file filenames must end in Yeast1, Yeast2, Yeast3,  Ecoli1, Ecoli2")
        print("filename for th Yeast1 case only.")

    def download_template(self, subname):
        # no template per se, so we return GS
        # self._check_subname(subname)
        #self._warning()
        if subname.startswith('10'):
            if subname in self.sub_challenges:
                subname2 = subname + "_Yeast1"
            else:
                subname2, netname = subname.split("_", 1)
                self._check_subname(subname2)
                subname2 = subname
            filename = self._pj([self.classpath, 'templates',
                'example_InSilicoSize%s.txt' % subname2])
        else:
            filename = self.download_goldstandard(subname)
        return filename

    def download_goldstandard(self, subname):
        subname = str(subname)
        if subname in self.sub_challenges:
            subname2 = subname + "_Yeast1"
        else:
            subname2, netname = subname.split("_", 1)
            self._check_subname(subname2)
            subname2 = subname

        return self.get_pathname('DREAM3GoldStandard_InSilicoSize%s.txt' %
                subname2)

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
        name1, name2 = subname.rsplit("_",1)

        gs_filename = self.download_goldstandard(subname)
        pdf_filename = self.get_pathname("PDF_InSilicoSize%s.mat" % subname)

        self.gold_data = self._load_network(gs_filename)
        self.test_data = self._load_network(filename)
        self.pdf_data = self.loadmat(pdf_filename)

        # we want to remove all entries for test that are not in GS
        # This can be done with a merge !
        newtest = pd.merge(self.test_data, self.gold_data, how='inner', on=[0,1])
        #test = list(newtest['2_x'])
        gold_index = list(newtest['2_y'])

        AUC, AUROC, prec, rec, tpr, fpr = self.get_statistics(self.gold_data,
                self.test_data, gold_index)

        p_auroc = self._probability(self.pdf_data['x_auroc'][0],
                self.pdf_data['y_auroc'][0], AUROC)
        p_aupr = self._probability(self.pdf_data['x_aupr'][0],
                self.pdf_data['y_aupr'][0], AUC)

        return {'AUPR': AUC, 'AUROC':AUROC, 'prec':prec,
                'rec':rec, 'tpr':tpr, 'fpr':fpr,
                'p_auroc':p_auroc, 'p_aupr':p_aupr}

    def _probability(self, X, Y, x):
        dx = X[2] - X[1]
        P = sum( Y[X>=x] * dx )
        return P

    def plot(self, filename, size, batch):
        aupr, auroc, prec, rec, tpr, fpr, p_auroc, p_aupr = self.score_prediction(filename, size, batch)
        super(D3C4, self).plot(metrics={'prec':prec, 'rec':rec, 'tpr':tpr, 'fpr':fpr})
