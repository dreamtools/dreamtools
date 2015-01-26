from dreamtools.dream8.D8C2.sc2 import D8C2_sc2
from dreamtools.dream8 import D8C2
import os

def test_sc2():

    filename = os.sep.join([D8C2.__path__[0], 'data', 'test_sc2.csv'])
    s = D8C2_sc2(filename)
    s.run()
    assert s.df['SC_m']['bestPerformer'] == 0.45085234093637499564

