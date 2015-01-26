from dreamtools.dream8.D8C1 import aggregation




def test_sc2a():
    a = aggregation.SC2A_aggregation()
    a.load_submissions()
    aucs = a.plot_aggr_best_score()
    assert aucs == [0.48434056686051674, 0.45297349456396707]
    aucs = a.plot_aggr_random(N=2, Nmax=2)


def test_sc2b():
    b = aggregation.SC2B_aggregation()
    b.load_submissions()
    aucs = b.plot_aggr_best_score()
    assert aucs == [0.24554824475398279, 0.25530788468348198]    
    aucs = b.plot_aggr_random(N=2, Nmax=2)

def test_sc1a():
    b = aggregation.SC1A_aggregation()
    b.load_submissions()
    aucs = b.plot_aggr_best_score(M=2)
    assert aucs['aggregation'] ==  [0.78202740472227761, 0.79045976573183718]
    aucs = b.plot_aggr_random(2,2)



def test_sc1b():
    b = aggregation.SC1B_aggregation()
    b.load_submissions()
    aucs = b.plot_aggr_best_score(M=2)
    assert aucs == [0.76422010245539662, 0.73489666136724974]
    aucs = b.plot_aggr_random(2,2)

