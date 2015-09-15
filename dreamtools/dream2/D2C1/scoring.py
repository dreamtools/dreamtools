# -*- python -*-
# -*- coding: utf-8 -*-
#
#  This file is part of DREAMTools software
#
#  Copyright (c) 2015, DREAMTools Development Team
#  All rights reserved
#
#  Distributed under the BSD 3-Clause License.
#  See accompanying file LICENSE distributed with this software
#
#  File author(s): Thomas Cokelaer <cokelaer@ebi.ac.uk>
#
#  website: http://github.com/dreamtools
#
##############################################################################
"""D2C2 scoring function

Class imlemented in Python based on original code in MATLAB from
Gustavo A. Stolovitzky.

"""
import pandas as pd
import numpy as np
from dreamtools.core.challenge import Challenge
from dreamtools.core.rocs import D3D4ROC, DREAM2


class D2C1(Challenge, D3D4ROC, DREAM2):
    def __init__(self):
        super(D2C1, self).__init__('D2C1')

        filename = [self.classpath, "data", "BCL6_targets_and_decoys.xls"]
        filename = self._pj(filename)
        self.decoys = pd.read_excel(filename)

    def _create_templates(self, filename='test_BCL6targets.txt'):
        templates = self.decoys.copy()
        templates['scores'] = np.random.random(200)
        df = templates[['Entrez GeneID', 'scores']]

        df = df.sort(columns=['scores'], ascending=[False])
        df.to_csv(filename, sep='\t', header=None, index=False)

    def download_template(self):
        """Returns D2C1 template location"""
        return self._pj([self.classpath, 'templates', 'D2C1_template.tsv'])

    def download_goldstandard(self):
        """Returns D2C1 gold standard file location"""
        return self._pj([self.classpath, 'goldstandard',
                        'D2C1_goldstandard.tsv'])

    def score(self, filename):
        """Returns statistics (e.g. AUPR/AUROC)

        :param str filename: a valid filename as returned by
            :meth:`download_template`

        """
        # SEE one of later challenges. Same methodology!
        # gold standard edges only
        gold = self.download_goldstandard()

        # load predictions
        self.gold_edges = pd.read_csv(gold, sep='\t', header=None)
        self.prediction = pd.read_csv(filename,  sep='\t', header=None)

        #
        newtest = pd.merge(self.prediction, self.gold_edges,
                how='inner', on=[0])

        test = list(newtest['1_x'])
        gold_index = list(newtest['1_y'])

        AUC, AUROC, prec, rec, tpr, fpr = self.get_statistics(self.gold_edges,
            self.prediction, gold_index)

        # specific precision values
        P = self.gold_edges[1].sum()
        spec_prec = self.compute_specific_precision_values(P, rec)

        # for plotting
        self.metrics = {'AUPR':AUC, 'AUROC':AUROC ,
            'tpr':  tpr, 'fpr':  fpr,
            'rec':  rec, 'prec':  prec,
            'precision at nth correct prediction':  spec_prec}

        results = {'AUPR':AUC, 'AUROC':AUROC }
        # precision at nth correct prediction
        results['precision_1st'] = spec_prec[1]
        results['precision_2nd'] = spec_prec[2]
        results['precision_5th'] = spec_prec[5]
        results['precision_20th'] = spec_prec[20]

        return results

    def score_and_compare_with_lb(self, filename):
        """Example of a comparative leaderboard that scores """
        lbofficial = self.load_leaderboard()
        df = self.score(filename)
        df = pd.DataFrame(df, index=[0])
        df['Team'] = 'DREAMTools'
        lb = pd.concat([lbofficial, df])
        lb = lb.sort(columns='AUROC', ascending=False)
        lb = lb[lbofficial.columns]
        lb.set_index('Team')
        return lb

    def load_leaderboard(self):
        filename = self.getpath_lb("D2C1_leaderboard.csv")
        df = pd.read_csv(filename)
        df.columns = [x.strip() for x in df.columns]
        return df


