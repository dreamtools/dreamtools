from dreamtools.dream8.D8C2.scoring import D8C2
from nose.plugins.attrib import attr
from nose.tools import assert_almost_equal

@attr('skip')
def test_sc1():
    s = D8C2()
    filename = s.download_template('sc1')
    df = s.score(filename, 'sc1')
    #assert_almost_equal(df.ix['yourSubmission']['meanPCI'], 0.51384184, 7)
    assert_almost_equal(df.ix['yourSubmission']['meanPCI'], 0.5138, 3)
    # not deterministic but 4 digits should be correct.
    # 0.51384570949323804534

def test_sc2():
    s = D8C2()
    filename = s.download_template('sc2')
    df = s.score(filename, 'sc2')#
    assert_almost_equal(df['SC_m']['bestPerformer'], 0.45085234093637499564)






test_sc1()
