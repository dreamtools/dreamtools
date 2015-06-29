from dreamtools import D2C1
from nose.tools import assert_almost_equal

def test_d2c1():
    s = D2C1()
    filename = s.download_template()
    d = s.score(filename)
    assert_almost_equal(d['AUPR'], 0.2563463, 7)
