from dreamtools.dream8.D8C2.scoring import D8C2
import os

from nose.plugins.attrib import attr


@attr('skip')
def test_sc1():
    s = D8C2()
    filename = s.download_template('sc1')
    s.score(filename, 'sc1')
    assert s.df.ix['yourSubmission']['meanPCI'] == 0.513854






