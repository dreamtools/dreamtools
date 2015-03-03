from dreamtools.dream8.D8C1 import ranking

from easydev import get_home
import os
path2data = os.sep.join(['.config', 'dreamtools', 'dream8', 'D8C1', 'submissions'])

def test_sc1a_ranking():
    r = ranking.SC1A_ranking()
    r.append_submission(os.sep.join([get_home(), path2data, "sc1a", 
        "limax-Network.zip"]))
    assert r.get_rank_your_submission() == 2

def test_sc1b_ranking():
    r = ranking.SC1B_ranking()
    r.append_submission(os.sep.join([get_home(), path2data, "sc1b",
        "NMSUSongLab-Network-Insilico.zip"]))
    assert r.get_rank_your_submission() == 1


def test_sc2a_ranking():
    r = ranking.SC2A_ranking()
    r.append_submission(os.sep.join([get_home(), path2data, "sc2a", 
        "ALAK-Prediction.zip"]))
    assert r.get_rank_your_submission() == 1

def test_sc2b_ranking():
    r = ranking.SC2B_ranking()
    r.append_submission(os.sep.join([get_home(), path2data, "sc2b",
        "CGR-Prediction-Insilico.zip"]))
    assert r.get_rank_your_submission() == 1


