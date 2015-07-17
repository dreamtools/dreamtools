from dreamtools import D5C4
from nose.tools import assert_almost_equal


def test_d5c4():
    s = D5C4()
    filenames = s.download_template()
    df = s.score(filenames)
    assert_almost_equal(df['Overall Score'], 0.793504,6)
