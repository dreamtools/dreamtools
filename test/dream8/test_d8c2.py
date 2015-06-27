from dreamtools.dream8.D8C2.scoring import D8C2
from nose.plugins.attrib import attr


@attr('skip')
def test_sc1():
    s = D8C2()
    filename = s.download_template('sc1')
    df = s.score(filename, 'sc1')
    assert df.ix['yourSubmission']['meanPCI'] == 0.513854

def test_sc2():
    s = D8C2()
    filename = s.download_template('sc2')
    df = s.score(filename, 'sc2')#
    assert df['SC_m']['bestPerformer'] == 0.45085234093637499564







