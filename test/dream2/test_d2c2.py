from dreamtools import D2C2


def test_d2c2():

    s = D2C2()
    filename = s.download_template()
    d = s.score(filename)
    assert d['AUPR']> 0.95
