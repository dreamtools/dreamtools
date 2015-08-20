"""D5C3 scoring function

Original matlab code from Gustavo A. Stolovitzky,  Robert Prill, Ph.D.
sub challenge B original code in R from A. de la Fuente

"""
import os
import random
from dreamtools.core.challenge import Challenge
import pandas as pd
import numpy as np
from dreamtools.core.rocs import D3D4ROC


__all__ = ["D5C3"]


class D5C3(Challenge, D3D4ROC):
    """A class dedicated to D5C3 challenge

    ::

        from dreamtools import D5C3
        s = D5C3()
        filename = s.download_template()
        s.score(filename)

    Data and templates are downloaded from Synapse. You must have a login.

    3 subchallenges (A100, A300, A999) but also 3 others simpler with
    B1, B2, B3

    For A series, 5 networks are required. For B, 3  are needed.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D5C3, self).__init__('D5C3')
        self._init()
        self.sub_challenges = ['A100', 'A300', 'A999', 'B']
        self.N_pvalues = 100

    def _init(self):
        # should download files from synapse if required.
        # The templates
        prefix = 'DREAM5_SysGen'
        self._download_data(prefix + 'A100_myteam_Network1.txt', 'syn4561478')
        self._download_data(prefix + 'A100_myteam_Network2.txt', 'syn4561482')
        self._download_data(prefix + 'A100_myteam_Network3.txt', 'syn4561486')
        self._download_data(prefix + 'A100_myteam_Network4.txt', 'syn4561489')
        self._download_data(prefix + 'A100_myteam_Network5.txt', 'syn4561493')

        # Get goldstandard and unpack zipped files
        self._download_data('D5C3_goldstandard.zip', 'syn4561554')
        self.unzip('D5C3_goldstandard.zip')

        # the probabilities for sub challenge A
        self._download_data('D5C3_probabilities.zip', 'syn4562041')
        self.unzip('D5C3_probabilities.zip')

    def _check_filename(self, filename):
        end = filename[-5:]
        if end[1] != '.':
            raise ValueError("File must end with a suffix of 3 letters e.g. .csv")
        end = end[0]
        if end not in ['1', '2', '3', '4', '5']:
            raise ValueError("File must end with a valid batch value in 1,2,3,4,5")
        return end

    def _check_subname(self, subname):
        if subname not in self.sub_challenges:
            raise ValueError("sub-challenge must be in %s" % self.sub_challenges)

    def _check_sub_challenge_name(self, name):
        assert name in self.sub_challenges

    def download_template(self, subname):
        # for B1, B2, B3, returns a single file
        # for A100, A300, A999 as well but to indicate the network,
        # append _1, _2, ..._5
        # if not, the network _1 is returned only
        # there is no A300 or a999 template
        if subname in ['A300', 'A999']:
            print("Warning:: there is no A300 or A999 template per se. " +
                    "Use the goldstandard instead")
            subname = 'A100'

        self._check_subname(subname)
        if subname == 'B':
            filenames = [self._pj([self.classpath, 'templates',
                                   "DREAM5_SysGenB1_your_Predictions.txt" ])]
            filenames.append(self._pj([self.classpath, 'templates',
                                   "DREAM5_SysGenB2_your_Predictions.txt" ]))
            filenames.append(self._pj([self.classpath, 'templates',
                                   "DREAM5_SysGenB3_your_Predictions.txt" ]))
        else:
            filenames = []
            for i in range(1, 6):
                gs_filename = self.get_pathname('DREAM5_SysGen%s_myteam_Network%s.txt' % (subname, i))
                filenames.append(gs_filename)
        return filenames

    def download_goldstandard(self, subname):
        # for B1, B2, B3, returns a single file
        # for A100, A300, A999 as well but to indicate the network, append _1, _2, ..._5
        # if not, the network _1 is returned only
        self._check_subname(subname)
        if subname == 'B':
            filenames = [self._pj([self.classpath, 'goldstandard',
                "DREAM5_SysGenB1_TestPhenotypeData.txt" ])]
            filenames.append(self._pj([self.classpath, 'goldstandard',
                "DREAM5_SysGenB2_TestPhenotypeData.txt"]))
            filenames.append(self._pj([self.classpath, 'goldstandard',
                "DREAM5_SysGenB3_TestPhenotypeData.txt"]))
            return filenames
        else:
            filenames = []
            for i in range(1, 6):
                gs_filename = self.get_pathname('DREAM5_SysGen%s_Edges_Network%s.tsv' % (subname, i))
                filenames.append(gs_filename)
            return filenames

    def _load_network(self, filename):
        df = pd.read_csv(filename, header=None, sep='[ \t]', engine='python')
        df[0] = df[0].apply(lambda x: x.replace('g', '').replace('G', ''))
        df[1] = df[1].apply(lambda x: x.replace('g', '').replace('G', ''))
        df = df.astype(float) # imoprtant for later to check for equality
        return df

    def score(self, filename, subname):
        self._check_subname(subname)
        if subname in ['A100', 'A300', 'A999']:
            return self._score_challengeA_bunch(filename, subname)
        elif subname == 'B':
            if isinstance(filename, list) is False:
                raise TypeError('Challenge B expects 3 input files B1, B2, B3')
            if len(filename)!=3:
                raise TypeError('Challenge B expects 3 input files B1, B2, B3')
            return self.score_challengeB(filename)
        else:
            raise ValueError('Sub challenge must be either A or B')

    def _score_challengeA_bunch(self, filenames, subname):

        from easydev import Progress
        pb = Progress(5, 1)
        pb.animate(0)
        results = []
        for i, filename in enumerate(filenames):
            res  = self.score_challengeA(filename, subname+"_" + str(i+1))
            pb.animate(i+1)
            results.append(res)

        aupr_score = -np.mean(np.log10([x['p_auroc'] for x in results]))
        auroc_score = -np.mean(np.log10([x['p_aupr'] for x in results]))
        score = (aupr_score + auroc_score)/2.

        df = pd.TimeSeries()
        df['Overall Score'] = score
        df['AUPR score (pval)'] = aupr_score
        df['AUROC score (pval)'] = aupr_score

        for i in range(1, 6):
            df['AUPR Net %s' % i] = results[i-1]['aupr']

        for i in range(1, 6):
            df['AUROC Net %s' % i] = results[i-1]['auroc']

        return df

    def score_challengeA(self, filename, subname):

        name1, name2 = subname.rsplit("_",1)
        goldfile = self.download_goldstandard(name1)[int(name2)-1]

        # gold standard edges only
        predictionfile = filename

        # precomputed probability densities for various metrics
        pdffile_aupr  = self.get_pathname(name1 + os.sep+ 'Network%s_AUPR.mat' % (name2))
        pdffile_auroc = self.get_pathname(name1+os.sep+ 'Network%s_AUROC.mat'% (name2))
        # load probability densities
        pdf_aupr  = self.loadmat(pdffile_aupr)
        pdf_auroc = self.loadmat(pdffile_auroc)

        self.pdf_auroc = self.loadmat(pdffile_auroc)
        self.pdf_aupr = self.loadmat(pdffile_aupr)

        # load gold standard
        self.gold_edges = self._load_network(goldfile)

        # load predictions
        self.prediction = self._load_network(predictionfile)

        # DISCOVERY
        # In principle we could resuse ROCDiscovery class but
        # here the pvalues were also computed. let us do it here for now

        merged = pd.merge(self.gold_edges, self.prediction, 
                how='inner', on=[0,1])
        self.merged = merged

        TPF = len(merged)
        # unique species should be 1000
        N = len(set(self.gold_edges[0]).union(self.gold_edges[1]))
        # positive
        Pos = len(self.gold_edges)
        # negative
        Neg = N*N-N-Pos
        # total
        Ntot = Pos + Neg

        L = len(self.prediction)

        discovery = np.zeros(L)
        values_gs =  [tuple(x) for x in merged[[0,1]].values]
        values_pred = [tuple(x) for x in self.prediction[[0,1]].values]
        count = 0
        for i in range(0, L):
            if values_pred[i] in values_gs:
                discovery[count] = 1
                # else nothing to do (vector is filled with zeros
            count += 1
        TPL = sum(discovery)

        self.discovery = discovery

        if L < Ntot:
            p = (Pos - TPL) / float(Ntot - L)
        else:
            p = 0

        random_positive_discovery = [p] * (Ntot - L)
        random_negative_discovery = [1-p] * (Ntot - L)

        # append discovery + random using lists
        positive_discovery = np.array(list(discovery)
                + random_positive_discovery)
        negative_discovery = np.array(list(1-discovery)
                + random_negative_discovery)

        #  true positives (false positives) at depth k
        TPk = np.cumsum(positive_discovery)
        FPk = np.cumsum(negative_discovery)

        #  metrics
        TPR = TPk / float(Pos)
        FPR = FPk / float(Neg)
        REC = TPR  # same thing
        PREC = TPk / range(1, Ntot+1)

        from dreamtools.core.rocs import ROCBase
        roc = ROCBase()
        auroc = roc.compute_auc(roc={'tpr':TPR, 'fpr':FPR})
        aupr = roc.compute_aupr(roc={'precision':PREC, 'recall':REC})

        # normalise by max possible value
        aupr /= (1.-1./Pos)

        p_aupr = self._probability(pdf_aupr['X'][0], pdf_aupr['Y'][0], aupr)
        p_auroc = self._probability(pdf_auroc['X'][0], pdf_auroc['Y'][0],
                auroc)

        results = {'auroc':auroc, 'aupr':aupr, 'p_auroc':p_auroc,
                'p_aupr':p_aupr}
        return results

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
        gold_filenames = self.download_goldstandard('B')
        print("Warning: your 3 submissions should be ordered as B1, B2, B3 files")

        for tag in [1, 2, 3]:
            #assumeing data and gs are sorted in the same way !!
            gold = pd.read_csv(gold_filenames[tag-1], sep='[ \t]', 
                    engine='python')
            self.golds.append(gold)

            #filename = 'DREAM5_SysGenB%s_your_Predictions.txt' % tag
            #filename = self._pj([self.classpath, 'data', filename])
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
        pvals = [sum(self.random_scores[k]>= self.scores[k])/float(self.N_pvalues)
                for k in [0,1,2]]
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

    def _probability(self, X, Y, x):
        dx = X[1] - X[0]
        return  sum(Y[X >= x]) * dx
