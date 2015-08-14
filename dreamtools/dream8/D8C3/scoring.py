
import os
from dreamtools.core.challenge import Challenge


class D8C3(Challenge):
    """A class dedicated to D8C3 challenge


    ::

        from dreamtools import D8C3
        s = D8C3()
        filename = s.download_template() 
        s.score(filename) 

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D8C3, self).__init__('D8C3')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self._init()
        self.sub_challenges = []

        msg = "This challenge is not yet part of DREAmTools"
        msg += "Please, see https://www.synapse.org/#!Synapse:syn1876068/wiki/232963"
        raise NotImplementedError(msg)

    def _init(self):
        # should download files from synapse if required.
        pass

    def score(self, prediction_file):
        raise NotImplementedError

    def download_template(self):
        # should return full path to a template file
        pass
