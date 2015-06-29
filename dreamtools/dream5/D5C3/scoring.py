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

    3 subchallenges (A100, A300, A999) but also 3 others simpler with B1, B2, B3

For A series, 5 networks are required. For B, only one is needed.

For A100, Network 1:

auroc =

    0.7111


aupr =

    0.0073


p_auroc =

   2.6335e-35


p_aupr =

    0.9990

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D5C3, self).__init__('D5C3')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self._init()
        self.sub_challenges = ['A100', 'A300', 'A999', 'B1', 'B2', 'B3']
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

    def _check_filename(self, filename):
        end = filename[-5:]
        if end[1] != '.':
            raise ValueError("File must end with a suffix of 3 letters e.g. .csv")
        end = end[0]
        if end not in ['1','2','3', '4', '5']:
            raise ValueError("File must end with a valid batch value in 1,2,3,4,5")
        return end

    def _check_subname(self, subname):
        if subname not in self.sub_challenges:
            raise ValueError("sub-challenge must be in %s" % self.sub_challenges)

    def _check_sub_challenge_name(self, name):
        assert name in self.sub_challenges

    def download_template(self, subname):
        # for B1, B2, B3, returns a single file
        # for A100, A300, A999 as well but to indicate the network, append _1, _2, ..._5
        # if not, the network _1 is returned only
        if subname in self.sub_challenges and subname.startswith("B"):
            return self._pj([self._path2data, 'templates', "DREAM5_SysGen%s_your_Predictions.txt" % subname])


        # subname should be "10_1" concat of size and a batch in 1..5
        if subname in self.sub_challenges:
            name1, name2 = subname, 1
        else:
            name1, name2 = subname.rsplit("_", 1)
        self._check_sub_challenge_name(name1)
        name = str(name1)
        filename = self.get_pathname('DREAM5_SysGen%s_myteam_Network%s.txt' % (name1, name2))
        return filename

    def download_goldstandard(self, subname):
        # for B1, B2, B3, returns a single file
        # for A100, A300, A999 as well but to indicate the network, append _1, _2, ..._5
        # if not, the network _1 is returned only
        if subname in self.sub_challenges and subname.startswith("B"):
            return self._pj([self._path2data, 'goldstandard', "DREAM5_SysGen%s_TestPhenotypeData.txt" % subname])

        if subname in self.sub_challenges:
            name1, name2 = subname, 1
        else:
            name1, name2 = subname.rsplit("_", 1)
        self._check_sub_challenge_name(name1)
        gs_filename = self.get_pathname('DREAM5_SysGen%s_Edges_Network%s.tsv' % (name1, name2))
        return gs_filename

    def _load_network(self, filename):
        df = pd.read_csv(filename, header=None, sep='[ \t]', engine='python')
        df[0] = df[0].apply(lambda x: x.replace('g','').replace('G',''))
        df[1] = df[1].apply(lambda x: x.replace('g','').replace('G',''))
        df = df.astype(float) # imoprtant for later to check for equality
        return df

    def score(self, filename, subname):
        self._check_subname(subname)
        if subname == 'A100':
            return self.score_challengeA(filename)
        elif subname == 'B':
            return self.score_challengeB(filename)
        else:
            raise ValueError('Sub challenge must be either A or B')

    def score_challengeA(self, filename, subname):


        name1, name2 = subname.rsplit("_",1)
        goldfile = self.download_goldstandard(subname)

        # gold standard edges only
        predictionfile = filename

        # precomputed probability densities for various metrics
        pdffile_aupr  = self.get_pathname('%s_Network%s_AUPR.mat' % (name1, name2))
        pdffile_auroc = self.get_pathname('%s_Network%s_AUROC.mat'% (name1, name2))

        # load gold standard
        self.gold_edges = self._load_network(goldfile)

        # load predictions
        self.prediction = self._load_network(predictionfile)

        # load probability densities
        self.pdf_aupr  = self.loadmat(pdffile_aupr)
        self.pdf_auroc = self.loadmat(pdffile_auroc)

        # DISCOVERY


        #random

    def _get_G(self, gold):

        df = gold[[0,1]]
        nodes = set(df[0]).union(set(df[1]))

        regulators = list(nodes)
        targets = list(nodes)


        """# lookup matrix for positive edges
        A = edgelist2sparse(gold_positives(:,1:2));

        #  build gold standard matrix for positives (1) AND negatives (-1)
        G = zeros(length(regulators),length(targets));
        for k = 1:length(regulators)
	        i = regulators(k);
	        for l = 1:length(targets)
		        j = targets(l);
		            if A(i,j)
			            G(i,j) = 1;		%% Positive
		            elseif i~=j			%% no self edges
			            G(i,j) = -1;	%% Negative
		        end
	        end
        end

        H = sparse(G>0)


%% total, positive, negative
P = full(sum(sum(G>0)));
N = full(sum(sum(G<0)));
T = P + N;
>>
>>
>>
>> P

P =

        2037

>> N

N =

      996963

>> T

T =

      999000

        """



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
            filename = self.download_goldstandard('B' + str(tag))
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
