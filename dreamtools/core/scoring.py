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
"""Main standalone application dreamtools"""
import os
import argparse
import sys
from easydev.console import red, purple, darkgreen
from easydev import DevTools
from dreamtools import Challenge
import dreamtools
import textwrap


def get_challenge(challenge_name):
    """Test validity of the challenge and returns an instance

    :param challenge_name: a valid name e.g. D5C3, D9dot5C1
    :return: instance of the challenge
    """
    try:
        c = Challenge(challenge_name)
    except:
        txt = "The challenge %s could not be found. " % challenge_name
        txt += "See --help for valid names"
        print_color(txt, red)
        sys.exit()
    return c


# Define the simple scoring functions here below
def generic_scoring(challenge_name, filename, subname=None, goldstandard=None):
    c = get_challenge(challenge_name)
    class_inst = c.import_scoring_class()
    try:
        score = class_inst.score(filename, subname=subname,
                                 goldstandard=goldstandard)
    except:
        try:
            score = class_inst.score(filename, subname=subname)
        except:
            try:
                score = class_inst.score(filename)
            except Exception as err:
                msg = "Error was caught in dreamtools.\n"
                msg += "Most probably an incorrect file format.\n"
                msg += "Here is the full error message to report it if needed\n"
                print_color(msg, red)
                raise err
    return {'Results': score}


# Figure out if the challenge exists and what are the sub challenges
def get_subchallenges(challenge_name):
    c = get_challenge(challenge_name)
    class_inst = c.import_scoring_class()
    return class_inst.sub_challenges


# ------------------------------------------------ The User Interface
def print_color(txt, func_color, underline=False):
    import easydev
    try:
        if underline:
            print(easydev.underline(func_color(txt)))
        else:
            print(func_color(txt))
    except:
        print(txt)


def scoring(args=None):
    """This function is used by the standalone application called dreamscoring

    ::

        dreamscoring --help

    """
    d = DevTools()

    if args is None:
        args = sys.argv[:]
    user_options = Options(prog="dreamtools")

    if len(args) == 1:
        user_options.parse_args(["prog", "--help"])
    else:
        options = user_options.parse_args(args[1:])

    # Check on the challenge name
    if options.challenge is None:
        print_color('--challenge and --sub-challenge must be provided', red)
        sys.exit()
    else:
        options.challenge = options.challenge.upper()
        options.challenge = options.challenge.replace('DOT', 'dot')

    # Check that the challenge can be loaded
    class_inst = get_challenge(options.challenge)
    try:
        class_inst.import_scoring_class()
    except NotImplementedError as err:
        print("\n"+err.message)
        sys.exit()

    # User may just request some information about the challenge.
    if options.info is True:
        this = class_inst.import_scoring_class()
        print(this)
        sys.exit()

    # or open the synapse project page
    if options.onweb is True:
        this = class_inst.import_scoring_class()
        url = "https://www.synapse.org/#!Synapse:%s"
        url = url % this.synapseId
        print(url)
        import webbrowser
        webbrowser.open_new(url)
        sys.exit()

    # Checks name of the sub-challenges
    subchallenges = get_subchallenges(options.challenge)

    if len(subchallenges) and options.sub_challenge is None:
        txt = "This challenge requires a sub challenge name."
        txt += "Please provide one amongst %s " % subchallenges
        print_color(txt, red)
        sys.exit(0)

    if options.sub_challenge is not None and len(subchallenges) != 0:
        try:
            d.check_param_in_list(options.sub_challenge, subchallenges)
        except ValueError as err:
            txt = "DREAMTools error: unknown sub challenge or not implemented"
            txt += "--->" + err.message
            print_color(txt, red)
            sys.exit()

    # maybe users just need a template
    if options.download_template is True:
        c = Challenge(options.challenge)
        class_inst = c.import_scoring_class()
        if options.sub_challenge is None:
            print(class_inst.download_template())
        else:
            print(class_inst.download_template(options.sub_challenge))
        return

    # similary for the GS
    if options.download_goldstandard is True:
        c = Challenge(options.challenge)
        class_inst = c.import_scoring_class()
        if options.sub_challenge is None:
            print(class_inst.download_goldstandard())
        else:
            print(class_inst.download_goldstandard(options.sub_challenge))
        return

    # finally, we need a submission
    if options.filename is None:
        txt = "---> filename not provided. You must provide a filename with correct format\n"
        txt += "You may get a template using --download-template option\n"
        txt += "https://github.com/dreamtools/dreamtools, or http://dreamchallenges.org\n"
        print_color(txt, red)
        sys.exit()

    # filename
    # filename in general is a single string but could be a list of filenames
    # Because on the parser, we must convert the string into a single string
    # if the list haa a length of 1
    for filename in options.filename:
        if os.path.exists(filename) is False:
            raise IOError("file %s does not seem to exists" % filename)
    if len(options.filename) == 1:
        options.filename = options.filename[0]

    print_color("DREAMTools scoring", purple, underline=True)
    print('Challenge %s (sub challenge %s)\n\n' % (options.challenge, options.sub_challenge))

    res = generic_scoring(options.challenge,
            options.filename,
            subname=options.sub_challenge,
            goldstandard=options.goldstandard)

    txt = "Solution for %s in challenge %s" % (options.filename, options.challenge)
    if options.sub_challenge is not None:
        txt += " (sub-challenge %s)" % options.sub_challenge
    txt += " is :\n"

    for k in sorted(res.keys()):
        txt += darkgreen("     %s:\n %s\n" %(k, res[k]))
    print(txt)


