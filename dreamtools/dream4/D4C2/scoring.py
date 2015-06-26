"""


Implementation in Python from Thomas Cokelaer.
Original code in matlab (Gustavo Stolovitzky and Robert Prill).


"""
import os
from dreamtools.core.challenge import Challenge
from dreamtools.core.rocs import D3D4ROC

import pandas as pd
import numpy as np
import pylab

class D4C2(Challenge, D3D4ROC):
    """A class dedicated to D4C2 challenge


    ::

        from dreamtools import D4C2
        s = D4C2()
        filename = s.download_template(10, )
        s.score(filename) 

    Data and templates are downloaded from Synapse. You must have a login.


    So far only 1 network at a time is scored using scor_prediction.



    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D4C2, self).__init__('D4C2')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self._init()
        self._sub_challenges = [100,10,'100', '10', '100_multifactorial']


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


    def score(self, filename, tag):
        print('Your filename must end with the batch value in 1,2,3,4,5 ')
        print('E.G. template_Ecoli1.txt')
        vals = os.path.split(filename)[-1].split('.')[0].split("_")
        results = self.score_prediction(filename, tag=tag, batch=vals[-1])
        AUC, AUROC, prec, rec, tpr, fpr, p_auroc, p_aupr = results
        return {'AUROC': AUROC, 'AUC':AUC, 'p_auroc':p_auroc, 'p_aupr':p_aupr}

    def _check_sub_challenge_name(self, name):
        assert name in [100, '100', 10, '10', '100_multifactorial']

    def download_template(self, name, batch):
        self._check_sub_challenge_name(name)
        name = str(name)
        filename = self._pj([self._path2data, 'templates', name,
            'DREAM4_Example_InSilico_Size%s_%s.txt' % (name, batch)])
        return filename

    def download_goldstandard(self, tag, batch):
        self._check_sub_challenge_name(tag)
        if tag in [100, 10]:
            tag = str(tag)
        gs_filename = self._pj([self._path2data, 'goldstandard', tag,
                                'DREAM4_GoldStandard_InSilico_Size%s_%s.tsv' % (tag, batch)])
        return gs_filename

    def _load_network(self, filename):
        df = pd.read_csv(filename, header=None, sep='[ \t]')
        df[0] = df[0].apply(lambda x: x.replace('g','').replace('G',''))
        df[1] = df[1].apply(lambda x: x.replace('g','').replace('G',''))
        df = df.astype(float) # imoprtant for later to check for equality
        return df

    def load_prob(self, filename):
        import scipy.io
        data = scipy.io.loadmat(filename)
        return data

    def score_prediction(self, filename=None, tag=10, batch=1):
        """This is a longish scoring function translated from the matlab original code of D4C2

        :param filename:
        :param tag:
        :param batch:
        :return:


        .. todo:: merge this function with the one from D4C2
        """
        gs_filename = self.download_goldstandard(tag, batch)

        # keep this it is used for testing.
        pdf_filename = self._pj([self._path2data, 'data', 'pdf_size%s_%s.mat' % (tag, batch)])


        self.test_data = self._load_network(filename)
        self.gold_data = self._load_network(gs_filename)
        self.pdf_data = self.load_prob(pdf_filename)

        test_data = self._load_network(filename)
        gold_data = self._load_network(gs_filename)
        pdf_data = self.load_prob(pdf_filename)


        # append rank small to large
        newtest = pd.merge(self.test_data, self.gold_data, how='inner', on=[0,1])
        test = list(newtest['2_x'])
        gold_index = list(newtest['2_y'])

        AUC, AUROC, prec, rec, tpr, fpr = self.get_statistics(self.gold_data, self.test_data, gold_index)
        p_auroc = self._probability(self.pdf_data['auroc_X'][0], self.pdf_data['auroc_Y'][0], AUROC)
        p_aupr = self._probability(self.pdf_data['aupr_X'][0], self.pdf_data['aupr_Y'][0], AUC)


        return AUC, AUROC, prec, rec, tpr, fpr, p_auroc, p_aupr

    def _probability(self, X, Y, x):
        ## Not that here X>=x in D4C1 and D4C3, X<=x
        dx = X[1]-X[0]
        P = sum(Y[X >= x])*dx
        return P

    def plot(self, filename, tag, batch):
        aupr, auroc, prec, rec, tpr, fpr, p_auroc, p_aupr = \
            self.score_prediction(filename, tag, batch)
        super(D4C2, self).plot(metrics={'prec':prec, 'rec':rec, 'tpr':tpr, 'fpr':fpr})



    def directed_to_undirected(self):
        raise NotImplementedError
        pass
        """
        function test_data_undirected = directed_2_undirected_predictions(test_data,N)
%% test data is an edge list ranked from high to low confidence
%% N is the number of nodes in the network

D = sparse(N,N,0);
E = test_data(:,1:2);	%% edgelist
R = 1:size(E,1);		%% rank (low to high)
for k = 1:size(E,1)
	i = E(k,1);
	j = E(k,2);
	r = R(k);
	D(i,j) = r;			%% add link denoted by rank
end

%% take the smallest rank greater than zero as the
%% undirected rank
count = 0;
for i = 1:N
	for j = (i+1):N		%% upper triangular
		count = count + 1;
		r_ij = D(i,j);
		r_ji = D(j,i);
		if (r_ij > 0) & (r_ji > 0)
 			%% they are both greater than zero
			if r_ij < r_ji
				E_undirected(count,:) = [ i j r_ij ];
			else
				E_undirected(count,:) = [ i j r_ji ];
			end
		elseif r_ij > 0
			E_undirected(count,:) = [ i j r_ij ];
		else
			E_undirected(count,:) = [ i j r_ji ];
		end
	end
end

%% finally, sort the edge list to produce the prediction
R = E_undirected(:,3);		%% ranks
idx = find(R);				%% just the nonzero ranks
E_nonzero_rank = E_undirected(idx,:);
R_nonzero = R(idx);
[ temp myorder ] = sort(R_nonzero);
test_data_undirected = E_nonzero_rank(myorder,:);
        """

