# -*- python -*-
#
#  This file is part of DreamTools software
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
"""


"""
import os
import sys
import argparse
from easydev import Logging

README_templates = '''
Overview
===========


:Title: 
:Nickname: %(nickname)s
:Summary: 
:Challenge:
:SubChallenges: 
:Synapse page: https://www.synapse.org/#!Synapse:synXXXXXXX


.. contents::


Scoring
---------

::

    from dreamtools import %(nickname)s
    s = %(nickname)s()
    filename = s.download_template() 
    s.score(filename) 


'''

scoring_templates = '''
import os
from dreamtools.core.challenge import Challenge

class %(nickname)s(Challenge):
    """A class dedicated to %(nickname)s challenge


    ::

        from dreamtools import %(nickname)s
        s = %(nickname)s()
        filename = s.download_template() 
        s.score(filename) 

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(%(nickname)s, self).__init__('%(nickname)s')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]

    def score(self, prediction_file):
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
            fh.write(scoring_templates % {'nickname': self.name})

        filename = 'README.rst'
        if os.path.exists(self._pj('README.rst')) is True:
            self.warning("%s already exists. Skipped the creation of this directory" % filename)
        else:
            fh = open(self._pj(filename), 'w')
            fh.write(README_templates % {'nickname': self.name})

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
    a valid nickname (e.g., D8C1 for Dream8, Challenge 1). Then, the following
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
                         help="nickname of the challenge (e.g., D8C1 stands for"
                         "dream8 challenge 1). Intermediate challenge such as first challenge of DREAM9.5 must be encoded as D9dot5C1")

if __name__ == "__main__":
    layout(sys.argv)
