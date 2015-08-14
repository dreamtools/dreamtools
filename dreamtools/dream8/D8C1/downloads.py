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

    .. note:: This is for admin usage only

    ::

        >>> from dreamtools.dream8.D8C1 import downloads
        >>> d = downloads.SubmissionsDownloader()
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

    def _download(self, subs, location):
        subs.load_submissions()
        for i, sub in enumerate(subs.submissions):
            subs.client.downloadSubmissionAndFilename(sub, downloadFile=True,
                    downloadLocation=self._get_location("sc1a"))
            print("downloading %s/%s"  % (i+1, len(subs.submissions)))

    def download_all_sc1a_final_submissions(self):
        """Download all submissions from the SC1A subchallenge"""
        subs = submissions.SC1ASubmissions()
        self._download(subs, 'sc1a')

    def download_all_sc1b_final_submissions(self):
        """Download all submissions from the SC1B subchallenge"""
        # Note:  The duplicated name is Bing-Network from Bing or Cai team name
        subs = submissions.SC1BSubmissions()
        self._download(subs, 'sc1b')

    def download_all_sc2a_final_submissions(self):
        """Download all submissions from the SC2A subchallenge"""
        subs = submissions.SC2ASubmissions()
        self._download(subs, 'sc2a')

    def download_all_sc2b_final_submissions(self):
        """Download all submissions from the SC2B subchallenge"""
        subs = submissions.SC2BSubmissions()
        self._download(subs, 'sc2b')





