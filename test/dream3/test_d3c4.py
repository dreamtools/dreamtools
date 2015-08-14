from dreamtools import D3C4
from easydev.easytest import assert_list_almost_equal



def test_d3c4_10():
    # we have templates for 10 only 
    s = D3C4()
    s.test()

    aurocs = []
    for batch in ['Ecoli1', 'Ecoli2', 'Yeast1']:
        filename = s.download_template('10_'+ batch)
        print filename
        aurocs.append(s.score(filename, '10')['AUPR'])

    assert_list_almost_equal(aurocs,
         [0.3294927, 0.6283442, 0.368482140], 7)

    # other code
    s._warning()
