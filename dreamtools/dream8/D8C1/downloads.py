# -*- python -*-
#
#  This file is part of dreamtools software
#
#  Copyright (c) 2014-2015 - EBI-EMBL
#
#  File author(s): Thomas Cokelaer <cokelaer@ebi.ac.uk>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  website: http://github.com/dreamtools
#
##############################################################################
"""Module to download final submissions for admin usage only

:status: FINAL

"""
import os
from dreamtools.dream8.D8C1 import submissions
from dreamtools.core.sageutils import Login


class SubmissionsDownloader(Login):
    """Tool to download all official submissions from synapse (zipped files).

    ::

        >>> from dreamtools.dream8.D8C1 import downloads
        >>> d = downloads.SubmissionsDownloader(directory="download")
        >>> d.download_all()


    """
    def __init__(self,  client=None):
        super(SubmissionsDownloader, self).__init__(client=client)
        from dreamtools import configuration as cfg
        mainpath = cfg.user_config_dir
        self.directory = os.sep.join([mainpath, "dream8", "D8C1", "submissions"])

    def _get_location(self, this):
        path = self.directory + os.sep + this
        if os.path.exists(self.directory) == False:
            os.mkdir(self.directory)
        if os.path.exists(path) == False:
            os.mkdir(path)
        return path

    def download_all(self):
        """Download all submissions from the 4 subchallenges"""
        self.download_all_sc1a_final_submissions()
        self.download_all_sc2a_final_submissions()
        self.download_all_sc1b_final_submissions()
        self.download_all_sc2b_final_submissions()

    def download_all_sc1a_final_submissions(self):
        """Download all submissions from the SC1A subchallenge"""
        s = submissions.SC1ASubmissions()
        s.load_submissions()
        for i, sub in enumerate(s.submissions):
            s.client.downloadSubmissionAndFilename(sub, downloadFile=True,
                    downloadLocation=self._get_location("sc1a"))
            print "downloading %s/%s"  % (i+1, len(s.submissions))

    def download_all_sc1b_final_submissions(self):
        """Download all submissions from the SC1B subchallenge

        There is a duplicated filename here. This command fails::

            easydev.swapdict([(x['submitterAlias'],
                    json.loads(x['entityBundleJSON'])['fileHandles'][0]['fileName'])
                                for x in s.submissions])

        The duplicated name is Bing-Network from Bing or Cai team name
        """
        s = submissions.SC1BSubmissions()
        s.load_submissions()
        for i,sub in enumerate(s.submissions):
            s.client.downloadSubmissionAndFilename(sub, downloadFile=True,
                    downloadLocation=self._get_location("sc1b"))
            print "downloading %s/%s"  % (i+1, len(s.submissions))

    def download_all_sc2a_final_submissions(self):
        """Download all submissions from the SC2A subchallenge"""
        s = submissions.SC2ASubmissions()
        s.load_submissions()
        for i,sub in enumerate(s.submissions):
            s.client.downloadSubmissionAndFilename(sub, downloadFile=True,
                    downloadLocation=self._get_location("sc2a"))
            print "downloading %s/%s"  % (i+1, len(s.submissions))

    def download_all_sc2b_final_submissions(self):
        """Download all submissions from the SC2B subchallenge"""
        s = submissions.SC2BSubmissions()
        s.load_submissions()
        for i,sub in enumerate(s.submissions):
            s.client.downloadSubmissionAndFilename(sub, downloadFile=True,
                    downloadLocation=self._get_location("sc2b"))
            print "downloading %s/%s"  % (i+1, len(s.submissions))


class GSDownloader(Login):
    """Factory to download gold standard files

    .. todo:: could be replaced with the dreamtools.core.download.Downloader class
    """
    def __init__(self, client=None):
        super(GSDownloader, self).__init__(client=client)
        from dreamtools import configuration as cfg
        mainpath = cfg.user_config_dir
        self.directory = os.sep.join([mainpath, "dream8", "D8C1"])


    def download_experimental(self):
        self.client.get("syn1920412", downloadLocation=self.directory)




