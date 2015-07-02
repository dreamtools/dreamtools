from dreamtools import D4C3
from nose.tools import assert_almost_equal
import os


def test_d4c3():
    # load data first
    s = D4C3()  # temporary directory will be created
    s.edge_count = 20 # must be provided otherwise waits for raw_input 
    filename = s.download_template()

    s.plot()
    results = s.score(filename)


    #assert_almost_equal(s.prediction_score, 1.7067596171386146)
    #assert_almost_equal(s.overall_score, 0.052759617138614656)
    #s.plot()



    
    assert_almost_equal(s.prediction_score, 1.8417941451247148)
    assert_almost_equal(s.overall_score, 0.18779414512471493)
    s.plot()
