# -*- python -*-
#
#  This file is part of DreamTools software
#
#  Copyright (c) 2014-2015 - EBI-EMBL
#
#  File author(s): Thomas Cokelaer <cokelaer@ebi.ac.uk>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  website: http://github.org/dreamtools
#
##############################################################################
from dreamtools.core.rtools import RTools
from dreamtools.core.challenge import Challenge
import os



class D8C2_sc1(Challenge, RTools):
    """Scoring class for D8C2 sub challenge 1

    ::

        from dreamtools impoty D8C2
        s = D8C2_sc1(filename)
        s.run()
        s.df


    see `github README <https://github.com/dreamtools/dreamtools/tree/master/dreamtools/dream8/D8C2>`_ for details

    """

    def __init__(self, filename, verboseR=True):
        Challenge.__init__(self, challenge_name='D8C2')
        RTools.__init__(self, verboseR=verboseR)

        self.filename = filename
        self._path2data = os.path.split(os.path.abspath(__file__))[0]

    def run(self):
        """Compute the score and populates :attr:`df` attribute with results

        """

        script = """
            load("%(path)sdata/data_sch1.RData")
            source("%(path)sfunctionsLeaderboard_sch1.R")
            source("%(path)sprob_Cidx.R")

            load("%(path)stestSubmissions_sch1.RData")
            yourSubmission = read.table("%(filename)s")
            #scoreByCompound<-computeByCompound(submission=randomSubmission1,
            #    observed=observed, metric="pearson", keepCompounds=toxCompoundsID)
            # example2, compute prob C-index for the best Performer (note: prob C-index
            # computation takes some time)
            #scoreByCompound<-computeByCompound(submission=bestPerformer, observed=observed,
            #    metric="probCindex", keepCompounds=toxCompoundsID, pooled_std=pooled_std)
            submissions<-list(bestPerformer=bestPerformer, randomSubmission1=randomSubmission1, 
                yourSubmission=yourSubmission)
            res <- computeOverallScores(submissions)
            """

        print("Running the scoring function. This may take a couple of minutes.")
        params = {'filename':self.filename, 'path':self._path2data + os.sep}
        self.session.run(script % params)
        self.res = self.session.res
        self.df = self.res['summaryScores']
        self.df.index = ['bestPerformer','randomSubmission','yourSubmission']
        self.df.columns = [c.strip() for c in self.df.columns]
        return self.df


