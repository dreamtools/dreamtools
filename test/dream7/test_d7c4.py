from dreamtools import D7C4
from nose.tools import assert_almost_equal
from nose.plugins.attrib import attr

@attr('skip')
def test_d7c4():
    s = D7C4()
    filename = s.download_template('A')
    df = s.score(filename, 'A')
    assert_almost_equal(df['Results']['probabilistic c-index'], 0.578443)

def test_d7c4_b():
    s = D7C4()
    filename = s.download_template('B')
    df = s.score(filename, 'B')
    assert_almost_equal(df['Results']['weighted cindex'], 0.47220967)
