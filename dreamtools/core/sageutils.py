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
"""A module dedicated to synapse

The class :class:`SynapseClient` is a specialised class built upon
synapseclient package, which source code is on GitHub::

    git clone git://github.com/Sage-Bionetworks/synapsePythonClient.git
    cd synapsePythonClient
    python setup.py install

This class may be removed but for now it is used in D8C1 challenge.


::

    >>> from dreamtools.core import sageutils
    >>> s = sageutils.SynapseClient()


"""
import os
import synapseclient

__all__ = ["SynapseClient", "Login"]


class Login(object):
    """A simple class to login to synapse

    :param client: Connection to synapse takes a
        couple of seconds. This may be too much if in a debugging mode or
        accessing to synapse from different places. The login can be instantiate
        with an existing instance of SynapseClient, if which case, the instance
        creation is fast. Otherwise, the default behaviour is to create a new
        connection.

    ::

        >>> from dreamtools.core.sageutils import Login
        >>> l = Login()
        This is a SynapseClient built on top of Synapse class.
        Trying to login automatically.
        Welcome, *****************
        You're logged in Synapse
        Welcome, XXX

        In [10]: l = sageutils.Login(l)

    """
    def __init__(self, client=None, username=None, password=None):
        if client is None:
            self.client = SynapseClient(username, password)
        else:
            self.client = client

# note that synapseclient.Synapse does not inherit from object, hence the
# additional base class here below that contains Synapse and object as base
# classes
class SynapseClient(synapseclient.Synapse, object):
    """This class inherits all methods from synapseClient.

    Be aware that most of the functionalities are now available in synapseclient
    itself. So, most of the methods that were written are hidden (double
    underscore) and may be removed in the future.

    The only remaining feature is the automatic login, and simple version of the
    downloadSubmission method. There is also a :meth:`json` method used
    throughout the dream8hpn code.

    """
    def __init__(self, username=None, password=None):
        """.. rubric:: Constructor

        :param username: your synapse usename
        :param password: your synapse password

        You can create create a file called **.synapseConfig** (note the dot)
        in your home directory and add something like::

            [authentication]
            username: yourlogin
            password: yourpassword

        """
        from requests import ConnectionError
        try:
            super(SynapseClient, self).__init__()
            self._connected = True
        except ConnectionError:
            self._connected = False

        self._try_to_login(username, password)

    def _try_to_login(self, username, password):
        if self._connected is False:
            return

        from synapseclient.exceptions import SynapseAuthenticationError
        try:
            self.login(username, password)
        except Exception as err:
            print("Could not login automatically to Synapse " + 
                    "(http://synapse.org).")
            print("Indeed, no .synapseConfig file could be found " +
                    "in your HOME directory.")
            print("Let us try to login manually (you must have a valid " +
                  "login and password associated with Synapse)\n")

            # use input instead of raw_input (Python3 has only input())
            try:
                input = raw_input
            except NameError: pass

            username = str(input("Please enter your Synapse login: "))
            password = str(input("and its password: "))

            try:
                self.login(username, password)

                print('\n')
                print("For future usage, you may login automatically to Synapse as follows::\n")
                print("1 - create a file called .synapseConfig in your HOME" + 
                        " directory (%s)" % os.getenv('HOME'))
                print("2 - Copy and paste the following text in the file"+
                      "changing the login and password with your credentials:\n")
                print("[authentication]")
                print("username: yourlogin")
                print("password: yourpassword")
                print("\n")
                _dummy = str(input("Press enter to continue"))
            except SynapseAuthenticationError:
                print("Invalid username and/or password ?")
                raise Exception
            except Exception as err:
                raise Exception(err)

    def downloadSubmissionAndFilename(self, sub, downloadFile=True, **kargs):
        """Return filename of a submission downloaded from synapse.

        :param sub:  A submission (as a dictionary).
        :param version:  The specific version to get. Defaults to the most
            recent version.
        :param downloadFile: Whether associated files(s) should be downloaded.
             Defaults to True. If set to False, downloadLocation and ifcollision are ignored
        :param downloadLocation: Directory where to download the Synapse File Entity.
            Defaults to the local cache.
        :param ifcollision: Determines how to handle file collisions.
            May be "overwrite.local", "keep.local", or "keep.both".
            Defaults to "keep.both".

        .. warning:: ifcollision does not seem to work (0.5.1)

        """

        if isinstance(sub, dict) == False:
            raise TypeError("input must be a submission (dictionary)")

        if downloadFile == False:
            filename = self.getSubmission(sub, downloadFile=False)['filePath']
        else:
            filename = self.getSubmission(sub, downloadFile=True, **kargs)['filePath']

        return filename

    def getMyProfile(self):
        """Returns user profile"""
        return self.restGET("/userProfile")

    def json(self, data):
        """Transform relevant object into json object"""
        import json
        data = json.dumps(data)
        return data
