from dreamtools import D5C1
from nose.tools import assert_almost_equal


def test_d5c1():

    s = D5C1()
    filename = s.download_template()
    res = s.score(filename)
    assert_almost_equal(res['score'], 0.0001266)
