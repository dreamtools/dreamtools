from dreamtools import D3C3
from nose.tools import assert_almost_equal


def test_d3c3():
    # load data first
    s = D3C3()  # temporary directory will be created
    filename = s.download_goldstandard()
    filename = s.download_template()
    res = s.score(filename)

    assert_almost_equal( res['score'], 0.3266163)

