"""D6C1 scoring function

scoring author: bobby prill
"""
from dreamtools.core.challenge import Challenge


class D6C1(Challenge):
    """A class dedicated to D6C1 challenge


    ::

        from dreamtools import D6C1
        s = D6C1()
        filename = s.download_template() 
        s.score(filename) 

    .. todo:: not yet implemented. Requires code to compute the 
        recall and precision from the GS and submission.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D6C1, self).__init__('D6C1')
        self._init()
        self.sub_challenges = []

    def _init(self):
        # should download files from synapse if required.
        pass

    def score(self, filename):
        raise NotImplementedError


        # heere, filename is not a prediction but 
        # a prediction already processed using a software/algo
        # that cannot be retrieved yet from any resources 
        # (synapse/developers)
        data = pd.read_csv(filename, sep="\t")

        P = data['GS'][0]           # positives
        K = data['PRED']    # index
        TP = data['PRED_WITH_GS']     # prediction in gold standard
        rec = TP / P                # traditional recall
        rec = data['PRECISION']     # Nicolas's way 
        prec = TP / K               # precision

        from dreamtools.core.rocs import BinaryClassifier
        bc = BinaryClassifier()
        bc.recall = rec
        bc.precision = prec
        aupr = bc.compute_aupr()
        return aupr

    def download_template(self):
        # should return full path to a template file
        raise NotImplementedError

    def download_goldstandard(self):
        # should return full path to a gold standard file
        raise NotImplementedError
