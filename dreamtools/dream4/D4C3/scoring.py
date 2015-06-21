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

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D4C3, self).__init__('D4C3')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]

        # cost_per_link Was determined empirically from all the teams' submissions
        # as r = min(prediction_score / edge_count).
        self.cost_per_link = 0.0827;

    def load_gold_standard(self):
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

    def load_prediction(self, filename):
        df = pd.read_csv(filename)
        df.replace('NOT AVAILABLE', np.nan, inplace=True)
        self.templates = df.copy()
        # load prediction 
        #files = directory_list(DATADIR)
        #file = [ DATADIR files{1} ]
        #[T T_rowlabels T_collabels] = self.loader(file)
        #T = T(G_idx_30,2:end)
        pass

    def score(self, prediction_file):
        raise NotImplementedError

        """
%
% This function produces the DREAM4 scores for Challenge 3.
%
% See go.m for an example of how to call it.
%

%PDFDIR  = '../INPUT/probability_densities/';
%edge_count = 20;

goldfile = [ GOLDDIR 'DREAM4_GoldStandard_SignalingNetworkPredictions_Test.csv' ];
PDF_ROOT = 'pdf_score_';


%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% compute error and pval for each molecular species

figure(1)
pn = 4;
pm = 3;
pj = 0;

%% for each molecular species (column)
for si = 1:size(G,2)
%for si = 1;

	%% fetch normalization based on common experiments
	[m b rho] = fetch_normalization(si);

	%% one column at a time
	t = T(:,si);
	g = G(:,si);

	%% zero counting correction prevents log(0)
	x_log = log10(t + 1);
	y_log = log10(g + 1);

	%% normalize
	x_norm_log = m * x_log + b;

	%% transform back to original space
	x_norm_lin = 10.^x_norm_log;
	y_lin = 10.^y_log;

	%% the same prediction score from DREAM3
	numerator = (y_lin - x_norm_lin).^2;	%% cancels +1 correction
	denominator = 300^2 + (0.08*g).^2;
	error_individual = numerator ./ denominator;

	%% add the individual scores
	idx = find(~isnan(error_individual));
	errors(si) = sum(error_individual(idx));

	%% load prob density function
	pdffile = [ PDFDIR PDF_ROOT num2str(si) ];
	load(pdffile)		%% sets X, Y, C

	%% compute pval
	x = errors(si);
	p = probability(X,Y,x);
	pvals(si) = p;

	%% show something
	pj = pj + 1;
	subplot(pn,pm,pj)
	plot(x_norm_log,y_log,'.')
	LIM = [ min(axis) max(axis) ];
	axis square; axis equal; axis([LIM LIM]);
	grid on
	lsline
	hold on
	plot(LIM,LIM,'k--')
	hold off
	title(labels{si})

end

prediction_score = -mean(log10(pvals)')';
overall_score = prediction_score - COST_PER_LINK .* edge_count;
    """

    def plot(self):
        # %% annotate plot
        # subplot(pn,pm,1)
        # xlabel('norm. prediction (log_1_0)')
        # ylabel('gold (log_1_0)')
        pass

    def loader(self, filename):
        # function [A rowlabels collabels] = loader(filename)
        # d = importdata(filename);
        # A = d.data;
        # collabels = d.textdata(1,:);
        # rowlabels = [ d.textdata(:,1) d.textdata(:,2) ];
        pass

    def probability(self):
        # % P(X<=x)
        # function P = probability(X,Y,x)

        # dx = X(2)-X(1);
        # P = sum( double(X<=x) .* Y * dx );
        pass

    def fetch_normalisation(self):

        filename = self._pj([self._path2data, 'data', 'common_training.csv'])
        training = pd.read_csv(filename)

        filename = self._pj([self._path2data, 'data', 'common_gold.csv'])
        goldfile = pd.read_csv(filename)

        #"""function [m b rho] = fetch_normalization(jj)
        #%% jj is the index of the molecule (1-7)

        colnames = ['AKT', 'ERK12', 'Ikb', 'JNK12', 'p38', 'HSP27', 'MEK12']

        self.norm_training = pylab.log10(training[colnames] + 1)
        self.norm_gold = pylab.log10(goldfile[colnames] + 1)

        #which one is x/y?
        #[m b rho] = fit_line(x,y);

    def fit_line(self, species):
        """
        function [m b rho] = fit_line(x,y)

        %% remove Nan
        idx = find(~isnan(x));
        x = x(idx,:);
        y = y(idx);

        %% linear fit
        X = [ ones(length(x),1) x ];
        myfit = X \ y;
        b = myfit(1);
        m = myfit(2);

        %% corr coeff
        rho = corr(x,y);
        """

        x = np.array(self.norm_gold[species])
        y = np.array(self.norm_training[species])
        N = 30
        b = np.array([1]*30)  / y
        m = x / y
        rho = np.corrcoef(x,y)[1,0]
        return b,m,rho


    def preprocess_prediction(self):
        """
cd my_prediction
for f in *
    do

        outfile="../my_processed_prediction/$f"

            echo
                echo "Processing prediction file in INPUT/my_prediction"
                    echo

                        ## change these strings to NaN (what Matlab likes)
                            cat $f | sed 's/NOT AVAILABLE/NaN/g' | sed 's/NA/NaN/g' | sed 's/"//g' > $outfile

                                echo "Wrote output file to INPUT/my_processed_prediction"
                                    echo

                                    done

    """



