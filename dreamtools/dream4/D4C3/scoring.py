"""


Based on Matlab script available on https://www.synapse.org/#!Synapse:syn2825304
Original code from  Gustavo A. Stolovitzky and Robert Prill.
Converted to this Python module by Thomas Cokelaer

"""
import os
from dreamtools.core.challenge import Challenge
import pandas as pd
import numpy as np
import pylab

class D4C3(Challenge):
    """A class dedicated to D4C3 challenge

    ::

        from dreamtools import D4C3
        s = D4C3()
        filename = s.download_template() 
        s.score(filename) 

    Data and templates are inside Dreamtools.


    .. note:: A parameter called cost_per_link is hardcoded for the challenge. IT was compute as
        the = min {Prediction Score / Edge Count} amongst all submissions. For this scoring
        function, :attr:`cost_per_link` is set to 0.0827 and may be changed by the user.



    """
    def __init__(self, edge_count=20, cost_per_link=0.0827):
        """.. rubric:: constructor

        """
        super(D4C3, self).__init__('D4C3')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]

        # cost_per_link Was determined empirically from all the teams' submissions
        # as r = min(prediction_score / edge_count).
        self.cost_per_link = cost_per_link
        self.edge_count = edge_count
        self.species = ['AKT', 'ERK12', 'Ikb', 'JNK12', 'p38', 'HSP27', 'MEK12']

        self._load_gold_standard()
        self._fetch_normalisation()

    def _load_gold_standard(self):
        filename = self._pj([self._path2data, 'goldstandard', 'D4C3_goldstandard.csv'])
        df = pd.read_csv(filename)
        df.replace('NOT AVAILABLE', np.nan, inplace=True)
        self.goldstandard = df.copy()
        # load gold standard
        # [G G_rowlabels G_collabels] = self.loader(goldfile)
        # G_time = G(:,1)  df.Time_of_Data
        # G = G(:,2:end)   # get rid ot time ?
        # G_idx_30 = find(G_time == 30)  index where time==30
        # G = G(G_idx_30,:)              keep only time 30
        # labels = G_collabels(4:end)    ?
        pass
    
    def download_template(self):
        filename = self._pj([self._path2data, 'templates', 'D4C3_templates.csv'])
        return filename

    def _load_prediction(self, filename):
        df = pd.read_csv(filename)
        df.replace('NOT AVAILABLE', np.nan, inplace=True)
        self.prediction = df.copy()
        # load prediction 
        #files = directory_list(DATADIR)
        #file = [ DATADIR files{1} ]
        #[T T_rowlabels T_collabels] = self.loader(file)
        #T = T(G_idx_30,2:end)
        pass

    def score(self, filename):
        """Compute the score

        See synapse page for details about the scoring function.

        """

        self._load_prediction(filename)

        # compute error and pval for each molecular species


        # some columns have NA that were originally string (NOT AVAILABLE) so
        # those columns are not float type. We need to cast them to float.
        # Besides, we care only about species and time 30
        T = self.prediction[self.species][self.prediction.Time==30].astype(float)
        G = self.goldstandard[self.species][self.goldstandard.Time==30].astype(float)

        self.errors = {}
        self.x_norm_log = {}
        self.y_log = {}
        self.pvals = {}
        for i, species in enumerate(self.species):
            m, b, rho = self._fit_line(species)

            t = T[species]
            g = G[species]

            # zero counting correction prevents log(0)
            x_log = pylab.log10(t + 1)
            y_log = pylab.log10(g + 1)

            # normalise
            x_norm_log = m * x_log + b

            # transform back to original space
            x_norm_lin = 10 ** x_norm_log
            y_lin = 10 ** y_log

            # the same prediction score from DREAM3
            numerator = (y_lin - x_norm_lin) ** 2	# cancels +1 correction
            denominator = 300**2 + (0.08*g) ** 2
            error_individual = numerator / denominator

            # add the individual scores
            self.errors[species] = error_individual.sum()

            # load prob density function
            import scipy.io
            filename = self._pj([self._path2data, 'data', 'pdf_score_%s.mat' % str(i+1)])
            proba = scipy.io.loadmat(filename)
            X, Y, C = proba['X'][0], proba['Y'][0], proba['C'][0]

            # save some information
            self.x_norm_log[species] = x_norm_log.copy()
            self.y_log[species] = y_log.copy()
            self.pvals[species] = self._probability(X, Y, self.errors[species])

        self.prediction_score = -pylab.mean(pylab.log10(self.pvals.values()))
        self.overall_score = self.prediction_score - self.cost_per_link * self.edge_count


        df = pd.DataFrame()
        df['Edge_count'] = [self.edge_count]
        df['Overall_score'] = [self.overall_score]
        df['Prediction_score'] = [self.prediction_score]
        for species in self.species:
            df[species+'_pvalue'] = [self.pvals[species]]
        return df

        #return a final data dataframe


    def plot(self):
        """Plots prediction versus gold standard for each species

        .. plot::
            :include-source:
            :width: 80%

            from dreamtools import D4C3
            s = D4C3()
            filename = s.download_template()
            s.score(filename)
            s.plot()

        """

        if hasattr(self, 'x_norm_log') is False:
            print('Call score() method first. Nothing to plot.')
            return
        pylab.clf()

        for i, species in enumerate(self.species):
            pylab.subplot(3, 3, i+1)
            pylab.plot(self.x_norm_log[species], self.y_log[species], '.')
            pylab.grid(True)
            pylab.axis('equal')


            Xlim = np.array(pylab.xlim())
            Xlim[1] = max([Xlim[1], self.y_log[species].max()])
            Xlim[0]-= 0.5
            Xlim[1]+=0.5


            pylab.plot(Xlim, Xlim, 'k--')


            X = self.x_norm_log[species]
            mask = X.isnull() == False
            N = mask.sum()
            Y = self.y_log[species]
            b, m = np.linalg.lstsq(np.vstack([np.ones(N), X[mask]]).T, Y[mask])[0]
            pylab.plot(Xlim, np.array(Xlim*m+b), 'g-')
            pylab.xlim(Xlim[0])
            #pylab.ylim([x0,x1])
            #print x0,x1


            pylab.title(species)
        pylab.tight_layout()



    def _probability(self, X, Y, x):
        dx = X[1]-X[0]
        P = sum(Y[X <= x])*dx
        return P


    def _fetch_normalisation(self):
        # x is training
        # y is gold
        filename = self._pj([self._path2data, 'data', 'common_training.csv'])
        training = pd.read_csv(filename)

        filename = self._pj([self._path2data, 'data', 'common_gold.csv'])
        goldfile = pd.read_csv(filename)

        #"""function [m b rho] = fetch_normalization(jj)
        #%% jj is the index of the molecule (1-7)

        colnames = self.species

        self.norm_training = pylab.log10(training[colnames] + 1)
        self.norm_gold = pylab.log10(goldfile[colnames] + 1)

        #which one is x/y?
        #[m b rho] = fit_line(x,y);

    def _fit_line(self, species):

        x = self.norm_training[species].dropna().values
        y = self.norm_gold[species].dropna().values
        N = len(x)

        # equivalent to X/y in matlab
        [solution, residuals, ranks, s] = np.linalg.lstsq(np.vstack([np.ones(N), x]).T, y)

        b,m =  solution
        rho = np.corrcoef(x,y)[1,0]
        return m,b,rho






