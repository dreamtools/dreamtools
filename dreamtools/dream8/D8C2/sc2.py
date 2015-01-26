from dreamtools.core.rtools import RTools
import os


__all__ = ['D8C2_sc2']

class D8C2_sc2(RTools):
    """D8C2 Tox challenge scoring (sub challenge 2)

    ::

        from dreamtools.dream8.D8C2.sc2 import D8C2_s2
        s = D8C2_sc2(filename)
        s.run()
        s.df

    """

    def __init__(self, filename, verboseR=True):
        super(D8C2_sc2,self).__init__(verboseR=verboseR)
        self.filename = filename
        self._path2data = os.path.split(os.path.abspath(__file__))[0]

    def run(self):
        """Compute the score and populates :attr:`df` attribute with results"""

        script = """
            load("%(path)sdata/data_sch2.RData")
            source("%(path)sfunctionsLeaderboard_sch2.R")
            source("%(path)sprob_Cidx.R")

            load("%(path)stestSubmissions_sch2.RData")
            yourSubmission = read.table("%(filename)s")
            #scoreByCompound<-computeByCompound(submission=randomSubmission2,
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
        self.df = self.session.res.copy()
        self.df.index = ['bestPerformer','randomSubmission','yourSubmission']
        self.df.columns =  [c.strip() for c in self.df.columns]
        return self.df


