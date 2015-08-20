"""D3C3 scoring function

Original matlab version (Gustavo A. Stolovitzky, Ph.D. Robert Prill) translated
into Python by Thomas Cokelaer.
"""
from dreamtools.core.challenge import Challenge
import pandas as pd
import numpy as np



class D3C3(Challenge):
    """A class dedicated to D3C3 challenge

    ::

        from dreamtools import D3C3
        s = D3C3()
        filename = s.download_template()
        s.score(filename)

    Data and templates are downloaded from Synapse. You must have a login.

    .. note:: the spearman pvalues are computed using R and are slightly 
        different from the official code that used matlab. The reason 
        being that the 2 implementations are different. Pleasee see cor.test 
        in R and corr() function in matlab for details.
        The scipy.stats.stats.spearman has a very different implementation 
        for small size cases.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D3C3, self).__init__('D3C3')

        #:SubChallenges: different network size (10, 50, 100)

    def download_goldstandard(self):
        return self._pj([self.classpath, 'goldstandard', 
            'D3C3_goldstandard.txt'])

    def score(self, filename):
        self.G = self._read_challenge(self.download_goldstandard())
        self.T = self._read_challenge(filename)

        #from scipy.stats.stats import pearsonr, spearmanr
        G = self.G[self.G.columns[2:]].values
        T = self.T[self.T.columns[2:]].values

        # Using scipy, the pvalue are not the same as in matlab for several reasons.
        # first scipy returns only 2-tail pvalue but more importantly, it is
        # a rough approximation as mentionned in their doc and when compared
        # to matlab differences can be large. So, we use R, which results are
        # also differnt but much close (1-2% different
        """data = [spearmanr(G[i,:], T[i,:]) for i in range(0,50)]
        rho_row = [x[0] for x in data]
        pval_row = [x[1] for x in data]
        # row correlation
        data = [spearmanr(G[:,i], T[:,i]) for i in range(0,8)]
        rho_col = [x[0] for x in data]
        pval_col = [x[1] for x in data]
        """

        from dreamtools.core.rtools import RTools
        rtool = RTools(verboseR=False)
        pval_row = []
        pval_col = []
        rho_row = []
        rho_col = []

        for i in range(0, 50):
            rtool.session.t = T[i, :].copy()
            rtool.session.g = G[i, :].copy()
            rtool.session.run("results = cor.test(t, g, method='spearman', alternative='greater', exact=F)")
            rho_row.append(rtool.session.results['estimate'])
            pval_row.append(rtool.session.results['p.value'])
        for i in range(0, 8):
            rtool.session.t = T[:, i].copy()
            rtool.session.g = G[:, i].copy()
            rtool.session.run("results = cor.test(t, g, method='spearman', alternative='greater', exact=F)")
            rho_col.append(rtool.session.results['estimate'])
            pval_col.append(rtool.session.results['p.value'])


        print("""
WARNING: the spearman correlation pvalue are computed using R. Pvalues are
slightly different from those computed using matlab and therefore the final
values may differ by a few percents to the pvlues reported in the original
challenge. \n""")

        self.rho_col = rho_col
        self.pval_col = pval_col
        self.rho_row = rho_row
        self.pval_row = pval_row

        score1 = np.exp(np.nansum(np.log(pval_row))/50)
        score2 = np.exp(np.nansum(np.log(pval_col))/8.)

        score = sum(-np.log10([score1, score2]))/2.
        return {'score': score}

    def download_template(self):
        return self._pj([self.classpath, 'templates', 'D3C3_template.txt'])

    def _read_challenge(self, filename):
        df = pd.read_csv(filename, sep='\t')
        return df
