from dreamtools import D7C3
from nose.tools import assert_almost_equal

def test():

    s = D7C3()
    res = s.score(s.download_template())
    assert_almost_equal(res['RMSE'], 0.5368661266170465)
    res = s.score(s.download_goldstandard())
    assert_almost_equal(res['RMSE'], 0)

