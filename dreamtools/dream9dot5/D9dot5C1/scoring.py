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
"""D9dot5C1 challenge scoring functions"""
import os
import pandas as pd

from easydev import TempFile, shellcmd
from dreamtools.core.ziptools import ZIP
from dreamtools.core.challenge import Challenge
from dreamtools.core.downloader import Downloader


__all__ = ['D9dot5C1']


class D9dot5C1(Challenge):
    """A class dedicated to D9dot5C1 challenge


    ::

        from dreamtools import D9dot5C1
        s = D9dot5C1()

        s.download_templates()
        s.score('templates.txt.gz') # takes about 5 minutes


    """
    def __init__(self):
        """.. rubric:: constructor """
        super(D9dot5C1, self).__init__('D9dot5C1')
        self.sub_challenges = ['sc1','sc2']

        self.download_gs()

    def score(self, filename, sub_challenge_name):

        if sub_challenge_name == 'sc1':
            self.score_sc1(filename)
        if sub_challenge_name == 'sc2':
            self.score_sc2(filename)
        else:
            raise ValueError('Invalid sub challenge name. Use %s' % self.sub_challenges)

    def score_sc1(self, prediction_file):
        """Compute all results and compare user prediction with all official participants

        This scoring function can take a long time (about 5-10 minutes).
        """
        fh = TempFile()
        gs1, _ = self.download_gs()
        script = self.classpath + os.sep + "DREAM_Olfaction_scoring_Q1.pl"
        cmd = "perl %s %s %s %s"
        cmd = cmd % (script, prediction_file, fh.name, gs1)
        shellcmd(cmd)
        df = pd.read_csv(fh.name, sep='\t', index_col=None).ix[0]
        fh.delete()
        return df


        # score sub1 = (zint +zple +zdec)/3
        # sigma_int = 0.0787
        # sigma_ple = 0.176
        # signa_dec = 0.0042

        # final is average of zscores

    def score_sc2(self, prediction_file):
        fh = TempFile()
        _, gs2 = self.download_gs()
        script = self.classpath + os.sep + "DREAM_Olfaction_scoring_Q2.pl"
        cmd = "perl %s %s %s %s"
        cmd = cmd % (script, prediction_file, fh.name, gs2)
        shellcmd(cmd)
        df = pd.read_csv(fh.name, sep='\t', index_col=None).ix[0]
        fh.delete()
        return df

        # intensity + pleasantness + dec_19others and sigma_int
        # score sub2 = 1/6 * (z_int + z_ple z_dec + z_sigma_int + z_sigma_ple +
        # z_sigma_dec)
        # sigma_int = 0.1193
        # sigma_ple = 0.1265
        # sigma_dec = 0.0265
        # sigma_sigma_int = 0.1195
        # sigma_sigma_ple = 0.1149
        # sigma_sigma_dec = 0.0281

    def download_template(self, name):
        filename1, filename2 = self.download_templates()
        if name == 'sc1':
            return filename1
        elif name == 'sc2':
            return filename2
        else:
            raise ValueError("Invalid name provided. Use %s" % self.sub_challenges)

    def download_templates(self):
        """Download a template from synapse into ~/config/dreamtools/dream5/D5C2

        :return: filename and its full path
        """
        filename1 = self._download_data('CecchiG_LB_s1_ok.txt', 'syn4538204')
        filename2 = self._download_data('CecchiG_LB_s2_ok.txt', 'syn4538216')
        return filename1, filename2

    def download_gs(self):
        self.gs2_filename = self._download_data('GS2.txt', 'syn4538229')
        self.gs1_filename = self._download_data('GS1.txt', 'syn4538223')
        return self.gs1_filename, self.gs2_filename

    def _download_data(self, name, synid):
        filename = self.directory + os.sep + name
        if os.path.exists(filename) is False:
            # must download the data now
            print("File %s not found. Downloading from Synapse. You must have a login." % filename)
            d = Downloader(self.alias)
            d.download(synid)

        return filename

    def download_goldstandard(self, subname):
        gs1, gs2 = self.download_gs()
        if subname == 'gs1':
            return gs1
        elif subname == 'gs2':
            return gs2



