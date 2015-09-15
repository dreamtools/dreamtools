# -*- python -*-
# -*- coding: utf-8 -*-
#
#  This file is part of DREAMTools software
#
#  Copyright (c) 2015, DREAMTools Development Team
#  All rights reserved
#
#  Distributed under the BSD 3-Clause License.
#  See accompanying file LICENSE distributed with this software
#
#  File author(s): Thomas Cokelaer <cokelaer@ebi.ac.uk>
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
    txt += formatter.replace(" ", "") % tuple(["-"*20 for x in range(0, N)]) + "\n"

    for row in df.iterrows():
        txt += formatter % tuple(row[1].values)
        txt += "\n"
    return txt
