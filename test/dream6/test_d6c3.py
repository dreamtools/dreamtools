from dreamtools import D6C3
from nose.tools import assert_almost_equal


def test_d6c3():


    s = D6C3()
    filename = s.download_template()
    results = s.score(filename)['results']
    assert_almost_equal(results['chi2'], 53.98074145)
    assert_almost_equal(results['R-square'], 34.733564565928198)
    assert_almost_equal(results['Spearman(Sp)'], 0.64691675481612498)
    assert_almost_equal(results['Pearson(Cp)'], 0.647516)


