
import os
from dreamtools.core.challenge import Challenge


class D4C2(Challenge):
    """A class dedicated to D4C2 challenge


    ::

        from dreamtools import D4C2
        s = D4C2()
        filename = s.download_template() 
        s.score(filename) 

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D4C2, self).__init__('D4C2')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self._init()

    def _init(self):
        # should download files from synapse if required.
        pass

    def score(self, prediction_file):
        raise NotImplementedError

    def download_template(self):
        # should return full path to a template file
        pass
