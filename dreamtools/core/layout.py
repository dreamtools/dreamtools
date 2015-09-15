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
"""Layout to create a new challenge from scratch"""
import os
import sys
import argparse
from easydev import Logging


__all__ = ['Layout', 'layout']


README_templates = '''
Overview
===========


:Title:
:Nickname: %(alias)s
:Summary:
:SubChallenges:
:Synapse page: https://www.synapse.org/#!Synapse:synXXXXXXX


.. contents::


Scoring
---------

::

    from dreamtools import %(alias)s
    s = %(alias)s()
    filename = s.download_template()
    s.score(filename)


'''

scoring_templates = '''
"""%(alias)s scoring function"""
import os
from dreamtools.core.challenge import Challenge


class %(alias)s(Challenge):
    """A class dedicated to %(alias)s challenge


    ::

        from dreamtools import %(alias)s
        s = %(alias)s()
        filename = s.download_template()
        s.score(filename)

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(%(alias)s, self).__init__('%(alias)s')
        self._init()
        self.sub_challenges = []

    def _init(self):
        # should download files from synapse if required.
        pass

    def score(self, filename, subname=None, goldstandard=None):
        raise NotImplementedError

    def download_template(self, subname=None):
        # should return full path to a template file
        raise NotImplementedError

    def download_goldstandard(self, subname=None):
        # should return full path to a gold standard file
        raise NotImplementedError
'''


class Layout(Logging):
    """Class to create automatic layout for a given challenge


    :Usage:

    ::

        dreamtools-layout --name D8C2


    .. warning:: for developers only.
    """
    def __init__(self, name, verbose=True):
        super(Layout, self).__init__(level=verbose)
        self.name = name
        # check the name is correct
        from dreamtools.core.challenge import Challenge
        c = Challenge(self.name)

    def create_layout(self):

        self._create_directory(self.name)

        self._create_file(self._pj('__init__.py'))
        for directory in ['misc', 'leaderboard', 'generator', 'data',
                'paper', 'templates', 'goldstandard']:
            self._create_directory(self._pj(directory))

        # now fill the contents of scoring.py if the file does not exists !

        filename = 'scoring.py'
        if os.path.exists(self._pj(filename)) is True:
            self.warning("%s already exists. Skipped the creation of this directory" % filename)
        else:
            fh = open(self._pj(filename), 'w')
            fh.write(scoring_templates % {'alias': self.name})

        filename = 'README.rst'
        if os.path.exists(self._pj('README.rst')) is True:
            self.warning("%s already exists. Skipped the creation of this directory" % filename)
        else:
            fh = open(self._pj(filename), 'w')
            fh.write(README_templates % {'alias': self.name})

    def _pj(self, filename):
        return os.sep.join([self.name, filename])

    def _create_file(self, filename):
        if os.path.exists(filename) is True:
            self.warning("%s already exists. Skipped the creation of the file" % filename )
        else:
            self.info('Creating %s' % filename)
            open(filename, 'a').close()

    def _create_directory(self, directory):
        if os.path.isdir(directory) is True:
            self.warning("%s already exists. Skipped the creation of this directory" % directory)
        else:
            self.info('Creating %s' % directory)
            os.mkdir(directory)


def layout(args=None):
    """This function is used by the standalone application called dreamscoring

    ::

        dreamtools-layout --help

    """
    import easydev
    d = easydev.DevTools()

    if args == None:
        args = sys.argv[:]
    user_options = Options(prog="dreamtools-layout")

    if len(args) == 1:
        user_options.parse_args(["prog", "--help"])
    else:
        options = user_options.parse_args(args[1:])

    if options.challenge_name is None:
        print_color('--challenge-name must be provided', red)
        sys.exit()

    lay = Layout(options.challenge_name)
    lay.create_layout()


class Options(argparse.ArgumentParser):
    description = "tests"
    def __init__(self, version="1.0", prog=None):

        usage = """\npython %s --challenge-name D8C1""" % prog
        usage += """\n%s --challenge-name D8C1""" % prog
        epilog="""Author(s):

        - Thomas Cokelaer (cokelaer at gmail dot com).

Source code on: https://github.com/dreamtools/dreamtools
Issues or bug report ? Please fill an issue on http://github.com/dreamtools/dreamtools/issues """
        description = """General Description:

    dreamtools-layout creates the layout for a challenge. You must provide
    a valid alias (e.g., D8C1 for Dream8, Challenge 1). Then, the following
    layout is created for you:

        D8C1/__init__.py
        D8C1/scoring.py
        D8C1/README.rst
        D8C1/generator/
        D8C1/data/
        D8C1/templates/
        D8C1/goldstandard/
        D8C1/leaderboard/
        D8C1/misc/
        D8C1/paper/
    """
        super(Options, self).__init__(usage=usage, version=version, prog=prog,
                epilog=epilog, description=description,
                formatter_class=argparse.RawDescriptionHelpFormatter)
        self.add_input_options()

    def add_input_options(self):
        """The input options.

        Default is None. Keep it that way because otherwise, the contents of
        the ini file is overwritten in :class:`apps.Apps`.
        """
        group = self.add_argument_group("General", '')

        group.add_argument("--challenge-name", dest='challenge_name',
                         default=None, type=str,
                         help="alias of the challenge (e.g., D8C1 stands for"
                         "dream8 challenge 1). Intermediate challenge such as first challenge of DREAM9.5 must be encoded as D9dot5C1")

if __name__ == "__main__":
    layout(sys.argv)
