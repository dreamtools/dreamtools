

# can be used by all
cellLines = ["BT20", "MCF7", "UACC812", "BT549"]
ligands = ["EGF", "HGF", "FGF1", "IGF1", "Insulin", "NRG1", "PBS", "Serum"]


metadata = {
    'sc1a': {"true_synapse_id": "syn1971278"},
    'sc1b': {},
    'sc2a': {},
    'sc2b': {},
        }


import commons
import scoring
from scoring import *
import hpn
from hpn import *
import submissions

import os
from dreamtools import dreampath
d8c1path = os.sep.join([dreampath, 'dream8', 'D8C1'])




# download data if not found
# syn1920412
