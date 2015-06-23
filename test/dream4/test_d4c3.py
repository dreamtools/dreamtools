from dreamtools import D4C3
from nose.tools import assert_almost_equal
import os


def test_d4c3():
    # load data first
    s = D4C3()  # temporary directory will be created
    filename = s.download_template()

    s.plot()
    results = s.score(filename)


    assert_almost_equal(s.prediction_score, 1.7067596171386146)
    assert_almost_equal(s.overall_score, 0.052759617138614656)
    s.plot()


