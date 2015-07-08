from dreamtools import D9C1
from nose.tools import assert_almost_equal


def test_d9c1():

    s = D9C1()
    filename = s.download_template()
    res = s.score(filename)
    assert_almost_equal(res['score'], 0.1632098)
