from dreamtools import D6C4


def test():
    # should correspond to the leaderboard
    # https://www.synapse.org/#!Synapse:syn2887788/wiki/72181
    # for 'team21'
    s = D6C4()
    results = s.score(s.download_goldstandard())
    results = s.score(s.download_template())
    assert results['MCC'] == 1.0
    assert results['pearson'] == 0.99522726332027467


