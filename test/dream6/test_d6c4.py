from dreamtools import D6C4



def test():
    s = scoring.D6C4()
    results = s.score(s.download_goldstandard())
    results = s.score(s.download_template())
    assert results['MCC'] == 1.0,
    assert results['pearson'] = 0.99522726332027467


