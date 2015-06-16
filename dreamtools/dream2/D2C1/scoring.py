import pandas as pd
import numpy as np
import os
from dreamtools.core.challenge import Challenge


class D2C1(Challenge):
    def __init__(self):
        super(D2C1, self).__init__('D2C1')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self.decoys = pd.read_excel(self.get_data("BCL6_targets_and_decoys.xls"))

    def get_data(self, filename):
        filename = self._path2data + os.sep + "data" + os.sep +"BCL6_targets_and_decoys.xls"
        return filename

    def create_templates(self, filename='test_BCL6targets.txt'):
        templates = self.decoys.copy()
        templates['scores'] = np.random.random(200)
        df = templates[['Entrez GeneID', 'scores']]

        df = df.sort(columns=['scores'], ascending=[False])
        df.to_csv(filename, sep='\t', header=None, index=False)
