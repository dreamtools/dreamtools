from dreamtools import D2C3


def test_d2c3():

    s = D2C3()
    tag = 'DIRECTED-SIGNED_EXCITATORY_chip'
    filename = s.download_template(tag)
    d = s.score(filename, subname=tag)
    assert d['AUROC']== 0.76
