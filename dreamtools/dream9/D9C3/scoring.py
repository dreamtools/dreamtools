"""D9C3 scoring function


Based on original source code from Mette Peters found at
https://www.synapse.org/#!Synapse:syn4308980

"""
from dreamtools.core.challenge import Challenge
import pandas as pd


class D9C3(Challenge):
    """A class dedicated to D9C3 challenge

    ::

        from dreamtools import D9C3
        s = D9C3()
        filename = s.download_template() 
        s.score(filename) 

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D9C3, self).__init__('D9C3')
        #self._init()
        self.sub_challenges = ['sc1', 'sc2', 'sc3']
        print("GS is not released. Challenge not availabl.")

    def _init(self):
        # should download files from synapse if required.
        self._download_data('q1.final.example.txt', 'syn2703452')
        self._download_data('q1.example_submission.txt', 'syn2509073')
        self._download_data('q2.final.example.txt', 'syn2703453')
        self._download_data('q2.example_submission.txt', 'syn2509074')
        self._download_data('q3.final.example.txt', 'syn2703454')

    def score(self, filename, subname=None):
        self._check_subname(subname)
        if subname == 'sc1':
            return self._score_q1(filename)
        elif subname == 'sc2':
            return self._score_q2(filename)
        elif subname == 'sc3':
            return self._score_q3(filename)

    def _score_q1(self, filename):
        self.prediction = pd.read_csv(filename, sep='\t')
        self.goldstandard = self.prediction.copy()

        #merge
        #calculate correlation 
        #pearson on clin
        #pearson on clin_gen
        #spearman on clin
        #spearman on clin_gen


    # Question 2 - Discordance ------------------------------------------------
    def _score_q2(self, filename):
        #
        # brier metric
        pass

    def _score_q3(self, filename):
        #Question 3 - Predict change in MMSE from image features
        # -----------------

        """wer case sample IDs ex: "sample8" which should be "Sample8"
    predicted$ID <- gsub("sample", "Sample", predicted$ID)

    combined = merge(predicted, observed, by.x='ID', by.y='Sample.ID')
    if (nrow(combined) != nrow(observed)) {
        stop("Sample IDs don't match up")
    }

    ## predicted colnames = "ID", "MMSE", "Diagnosis"
    ## observed colnames = "Sample.ID", ...,  "MMSE_Total", ..., "V1.Conclusion.Disease_Status", ...

    ## compute two statistics on the MMSE
    pearson_mmse = cor(combined$MMSE, combined$MMSE_Total, method="pearson")
    ccc_mmse = epi.ccc(combined$MMSE, combined$MMSE_Total, ci="z-transform", conf.level=0.95)

    percent_correct_diagnosis = sum(combined$Diagnosis==combined$V1.Conclusion.Disease_Status) / nrow(combined) * 100.0

    list(pearson_mmse=pearson_mmse,
         ccc_mmse=ccc_mmse$rho.c$est,
         percent_correct_diagnosis=percent_correct_diagnosis)
        """
        pass

    def download_template(self, subname=None):
        # should return full path to a template file
        if subname == 'sc1':
            filename = self.getpath_template('q1.final.example.txt')
        elif subname == 'sc2':
            filename = self.getpath_template('q2.final.example.txt')
        elif subname == 'sc3':
            filename = self.getpath_template('q3.final.example.txt')
        return filename

    def download_goldstandard(self, subname=None):
        # should return full path to a gold standard file
        # GS is not released!
        raise NotImplementedError

