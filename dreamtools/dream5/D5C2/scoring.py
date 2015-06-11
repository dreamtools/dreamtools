"""

  Copyright 2015 EBI


:Author: Thomas Cokelaer . Based on TF_web.pl (perl version) provided by Rachel Norel (Columbia University/IBM)
   that is used wihtin the web server http://www.ebi.ac.uk/saezrodriguez-srv/d5c2/cgi-bin/TF_web.pl
"""
import tempfile
import os
from os.path import join as pj
import StringIO
import subprocess
import time
import collections
import numpy as np
import pandas as pd

from easydev import progress_bar
from cno.misc.profiler import  do_profile
from dreamtools.core.ziptools import ZIP


# Nothing to changed here below #####################################

#cgitb.enable() # to allow tracking exception in the HTML page.
 


class D5C2(object):
    """A class dedicated to running the different processing steps on 
    the data provided by the user.


    ::

        s = D5C2("prediction.zip")
        s.split_data()
        s.

        s.get_table()
        s.plot()

    A prediction example can be downloaded using ::

        s.download_templates()

    """
    def __init__(self, prediction_file, tmpdir=None, goldstandard=None):

        self.tmpdir = tmpdir               # directory where to save the results
        self.prediction_file = prediction_file
        self.init(tmpdir=tmpdir) # this provides a temporary file



        print('Loading user data set (step 1 out of 6)')
        self._loading_user_data()
        print('Loading octomers and other data files required for the scoring (step 2 out of 6)')
        self.read_octomers()

        print('Loading the gold standard and user prediction. Takes a few seconds (step 3 out 6')
        self.load_gs(filename=goldstandard)

        print('\nProcessing\nSplitting data sets (step 4 out of 6)')
        self.split_data()
        print('\nComputing probes (step 5 out of 6)')
        self.probe_data_preprocessing1()
        print('\nComputing performances (step 6 out of 6)')
        self.probe_data_processing()

    def init(self, tmpdir=None):
        """Creates the temporary directory and the sub directories.

        Behaviour differs whether the directory was provided
        in the constructor or not.
        """
        self.cwd = os.path.abspath(os.path.curdir)

        if tmpdir is None:
            import tempfile
            self.tmpdir = tempfile.mkdtemp()
        else:
            self.tmpdir = tmpdir
            try:
                os.mkdir(self.tmpdir)
            except:
                pass

        for directory in ['Data', 'Out', 'DV', 'DVP', 'Probes']:
            this = pj(self.tmpdir, directory)
            if os.path.exists(this) is False:
                os.mkdir(this)

    def cleanup(self):
        #TODO
        # remove temp file
        pass

    def load_gs(self, filename=None):
        if filename is None:
            from dreamtools.core import sageutils
            s = sageutils.SynapseClient()
            print('Downloading answers if not already downloaded',)
            out = s.downloadEntity('syn2898469')
            print('...done')
            filename = out.path

        z = ZIP()
        z.loadZIPFile(filename)
        data = z.read('Answers.txt')
        self.gs = pd.read_csv(StringIO.StringIO(data), sep='\t')

    def split_data(self, precision=6):
        """precision is to get same results as in the original perl script"""
        mask = self.gs.Flag == 0
        self.user_data_clean = self.user_data[mask].copy()
        print('Splitting the user data set and removing flagged data (%s out of %s)' % (self.gs.shape[0] - mask.sum(), self.gs.shape[0]))
        self.gs_clean = self.gs[mask].copy()
        # local aliases
        gs = self.gs_clean
        user_data = self.user_data_clean

        pb = progress_bar(66, interval=1)
        for tf_index in range(1,67):
            this_tf = 'TF_%s'  % tf_index
            tf_gs = gs.query("Id == @this_tf").Answer
            tf_user = user_data.query("TF_Id == @this_tf").Signal_Mean
            df = pd.concat([tf_gs, tf_user], axis=1)
            df.to_csv(self._setfile(tf_index, 'Data'), index=False, sep='\t',
                      header=False, float_format="%f")
            pb.animate(tf_index)

    def _loading_user_data(self):
        """Get the file from the form, save it, decompress it."""
        # TODO: replace TF_Id with same name as in GS

        import zipfile
        z = zipfile.ZipFile(self.prediction_file)
        assert len(z.filelist) == 1, "zipped archive should contain only 1 file"

        # extract in byte
        data = z.read(z.filelist[0])


        self.prediction_file_unzipped = 'tmp_' + z.filelist[0].filename

        df = pd.read_csv(StringIO.StringIO(data), sep='\t');# engine='python')

        self.user_data = df

    def validating(self):
        cwd = os.path.abspath(os.path.curdir)
        proc = subprocess.Popen(
                ["perl", "%s/DREAM5_challenge2_Validate.pl"%cwd, "%s" % self.prediction_file_unzipped],
                        stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        error = proc.stderr.read()
        if len(error)>0:
            Exception("Validation failed with this error:" + error)

    def probe_data_preprocessing1(self):
        """Create temporary files for before further processing



        :return: nothing
        """
        # mkdir Probes
        try: os.mkdir('Probes')
        except: pass

        # reads probes (sequences)
        print('Reading probes')
        # just one column so no need for a separator
        probes = pd.read_csv('Data/probes35.txt')

        # create the val.txt (first and third column of pred.txt)
        df = self.user_data[['TF_Id', 'Signal_Mean']].copy()
        df['Signal_Mean'] = df['Signal_Mean'].map(lambda x: round(x,6))

        # data.txt is paste of probes35.txt and val.txt
        data = pd.concat([probes, df], axis=1)

        # Creates probes/TF_1.dat that contains the sequence from the GS and the answer from the user
        # for each TF
        print('Creating probes/TF_1.csv + sorting')
        pb = progress_bar(67, interval=1)
        for i in range(1,67):
            # could use a groupby here ? faster  maybe
            tag = 'TF_%s' % i
            sequence = data[['Sequence']].ix[self.gs.Id==tag]
            answer = data.Signal_Mean[data.TF_Id == tag]
            df = pd.concat([sequence, answer], axis=1)
            df.sort(columns=['Signal_Mean', 'Sequence'], ascending=[False, False], inplace=True)
            df['Signal_Mean'] = df['Signal_Mean'].map(lambda x: round(x,6))
            df.to_csv(self._setfile(i, 'Probes'), sep='\t', index=False, header=False,
                      float_format="%.6f")
            pb.animate(i)

    def read_octomers(self):
        self.octomers_gs = pd.read_csv('Data/8mers_gs.txt', sep='\t', header=None)
        self.octomers = pd.read_csv('Data/all_8mers.txt', sep='\t', header=None)  # contains reverse complemtn
        self.octomers.columns = ['octomer','octomerRC']

        self.probes_gs = pd.read_csv('Data/probe35_gs.txt', header=None, sep='\t')
        self.probes_gs.columns = ['Id', 'Sequence']

    def _setfile(self, index, directory):
        return self.tmpdir + os.sep + directory + os.sep + 'TF_%s' % index + '.csv'

    def probe_data_processing(self):
        #
        """

        :return:
        """

        ########################################  1 Create the Out/TF_XX.dat files
        octomers = self.octomers.octomer
        octomersRC = self.octomers.octomerRC
        mapping1  = dict([(k,v) for k,v in zip(octomers.values, octomersRC.values)])
        mapping2  = dict([(k,v) for k,v in zip(octomersRC.values, octomers.values)])
        keys = tuple(sorted(octomers.values))

        self.keys = keys
        self.mapping1 = mapping1
        Ntf = 66
        pb = progress_bar(Ntf, interval=1)
        pb.animate(0)
        for tf_index in range(1,Ntf+1):
            filename = self._setfile(tf_index, 'Probes')
            tf = pd.read_csv(filename, sep="\t", header=None)
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

            # now let us build the new dataframe for the indices found
            df = pd.DataFrame({0:[k for k in  ids.keys()],
                               1:[np.median(v) for v in ids.values()]})
            df.sort(columns=[1,0], ascending=[False, False], inplace=True)
            df[1] = df[1].map(lambda x: round(x,6))

            df.to_csv(self._setfile(tf_index, 'Out'), sep=' ', index=False, header=None, float_format="%.6f")
            pb.animate(tf_index)

        ################################################# 2 create the DVP

        pb = progress_bar(Ntf, interval=1)
        for tf_index in range(1,Ntf+1):
            tag = 'TF_%s' % tf_index
            tf_probes = list(self.probes_gs.ix[self.probes_gs.groupby('Id').groups[tag]].Sequence)
            tf = pd.read_csv(self._setfile(tf_index, "Probes"), sep="\t",
                             header=None)
            tf.columns = ['Sequence', 'Score']
            dv = tf.Sequence.apply(lambda x: x in tf_probes).astype(int)
            dv.to_csv(self._setfile(tf_index, 'DVP'), header=None, index=None)
            pb.animate(tf_index)

        ########################################################## DV
        gs_octomers = self.octomers_gs.copy()
        gs_octomers.columns = ['id', 'octomer']
        pb = progress_bar(Ntf, interval=1)
        for tf_index in range(1,Ntf+1):
            tag = 'TF_%s' % tf_index
            tf_octomers = list(gs_octomers.ix[gs_octomers.groupby('id').groups[tag]].octomer)
            tf = pd.read_csv(self._setfile(tf_index, "Out"), sep=" ",
                             header=None)
            tf.columns = ['Octomer', 'Score']
            dv = tf.Octomer.apply(lambda x: x in tf_octomers).astype(int)
            dv.to_csv(self._setfile(tf_index, 'DV'), header=None, index=None)
            pb.animate(tf_index)

    def probe_data(self, ROnly):
        """Launch the probe_to_mersFULL.pl script and tf.r script 

        Since this part is long to run (about 4-5 minutes), the output is really
        dependent on the server configuration. This function ideally should be written
        in a very simple manner. However, because of the current configuration server, the 
        timeout is less than the duration of this script. Therefore, trick had to be found. 

        This is done by running the script in the background, writting the status in a frame
        that is refreshed.

        The R command must be after the probe is over.

        :param ROnly: to run only the R script

        
        """
        self.read_octomers()
        self.probe_data_preprocessing1()
        self.probe_data_processing()

    def compute_statistics(self):
        data = {'Pearson': [],
                'Spearman': [],
                'Pearson_Log': [],
                "AUROC_8mer": [],
                "AUPR_8mer": [],
                "AUROC_probe": [],
                "AUPR_probe": []}

        pb = progress_bar(66, interval=1)
        for tf_index in range(1,67):
            dfdata = pd.read_csv(self._setfile(tf_index, "Data"), sep='\t', header=None)
            pearson = dfdata.corr('pearson').ix[0,1]
            spearman = dfdata.corr('spearman').ix[0,1]
            pearsonLog = np.log10(dfdata).corr('pearson').ix[0,1]

            data['Pearson'].append(pearson)
            data['Pearson_Log'].append(pearsonLog)
            data['Spearman'].append(spearman)

            from dreamtools.core.rocs import ROCDiscovery

            dvdata = pd.read_csv(self._setfile(tf_index, "DV"), index_col=False, header=None)
            r = ROCDiscovery(dvdata.values)
            rocdata = r.get_statistics()
            auroc = r.compute_auc(roc=rocdata)
            aupr = r.compute_aupr(roc=rocdata)
            data['AUROC_8mer'].append(auroc)
            data['AUPR_8mer'].append(aupr)

            dvdata = pd.read_csv(self._setfile(tf_index, 'DVP'), index_col=False, header=None)
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
        """Return table with participants results compared to 14 other participants

        14 as in the Leaderboard found here https://www.synapse.org/#!Synapse:syn2887863/wiki/72188


        :return:


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

        participants = pd.read_csv("d5c2_data_table.csv", sep='\t', index_col=0)
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
        participants = pd.read_csv('d5c2_data_plot.csv', sep='\t', )
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



