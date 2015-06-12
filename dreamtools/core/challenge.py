import os
import re
from dreamtools import configuration as cfg


class Challenge(object):
    """Handler for the creation of config directory for each challenge"""

    def __init__(self, challenge_name):
        """

        """
        self.nickname = challenge_name
        self._check_challenge_name()
        self.mainpath = cfg.user_config_dir

    def _get_directory(self):
        """Gets directory where data will be stored."""
        name_dir = self._get_challenge_directory()
        directory = os.sep.join([self.mainpath, name_dir, self.nickname])
        return directory
    directory = property(_get_directory)

    def _check_challenge_name(self):
         results = re.search("^D\d+C\d+$", self.nickname)
         if results is None:
            msg = "Challenge name provided (%s) is incorrect expects DXCY with X and Y as numbers"
            raise ValueError(msg % name)

    def _get_challenge_directory(self):
        # name is e.g., D1C2 we want to extract the 1 (with more than 1 digit)
        name = self.nickname[1:] # get rid of first letter D
        version = name.split("C")[0]
        return "dream" + str(version)

    def mkdir(self):
        """Creates directory if does not exist already"""
        directory = self.get_directory()
        if os.path.exists(directory) is False:
            os.mkdir(directory)
        


