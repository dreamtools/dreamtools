
import os
from dreamtools.core.challenge import Challenge

class D7C4(Challenge):
    """A class dedicated to D7C4 challenge


    ::

        from dreamtools import D7C4
        s = D7C4()
        filename = s.download_template() 
        s.score(filename) 

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D7C4, self).__init__('D7C4')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]

    def score(self, prediction_file):
        raise NotImplementedError

    def download_template(self):
        raise NotImplementedError
