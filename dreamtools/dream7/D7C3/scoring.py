"""


"""
from dreamtools.core.challenge import Challenge

import pandas as pd
import math

class D7C3(Challenge):
    """A class dedicated to D7C3 challenge


    ::

        from dreamtools import D7C3
        s = D7C3()
        filename = s.download_template() 
        s.score(filename) 

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D7C3, self).__init__('D7C3')
        self.sub_challenges = []

    def score(self, filename, subname=None, goldstandard=None):
        self.df = pd.read_csv(filename, header=None, sep=",")
        self.gs = pd.read_csv(self.download_goldstandard(), header=None,
                sep=",")

        df = pd.merge(self.df, self.gs, on=[0])[['1_x','1_y']]
        score = math.sqrt(((df['1_x']-df['1_y'])**2).mean())
        return {'RMSE': score}

    def download_template(self, subname=None):
        # should return full path to a template file
        return self.getpath_template('D7C3_template.csv')

    def download_goldstandard(self, subname=None):
        # should return full path to a gold standard file
        return self.getpath_gs('D7C3_goldstandard.csv')
