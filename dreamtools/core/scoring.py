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
"""Main standalone application dreamtools-scoring"""
import os
import argparse
import sys
from easydev.console import red, purple, darkgreen
from dreamtools import Challenge


registered = {
        'D8C1': ['sc1a', 'sc1b', 'sc2a', 'sc2b'],
        'D8C2': ['sc1', 'sc2'],
        'D7C1':['parameter', 'topology', 'timecourse'],
        'D5C2': [],
        'D3C1':[],
        'D9dot5C1': ['sc1', 'sc2']}


# Define the simple scoring functions here below
def generic_scoring( challenge_name, sub_challenge_name, filename):
    c = Challenge(challenge_name)
    class_inst = c.import_scoring_class()
    if sub_challenge_name is None:
        score = class_inst.score(filename)
    else:
        score = class_inst.score(filename, sub_challenge_name)
    return {'Results': score}


def d5c2(filename):
    """wrapper to score D5C2 submission"""
    from dreamtools import D5C2
    s = D5C2(Ntf=2)
    s.score(filename)

    df = s.get_table()
    results = {}
    results['table']  = df
    results['user model'] = df.ix[20] # 20 is the user id
    return results


def d8c1_sc1a(filename, verbose=False):
    """wrapper to score D8C1 submission(SC1A sub challenge)"""
    from dreamtools.dream8.D8C1 import scoring, ranking
    sc1a = scoring.HPNScoringNetwork(filename,  verbose=verbose)
    sc1a.compute_all_aucs()
    rank = ranking.SC1A_ranking()
    rank.append_submission(filename)

    return {'AUROC': sc1a.get_auc_final_scoring(),
            'Rank LB': rank.get_rank_your_submission()}


def d8c1_sc1b(filename, verbose=False):
    """wrapper to score D8C1 submission(SC1B sub challenge)"""
    from dreamtools.dream8.D8C1 import scoring, ranking
    sc1b = scoring.HPNScoringNetworkInsilico(filename,  verbose=verbose)
    sc1b.compute_score()
    rank = ranking.SC1B_ranking()
    rank.append_submission(filename)
    return {'AUROC': sc1b.auc,
            'Rank LB': rank.get_rank_your_submission()}


def d8c1_sc2a(filename, verbose=False):
    """wrapper to score D8C1 submission(SC2A sub challenge)"""
    from dreamtools.dream8.D8C1 import scoring, ranking
    sc2a = scoring.HPNScoringPrediction(filename, verbose=verbose)
    sc2a.compute_all_rmse()
    rank = ranking.SC2A_ranking()
    rank.append_submission(filename)
    return {'RMSE': sc2a.get_mean_rmse(),
            'Rank LB': rank.get_rank_your_submission()}


def d8c1_sc2b(filename, verbose=False):
    """wrapper to score D8C1 submission(SC2B sub challenge)"""
    from dreamtools.dream8.D8C1 import scoring, ranking
    sc2b = scoring.HPNScoringPredictionInsilico(filename, verbose=verbose)
    sc2b.compute_all_rmse()
    rank = ranking.SC2B_ranking()
    rank.append_submission(filename)
    return {'RMSE': sc2b.get_mean_rmse(),
            'Rank LB': rank.get_rank_your_submission()}


# DREAM8 Challenge 2
def d8c2_sc1(filename, verbose=False, verboseR=False):
    """wrapper to score D8C2 submission(SC1 sub challenge)"""
    from dreamtools.dream8.D8C2 import sc1
    s = sc1.D8C2_sc1(filename, verboseR=verboseR)
    s.run()
    return {'results': s.df}


def d8c2_sc2(filename, verbose=False, verboseR=False):
    """wrapper to score D8C2 submission(SC2 sub challenge)"""
    from dreamtools.dream8.D8C2 import sc2
    s = sc2.D8C2_sc2(filename, verboseR=verboseR)
    s.run()
    return {'results': s.df}





