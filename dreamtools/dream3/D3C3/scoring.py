"""

Python code implemented by Thomas Cokelaer from matlab version (Gustavo A. Stolovitzky, Ph.D.
Robert Prill).
"""
import os
from dreamtools.core.challenge import Challenge
import pandas as pd

class D3C3(Challenge):
    """A class dedicated to D3C3 challenge


    ::

        from dreamtools import D3C3
        s = D3C3()
        filename = s.download_template() 
        s.score(filename) 

    Data and templates are downloaded from Synapse. You must have a login.

    outputs are	::
    
        overall_gene_profile_pval:	geometric mean of the gene-profile p-values

    	overall_time_profile_pval:	geometric mean of the time-profile p-values

    	rho_gene_profile:		Spearman correlation coeff of gene-profiles

    	pval_gene_profile:		p-value of Spearman correlation coeff

    	rho_time_profile:		Spearman correlation coeff of time-profiles

    	pval_time_profile:		p-value of Spearman correlation coeff

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D3C3, self).__init__('D3C3')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        #self._init()

    def _init(self):
        # should download files from synapse if required.
        #self._download_data('DREAM3GoldStandard_ExpressionChallenge.txt', 'syn3033096')
        #s.get('syn3033092', downloadLocation='data')
        #s.get('syn3033091', downloadLocation='data')
        #s.get('syn3033093', downloadLocation='data')
        pass

    def download_goldstandard(self):
        return self._pj([self._path2data, 'goldstandard', 'D3C3_goldstandard.txt'])

    def score(self, filename):
        self.G = self._read_challenge(self.download_goldstandard())
        self.T = self._read_challenge(filename)

        from scipy.stats.stats import pearsonr
        
        G = self.G[self.G.columns[2:]].values
        T = self.T[self.T.columns[2:]].values
        # column correlation
        data = [pearsonr(G[i,:], T[i,:]) for i in range(0,50)]
        rho_col = [x[0] for x in data]
        pval_col = [x[0] for x in data]
        # row correlation
        data = [pearsonr(G[:,i], T[:,i]) for i in range(0,8)]
        rho_row = [x[0] for x in data]
        pval_row = [x[0] for x in data]

        self.rho_col = rho_col
        self.pval_col = pval_col
        
        """

for ri = 1:size(G,2)
	g = G(:,ri);
	t = T(:,ri);
	[rho, pval] = corr(g,t,'type','Spearman','tail','gt');  % rho greater than zero
	rho_col(ri) = rho;
	pval_col(ri) = pval;
end


%% row correlation
for ci = 1:size(G,1)
	g = G(ci,:)';
	t = T(ci,:)';
	[rho, pval] = corr(g,t,'type','Spearman','tail','gt');  % re-ranks before computing corr coeff 
	rho_row(ci) = rho;
	pval_row(ci) = pval;
end
%% pretty names
%% gene profile:  all genes at a given time-point (a col)
%% time profile:  a single gene across all times (a row)
rho_gene_profile = rho_col;
rho_time_profile = rho_row;
pval_gene_profile = pval_col;
pval_time_profile = pval_row;
%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% summary statistics
%% overall pval is the geometric mean
N = length(pval_time_profile);
overall_time_profile_pval = exp(sum(log(pval_time_profile))/N);

N = length(pval_gene_profile);
overall_gene_profile_pval = exp(sum(log(pval_gene_profile))/N);

%% SCORE
score = sum(-log10([ overall_time_profile_pval overall_gene_profile_pval ]))/2;

        """

    def download_template(self):
        return self._pj([self._path2data, 'template', 'D3C3_template.txt'])


    def _read_challenge(self, filename):
        df = pd.read_csv(filename, sep='\t')
        return df



