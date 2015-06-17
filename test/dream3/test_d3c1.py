from dreamtools import D3C1
from nose.tools import assert_almost_equal
import os


def test_d3c1():
    # load data first
    s = D3C1()  # temporary directory will be created
    filename = s.get_template()
    num, pval = s.score(filename)
    assert num == 2
    assert_almost_equal(pval, 0.108333333)
