"""


"""
from dreamtools.core.challenge import Challenge


class D7C2(Challenge):
    """A class dedicated to D7C2 challenge


    ::

        from dreamtools import D7C2
        s = D7C2()
        filename = s.download_template() 
        s.score(filename) 

    Data and templates are downloaded from Synapse. You must have a login.


as R objects implementing a function called customPredict() that returns a
vector of risk predictors when given a set of feature data as input. The
customPredict()

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D7C2, self).__init__('D7C2')
        self._init()
        self.sub_challenges = []

    def _init(self):
        # should download files from synapse if required.
        pass

    def score(self, filename):
        print("D7C2 Breast Cancer Prognosis is not available right now.\n" + 
                "It will be implemented in dreamtools  version 2\n")

    def download_template(self, subname=None):
        # should return full path to a template file
        raise NotImplementedError

    def download_goldstandard(self, subname=None):
        # should return full path to a gold standard file
        raise NotImplementedError
