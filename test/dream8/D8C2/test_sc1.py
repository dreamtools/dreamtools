from dreamtools.dream8.D8C2.sc1 import D8C2_sc1
from dreamtools.dream8 import D8C2
import os





def test_sc1():
    filename = os.sep.join([D8C2.__path__[0], 'data', 'test_sc1.csv'])
    s = D8C2_sc1(filename)
    s.run()
    assert s.df.ix['yourSubmission']['meanPCI'] == 0.513854






