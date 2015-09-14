# -*- python -*-
#
#  This file is part of DREAMTools software
#
#  Copyright (c) 2014-2015 - EBI-EMBL
#
#  File author(s): Thomas Cokelaer <cokelaer@ebi.ac.uk>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  website: http://github.org/dreamtools
#
##############################################################################
"""Common utility to all challenges"""
import os
import sys
import re

from dreamtools import configuration as cfg


__all__ = ['LocalData', 'Challenge']


class LocalData(object):
    def __init__(self):
        # dynamically find the path of the module.
        filename = os.path.abspath(sys.modules[self.__module__].__file__)
        self.classpath = filename.rsplit(os.sep, 1)[0]

    def getpath_data(self, filename):
        filename = self._pj([self.classpath, 'data', filename])
        assert os.path.exists(filename), 'file %s does not exists' % filename
        return filename

    def getpath_template(self, filename):
        filename = self._pj([self.classpath, 'templates', filename])
        assert os.path.exists(filename), 'file %s does not exists' % filename
        return filename

    def getpath_gs(self, filename):
        filename = self._pj([self.classpath, 'goldstandard', filename])
        assert os.path.exists(filename), 'file %s does not exists' % filename
        return filename

    def getpath_lb(self, filename):
        filename = self._pj([self.classpath, 'leaderboard', filename])
        assert os.path.exists(filename), 'file %s does not exists' % filename
        return filename

    def _pj(self, listdir):
        return os.sep.join(listdir)


