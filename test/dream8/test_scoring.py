from dreamtools.dream8.D8C1 import scoring


def test_scoring_sc1a():
    s = scoring.HPNScoringNetwork(
        "hpndream8_downloads/sc1a/limax-Network.zip")
    s.compute_all_aucs()
    assert s.get_auc_final_scoring() == 0.77107383364675341

    s.load_submission("hpndream8_downloads/sc1a/DC_GFP-Network.zip")
    s.compute_all_aucs()
    assert s.get_auc_final_scoring() == 0.78202740472227761


def test_scoring_sc1b():
    s = scoring.HPNScoringNetworkInsilico(
        "hpndream8_downloads/sc1b/NMSUSongLab-Network-Insilico.zip")

    s.compute_score()
    assert s.auc == 0.76422010245539662


def test_scoring_sc2a():
    s = scoring.HPNScoringPrediction(
        "hpndream8_downloads/sc2a/guanlab10-Prediction.zip")
    s.compute_all_rmse()
    assert s.get_mean_rmse() == 0.45297349456396707


def test_scoring_sc2b():
    s = scoring.HPNScoringPredictionInsilico(
        "hpndream8_downloads/sc2b/CGR-Prediction-Insilico.zip")
    s.compute_all_rmse()
    assert s.get_mean_rmse() == 0.27750290989139931
