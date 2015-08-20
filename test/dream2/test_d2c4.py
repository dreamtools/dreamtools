from dreamtools import D2C4


def test_d2c4():

    s = D2C4()

    subname = s.sub_challenges[0]
    filename = s.download_template(subname)
    d = s.score(filename, subname)
    assert d['AUPR']

    s.test()
