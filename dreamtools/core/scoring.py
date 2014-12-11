import os
import argparse
import easydev
import sys
from easydev.console import purple, darkgreen

registered = {'d8c1': ['sc1a', 'sc1b', 'sc2a', 'sc2b']}


# Define the simple scoring functions here below

def d8c1_sc1a(filename):
    from dreamtools.dream8.D8C1 import scoring
    sc1a = scoring.HPNScoringNetwork(filename)
    sc1a.compute_all_aucs()
    return {'AUROC': sc1a.get_auc_final_scoring()}


def d8c1_sc1b(filename):
    from dreamtools.dream8.D8C1 import scoring
    sc1b = scoring.HPNScoringNetworkInsilico(filename)
    sc1b.compute_score()
    return {'AUROC': sc1b.auc}


def d8c1_sc2a(filename):
    from dreamtools.dream8.D8C1 import scoring
    sc2a = scoring.HPNScoringPrediction(filename)
    sc2a.compute_all_rmse()
    return {'RMSE': sc2a.get_mean_rmse()}


def d8c1_sc2b(filename):
    from dreamtools.dream8.D8C1 import scoring
    sc2b = scoring.HPNScoringPredictionInsilico(filename)
    sc2b.compute_all_rmse()
    return {'RMSE': sc2b.get_mean_rmse()}



def scoring(args=None):
    """This function is used by the standalone application called dreamscoring

    ::

        dreamscoring-scoring --help

    """
    d = easydev.DevTools()

    if args == None:
        args=sys.argv[:]
    user_options = Options(prog="dreamtools-scoring")
    if len(args) == 1:
        user_options.parse_args(["prog", "--help"])
    else:
        options = user_options.parse_args(args[1:])

    if options.sub_challenge:
        subchallenge = options.sub_challenge
    else:
        subchallenge = None

    try:
        d.check_param_in_list(options.challenge, registered.keys())
    except ValueError as err:
        print("DreamScoring error: unknown challenge or not yet implemented")
        print("--->" + err.message)
        sys.exit()

    try:
        d.check_param_in_list(subchallenge, registered[options.challenge])
    except ValueError as err:
        print("DreamScoring error: unknown sub challenge or not yet implemented")
        print("--->" + err.message)

    if os.path.exists(options.filename) is False:
        raise IOError("file %s does not seem to exists" % options.filename)

    try:
        print(easydev.underline(purple("Dreamtools scoring ")))
    except:
        print(easydev.underline("Dreamtools scoring "))

    res = '??'
    if options.challenge == 'd8c1':
        if options.sub_challenge == 'sc1a':
            res = d8c1_sc1a(options.filename)
        elif options.sub_challenge == 'sc1b':
            res = d8c1_sc1b(options.filename)
        elif options.sub_challenge == 'sc2a':
            res = d8c1_sc2a(options.filename)
        elif options.sub_challenge == 'sc2b':
            res = d8c1_sc2b(options.filename)
    txt = "Solution for %s in challenge %s" % (options.filename, options.challenge)
    if subchallenge is not None:
        txt += " (sub-challenge %s)" % subchallenge
    txt += " is :\n"
    for k in sorted(res.keys()):
        txt += darkgreen("     %s: %s" %(k, res[k]))

    print(txt)






class Options(argparse.ArgumentParser):

    def __init__(self, version="1.0", prog=None):
        usage = """usage: python %s --challenge d8c1 --sub-challenge sc1a --input""" % prog
        super(Options, self).__init__(usage=usage, version=version, prog=prog)
        self.add_input_options()

    def add_input_options(self):
        """The input oiptions.

        Default is None. Keep it that way because otherwise, the contents of
        the ini file is overwritten in :class:`apps.Apps`.
        """

        group = self.add_argument_group("General",
                    """You must provide the challenge nickname (e.g., d8c1) and 
                    if there were several sub-challenges, you also must 
                    provide the sub-challenge nickname (e.g., sc1).
                    Finally, the submission has to be provided. The format must
                    be in agreement with the description of the challenge
                    itself.
                    """)

        group.add_argument("--challenge", dest='challenge',
                         default=None, type=str, 
                         help="nickname of the challenge (e.g., d8c1 stands for"
                         "dream8 challenge 1). Challenge nicknames can be found on"
                         "dreamchallenges.org.")
        group.add_argument("--sub-challenge", dest='sub_challenge', 
                         default=None, type=str,
                         help="Name of the data files")
        group.add_argument("--verbose", dest='verbose',
                         action="store_true",
                         help="verbose option.")
        group.add_argument("--submission", dest='filename',
                         help="submission/filename to score.")
        #group.add_argument("--help", dest='help',
        #                 action="store_true",
        #                 help="this help.")

if __name__ == "__main__":
    scoring(sys.argv)
