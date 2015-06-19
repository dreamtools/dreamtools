"""


"""
import os
from easydev import Logging

class Layout(Logging):
    """Class to create automatic layout for a given challenge


    :Usage:

    ::

        dreamtools-layout --name D8C2


    .. warning:: for developers only.
    """
    def __init__(self, verbose=True):
        super(Layout, self).__init__(verbose=verbose)

        for filename in ['README.rst', '__init__.py']:
            self._create_file(filename)
        for directory in ['data', 'paper', 'templates', 'goldstandard']:
            self._create_directory(directory)

    def _create_init(self):
        pass


    def _create_file(self, filename):
        if os.path.exists(filename) is True:
            self.warning("%s already exists. Skipped the creation of the file" % filename )
        else:
            open(filename, 'a').close()

    def _create_directory(self, directory):
        if os.path.isdir(directory) is True:
            self.warning("%s already exists. Skipped the creation of the file" % directory)
        else:
            os.mkdir(directory)
