# -*- python -*-
# -*- coding: utf-8 -*-
#
#  This file is part of DREAMTools software
#
#  Copyright (c) 2015, DREAMTools Development Team
#  All rights reserved
#
#  Distributed under the BSD 3-Clause License.
#  See accompanying file LICENSE distributed with this software
#
#  File author(s): Thomas Cokelaer <cokelaer@ebi.ac.uk>
#
#  website: http://github.com/dreamtools
#
##############################################################################
"""Utility to download a synapse project in the dreamtools directory"""

from dreamtools.core.sageutils import Login
from dreamtools.core.challenge import Challenge


__all__ = ['Downloader']


class Downloader(Challenge, Login):
    """Factory to download gold standard files

    Download a synpase file once for all in the dreamtools directory.

    """
    def __init__(self, challenge, client=None, username=None, password=None):
        """.. rubric:: constructor

        :param str challenge: alias of a challenge (e.g., D5C1)

        To automatically connect to synapse, create a file called .synapseConfig with this
        content::

            [authentication]
            username: email
            password: password

        """
        Challenge.__init__(self, challenge_name=challenge)
        Login.__init__(self, client=client, username=username,
                password=password)

    def download(self, synid):
        """Download a file into the dreamtools directory

        :param synid: a valid synapse id (e.g., syn123456)

        You must have a login on synapse website.
        """
        assert synid.startswith('syn'), "synid must be a valid synapse identifier e.g., syn123456"
        self.client.get(synid, downloadLocation=self.directory)
