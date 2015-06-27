from dreamtools import D5C3
from easydev import assert_list_almost_equal


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
    pass
