
"""D9dot5C2 scoring function"""
import os
from dreamtools.core.challenge import Challenge


class D9dot5C2(Challenge):
    """A class dedicated to D9dot5C2 challenge


    ::

        from dreamtools import D9dot5C2
        s = D9dot5C2()
        filename = s.download_template()
        s.score(filename)

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D9dot5C2, self).__init__('D9dot5C2')
        self._init()
        self.sub_challenges = []

    def _init(self):
        # should download files from synapse if required.
        pass

    def score(self, filename, subname=None, goldstandard=None):
        raise NotImplementedError

    def download_template(self, subname=None):
        # should return full path to a template file
        raise NotImplementedError

    def download_goldstandard(self, subname=None):
        # should return full path to a gold standard file
        raise NotImplementedError
