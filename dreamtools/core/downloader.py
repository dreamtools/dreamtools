import os

from dreamtools.core.sageutils import Login
from dreamtools.core.challenge import Challenge


__all__ = ['Downloader']


class Downloader(Challenge, Login):
    """Factory to download gold standard files"""
    def __init__(self, challenge, client=None):
        """.. rubric:: constructor

        :param str challenge: nickname of a challenge (e.g., D5C1)

        To automatically connect to synapse, create a file called .synapseConfig with this
        content::

            [authentication]
            username: email
            password: password

        """
        Challenge.__init__(self, challenge_name=challenge)
        Login.__init__(self, client=client)

    def download(self, synid):
        """Download a file into the dreamtools directory
        
        :param synid: a valid synapse id (e.g., syn123456)

        You must have a login on synapse website. 
        """
        assert synid.startswith('syn'), "synid must be a valid synapse identifier e.g., syn123456"
        self.client.get(synid, downloadLocation=self.directory)