# -------------------------------------------------- The User Interface
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

        dreamscoring-scoring --help

    """
    import easydev
    d = easydev.DevTools()

    if args == None:
        args = sys.argv[:]
    user_options = Options(prog="dreamtools-scoring")

    if len(args) == 1:
        user_options.parse_args(["prog", "--help"])
    else:
        options = user_options.parse_args(args[1:])

    if options.challenge is None:
        if len(registered[options.challenge])!=0 and options.sub_challenge is None:
            print_color('--challenge and --sub-challenge must be provided', red)
            sys.exit()
    else:
        options.challenge = options.challenge.upper()
        options.challenge = options.challenge.replace('DOT', 'dot')

    try:
        d.check_param_in_list(options.challenge, registered.keys())
    except ValueError as err:
        txt = "DreamScoring error: unknown challenge name (%s) or not yet implemented\n" % options.challenge
        txt += "--->" + err.message
        print_color(txt, red)
        sys.exit()

    if options.sub_challenge is not None:
        try: 
            d.check_param_in_list(options.sub_challenge, registered[options.challenge])
        except ValueError as err:
            txt = "DreamScoring error: unknown sub challenge or not yet implemented"
            txt += "--->" + err.message
            print_color(txt, red)
            sys.exit()

    if options.challenge not in registered.keys():
        raise ValueError('Invalid challenge name. Choose one of %s' % registered.keys())

    if options.download_template is True:
        c = Challenge(options.challenge)
        class_inst = c.import_scoring_class()
        if options.sub_challenge is None:
            try:
                filename = class_inst.download_template()
            except:
                print_color('could not download template. Missing sub challenge name', red)
                print_color(registered[options.challenge], red)
                return
        else:
            filename = class_inst.download_template(options.sub_challenge)
        print(filename)
        return

    if options.filename is None:
        txt = "---> filename not provided. You must provide a filename with correct format\n"
        txt += "You may get a template using --download-template option\n"
        txt += "https://github.com/dreamtools/dreamtools, or http://dreamchallenges.org\n"
        print_color(txt, red)
        sys.exit()

    if os.path.exists(options.filename) is False:
        raise IOError("file %s does not seem to exists" % options.filename)

    print_color("Dreamtools scoring", purple, underline=True)
    print('Challenge %s (sub challenge %s)\n\n' % (options.challenge, options.sub_challenge))

    res = '??'


    if options.challenge == 'D8C1':
        if options.sub_challenge == 'sc1a':
            res = d8c1_sc1a(options.filename, verbose=options.verbose)
        elif options.sub_challenge == 'sc1b':
            res = d8c1_sc1b(options.filename, verbose=options.verbose)
        elif options.sub_challenge == 'sc2a':
            res = d8c1_sc2a(options.filename, verbose=options.verbose)
        elif options.sub_challenge == 'sc2b':
            res = d8c1_sc2b(options.filename, verbose=options.verbose)
    else:
        res = generic_scoring(options.challenge, options.sub_challenge, options.filename)


    txt = "Solution for %s in challenge %s" % (options.filename, options.challenge)
    if options.sub_challenge is not None:
        txt += " (sub-challenge %s)" % options.sub_challenge
    txt += " is :\n"

    for k in sorted(res.keys()):
        txt += darkgreen("     %s: %s\n" %(k, res[k]))

    print(txt)


class Options(argparse.ArgumentParser):
    description = "tests"
    def __init__(self, version="1.0", prog=None):

        usage = """usage: python %s --challenge d8c1 --sub-challenge sc1a --submission <filename>""" % prog
        usage += """      python %s --challenge d5c2 --submission <filename>""" % prog
        epilog="""Author(s):

        - Thomas Cokelaer: DreamTools package and framework including tests and docs
        - Thomas Cokelaer: D8C1, Parameter Estimation D6 and D7
        - Federica Eduati: original R scripts for D8C2
        - Pablo Meyer: Parameter Estimation D6 and D7


Source code on: https://github.com/dreamtools/dreamtools
Issues or bug report ? Please fill an issue on http://github.com/dreamtools/dreamtools/issues """
        description = """General Description:
    You must provide the challenge nickname (e.g., d8c1 for Dream8, Challenge 1) and
    if there were several sub-challenges, you also must provide the sub-challenge
    nickname (e.g., sc1). Finally, the submission has to be provided. The format must
    be in agreement with the description of the challenge itself.

    Help and documentation about the templates may be found either within the online
    documentation http://pythonhosted.org/dreamtools/ or within the source code
    hosted on github http://github.org/dreamtools/dreamtools

    Registered challenge so far (and sub-challenges) are:
    """
        description +="\n"
        for c in registered.keys():
            description +=  "    - " + c + ": "
            for s in registered[c]:
                description += s + " "
            description += "\n"

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
                         help="nickname of the challenge (e.g., D8C1 stands for"
                         "dream8 challenge 1).")
        group.add_argument("--sub-challenge", dest='sub_challenge', 
                         default=None, type=str,
                         help="Name of the data files")
        group.add_argument("--verbose", dest='verbose',
                         action="store_true",
                         help="verbose option.")
        group.add_argument("--submission", dest='filename',
                         help="submission/filename to score.")
        group.add_argument("--filename", dest='filename',
                         help="submission/filename to score.")
        group.add_argument("--download-template", dest='download_template',
                         help="download template. Templates for challenge may be downloaded using this option. It returns the path to template.", action='store_true')


        #group.add_argument("--help", dest='help',
        #                 action="store_true",
        #                 help="this help.")

if __name__ == "__main__":
    scoring(sys.argv)
