from dreamtools.core.cindex import concordanceIndex, ConcordanceIndex
from nose.tools import assert_almost_equal


def test_cindex():
    testObservations = [1.078304837, 2.646866651, 1.165920248, 0.537903100,
        1.726597615, 1.166453794, 0.080994131, 0.102762485, 2.434480043,
        0.170285918, 0.211224424, 0.335248849, 1.172972616,
        0.018286180, 0.810920450, 0.447176348, 1.034328426
        ,0.504800631, 0.159534333,0.583315557]


    myPredictions = [15.325381588,  3.485879452, 10.993454286,  0.775569668,
            9.718363379, 1.011624518, 24.066998015, 10.644879046,  8.246779821,
            4.644882463, 0.003919197, 10.186298220,  3.734309896, 16.905509362,
            7.384189707, 2.594689418, 3.701121718,  9.671040180,  7.414466980,
            3.289922854]

    N = len(testObservations)

    score = concordanceIndex(myPredictions, testObservations, [True]*N)

    assert_almost_equal(score, 0.5894737, 7)


def test_cindex_class():
    ci = ConcordanceIndex()
    ci._test()
