from dreamtools import D7C4
from nose.tools import assert_almost_equal
from nose.plugins.attrib import attr

@attr('skip')
def test_d7c4():
    s = D7C4()
    filename = s.download_template()
    df = s.score(filename)
    assert_almost_equal(df['c-index']['probabalistic c-index'], 0.578443)
