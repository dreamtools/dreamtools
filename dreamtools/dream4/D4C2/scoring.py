"""


Implementation in Python from Thomas Cokelaer.
Original code in matlab (Gustavo Stolovitzky and Robert Prill).


"""
import os
from dreamtools.core.challenge import Challenge

import pandas as pd
import numpy as np
import pylab

class D4C2(Challenge):
    """A class dedicated to D4C2 challenge


    ::

        from dreamtools import D4C2
        s = D4C2()
        filename = s.download_template() 
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
        pass

    def score(self, prediction_file):

        raise NotImplementedError

    def _check_sub_challenge_name(self, name):
        assert name in [100, '100', 10, '10', '100_multifactorial']

    def download_template(self, name):
        self._check_sub_challenge(name)
        name = str(name)
        filename = self._pj([self._path2data, 'templates', name,
            'DREAM4_Example_InSilico_Size%s_%s.txt' % (name, 1)])
        return filename

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


        """
        #, filename, challenge_name):
        self._check_sub_challenge_name(tag)
        if tag in [100, 10]:
            tag = str(tag)

        gs_filename = self._pj([self._path2data, 'goldstandard', tag,
                                'DREAM4_GoldStandard_InSilico_Size%s_%s.tsv' % (tag, batch)])

        # keep this it is used for testing.
        if filename is None:
            filename = self._pj([self._path2data, 'templates', tag,
                                'DREAM4_Example_InSilico_Size%s_%s.txt' % (tag, batch)])

        pdf_filename = self._pj([self._path2data, 'data', 'pdf_size%s_%s.mat' % (tag, batch)])

        test_data = self._load_network(filename)
        gold_data = self._load_network(gs_filename)
        pdf_data = self.load_prob(pdf_filename)


        T = len(gold_data)          # Total potential edges n(n-1)
        P = gold_data[2].sum()      # positives
        N = T - P                   # negatives
        L = len(test_data)          # length of prediction list

        # append rank small to large
        test_data['rank'] = range(1,L+1)

        # order the edgelist for test the same as the edgelist for gold
        test = [0] * T
        for index, row in test_data.iterrows():
            indices = row[[0,1]]
            rank = row['rank']
            try:
                idx = list((gold_data[[0,1]].values == indices.values).sum(axis=1)).index(2)
            except:
                raise ValueError('Did not find this edge (%s) in the gold standard network' % indices.values)
            test[idx] = rank

        # counters
        k = 0
        Ak = 0
        TPk = 0
        FPk = 0

        gold = list(gold_data[2].values)
        rec = []
        prec = []
        tpr=[]
        fpr = []
        while k < L:

            k = k + 1
            # index of the kth predicted edge
            idx = test.index(k)
            if gold[idx] == 1:
                #%% the edge IS present in the gold standard

                #%% increment TPk
                TPk = TPk + 1.

                #%% update area under precision-recall curve
                if k == 1:
                    delta = 1. / P
                else:
                    delta = (1. - FPk * np.log(k/(k-1.))) / P
                Ak = Ak + delta

            else: # the edge is NOT present in the gold standard
                #%% icrement FPk
		        FPk = FPk + 1.

            # do NOT update area under P-R
	        #remember
            rec.append(TPk/float(P))
            prec.append(TPk/float(k))
            tpr.append(rec[k-1])
            fpr.append(FPk/float(N))

        # Done with the positive predictions.

        # If the number of predictions (L) is less than the total possible edges (T),
        # we assume that they would achieve the accuracy of the null model (random guessing).

        TPL = TPk

        # rho
        if L < T:
            rh = (P-TPL)/float(T-L)
        else:
            rh = 0.

        # recall at L
        if L > 0:
            recL = rec[L-1]   # note -1 to use python syntax
        else:
            recL = 0

        # the remaining positives would eventually be predicted
        while TPk < P:
            k = k + 1
            TPk = TPk + 1.
            rec.append(TPk/float(P))
            if ((rec[k-1]-recL) * P + L * rh) != 0:
                prec.append( rh * P * rec[k-1]/((rec[k-1]-recL)*P + L * rh))
            else:
                prec.append(0)

            tpr.append(rec[k-1])
            FPk = TPk * (1-prec[k-1])/prec[k-1]
            fpr.append(FPk/float(N))

        # Now, update the area under the P-R curve
        # %% rh = (P-TPk)/(T-L);  % BP: I removed this line because it is an error in logic to redefine this here.
        AL = Ak

        #if ~isnan(rh) and rh != 0 and L != 0:
        if rh != 0 and L != 0:
            AUC = AL + rh * (1.-recL) + rh * (recL - L * rh / P) * np.log((L * rh + P * (1-recL) )/(L *rh))
        elif L == 0:
            AUC = P/float(T)
        else:
            AUC = Ak

        # Integrate area under ROC
        lc = fpr[0] * tpr[0] /2.
        for n in range(1,int(L+P-TPL-1 + 1)):
            lc = lc + ( fpr[n] + fpr[n-1]) * (tpr[n]-tpr[n-1]) / 2.

        AUROC = 1. - lc

        auroc = AUROC
        aupr = AUC
        p_auroc = self._probability(pdf_data['auroc_X'][0], pdf_data['auroc_Y'][0], auroc)
        p_aupr = self._probability(pdf_data['aupr_X'][0], pdf_data['aupr_Y'][0], aupr)


        return AUC, AUROC, prec, rec, tpr, fpr, p_auroc, p_aupr

    def _probability(self, X, Y, x):
        ## Not that here X>=x in D4C1 and D4C3, X<=x
        dx = X[1]-X[0]
        P = sum(Y[X >= x])*dx
        return P

    def plot(self, filename=None):
        aupr, auroc, prec, rec, tpr, fpr, p_auroc, p_aupr = self.score_prediction()

        pylab.figure(1)
        pylab.subplot(1,2,1)
        pylab.plot(fpr,tpr)
        pylab.title('ROC')
        pylab.xlabel('FPR')
        pylab.ylabel('TPR')
        pylab.subplot(1,2,2)
        pylab.plot(rec,prec)
        pylab.title('P-R')
        pylab.xlabel('Recall')
        pylab.ylabel('Precision')


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

