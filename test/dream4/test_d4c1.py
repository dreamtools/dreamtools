from dreamtools import D4C1
from nose.tools import assert_almost_equal

def test_d4c1():
    s = D4C1()
    filename = s.download_template()
    s.score(filename)
    assert_almost_equal(s.results['kinase']['overall_score'],
            2.7894344039299788)


    assert_almost_equal(s.results['pdz']['overall_score'],
        1.8432749244847197)


    assert_almost_equal(s.results['sh3']['overall_score'],
        0.89373894121248987)


