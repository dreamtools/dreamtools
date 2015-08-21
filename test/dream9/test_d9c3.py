from dreamtools import D9C3
from nose.tools import assert_almost_equal


# Number double check with the orignal R code
def test_d9c3_sc1():
    s = D9C3()
    filename = s.download_template('sc1')
    res = s.score(filename, 'sc1')
    #assert_almost_equal(res['score'], 0.1632098)


def test_d9c3_sc2():
    s = D9C3()
    filename = s.download_template('sc2')
    res = s.score(filename, 'sc2')
    #assert_almost_equal(res['score'], 0.05098946)


def test_d9c3_sc3():
    s = D9C3()
    filename = s.download_template('sc3')
    res = s.score(filename, 'sc3')
    #assert_almost_equal(res['score'], 0.1121396)
