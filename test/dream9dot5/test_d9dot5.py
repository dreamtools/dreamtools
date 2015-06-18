from dreamtools import D9dot5C1
from nose.tools import assert_almost_equal


def test():
    # load data first
    s = D9dot5C1()
    file1, file2 = s.download_templates()


    df1 = s.score_sc1(file1)
    assert_almost_equal(df1['avg of Z-scores'], 20.875287, places=6)
    
    df2 = s.score_sc2(file2)

    assert_almost_equal(df2['avg of Z-scores'], 6.673661, places=6)



