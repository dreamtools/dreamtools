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
"""Concordance index computation (exact version)

Based on R code provided by Ben Sauerwine and Erhan Bilal
double checked with concordance.index from survcomp R package.
"""
# some resources : ftp://ftp.esat.kuleuven.be/sista/vanbelle/reports/07-213.pdf
# nice blog : http://sauerwine.blogspot.co.uk/2012/03/concordance-index-and-cox-modeling.html
# See notebook concordanceIndex
# Cython version speedup the code by 1.5 times only.


#    This code seems to be much faster (10-20 times) than R code
#    exactConcordanceIndex.R to be found in D7C2/misc and 2 times
#    faster than original R code exactConcordanceIndexV.R
#    (vectorised) to be found in the same directory.
#
#    A Cython version showed a slight increase of 1.5, so we keep a pure Python
#    implementation for simplicity.


def concordanceIndex(prediction, survtime, survevent):
    return cindex(prediction, survtime, survevent)


def cindex(prediction, survtime, survevent):
    """Function to compute the concordance index for a risk prediction,
    i.e., the probability that, for a pair of randomly chosen
    comparable samples, the sample with the higher risk prediction
    will experience an event before the other sample or belongs to a
    higher binary class.

    :param prediction: a vector of risk predictions.
    :param survtime: a vector of event times.
    :param survevent: a vector of event occurence indicators (True and False).

    :: 

        >>> from dreamtools.core.cindex import cindex
        >>> print(cindex([0, 1, 3,4], [0, 4, 3, 1], [True]*4))
        0.5
        >>> print(cindex([0, 1, 3,4], [0, 1, 3, 4], [True]*4))
        0.0

    """
    count = 0
    score = 0

    N = len(survtime)

    for i in xrange(0, N-1):
        for j in xrange(i+1, N): # For each pair of observations
            if (((survevent[i] == True) and (survevent[j] == True)) or \
                ((survevent[i] == True) and (survtime[j] >= survtime[i])) or \
                ((survevent[j] == True) and (survtime[i] >= survtime[j]))):

                # This pair is comparable.
                count = count + 2

                if (survtime[i] < survtime[j]) :
                    if (prediction[i] > prediction[j]) :
                        score = score + 2
                    if (prediction[i] == prediction[j]):
                        score = score + 1  # This line needs a test !!

                if (survtime[i] == survtime[j]) :
                    if (prediction[i] == prediction[j]) :
                        score = score + 2

                if (survtime[i] > survtime[j]):
                    if (prediction[i] < prediction[j]):
                        score = score + 2
                    if (prediction[i] == prediction[j]):
                        score = score + 1
    return score/float(count)


class ConcordanceIndex(object):
    """See :func:`cindex` function for details"""
    def __init__(self, survtime=None, survevent=None):
        print('Experimental version. API may change. Use the function concordanceIndex instead.')
        self.survtime = survtime
        self.survevent = survevent

    def cindex(self, prediction):
        """Returns concordance index"""
        return concordanceIndex(prediction, self.survtime, self.survevent)

    def _test(self):
        self.survtime = [1.078304837, 2.646866651, 1.165920248,
                0.537903100, 1.726597615, 1.166453794, 0.080994131,
                0.102762485, 2.434480043, 0.170285918, 0.211224424,
                0.335248849, 1.172972616, 0.018286180, 0.810920450,
                0.447176348, 1.034328426, 0.504800631, 0.159534333,
                0.583315557]
        self.survevent = [True] * len(self.survtime)

        self.predictions = [15.325381588,  3.485879452, 10.993454286,
                0.775569668, 9.718363379, 1.011624518, 24.066998015,
                10.644879046,  8.246779821, 4.644882463, 0.003919197,
                10.186298220,  3.734309896, 16.905509362, 7.384189707,
                2.594689418,  3.701121718, 9.671040180, 7.414466980,
                3.289922854]
        return self.cindex(self.predictions)
