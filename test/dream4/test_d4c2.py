from dreamtools import D4C2
from easydev.easytest import assert_list_almost_equal

fast = range(1,3)
slow = range(1,6)

myrange = fast

def test_d4c2_10():
    s = D4C2()
    aurocs = []
    for batch in myrange:
        filename = s.download_template("10_" + str(batch))
        res = s.score(filename, '10')
        aurocs.append(res['AUROC'])

    assert_list_almost_equal(aurocs,
         [0.556444444444, 0.521537162162, 0.54, 0.518481518482,
            0.449786324786])


def test_d4c2_100():
    s = D4C2()
    aurocs = []
    for batch in myrange:
        filename = s.download_template("100_" + str(batch))
        res = s.score(filename, '100')
        aurocs.append(res['AUROC'])

    assert_list_almost_equal(aurocs,
        [0.5177063077, 0.59869942, 0.515280254692,0.5796535, 0.50947022])


def test_d4c2_100_2():
    s = D4C2()
    aurocs = []
    for batch in myrange:
        filename = s.download_template("100_multifactorial_" + str(batch))
        res = s.score(filename, '100_multifactorial')
        aurocs.append(res['AUROC'])

    assert_list_almost_equal(aurocs,
       [0.491887457, 0.495480003, 0.506360189, 0.501096420, 0.501367796])

