"""D4C2 scoring function


From an original code in matlab (Gustavo Stolovitzky and Robert Prill).

"""
from dreamtools.core.challenge import Challenge
from dreamtools.core.rocs import D3D4ROC

import pandas as pd
import numpy as np


class D4C2(Challenge, D3D4ROC):
    """A class dedicated to D4C2 challenge

    ::

        from dreamtools import D4C2
        s = D4C2()
        filename = s.download_template(10, )
        s.score(filename)

    Data and templates are downloaded from Synapse. You must have a login.


    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D4C2, self).__init__('D4C2')
        self._init()
        self.sub_challenges = ['10', '100', '100_multifactorial']

    def _init(self):
        # should download files from synapse if required.
        self._download_data('pdf_size100_1.mat', 'syn4558445')
        self._download_data('pdf_size100_2.mat', 'syn4558446')
        self._download_data('pdf_size100_3.mat', 'syn4558447')
        self._download_data('pdf_size100_4.mat', 'syn4558448')
        self._download_data('pdf_size100_5.mat', 'syn4558449')

        self._download_data('pdf_size100_multifactorial_1.mat', 'syn4558450')
        self._download_data('pdf_size100_multifactorial_2.mat', 'syn4558451')
        self._download_data('pdf_size100_multifactorial_3.mat', 'syn4558452')
        self._download_data('pdf_size100_multifactorial_4.mat', 'syn4558453')
        self._download_data('pdf_size100_multifactorial_5.mat', 'syn4558454')

        self._download_data('pdf_size10_1.mat', 'syn4558440')
        self._download_data('pdf_size10_2.mat', 'syn4558441')
        self._download_data('pdf_size10_3.mat', 'syn4558442')
        self._download_data('pdf_size10_4.mat', 'syn4558443')
        self._download_data('pdf_size10_5.mat', 'syn4558444')

    def _check_filename(self, filename):
        end = filename[-5:]
        if end[1] != '.':
            raise ValueError("File must end with a suffix of 3 letters e.g. .csv")
        end = end[0]
        if end not in ['1','2','3', '4', '5']:
            raise ValueError("File must end with a valid batch value in 1,2,3,4,5")
        return end

    def score(self, filename, subname=None):
        # here subname must be a valid sub challenge (10,100,100_multifactorial
        # the batch will be infered from the file name


        # if a list, return the overall score otherwise just score for that filename
        if isinstance(filename, str):
            end = self._check_filename(filename)

            assert subname is not None, "If one file provided, subname must be provided e.g., 10"
            subname = subname+"_"+end
            results = self.score_prediction(filename, subname=subname)
            del results['tpr']
            del results['fpr']
            del results['rec']
            del results['prec']
            return results
        elif isinstance(filename, list):
            assert len(filename) == 5, "if a list of gilenames is provide, it must contains 5 names"

            results = {}
            for i in [1, 2, 3, 4, 5]:
                tag = subname + "_" + str(i)
                assert tag in filename[i-1], "files must be sorted and ending in Size10_1, Size10_2, ...Size10_5"
                results['Net%s' % i] = self.score_prediction(filename[i-1], subname=tag)
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

            results = results[['SCORE', 'AUPR_PVAL', 'AUPR_SCORE',
                'AUROC_PVAL', 'AUROC_SCORE', 'Net1_AUPR',  'Net2_AUPR',
                'Net3_AUPR', 'Net4_AUPR', 'Net5_AUPR',
                'Net1_AUROC', 'Net2_AUROC',   'Net3_AUROC',
                'Net4_AUROC', 'Net5_AUROC']]
            return results

    def _check_sub_challenge_name(self, name):
        assert name in self.sub_challenges

    def download_template(self, subname):
        # subname should be "10_1" concat of size and a batch in 1..5
        if subname in self.sub_challenges:
            name1, name2 = subname, 1
        else:
            name1, name2 = subname.rsplit("_", 1)
        self._check_sub_challenge_name(name1)
        name = str(name1)
        filename = self._pj([self.classpath, 'templates', name1,
            'DREAM4_Example_InSilico_Size%s_%s.txt' % (name1, name2)])
        print("\nNote that there are 5 networks ending in 1,2,3,4,5.")
        return filename

    def download_goldstandard(self, subname):
        # subname should be "10_1" concat of size and a batch in 1..5
        if subname in self.sub_challenges:
            name1, name2 = subname, 1
        else:
            name1, name2 = subname.rsplit("_", 1)
        self._check_sub_challenge_name(name1)
        gs_filename = self._pj([self.classpath, 'goldstandard', name1,
                                'DREAM4_GoldStandard_InSilico_Size%s_%s.tsv' % (name1, name2)])
        return gs_filename

    def _load_network(self, filename):
        df = pd.read_csv(filename, header=None, sep='[ \t]', engine='python')
        df[0] = df[0].apply(lambda x: x.replace('g','').replace('G',''))
        df[1] = df[1].apply(lambda x: x.replace('g','').replace('G',''))
        df = df.astype(float) # imoprtant for later to check for equality
        return df

    def load_prob(self, filename):
        import scipy.io
        data = scipy.io.loadmat(filename)
        return data

    def score_prediction(self, filename=None, subname=None):
        """This is a longish scoring function translated from the
        matlab original code of D4C2

        :param filename:
        :param tag:
        :param batch:
        :return:

        .. todo:: merge this function with the one from D4C2
        """
        name1, name2 = subname.rsplit("_",1)
        gs_filename = self.download_goldstandard(subname)

        # keep this it is used for testing.
        pdf_filename = self.get_pathname('pdf_size%s_%s.mat' % (name1, name2))

        self.test_data = self._load_network(filename)
        self.gold_data = self._load_network(gs_filename)
        self.pdf_data = self.load_prob(pdf_filename)

        # append rank small to large
        newtest = pd.merge(self.test_data, self.gold_data, how='inner',
                on=[0,1])
        test = list(newtest['2_x'])
        gold_index = list(newtest['2_y'])

        AUC, AUROC, prec, rec, tpr, fpr = self.get_statistics(self.gold_data,
                self.test_data, gold_index)

        p_auroc = self._probability(self.pdf_data['auroc_X'][0],
                self.pdf_data['auroc_Y'][0], AUROC)
        p_aupr = self._probability(self.pdf_data['aupr_X'][0],
                self.pdf_data['aupr_Y'][0], AUC)

        return {'AUPR': AUC, 'AUROC':AUROC, 'prec':prec,
                'rec':rec, 'tpr':tpr, 'fpr':fpr,
                'p_auroc':p_auroc, 'p_aupr':p_aupr}

    def _probability(self, X, Y, x):
        ## Not that here X>=x in D4C1 and D4C3, X<=x
        dx = X[1] - X[0]
        P = sum(Y[X >= x]) * dx
        return P

    def plot(self, filename, subname):
        aupr, auroc, prec, rec, tpr, fpr, p_auroc, p_aupr = \
            self.score_prediction(filename, subname)
        self.metrics = {'prec':prec, 'rec':rec, 'tpr':tpr, 'fpr':fpr}
        super(D4C2, self).plot()

    def directed_to_undirected(self):
        raise NotImplementedError
        pass
