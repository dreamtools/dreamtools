# -*- python -*-
#
#  This file is part of DreamTools software
#
#  Copyright (c) 2014-2015 - EBI-EMBL
#
#  File author(s): Thomas Cokelaer <cokelaer@ebi.ac.uk>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  website: http://github.org/dreamtools
#
##############################################################################
"""D5C2 challenge scoring functions

:Credits: Based on TF_web.pl (perl version) provided by Raquel Norel (Columbia University/IBM)
   that is used wihtin the web server http://www.ebi.ac.uk/saezrodriguez-srv/d5c2/cgi-bin/TF_web.pl
"""
import os
from os.path import join as pj
import zipfile
import StringIO
import collections
import numpy as np
import pandas as pd
import tempfile

from easydev import progress_bar
from dreamtools.core.ziptools import ZIP
from dreamtools.core.challenge import Challenge
from dreamtools.core.rocs import ROCDiscovery
from dreamtools.core.downloader import Downloader



class D5C2(Challenge):
    """A class dedicated to D5C2 challenge


    ::

        from dreamtools import D5C2
        s = D5C2()

        # You can get a template from www.synapse.org page (you need to register)
        s.download_templates() 
        s.score('templates.txt.gz') # takes about 5 minutes
        s.get_table()
        s.plot()

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self, tmpdir=None, Ntf=66):
        """.. rubric:: constructor
        
        :param Ntf: not to be used. Used for fast testing and debugging
        :param tmpdir: a local temporary file if provided. 
        """
        super(D5C2, self).__init__('D5C2')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self.Ntf = Ntf
        self.tmpdir = tmpdir               # directory where to save the results

        self._dvs = {}
        self._dvps = {}
        self._probes = {}

    def score(self, prediction_file):
        """Compute all results and compare user prediction with all official participants
        
        This scoring function can take a long time (about 5-10 minutes). 
        """

        self.init() # this provides a temporary file
        self.prediction_file = prediction_file
        print('Loading user data set (step 1 out of 5)')
        self._loading_user_data()

        print('Loading the gold standard and user prediction. Takes a few seconds (step 2 out 5')
        self.download_all_data()

        print('\nProcessing\nSplitting data sets (step 3 out of 5)')
        self._split_data()
        print('\nComputing probes (step 4 out of 5)')
        self._preprocessing()
        print('\nComputing performances (step 5 out of 5)')
        self._processing()

    def init(self):
        """Creates the temporary directory and the sub directories.

        Behaviour differs whether the directory was provided
        in the constructor or not.
        """
        if self.tmpdir is None:
            self.tmpdir = tempfile.mkdtemp()
        else:
            try:
                os.mkdir(self.tmpdir)
            except:
                pass

        for directory in ['Data', 'Out']:
            this = pj(self.tmpdir, directory)
            if os.path.exists(this) is False:
                os.mkdir(this)

    def download_all_data(self):
        """Download all large data sets from Synapse"""
        pb = progress_bar(5)
        # load the large gold standard file from D5C2 synapse main page
        filename = self._download_data('DREAM5_GoldStandard_probes.zip', 'syn2898469')
        pb.animate(1)
        z = ZIP()
        z.loadZIPFile(filename)
        data = z.read('Answers.txt')
        self.gs = pd.read_csv(StringIO.StringIO(data), sep='\t')

        # download 4 other filenames from dreamtools synapse project
        self._download_data('all_8mers.txt', 'syn4483185')
        pb.animate(2)
        self._download_data('8mers_gs.txt', 'syn4483187')
        pb.animate(3)
        self._download_data('probe35_gs.txt', 'syn4483184')
        pb.animate(4)
        self._download_data('probes35.txt', 'syn4483183')
        pb.animate(5)
    
    def download_templates(self):
        """Download a template from synapse into ~/config/dreamtools/dream5/D5C2

        :return: filename and its full path
        """
        filename = self._download_data('templates.txt.gz', 'syn4483192')
        return filename

    def _download_data(self, name, synid):
        filename = self.directory + os.sep + name
        if os.path.exists(filename) is False:
            # must download the data now
            print("File %s not found. Downloading from Synapse. You must have a login." % filename)
            d = Downloader(self.nickname)
            d.download(synid)

        return filename

    def _split_data(self, precision=6):
        """precision is to get same results as in the original perl script"""
        mask = self.gs.Flag == 0
        self.user_data_clean = self.user_data[mask].copy()
        print('Splitting the user data set and removing flagged data (%s out of %s)' % (self.gs.shape[0] - mask.sum(), self.gs.shape[0]))
        self.gs_clean = self.gs[mask].copy()
        # local aliases
        gs = self.gs_clean
        user_data = self.user_data_clean

        pb = progress_bar(self.Ntf, interval=1)
        for tf_index in range(1, self.Ntf + 1):
            this_tf = 'TF_%s'  % tf_index
            tf_gs = gs.query("Id == @this_tf").Answer
            tf_user = user_data.query("TF_Id == @this_tf").Signal_Mean
            df = pd.concat([tf_gs, tf_user], axis=1)
            df.to_csv(self._setfile(tf_index, 'Data'), index=False, sep='\t',
                      header=False, float_format="%f")
            pb.animate(tf_index)

    def _loading_user_data(self):
        """Get the file from the form, save it, decompress it."""

        # could be either gz or zip
        import mimetypes
        itemtype = mimetypes.guess_type(self.prediction_file)[1]
        
        if itemtype == 'gzip':
            import gzip
            fh = gzip.open(self.prediction_file, 'rb')
            data = fh.read()
            fh.close()
        elif itemtype == 'zip':
            z = zipfile.ZipFile(self.prediction_file)
            assert len(z.filelist) == 1, "zipped archive should contain only 1 file"
            # extract in byte
            data = z.read(z.filelist[0])
            self.prediction_file_unzipped = 'tmp_' + z.filelist[0].filename
        else:
            raise IOError("input file must be gzipped or zipped")

        df = pd.read_csv(StringIO.StringIO(data), sep='\t');# engine='python')
        self.user_data = df

    def _preprocessing(self):
        """Create temporary files for before further processing

        :return: nothing
        """
        # Read file octomers gold standard
        filename = self.directory + os.sep + '8mers_gs.txt'
        self.octomers_gs = pd.read_csv(filename, sep='\t', header=None)

        # Read file octomers 
        filename = self.directory + os.sep + 'all_8mers.txt'
        self.octomers = pd.read_csv(filename, sep='\t', header=None)  # contains reverse complemtn
        self.octomers.columns = ['octomer','octomerRC']

        # Read probes gs
        filename = self.directory + os.sep + 'probe35_gs.txt'
        self.probes_gs = pd.read_csv(filename, header=None, sep='\t')
        self.probes_gs.columns = ['Id', 'Sequence']

        # reads probes (sequences)
        print('Reading probes')
        filename = self.directory + os.sep + 'probes35.txt'
        # just one column so no need for a separator
        probes = pd.read_csv(filename)

        # Extract information (first and third column of pred.txt)
        df = self.user_data[['TF_Id', 'Signal_Mean']].copy()
        df['Signal_Mean'] = df['Signal_Mean'].map(lambda x: round(x,6))

        # data.txt is paste of probes35.txt and val.txt
        data = pd.concat([probes, df], axis=1)

        # Creates probes/TF_1.dat that contains the sequence from the GS and the answer from the user
        # for each TF
        print('Creating probes/TF_1.csv + sorting')
        pb = progress_bar(self.Ntf, interval=1)
        for i in range(1, self.Ntf+1):
            # could use a groupby here ? faster  maybe
            tag = 'TF_%s' % i
            sequence = data[['Sequence']].ix[self.gs.Id==tag]
            answer = data.Signal_Mean[data.TF_Id == tag]
            df = pd.concat([sequence, answer], axis=1)
            df.sort(columns=['Signal_Mean', 'Sequence'], ascending=[False, False], inplace=True)
            df['Signal_Mean'] = df['Signal_Mean'].map(lambda x: round(x,6))

            self._probes[i] = df
            pb.animate(i)

    def _setfile(self, index, directory):
        return self.tmpdir + os.sep + directory + os.sep + 'TF_%s' % index + '.csv'

    def _processing(self):
        """

        :return:
        """
        ########################################  1 Create the Out/TF_XX.dat files
        octomers = self.octomers.octomer
        octomersRC = self.octomers.octomerRC
        mapping1  = dict([(k,v) for k,v in zip(octomers.values, octomersRC.values)])
        mapping2  = dict([(k,v) for k,v in zip(octomersRC.values, octomers.values)])
        keys = tuple(sorted(octomers.values))

        lm = set(octomers.values)

        pb = progress_bar(self.Ntf, interval=1)
        pb.animate(0)
        for tf_index in range(1, self.Ntf + 1):
            tf = self._probes[tf_index]
            tf.columns = ['Sequence', 'Score']
            ids = collections.defaultdict(list)
            ###### TODO: most of the time is spent in the "for curR in generator" loop
            for seq, score in zip(tf.Sequence, tf.Score):
                # scan the sequence by chunk of octomers using a generator
                # for speed (although gain is small)
                generator = (seq[i:i+8] for i in xrange(0,28))
                for curR in generator:
                    if mapping1.has_key(curR) is False:
                        curR = mapping2[curR]
                    ids[curR].append(score)
                # Using a set does not help speeding up the code
                #for curR in generator:
                #    if curR not in lm:
                #        curR = mapping2[curR]
                #    ids[curR].append(score)

            # now let us build the new dataframe for the indices found
            df = pd.DataFrame({0:[k for k in  ids.keys()],
                               1:[np.median(v) for v in ids.values()]})
            df.sort(columns=[1,0], ascending=[False, False], inplace=True)
            df[1] = df[1].map(lambda x: round(x,6))

            df.to_csv(self._setfile(tf_index, 'Out'), sep=' ', index=False, header=None, float_format="%.6f")
            pb.animate(tf_index)
        print("")
        ################################################# 2 create the DVP

        pb = progress_bar(self.Ntf, interval=1)
        for tf_index in range(1,self.Ntf+1):
            tag = 'TF_%s' % tf_index
            tf_probes = list(self.probes_gs.ix[self.probes_gs.groupby('Id').groups[tag]].Sequence)

            tf = self._probes[tf_index]
            dv = tf.Sequence.apply(lambda x: x in tf_probes).astype(int)
            self._dvps[tf_index] = dv
            pb.animate(tf_index)
        print("")

        ########################################################## DV
        gs_octomers = self.octomers_gs.copy()
        gs_octomers.columns = ['id', 'octomer']
        pb = progress_bar(self.Ntf, interval=1)
        for tf_index in range(1,self.Ntf+1):
            tag = 'TF_%s' % tf_index
            tf_octomers = list(gs_octomers.ix[gs_octomers.groupby('id').groups[tag]].octomer)
            tf = pd.read_csv(self._setfile(tf_index, "Out"), sep=" ",
                             header=None)
            tf.columns = ['Octomer', 'Score']
            dv = tf.Octomer.apply(lambda x: x in tf_octomers).astype(int)

            # Stores the dataframe
            self._dvs[tf_index] = dv
            pb.animate(tf_index)

    def compute_statistics(self):
        """Returns final results of the user predcition
        
        :return: a dataframe with various metrics for each transcription factor.
        
        Must call :meth:`score` before.

        """
        data = {'Pearson': [],
                'Spearman': [],
                'Pearson_Log': [],
                "AUROC_8mer": [],
                "AUPR_8mer": [],
                "AUROC_probe": [],
                "AUPR_probe": []}

        pb = progress_bar(self.Ntf, interval=1)
        for tf_index in range(1, self.Ntf + 1):
            dfdata = pd.read_csv(self._setfile(tf_index, "Data"), sep='\t', header=None)
            pearson = dfdata.corr('pearson').ix[0,1]
            spearman = dfdata.corr('spearman').ix[0,1]
            pearsonLog = np.log10(dfdata).corr('pearson').ix[0,1]

            data['Pearson'].append(pearson)
            data['Pearson_Log'].append(pearsonLog)
            data['Spearman'].append(spearman)


            dvdata = self._dvs[tf_index]

            #dvdata = pd.read_csv(self._setfile(tf_index, "DV"), index_col=False, header=None)
            r = ROCDiscovery(dvdata.values)
            rocdata = r.get_statistics()
            auroc = r.compute_auc(roc=rocdata)
            aupr = r.compute_aupr(roc=rocdata)
            data['AUROC_8mer'].append(auroc)
            data['AUPR_8mer'].append(aupr)

            dvdata = self._dvps[tf_index] 
            #dvdata = pd.read_csv(self._setfile(tf_index, 'DVP'), index_col=False, header=None)
            r = ROCDiscovery(dvdata.values)
            rocdata = r.get_statistics()
            auroc = r.compute_auc(roc=rocdata)
            aupr = r.compute_aupr(roc=rocdata)
            data['AUROC_probe'].append(auroc)
            data['AUPR_probe'].append(aupr)
            pb.animate(tf_index)

        df =  pd.DataFrame(data)
        df = df[['Pearson', u'Spearman', u'Pearson_Log', u'AUROC_8mer', u'AUPR_8mer', u'AUROC_probe', u'AUPR_probe']]

        return df

    def get_table(self):
        """Return table with user results from the user and participants

        There are 14 participants as in the Leaderboard found here 
        https://www.synapse.org/#!Synapse:syn2887863/wiki/72188


        :return: a dataframe with different metrics showing performance of the submission
            with respect to other participants.


        ::

            table = s.get_table()
            with open('test.html', 'w') as fh:
                fh.write(table.to_html(index=False))

        """
        userdf = self.compute_statistics()
        userdf = userdf.mean().to_frame().T
        userdf.index = [20] # there are 20 participants, let us add this user as the 21st
        userdf = userdf[['Pearson', 'Pearson_Log', 'Spearman', 'AUROC_8mer', 'AUPR_8mer']]
        userdf['Team'] = 'Your team'
        userdf['Model type'] = 'Your model'

        filename = os.sep.join([self._path2data, "data", "d5c2_data_table.csv"])
        participants = pd.read_csv(filename, sep='\t', index_col=0)
        table = pd.concat([participants, userdf])

        # compute ranks based on those columns. Using method first to be in agreement with the server
        rank_columns = ['Pearson', 'Pearson_Log', 'Spearman', 'AUPR_8mer', 'AUROC_8mer']
        ranks = table[rank_columns]
        mean_ranks = ranks.rank(ascending=False, method='first').mean(axis=1)
        table['Final Rank (average)'] = mean_ranks.values
        table['Final Rank'] = table['Final Rank (average)'].rank(method='first')
        table = table[['Team', 'Model type', 'Final Rank', 'Final Rank (average)'] + rank_columns]
        table = table.sort(columns=['Final Rank'])
        return table

    def _get_table(self):
        userdf = self.compute_statistics()
        userdf = userdf.mean().to_frame().T
        userdf.index = [20] # there are 20 participants, let us add this user as the 21st

        # load all data from participants for comparison
        filename = os.sep.join([self._path2data, "data", "d5c2_data_plot.csv"])
        participants = pd.read_csv(filename, sep='\t', )

        df = pd.concat([participants, userdf])
        return (df, userdf)

    def plot(self):
        """Show the user prediction compare to 20 other participants"""
        df, userdf = self._get_table()

        import pylab
        pylab.clf();
        pylab.subplot(2,2,1)
        pylab.plot(df.AUROC_8mer, df.AUPR_8mer, marker='+', color='k', lw=0, markersize=10)
        pylab.plot(userdf.AUROC_8mer, userdf.AUPR_8mer, marker='s', color='b', lw=0, markersize=10)
        pylab.xlim([0,1])
        pylab.ylim([0,1])
        pylab.xlabel('AUROC octamers')
        pylab.ylabel('AURPR octamers')

        pylab.subplot(2,2,2)
        pylab.plot(df.AUROC_probe, df.AUPR_probe, marker='+', color='k', lw=0, markersize=10)
        pylab.plot(userdf.AUROC_probe, userdf.AUPR_probe, marker='s', color='b', lw=0, markersize=10)
        pylab.xlim([0,1])
        pylab.ylim([0,1])
        pylab.xlabel('AUROC probes')
        pylab.ylabel('AURPR probes')

        pylab.subplot(2,2,3)
        pylab.plot(df.Pearson, df.Spearman, marker='+', color='k', lw=0, markersize=10)
        pylab.plot(userdf.Pearson, userdf.Spearman, marker='s', color='b', lw=0, markersize=10)
        pylab.xlim([0,1])
        pylab.ylim([0,1])
        pylab.xlabel('Pearson probes')
        pylab.ylabel('Spearman probes')

        pylab.subplot(2,2,4)
        pylab.plot(df.Pearson, df.Pearson_Log, marker='+', color='k', lw=0, markersize=10)
        pylab.plot(userdf.Pearson, userdf.Pearson_Log, marker='s', color='b', lw=0, markersize=10)
        pylab.xlim([0,1])
        pylab.ylim([0,1])
        pylab.xlabel('Pearson probes')
        pylab.ylabel('Log Pearson probes')

    def cleanup(self):
        """Remove the temporary directory"""
        import shutil
        shutil.rmtree(self.tmpdir)
