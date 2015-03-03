from dreamtools.dream8.D8C1 import scoring
from dreamtools.dream8.D8C1 import d8c1path
import os

def test_scoring_sc1a():
    filename = os.sep.join([d8c1path, 'submissions', 'sc1a',
        'limax-Network.zip'])
    s = scoring.HPNScoringNetwork(filename)

    s.compute_all_aucs()
    assert s.get_auc_final_scoring() == 0.77107383364675341

    filename = os.sep.join([d8c1path, 'submissions', 'sc1a',
        'DC_GFP-Network.zip'])
    s.load_submission(filename)
    s.compute_all_aucs()
    assert s.get_auc_final_scoring() == 0.78202740472227761

    # just try some other functions
    s.get_null_distribution(2)
    s.plot_all_rocs()


def test_scoring_sc1b():
    filename = os.sep.join([d8c1path, 'submissions', 'sc1b',
        'NMSUSongLab-Network-Insilico.zip'])
    s = scoring.HPNScoringNetworkInsilico(filename)
    s.compute_score()
    assert s.auc == 0.76422010245539662


def test_scoring_sc2a():
    filename = os.sep.join([d8c1path, 'submissions', 'sc2a',
        'guanlab10-Prediction.zip'])
    s = scoring.HPNScoringPrediction(filename)
    s.compute_all_rmse()
    assert s.get_mean_rmse() == 0.45297349456396707


def test_scoring_sc2b():
    filename = os.sep.join([d8c1path, 'submissions', 'sc2b',
        'CGR-Prediction-Insilico.zip'])
    s = scoring.HPNScoringPredictionInsilico(filename)
    s.compute_all_rmse()
    #assert s.get_mean_rmse() == 0.24554824475398279 former wrong true prediction
    assert s.get_mean_rmse() == 0.27750290989139931 


