# -*- python -*-
#
#  This file is part of dreamtools software
#
#  Copyright (c) 2011-2014 - EBI-EMBL
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
"""Module to download final submissions

:status: FINAL

"""
import os
from dreamtools.dream8.D8C1 import submissions
import pandas as pd
from easydev import get_share_file as gsf
from dreamtools.core.sageutils import Login
from  synapseclient import exceptions


class SubmissionsDownloader(object):
    """Tool to download all official submissions from synapse (zipped files).

    ::

        >>> from dreamtools.dream8hpn import downloads
        >>> d = downloads.SubmissionsDownloader(directory="download")
        >>> d.download_all()


    """
    def __init__(self, directory="hpndream8_downloads"):
        self.directory = directory

    def _get_location(self, this):
        path = "/".join([".", self.directory, this])
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

        There is as duplicated filename here. This commandfails::

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



class SurveyInfo(Login):
    """

    Need access to a file called sc1a_survey.xlsx that contains list
    of synapse id of the writeups plus more info.

    :meth:`download_writeup` downlads all writeups and prints
    informative messages.


    :STATUS: used only once to get the writeups. Worked.

    """
    def __init__(self, filename="sc1a_survey_info.csv",client=None):
        super(SurveyInfo, self).__init__(client=client)

        # survey is extracted from
        # https://docs.google.com/spreadsheet/ccc?key=0AjRfQOSvR8KqdGJwSnhmTEhkZkJjbkJJU293aklEcUE&usp=drive_web#gid=3

        if os.path.isfile(filename) == False:
            # try with gsf
            filename = gsf("dreamtools", "data/dream8hpn", filename)

        self.df = pd.read_csv(filename, nrows=78)

        columns = list(self.df.columns)

        columns[2] = "synapseId"
        columns[11] = "pkn_synapseId"
        self.df.columns = columns

    def _get_team_names(self):
        return self.df['Team name']
    teamNames = property(_get_team_names)

    #def _get_writeup_ids(self):
    #    return self.df['writeup_synapseId']
    #writeup_ids = property(_get_writeup_ids)

    def _get_pkn_ids(self):
        return self.df['pkn_synapseId']
    pkn_ids = property(_get_pkn_ids)

    def _download_writeups(self):
        """obsolet
        Download all writeups

        """

        self.writeups = {}
        print("Fetching information")
        for i , id_ in enumerate(self.writeup_ids):
            try:
                entity = self.client.getEntity(id_)
                print(self.teamNames[i] + " ok")
                self.writeups[self.teamNames[i]] = entity
            except exceptions.SynapseHTTPError, e:
                if "lacks read access to" in e.message:

                    print("{} Permission Issue {}".format(self.teamNames[i], id_))
                else:
                    print self.teamNames[i],
                    print e.message + "\n"

            except Exception,e:
                print self.teamNames[i],
                print e.message + "\n"

        print("Downloading")
        if os.path.isdir("sc1a_writeups") ==  False:
            os.mkdir("sc1a_writeups")

        for key in self.writeups.keys():
            try:
                print("{} {}".format(key, self.writeups[key]['id']))
                self.client.get(self.writeups[key]['id'], version=None,
                            downloadLocation="sc1a_writeups")
            except:
                print("Could not download {}".format(key) )

    def download_pkns(self, location="sc1a_pkns"):
        """Downloads all PKNs

        """
        self.pkns = {}
        print("Fetching information")
        for i , id_ in enumerate(self.pkn_ids):
            try:
                id_ = id_.split(":")[-1]
            except:
                print("No valid id provided")
                continue
            if id_.startswith("syn") == False:
                print("No valid id provided")
                continue
            print(id_),
            if pd.isnull(id_) != True:
                try:
                    entity = self.client.getEntity(id_)
                    print(self.teamNames[i] + " ok")
                    self.pkns[self.teamNames[i]] = entity
                except exceptions.SynapseHTTPError, e:
                    if "lacks read access to" in e.message:
                        print("{} Permission Issue {}".format(self.teamNames[i], id_))
                    else:
                        print self.teamNames[i],
                        print e.message + "\n"

                except Exception,e:
                    print self.teamNames[i],
                    print e.message + "\n"
            else:
                print(self.teamNames[i] + " no id provided")

        print("\nDownloading")
        if os.path.isdir(location) ==  False:
            os.mkdir(location)

        for key in self.pkns.keys():
            try:
                print("{} {}".format(key, self.pkns[key]['id']))
                self.client.get(self.pkns[key]['id'], version=None,
                            downloadLocation=location)
            except:
                print("Could not download {}".format(key) )







