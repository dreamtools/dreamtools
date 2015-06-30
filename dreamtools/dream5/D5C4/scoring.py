"""

Based on original matlab code from Gustavo A. Stolovitzky and Robert Prill


"""
from dreamtools.core.challenge import Challenge
import pandas as pd
from dreamtools.core.rocs import D3D4ROC
import numpy as np

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

    # copy and paste from D5C3 ' FIXME use classes to factorise code
    def score_challengeA(self, filename, tag):
        """



auroc =

    0.6818


aupr =

    0.0271


p_auroc =

    0.6268


p_aupr =

    0.9999


    all



        :param filename:
        :param tag:
        :return:
        """
        assert tag in [1,3,4]
        tag = str(tag)

        if tag == '1':
            goldfile = self.download_goldstandard()[0]
        elif tag == '3':
            goldfile = self.download_goldstandard()[1]
        elif tag == '4':
            goldfile = self.download_goldstandard()[2]

        # gold standard edges only
        predictionfile = filename

        # precomputed probability densities for various metrics
        pdffile_aupr  = self.get_pathname('Network%s_AUPR.mat' % tag)
        pdffile_auroc = self.get_pathname('Network%s_AUROC.mat'% tag)

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
        # here the pvaluse were also computed. let us do it here for now

        merged = pd.merge(self.gold_edges, self.prediction, how='inner', on=[0,1])
        self.merged = merged

        TPF = len(merged)
        # unique species should be 1000
        N = len(set(self.gold_edges[0]).union(self.gold_edges[1]))
        # positive
        Pos = len(self.gold_edges)  #4012
        # this can be computed using self._get_P_N_Z(self.gold_edges)
        # but slow computation, so let us hard code it
        Neg = 274380     #
        # total
        Ntot = Pos + Neg

        L = len(self.prediction)

        print N
        print Pos
        print Neg
        print TPF
        print "length prediction:",L

        # should be 86225

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
        positive_discovery = np.array(list(discovery) + random_positive_discovery)
        negative_discovery = np.array(list(1-discovery) + random_negative_discovery)

        #  true positives (false positives) at depth k
        TPk = np.cumsum(positive_discovery)
        FPk = np.cumsum(negative_discovery)

        #  metrics
        TPR = TPk / float(Pos)
        FPR = FPk / float(Neg)
        REC = TPR  # same thing
        PREC = TPk / range(1,Ntot+1)

        #  sanity check
        #if ( (P ~= round(TPk(end))) | (N ~= round(FPk(end))) )
        #	        disp('ERROR. There is a problem with the completion of the prediction list.')
        #  end

        # finishing touch
        #TPk(end) = round(TPk(end));
        #FPk(end) = round(FPk(end));

        from dreamtools.core.rocs import ROCBase
        roc = ROCBase()
        auroc = roc.compute_auc(roc={'tpr':TPR, 'fpr':FPR})
        aupr = roc.compute_aupr(roc={'precision':PREC, 'recall':REC})

        # normalise by max possible value
        aupr /= (1.-1./Pos)

        p_aupr = self._probability(pdf_aupr['X'][0], pdf_aupr['Y'][0], aupr)
        p_auroc = self._probability(pdf_auroc['X'][0], pdf_auroc['Y'][0], auroc)

        results = {'auroc':auroc, 'aupr':aupr, 'p_auroc':p_auroc, 'p_aupr':p_aupr}
        return results

    def _probability(self, X, Y, x):
        dx = X[1]-X[0]
        return  sum(Y[X >= x])*dx


    def _get_P_N_Z(self, gold):
        from easydev import Progress

        regulators = list(set(gold[0]))
        targets = list(set(gold[[0,1]].stack()))
        gs = gold[[0,1]].values
        gs = [tuple(x) for x in gs]

        pb = Progress(len(regulators), 1)
        P, Z, N = 0,0,0
        for i, regulator in enumerate(regulators):
            for l in range(0, len(targets)):
                j = targets[l]
                if (regulator, j) in gs:
                    P +=1
                elif regulator!=j:
                    N+=1
                else:
                    Z+=1
            pb.animate(i+1)
        return P, N, Z

    def _get_cleaned_prediction(self, prediction, gold):
        from easydev import Progress

        regulators = list(set(prediction[0]))

        pred = prediction[[0,1]].values
        data = [tuple(x) for x in pred]

        gs = gold[[0,1]].values
        gs = [tuple(x) for x in gs]


        pb = Progress(len(data), 1)
        #for this in data:

        #    i, j = this
        #    if (i,j) in gs


144.0 1466.0



