from dreamtools import D2C5


def test_d2c5():

    s = D2C5()

    subname = s.sub_challenges[0]
    filename = s.download_template(subname)
    gs = s.download_goldstandard(subname)
    d = s.score(filename, subname)
    assert d['AUPR']
