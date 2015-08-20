from dreamtools import D5C2
from nose.tools import assert_almost_equal
import os


def test_d5c2():
    # load data first
    s = D5C2(Ntf=2)  # temporary directory will be created 
    filename = s.download_template()
    res = s.score(filename)
    v = res.Pearson
    assert_almost_equal(v, 0.51295034)
    s.plot()

    s.cleanup() # so we cleanit up now
