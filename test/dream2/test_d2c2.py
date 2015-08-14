from dreamtools import D2C2
from nose.tools import assert_almost_equal

def test_d2c2():
    s = D2C2()
    s.test()

    filename = s.download_template()
    d = s.score(filename)
    assert_almost_equal(d['AUPR'], 0.48010135, 7)
