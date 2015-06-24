from dreamtools import D3C2
from nose.tools import assert_almost_equal


def test_cytokine():
    s = D3C2()
    results = s.score(s.download_template('cytokine'), 'cytokine')
    assert_almost_equal(results['score'], 25244.9980236)
    assert_almost_equal(results['pvalue'], 0.7239793)

def test_phospho():
    s = D3C2()
    results = s.score(s.download_template('phospho'), 'phospho')
    assert_almost_equal(results['score'], 26505.3099294)
    assert_almost_equal(results['pvalue'], 0.0002585)


