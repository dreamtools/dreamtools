from dreamtools import D8C1
import os
from nose.tools import assert_almost_equal


def test_score_sc1a():
    s = D8C1()
    res = s.score(s.download_template('SC1A'), 'SC1A')
    assert_almost_equal(res['meanAUROC'], 0.80362891940311265)

def test_score_sc1b():
    s = D8C1()
    res = s.score(s.download_template('SC1B'), 'SC1B')
    assert_almost_equal(res['meanAUROC'], 0.80582052640876178)

def test_score_sc2a():
    s = D8C1(version=1)
    res = s.score(s.download_template('SC2A'), 'SC2A')
    assert_almost_equal(res['meanRMSE'],  0.48434056686051685)

    s = D8C1(version=2)
    res = s.score(s.download_template('SC2A'), 'SC2A')
    assert_almost_equal(res['meanRMSE'],  0.50023848102569435)

def test_score_sc2b():
    s = D8C1(version=1)
    res = s.score(s.download_template('SC2B'), 'SC2B')
    assert_almost_equal(res['meanRMSE'], 0.27750290989139931)

    s = D8C1(version=2)
    res = s.score(s.download_template('SC2B'), 'SC2B')
    assert_almost_equal(res['meanRMSE'], 0.24071058884458607)


def _test_scoring_sc1a():

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


def _test_scoring_sc1b():
    filename = os.sep.join([d8c1path, 'submissions', 'sc1b',
        'NMSUSongLab-Network-Insilico.zip'])
    s = scoring.HPNScoringNetworkInsilico(filename)
    s.compute_score()
    assert s.auc == 0.76422010245539662


def _test_scoring_sc2a():
    filename = os.sep.join([d8c1path, 'submissions', 'sc2a',
        'guanlab10-Prediction.zip'])
    s = scoring.HPNScoringPrediction(filename)
    s.compute_all_rmse()
    assert s.get_mean_rmse() == 0.45297349456396707


def _test_scoring_sc2b():
    filename = os.sep.join([d8c1path, 'submissions', 'sc2b',
        'CGR-Prediction-Insilico.zip'])
    s = scoring.HPNScoringPredictionInsilico(filename)
    s.compute_all_rmse()
    #assert s.get_mean_rmse() == 0.24554824475398279 former wrong true prediction
    assert s.get_mean_rmse() == 0.27750290989139931 


