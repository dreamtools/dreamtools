from dreamtools.dream7.D7C1 import scoring
import os
import nose

def test_scoring_model1():
    s = scoring.D7C1(path='D7C1/submissions')

    ################## model1 parameters:
    # best performer
    filename = s.download_template('parameter')
    score = s.score(filename, 'parameter')
    nose.tools.assert_almost_equal(score['score'],0.02286755)
    # gold standard
    filename = s.download_goldstandard('parameter')
    score = s.score_model1_parameters(filename)
    assert score == 0


    #s.load_submissions()
    #s.compute_score_distance_model1()
    #s.compute_score_parameter_prediction_model1()
    #s.compute_score_topology()


def test_scoring_topology_leaderboard():
    s = scoring.D7C1()
    try:
        s.compute_score_topology()
        assert all(s.scores['topo2'].scores == [2,3,4,4,5,6,7,8,8,8,9,12])
    except:
        # needs all submissions
        pass

def test_scoring_topology():
    s = scoring.D7C1()
    filename = s.download_template('topology')
    score = s.score(filename, 'topology')['score']
    assert score == 4

def test_scoring_parameters():
    s = scoring.D7C1()
    filename = s.download_template('parameter')
    score = s.score(filename, 'parameter')['score']
    nose.tools.assert_almost_equal(score, 0.02286755501)

def test_scoring_timecourse():
    s = scoring.D7C1()
    filename = s.download_template('timecourse')
    score = s.score(filename, 'timecourse')['score']
    nose.tools.assert_almost_equal(score, 0.002438361267)

def _test_others():
    s = scoring.D7C1()
    df = s.get_null_parameters_model1()
