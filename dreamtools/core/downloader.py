import os

from dreamtools.core.sageutils import Login
from dreamtools.core.challenge import Challenge


__all__ = ['Downloader']


class Downloader(Challenge, Login):
    """Factory to download gold standard files"""
    def __init__(self, challenge, client=None):
        """.. rubric:: constructor

        :param str challenge: nickname of a challenge (e.g., D5C1)


        """
        Challenge.__init__(self, challenge_name=challenge)
        Login.__init__(self, client=client)

    def download(self, synid):
        assert synid.startswith('syn'), "synid must be a valid synapse identifier e.g., syn123456"
        self.client.get(synid, downloadLocation=self.directory)


