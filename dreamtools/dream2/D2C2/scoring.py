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
"""D2C2 scoring function.


Implementation in Python based on a MATLAB code from
Gustavo A. Stolovitzky

"""
import os
from dreamtools.core.challenge import Challenge
import pandas as pd
from dreamtools.core.rocs import D3D4ROC, DREAM2


class D2C2(Challenge, D3D4ROC, DREAM2):
    """A class dedicated to D2C2 challenge

    ::

        from dreamtools import D2C2
        s = D2C2()
        filename = s.download_template()
        s.score(filename)

    """
    def __init__(self):
        """.. rubric:: constructor"""
        super(D2C2, self).__init__('D2C2')

    def download_template(self):
        """Returns a valid template"""
        return self._pj([self.classpath, 'templates', 'D2C2_template.txt'])

    def download_goldstandard(self):
        """Returns the gold standard"""
        return self._pj([self.classpath, 'goldstandard',
            'D2C2_goldstandard.txt'])

    def score(self, filename):
        """Returns statistics (e.g. AUROC)

        :param str filename: a valid filename as returned by
            :meth:`download_template`

        """
        gold = self.download_goldstandard()

        self.gold_edges = pd.read_csv(gold, sep='\t', header=None)
        self.prediction = pd.read_csv(filename, sep='\t', header=None)

        #
        newtest = pd.merge(self.prediction, self.gold_edges,
            how='inner', on=[0, 1])

        test = list(newtest['2_x'])
        gold_index = list(newtest['2_y'])

        AUC, AUROC, prec, rec, tpr, fpr = self.get_statistics(self.gold_edges,
            self.prediction, gold_index)

        # specific precision values
        P = self.gold_edges[2].sum()
        spec_prec = self.compute_specific_precision_values(P, rec)

        # for plotting
        self.metrics = {'AUPR': AUC, 'AUROC': AUROC ,
            'tpr':  tpr, 'fpr':  fpr,
            'rec':  rec, 'prec':  prec,
            'precision at nth correct prediction':  spec_prec}

        results = {'AUPR': AUC, 'AUROC': AUROC}
        results['precision at nth correct prediction'] = spec_prec

        return results