class Challenge(LocalData):
    """Common class to all challenges


    If you have not setup a .synapseConfig in your HOME,
    you must provide a synapse client

    ::

        from dreamtools import *
        s = Challenge('D2C1')
        client = Login(username=username, password=pwd).client
        s.client = client

    """

    def __init__(self, challenge_name):
        """.. rubric:: constructor

        :param str challenge_name: Must be formatted as DXCY
            where X and Y are numbers. Intermediate challenges from
            e.g. D9.5 should be encoded as D9dot5CY

        """
        super(Challenge, self).__init__()

        #: alias of the challenge as DXCY form with X, Y being 2 numbers
        self.debug = False
        self.alias = challenge_name
        self._check_challenge_name()
        #: directory where is stored the configuration file and data files.
        self.mainpath = cfg.user_config_dir

        # More METADATA
        self.sub_challenges = []

        # Get data from the README if possible
        try:
            metadata = self._get_metadata()
            self.synapseId = metadata['synapseId']
            self.summary = metadata['summary']
            self.title = metadata['title']
        except:
            self.synapseId = 'undefined'
            self.summary = 'undefined'
            self.title = 'undefined'

        # initialisation
        self.mkdir()

        self.client = None

    def _get_directory(self):
        """Gets directory where data will be stored."""
        name_dir = self._get_challenge_directory()
        directory = os.sep.join([self.mainpath, name_dir, self.alias])
        return directory
    directory = property(_get_directory)

    def _check_challenge_name(self):
         results = re.search("^D\d+(dot5)?C\d+$", self.alias)
         if results is None:
            msg = "Challenge name provided (%s) is incorrect expects DXCY with X and Y as numbers. Or possibly DXdot5CY (e.g. D8C3, D9dot5C2)"
            raise ValueError(msg % self.alias)

    def _get_challenge_directory(self):
        # name is e.g., D1C2 we want to extract the 1 (with more than 1 digit)
        name = self.alias[1:] # get rid of first letter D
        version = name.split("C")[0]
        return "dream" + str(version)

    def mkdir(self):
        """Creates local dreamtools directory"""
        directory = self._get_challenge_directory()
        directory = os.sep.join([self.mainpath, directory])
        if os.path.exists(directory) is False:
            os.mkdir(directory)
        directory = self._get_directory()
        if os.path.exists(directory) is False:
            os.mkdir(directory)

    def download_template(self, sub_challenge=None):
        """Must be provided"""
        raise NotImplementedError

    def score(self, filename, sub_challenge=None):
        """Must be provided"""
        raise NotImplementedError

    def import_scoring_class(self):
        """Dynamic import of a challenge class

        ::

            c = Challenge('D7C1')
            inst_class = c.import_scoring_class()


        """
        import imp
        import dreamtools

        pathname = os.path.split(dreamtools.__file__)[0]
        pathname += os.sep + self._get_challenge_directory()
        pathname += os.sep + self.alias
        pathname += os.sep + 'scoring.py'
        py_mod = imp.load_source('scoring', pathname)
        class_inst = getattr(py_mod, self.alias)()

        return class_inst

    def _download_data(self, name, synid):
        # name is not strictly required but if already found,
        # it will not be downloaded again
        from dreamtools.core.downloader import  Downloader

        filename = self.directory + os.sep + name
        if os.path.exists(filename) is False:
            # must download the data now
            print("File %s not found. Downloading from Synapse." % filename)
            d = Downloader(self.alias, self.client)
            d.download(synid)
            # save the login if needed again, it will be faster
            self.client = d.client

        return filename

    def get_pathname(self, filename):
        """Return pathname of a file to be found on ./config/dreamtools
        if available"""
        filename = self.directory + os.sep + filename
        if os.path.exists(filename) is False:
            raise ValueError("Could not find the file %s in %s" % (filename, self.directory))
        return filename

    def loadmat(self, filename):
        """Load a MATLAB matrix"""
        import scipy.io
        return scipy.io.loadmat(filename)

    def unzip(self, filename):
        """Simple method to extract all files contained in an archive"""
        from dreamtools.core.ziptools import ZIP
        z = ZIP()
        z.loadZIPFile(self.get_pathname(filename)), z.extractall(self.directory)
    def _check_subname(self, subname):
        from easydev import check_param_in_list
        check_param_in_list(subname, self.sub_challenges)

    def __str__(self):
        txt = """Challenge %s\n""" % self.alias
        txt += "=" * len(txt) + "\n"
        if len(self.sub_challenges):
            txt += """Note that this challenge contains sub-challenges.\n"""
            for this in self.sub_challenges:
                txt += " * %s \n" % this
            txt += "\n"

        metadata = """
:Title: %(title)s
:Alias: %(alias)s
:Summary: %(summary)s
:SubChallenges: %(subchallenge)s
:Synapse page: https://www.synapse.org/#!Synapse:%(synapseId)s"""


        txt += metadata % {
            'alias': self.alias,
            'title': self.title,
            'summary': self.summary,
            'subchallenge': " ".join(self.sub_challenges),
            'synapseId': self.synapseId}
        txt += """\n\n\nVisit http://dreamchallenges.org to get more information about the challenge\n\n\n"""

        txt += "Any issues/suggestions about DREAMTools itself ? "
        txt += "Please visit http://github.com/dreamtools/\n\n"

        return txt

    def _get_metadata(self):
        metadata = {
                'title': 'undefined',
                'summary':'undefined',
                'synapse page':'undefined'}

        filename = self.classpath + os.sep + "README.rst"
        if os.path.exists(filename) is False:
            print("Missing README.rst. Please add one in %s" % self.alias)
        data = open(filename, 'r').read()
        for line in data.split("\n"):
            for prefix in ['title', 'summary', 'synapse page']:
                if line.lower().startswith(":" + prefix + ":"):
                    N = len(prefix) + 2
                    metadata[prefix] = line[N:].strip()

        for k, v in metadata.items():
            if metadata[k] == 'undefined':
                if self.debug:
                    print("Did not find %s in README.rst" % k)
        metadata['synapseId'] = metadata['synapse page'].split("!Synapse:")[1]

        return metadata

    def test(self):
        if len(self.sub_challenges) == 0:
            self.download_template()
            self.download_goldstandard()
        else:
            for subname in self.sub_challenges:
                self.download_template(subname)
                self.download_goldstandard(subname)
        print(self)
