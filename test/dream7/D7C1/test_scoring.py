from dreamtools.dream7.D7C1 import scoring
from dreamtools.dream7.D7C1 import d7c1path
import os
import easydev
def test_scoring_model1():
    s = scoring.D7C1()

    ################## model1 parameters:
    # best performer
    filename = s._path2data + os.sep + 'templates' + \
            os.sep + 'dream7_netparinf_parameters_model_1_orangeballs.txt'
    score = s.score_model1_parameters(filename)
    assert easydev.easytest.assert_list_almost_equal([score],[0.02286755])
    # gold standard
    filename = s._path2data + os.sep + 'goldstandard' + \
            os.sep + 'model1_parameters_answer.txt'
    score = s.score_model1_parameters(filename)
    assert score == 0