class Options(argparse.ArgumentParser):
    description = "tests"
    def __init__(self, version="1.0", prog=None):

        usage = """usage: python %s --challenge d8c1 --sub-challenge sc1a --submission <filename>\n""" % prog
        usage += """      python %s --challenge d5c2 --submission <filename>""" % prog
        epilog="""Author(s): Thomas Cokelaer (DREAMTools framework) and authors from
the DREAM consortium. Please see the scoring files headers for details
and the GitHub repository.

Source code on: https://github.com/dreamtools/dreamtools
Issues or bug report ? Please fill an issue on http://github.com/dreamtools/dreamtools/issues """
        description = """General Description:
    You must provide the challenge alias (e.g., d8c1 for Dream8, Challenge 1) and
    if there were several sub-challenges, you also must provide the sub-challenge
    alias (e.g., sc1). Finally, the submission has to be provided. The format must
    be in agreement with the description of the challenge itself.

    Help and documentation about the templates may be found either within the online
    documentation http://pythonhosted.org/dreamtools/ or within the source code
    hosted on github http://github.org/dreamtools/dreamtools

    Registered challenge so far (and sub-challenges) are:
"""
        # FIXME : not robust but will work for now
        registered = sorted([x for x in dir(dreamtools) if x.startswith('D')
                 and 'C' in x])

        for this in textwrap.wrap(", ".join(registered), 80):
            description += this + "\n"

        super(Options, self).__init__(usage=usage, version=version, prog=prog,
                epilog=epilog, description=description,
                formatter_class=argparse.RawDescriptionHelpFormatter)
        self.add_input_options()

    def add_input_options(self):
        """The input oiptions.

        Default is None. Keep it that way because otherwise, the contents of
        the ini file is overwritten in :class:`apps.Apps`.
        """
        group = self.add_argument_group("General", 'General options (compulsary or not)')

        group.add_argument("--challenge", dest='challenge',
                         default=None, type=str,
                         help="alias of the challenge (e.g., D8C1 stands for"
                         "dream8 challenge 1).")
        group.add_argument("--sub-challenge", dest='sub_challenge',
                         default=None, type=str,
                         help="Name of the data files")
        group.add_argument("--verbose", dest='verbose',
                         action="store_true",
                         help="verbose option.")
        group.add_argument("--submission", dest='filename', nargs='*',
                         help="submission/filename to score.")
        group.add_argument("--filename", dest='filename', nargs='*',
                         help="submission/filename to score.")
        group.add_argument("--gold-standard", dest='goldstandard',
                         help="""a gold standard filename. This may be
                         required in some challenges e.g. D2C3""")
        group.add_argument("--onweb", dest='onweb',action='store_true',
                help="Open synapse project page in a browser")
        group.add_argument("--info", dest='info', action="store_true",
                help="Prints general information about the challenge")
        group.add_argument("--download-template",
                dest='download_template',
                help="""Download template. Templates for challenge may be
                downloaded using this option. It returns the path to
                template.""",
                action='store_true')
        group.add_argument("--download-gold-standard",
                dest='download_goldstandard',
                help="""Download a gold standard, which can be used as a
                submissions as well. It returns the location of the file.""",
                action='store_true')


if __name__ == "__main__":
    scoring(sys.argv)