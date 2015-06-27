from dreamtools import D2C3


def test_d2c3():

    s = D2C3()
    filename = s.download_template()
    d = s.score(filename)
    assert d['AUPR']> 0.5
