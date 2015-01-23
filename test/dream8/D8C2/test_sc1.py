from dreamtools.dream8.D8C2.sc1 import D8C2_sc1



def test_sc1():

    s =D8C2_sc1()
    s.run()
    assert s.df.ix['yourSubmission']['meanPCI'] == 0.513854






