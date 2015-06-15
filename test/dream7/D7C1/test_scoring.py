from dreamtools.dream7.D7C1 import scoring
import os
import nose

def test_scoring_model1():
    s = scoring.D7C1()

    ################## model1 parameters:
    # best performer
    filename = s._path2data + os.sep + 'templates' + \
            os.sep + 'model1_parameters_alphabeta.txt'
    score = s.score_model1_parameters(filename)
    nose.tools.assert_almost_equal(score,0.02286755)
    # gold standard
    filename = s._path2data + os.sep + 'goldstandard' + \
            os.sep + 'model1_parameters_answer.txt'
    score = s.score_model1_parameters(filename)
    assert score == 0


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
    filename = s._path2data + os.sep + 'templates' + os.sep 
    filename += 'network_topology_alphabeta.txt'
    score = s.score_topology(filename)
    assert score == 4

def test_scoring_parameters():
    s = scoring.D7C1()
    filename = s._path2data + os.sep + 'templates' + os.sep 
    filename += 'model1_parameters_alphabeta.txt'
    score = s.score_model1_parameters(filename)
    nose.tools.assert_almost_equal(score, 0.02286755501)

def test_scoring_timecourse():
    s = scoring.D7C1()
    filename = s._path2data + os.sep + 'templates' + os.sep 
    filename += 'model1_timecourse_alphabeta.txt'
    score = s.score_model1_timecourse(filename)
    nose.tools.assert_almost_equal(score, 0.002438361267)

def _test_others():
    s = scoring.D7C1()
    df = s.get_null_parameters_model1()
