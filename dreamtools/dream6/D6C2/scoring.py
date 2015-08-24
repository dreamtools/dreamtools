"""D6C2 scoring function

See D7C1

"""
from dreamtools.core.challenge import Challenge

__all__ = ['D6C2']


class D6C2(Challenge):
    """A class dedicated to D6C2 challenge


    ::

        from dreamtools import D6C2
        s = D6C2()
        filename = s.download_template() 
        s.score(filename) 

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D6C2, self).__init__('D6C2')
        self.sub_challenges = []

        msg = "This challenge was re-done in DREAM7. "
        msg += "Please, use D7C1 challenge instead"
        print(msg)

    def score(self, prediction_file):
        raise NotImplementedError

    def download_template(self):
        # should return full path to a template file
        pass
        #raise NotImplementedError

    def download_goldstandard(self):
        # should return full path to a gold standard file
        pass
        #raise NotImplementedError
