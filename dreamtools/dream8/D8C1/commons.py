# -*- python -*-
# -*- coding: utf-8 -*-
#
#  This file is part of dreamtools software
#
#  Copyright (c) 2013-2015 - EBI-EMBL
#
#  File author(s): Thomas Cokelaer <cokelaer@ebi.ac.uk>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  website: http://github.com/dreamtools
#
##############################################################################

"""
Created on Fri Mar 21 11:51:26 2014

@author: cokelaer
"""

cellLines = ["BT20", "MCF7", "UACC812", "BT549"]
ligands = ["EGF", "HGF", "FGF1", "IGF1", "Insulin", "NRG1", "PBS", "Serum"]

valid_ligands_final = {
                   'UACC812': ['PBS', 'Serum', 'NRG1', 'Insulin', 'HGF', 'EGF', 'FGF1',  'IGF1'],
                      'BT20': ['IGF1', 'PBS', 'Serum', 'NRG1', 'HGF', 'EGF', 'FGF1'],
                      'BT549': ['IGF1', 'PBS', 'Serum', 'Insulin', 'HGF', 'EGF', 'FGF1'],
                      'MCF7': ['IGF1', 'PBS', 'Serum', 'NRG1', 'Insulin',  'HGF', 'EGF', 'FGF1']
                      }


metadata = {
    'sc1a': {"true_synapse_id": "syn1971278"},
    'sc1b': {},
    'sc2a': {},
    'sc2b': {},
}
