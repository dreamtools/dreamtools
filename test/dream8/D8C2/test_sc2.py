from dreamtools import D8C2
import os

from nose.plugins.attrib import attr


@attr('skip')
def test_sc2():
    s = D8C2()
    filename = s.download_template('sc2')
    s.score(filename, 'sc2')#
    assert s.df['SC_m']['bestPerformer'] == 0.45085234093637499564







