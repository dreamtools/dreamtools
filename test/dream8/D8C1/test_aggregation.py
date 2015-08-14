from dreamtools.dream8.D8C1 import aggregation
from nose.plugins.attrib import attr
import easydev

@attr('skip')
def test_sc2a():
    a = aggregation.SC2A_aggregation(version=1)
    #a.load_submissions()
    aucs = a.plot_aggr_best_score(N=2)
    easydev.assert_list_almost_equal(aucs['aggregation'], [0.48434056686051674, 0.46329666463290453])
    aucs = a.plot_aggr_random(N=2, Nmax=2)

@attr('skip')
def test_sc2b():
    b = aggregation.SC2B_aggregation(version=1)
    #b.load_submissions()
    aucs = b.plot_aggr_best_score(N=2)
    easydev.assert_list_almost_equal(aucs['aggregation'], [0.25428664093754277, 0.22176905909721403])
    aucs = b.plot_aggr_random(N=2, Nmax=2)

@attr('skip')
def test_sc1a():
    b = aggregation.SC1A_aggregation()
    #b.load_submissions()
    aucs = b.plot_aggr_best_score(M=2)
    easydev.assert_list_almost_equal(aucs['aggregation'],
            [0.78202740472227761, 0.79045976573183718])
    aucs = b.plot_aggr_random(2,2)

@attr('skip')
def test_sc1b():
    b = aggregation.SC1B_aggregation()
    
    aucs = b.plot_aggr_best_score(M=2)
    easydev.assert_list_almost_equal(aucs['aggregation'],
            [0.76422010245539662, 0.76991697579932872])
    aucs = b.plot_aggr_random(2,2)

