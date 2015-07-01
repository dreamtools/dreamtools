from dreamtools import D5C3
from easydev import assert_list_almost_equal
from nose.tools import assert_almost_equal

def test_d5c3_B():
    s = D5C3()

    s.N_pvalues = 10

    filenames = s.download_template('B')

    df = s.score_challengeB(filenames)

    df = df['SysGenB1']
    del df['pvalues'] # this is not deterministic so let us delete it
    assert_list_almost_equal(df.values,
            [-0.19757481,  0.09499444, 0.85234405,  0.30814104, 1.33696271])



def test_d5c3_A():
    
    s = D5C3()
    filenames = s.download_template('A100')
    res = s.score_challengeA(filenames[0], 'A100_1')
    assert_list_almost_equal([res['aupr'], res['auroc'], res['p_aupr'],
        res['p_auroc']],  [0.0072659,  0.71110535, 0.9989876,  2.6334871e-35])



def test_score_a100():

    s = D5C3()
    results = s.score(s.download_template('A100'), 'A100')
    assert_almost_equal(results['Overall Score'],67.488298, 6)

