# -*- python -*-
# -*- coding: utf-8 -*-
#
#  This file is part of dreamtools software
#
#  Copyright (c) 2013-2014 - EBI-EMBL
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
__all__ = ['dataframe_towiki']



def dataframe_towiki(df):
    """Creates a table in WIKI format from a dataframe

    This WIKI format should be compatible with Synapse
    """

    df = df.fillna('nan')
    txt = ""

    header = list(df.columns[:])
    N = len(header)

    formatter = " | ".join(["%20s" for this in header])
    formatter = "| " + formatter + " |"

    txt += formatter % tuple(header) + "\n"

    # no spaces before/after the pipe character.
    txt += formatter.replace(" ", "") % tuple([ "-"*20 for x in range(0, N)]) + "\n"

    for row in df.iterrows():
        txt += formatter % tuple(row[1].values)
        txt += "\n"
    return txt
