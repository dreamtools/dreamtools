from dreamtools import D8dot5C1
from nose.tools import assert_almost_equal


def test():
    # load data first
    s = D8dot5C1()
    s.score(s.download_template('sc2'), 'sc2')
    s.score(s.download_template('sc1'), 'sc1')
    # check values will be done once the GS and templates are frozen

