from dreamtools import D5C2
from nose.tools import assert_almost_equal
import os


def test_d5c2():
    # load data first
    s = D5C2(Ntf=2)  # temporary directory will be created
    s.download_templates()
    filename = s.directory + os.sep + 'templates.txt.gz'
    s.score(filename)
    v = s.get_table().ix[20].Pearson
    assert_almost_equal(v, 0.51295034)

    s.cleanup()
