#-*- python -*-
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
"""This module provides utilities to compute scores related to HPN-Dream8

It can be used and should be used indepently of Synapse altough for testing,
data sets may be downloading from synapse if you don't have any local files to
play with.

Here is an example related to the Network subchallenge::

    >>> from dreamtools.dream8.D8C1 import scoring
    >>> s = scoring.HPNScoringNetwork()
    >>> s.compute_all_descendant_matrices()
    >>> s.compute_all_rocs()
    >>> s.compute_all_aucs()


https://www.synapse.org/#!Synapse:syn1720047/wiki/60530


"""
import csv
import os
import copy
import pickle
import zipfile

import pylab
import numpy as np

from dreamtools.core import rocs
import cython_scoring
from dreamtools.core.ziptools import ZIP
from dreamtools.core.rocs import ROC
from dreamtools.core.challenge import Challenge


__all__ = ["HPNScoringNetwork", "HPNScoring", "HPNScoringNetworkInsilico",
    "HPNScoringNetwork_ranking", "HPNScoringPrediction",
    "HPNScoringPrediction_ranking", "ScoringError",
    "HPNScoringPredictionInsilico_ranking",
    "HPNScoringPredictionInsilico"]


class ScoringError(Exception):
    """An exception class for scoring classes"""
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr("ScoringError(HPN-DREAM8): %s " % self.value )


class HPNScoring(ZIP):
    """Base class common to all scoring classes

    The HPN challenges use data from 32 types of combinaison of cell lines (4) and
    ligands (8). This class provides aliases to:

     * valid cell lines (:attr:`~dreamtools.dream8.D8C1.scoring.HPNScoring.valid_cellLines`)
     * valid ligands (:attr:`~dreamtools.dream8.D8C1.scoring.HPNScoring.valid_ligands`)
     * expected length of the vectors for each cell line
       (:attr:`~dreamtools.dream8.D8C1.scoring.HPNScoring.valid_length`)
     * indices of the row vectors containing the mTOR species within the
       descendancy matrices
       (:attr:`~dreamtools.dream8.D8C1.scoring.HPNScoring.mTor_index`)

    .. note:: all matrices and vectors are sorted according to a hard-coded
        list of species for a combinaison of cell line and ligand. The species
        are indeed sorted alphabetically following hhe same order as in the
        original CSV files containing the data sets.

    In addition, it the :attr:`score` attributes can be used
    to store the score computed by :meth:`compute_score` .

    All classes that need to compute scores require a data file
    submitted by a participant. We enforce the usage of ZIP file, which can
    be loaded by using :meth:`loadZIPFile`.

    """

    def __init__(self, verbose=True):
        super(HPNScoring, self).__init__()
        self._path2data = os.path.split(os.path.abspath(__file__))[0]

        #: List of valid cell lines (e.g, BT20)
        self.valid_cellLines =  ["MCF7", "UACC812", "BT549", "BT20"]
        #: List of valid ligands (e.g, EGF)
        self.valid_ligands = ["EGF", "HGF", "FGF1", "IGF1", "Insulin", "NRG1",
                              "PBS", "Serum"]
        #: length of the vectors to be found within each cell line ignoring TAZ_p89 and FOXO3a_pS318
        # sometimes, like in the true descendants, the TAZ and FOX are inlcude
        # but set to None, which may be confusing
        self.valid_length = {'BT549': 44, 'MCF7': 39, 'UACC812': 44, 'BT20': 46}
        self.valid_length_extended = {'BT549': 45, 'MCF7': 41, 'UACC812': 45,
                                      'BT20': 48}

        #: indices of the mTOR species in the different cell lines within the true descendants vectors
        # assuming length are 44, 39, 44, 46 that is excludnig  the taz and fox phosphos
        self.mTor_index = {'BT20': 23, 'UACC812': 21, 'MCF7':21, 'BT549':21}
        #indices are computed using:

        self.species_to_ignore = {
            'MCF7':['TAZ_pS89', 'FOXO3a_pS318_S321'],
            'BT20':['TAZ_pS89', 'FOXO3a_pS318_S321'],
            'BT549':['TAZ_pS89'],
            'UACC812':['TAZ_pS89']
            }

        # We need to retrieve list of phosphos as coded in the experimental data sets .
        self.cellLines_names_steven = ['UACC812', 'BT549', 'MCF7', 'BT20']
        self.ligands_names_steven = ['Serum', 'PBS', 'EGF', 'Insulin', 'FGF1', 'HGF', 'NRG1', 'IGF1']

        self._score = None
        self.verbose = verbose

    def _get_score(self):
        return self._score
    def _set_score(self, value):
        assert value>=0  and value<=1
        self._score = value
    score = property(_get_score, _set_score,
        doc="R/W attribute to store the score (in [0,1] only)")

    def error(self, message):
        """If you want to raise an error, use this method.

        It raises a ScoringException and set the :attr:`exception`
        attribute. The message is stored in exception.value
        If called, the :attr:`
        ` is set to "INVALID" and
        the score is set to 1 (worst score).

        """
        print("ERROR:"+ message)
        ScoringError(message)

    def load_species(self):
        """Loads names of the expected phospho names for each cell line from the synapse files provided to the users"""
        from dreamtools.dream8.D8C1 import experimental_filename as filename
        z = zipfile.ZipFile(filename)
        self.species = {}
        for cell in self.valid_cellLines:
            header = z.read("experimental/MIDAS/MD_%s_main.csv" % cell).split("\n")[0]
            phosphos = [x.split(":")[1] for x in header.split(",") if x.startswith("DV")]

            phosphos = [x for x in phosphos if x not in self.species_to_ignore[cell]]
            assert len(phosphos) == self.valid_length[cell], "wrong length (%s) for cell %s " % (len(phosphos), cell)
            self.species[cell] = phosphos


class HPNScoringNetworkBase(HPNScoring, Challenge):
    test_synapse_id = "syn1971273"
    true_synapse_id = "syn1971278"

    def __init__(self, filename=None, verbose=True):
        HPNScoring.__init__(self, verbose=verbose)
        Challenge.__init__(self, challenge_name='D8C1')
        self.filename = filename
        self.load_species()

    def _validate_eda(self, filename):

        if self.verbose: print("Validating %s" % filename),
        f = self.zip_data.open(filename)
        reader = csv.reader(f)
        reader.next() # skip the header
        f.close()
        if self.verbose: print("ok")

    def _str_cleanup(self, text):
        # required to cleanup some submissions
        text = text.replace("\r", "\n")
        text = text.replace("\n\n", "\n")
        text.strip()
        return text

    def get_eda_file(self, filename):
        if self.verbose:print("Loading EDA scores from %s" % filename)
        # read the data and stores it into vectors
        #index = self.zip_filenames.index(filename)
        #tail = os.path.split(self.zip_filenames[index])[-1]
        zipdata = self.zip_data.open(filename)

        # prevent issue with NULL byte from Boston team
        data_iter = [x.replace("\x00", "") for x in zipdata]
        data_iter = [x.replace("\t", " ") for x in data_iter]
        data_iter = [self._str_cleanup(x) for x in data_iter if len(x)]

        if len(data_iter) == 1 and "\n" in data_iter[0]:
            data_iter = data_iter[0].split("\n")
        # skip header:
        if "EdgeScore" in data_iter[0]:
            del data_iter[0]

        data = []
        for i, datum in enumerate(data_iter):

            datum = datum.replace("=", " = ").replace("("," (").replace(")", ") ")

            datum = datum.split()
            if len(datum) == 5:
                data.append(datum)
            else:
                ValueError("EDA file (%s) should be made of 5 columns" % filename)
        node1 = [x[0] for x in data]
        node2 = [x[2] for x in data]
        edges = [x[1] for x in data]
        scores = [x[4] for x in data]
        return node1, node2, edges, scores


class HPNScoringNetwork(HPNScoringNetworkBase):
    """Class to compute the score of a Network submission

    A user will provide a ZIP file that contains 65 files: 32 EDA,
    The 32 files should be tagged with the 32 combos of cell
    lines and ligands. To create an instance of HPNScoringNetwork, type::

        s = HPNScoringNetwork("TeamName-Network.zip")
        # or later
        s = HPNScoringNetwork()
        s.load_submission("TeamName-Network.zip")

        s.get_auc_final_scoring() # as in the challenge ignoring some regimes


    You then need to specifically load the EDA files. This may be done
    with :meth:`load_all_eda_files_from_zip`::

        s.load_all_eda_files_from_zip()

    The content of the ZIP file can be validated using the :meth:`validation`
    method.::

        s.validation()

    Each EDA and SIF file must be a complete graph where all species correspond to
    the CSV files provided on the synapse web page. The size of the network
    varies depending on the cell line.

    Each EDA file that contains score on each edge and first needs to be transformed into
    a descendancy matrix. This is achieve via :meth:`compute_descendant_matrix`
    and/or :meth:`compute_descendant_matrix` methods.::

        s.compute_all_descendant_matrices()

    From each matrix, we'd like to compare a specific row (corresponding to
    mTOR) to the true scores that are expected. The true descendant for each
    combinaison of cell line and ligand are provided and loaded in the
    constructor via :meth:`load_true_descendants_from_zip`, which can be called at
    any time.

    """
    test_synapse_id = "syn1971273"
    true_synapse_id = "syn1971278"

    def __init__(self, filename=None, verbose=False, true_descendants=None):
        """

        :param str filename:

        """
        super(HPNScoringNetwork, self).__init__(filename, verbose=verbose)
        self._init()
        if filename:
            self.load_submission(self.filename)
        self.robustness_testing = False
        self.masking = 0.1
        if true_descendants is None:
            self._load_true_descendants_from_zip()
        else:
            self.true_descendants = copy.deepcopy(true_descendants)

    def load_submission(self, filename):
        self.loadZIPFile(filename)
        self.load_all_eda_files_from_zip()

    def _init(self):
        """Creates attributes to store edge scores from 32 EDA files"""
        self.edge_scores = dict([(x,{}) for x in self.valid_cellLines])
        #self.species = dict([(x,{}) for x in self.valid_cellLines])
        self.descendancy_matrices = dict([(x,{}) for x in self.valid_cellLines])
        self.roc = dict([(x,{}) for x in self.valid_cellLines])
        self.auc = dict([(x,{}) for x in self.valid_cellLines])
        self.aupr = dict([(x,{}) for x in self.valid_cellLines])

    def edge_score_to_eda_files(self, teamname):
        directory = teamname
        try:os.mkdir(directory)
        except:pass
        for k1 in self.edge_scores.keys():
            species = self.species[k1]
            N = len(species)
            for k2 in self.edge_scores[k1].keys():
                filename = teamname + "-" +  k1 + "-" + k2 + "-Network.eda"
                fh = open(directory + os.sep + filename, "w")
                assert self.edge_scores[k1][k2].shape == (N, N)
                for i in range(0, N):
                    for j in range(0, N):
                        name1 = species[i]
                        name2 = species[j]
                        value = self.edge_scores[k1][k2][i][j]
                        fh.write("{} (1) {} = {}\n".format(name1, name2,value))
                fh.close()

    def validation(self):
        """General validation

            * Check that there are 32 EDA files
            * For each EDA file, calls further check
                * format of the filename (correct cell line and ligand names)
                * format of the dataa = character with a RHS and LHS
                * LHS is made of 3 elements
                * skip the header

        """
        # check that the number of files are correct.

        if self.verbose:print("Checking number of files and extensions..."),
        extensions = [os.path.splitext(x)[1] for x in self.zip_filenames if "MACOSX" not in x]

        # check that the contents of the SIF are 3 columns
        if self.verbose:
            print("ok\nChecking filename and contents of SIF files"),

        # check that the contents of the EDA files are correct.
        if self.verbose:
            print("All SIF files seem ok\nChecking filename and contents of EDA files"),
        for filename in self.zip_filenames:
            if filename.endswith(".eda"):
                self._check_filename(filename)
                try:
                    self._validate_eda(filename)
                except:
                    pass
        if self.verbose:print("All EDA files seem ok")

    def _check_filename(self, filename):
        filename = os.path.split(filename)[1]
        if len(filename)==0:
            return
        try:
            team, cellLine, ligand, name = filename.split("-")
            if cellLine not in self.valid_cellLines:
                self.error(" * filename %s ill-formed. unrecognised Cell Line. must be in %s " % filename, self.valid_cellLines )
            if ligand not in self.valid_ligands:
                self.error(" * filename %s ill-formed. unrecognised ligand. must be in %s " % filename, self.valid_ligands)
        except ValueError:
            self.error(" * filename %s is ill formed. Expects TeamName-CellLine-Ligand-Network.eda" % filename)

    def compute_score(self, validation=True):
        """Computes the final score that is the average over the 32 AUCs

        This function compute the final score. First, il loads all EDA files
        provided by the  participany (from the ZIP file). Then, it computes
        the 32 descendant matrices. Finally, it computes the 32 ROCS and AUCS.
        The scores is for now based on the z-score. Since scores must be between
        0 and 1, where 0 is the best, we will need to normalise.

        :param bool validation: perform validation of the input ZIP file

        """
        # First let us load all EDA edge scores into 32 matrices in edge_scores
        # together with the correponsind species

        self.compute_all_aucs()
        if len(self.auc['BT20']):
            self.score = self.get_average_auc()

    def get_auc_final_scoring(self):
        """This function returns the mean AUC using only official ligands as
        used in final scoring and collaborative rounds.

        The individual AUCs must be computed first with
        :meth:`compute_all_aucs` or .::


            >>> s = scoring.HPNScoringNetwork(filename)
            >>> auc = s.get_auc_final_scoring()

        """
        self.compute_all_aucs()
        ligands = {'BT20': ['IGF1', 'PBS', 'Serum', 'NRG1', 'HGF', 'EGF',  'FGF1'],
            'BT549': ['IGF1', 'PBS', 'Serum', 'Insulin', 'HGF', 'EGF', 'FGF1'],
            'MCF7': ['IGF1', 'PBS', 'Serum', 'NRG1', 'Insulin', 'HGF', 'EGF', 'FGF1'],
            'UACC812': ['PBS', 'Serum', 'NRG1', 'Insulin', 'HGF', 'EGF', 'FGF1', 'IGF1']}
        auc = np.mean([self.auc[k1][k2] for k1 in self.auc.keys()
            for k2 in self.auc[k1].keys() if  k2 in ligands[k1]])
        return auc

    def _load_true_descendants_from_zip(self):
        """Reads true descendants provided by Steven 27 June 2013

        The ZIP file should contains 32 vectors that contains the score for the
        edge positive (1) or negative (0)

        This method stores the data in the :attr:`true_descendants`.

        """
        self.true_descendants = dict([(x,{}) for x in self.valid_cellLines])
        filename = os.sep.join([self._path2data, "goldstandard", "TrueDescVectors.zip"])

        zipdata = zipfile.ZipFile(filename)
        if self.verbose:
            print("Loading all true descendants data set (%s)" % filename)

        for filename in zipdata.namelist():
            try:
                teamName, cellLine, ligand = os.path.splitext(filename)[0].split("_")
                data = zipdata.open(filename).next()
                data = [int(x) if x!="NaN" else None for x in data.strip().split(',')]
                self.true_descendants[cellLine][ligand] = data[:]
            except:
                #print("note: skipping " + filename)
                pass

    def load_all_eda_files_from_zip(self):
        """Loads all EDA file from a participant into :attr:`edge_scores`"""
        for filename in self.zip_filenames:
            if filename.endswith(".eda") and "__MACOS" not in filename:
                self.load_eda_file(filename)

        # Issue in github https://github.com/dreamtools/dreamtools/issues/16
        M = max([self.edge_scores[cell][l].max() for cell in
            self.cellLines_names_steven for l in self.ligands_names_steven])
        for cell in self.cellLines_names_steven:
            for lig in self.ligands_names_steven:
                self.edge_scores[cell][lig] /= float(M)

    def load_eda_file(self, filename, local=False):
        """Loads scores from one EDA file

        :param filename: here filename should be one of the filename to be
            found within the ZIP file! This is not a standard file system (See
            note).

        Input data is EDA format that is::

            A 1 B = 0.4
            A 1 C = 0.5

        It containts edges such that the final graph is complete and a matrix
        can be built with column1 as the rows and column2 as the columns.
        The values being tmade from the fifth column. Second and fourth are
        ignored.

        loaded data is stored in :attr:`data` as a numpy matrix.

        .. note:: to overwrite the input ZIP file, use :meth:`loadZIPFile`

        """
        if self.verbose:print("Loading EDA scores from %s" % filename),
        if local == True:
            tail = os.path.split(filename)[-1]
            data = open(filename)
            data_iter = csv.reader(data, delimiter=" ")
        else:
            # read the data and stores it into vectors
            index = self.zip_filenames.index(filename)
            tail = os.path.split(self.zip_filenames[index])[-1]
            zipdata = self.zip_data.open(filename)
            data_iter = [x for x in zipdata]

        if len(data_iter) and "EdgeScore" in data_iter[0]:
            del data_iter[0]

        try:
            teamName, cellLine, ligand, tag = tail.split("-")
        except:
            self.error(" * filename %s is ill formed. Expects TeamName-CellLine-Ligand-Network.eda" % filename)
            return

        # skip first row
        #header = data_iter.next()
        data = []
        for i, datum in enumerate(data_iter):
            datum = datum.replace("=", " = ").replace("("," (").replace(")", ") ")

            datum = datum.split()
            if len(datum) == 5:
                data.append(datum)
            elif len(datum) == 0 or len(datum) == 1:
                pass
                #print("Found empty line in EDA file %s" %  filename)
            else:
                self.error("- Line %s in %s is ill formed (expected 3 or 5 columns): %s" % (i,filename, datum))
                break
        node1 = [x[0] for x in data]
        node2 = [x[2] for x in data]
        #edges = [x[1] for x in data]
        scores = [x[4] for x in data]

        N = self.valid_length[cellLine]
        species = self.species[cellLine]

        tempdata  = np.zeros((N, N))
        for x,y,z in zip(node1, node2, scores):
            if x in self.species_to_ignore[cellLine] or y in self.species_to_ignore[cellLine]:
                pass
            else:
                #update from july 16 . error in MIDAS and CSV PKC-delta should
                # have been PKC-delta_pS664 so some people use one or the other
                # similarly for PRKCD
                if x == "PKC-delta_pS664":
                    x = "PKC-delta"

                mapping = {'c-RAF_pS338': "c-Raf_pS338",
                            "YB-1_pS102": "YB-1_PS102",
                            "MEK1_pS217_pS221": "MEK1_pS217_S221",
                            "EGFR_pY922": "EGFR_pY992"
                        }
                for k,v in mapping.iteritems():
                    if x == k:
                        print("Warning mapping required in the EDA")
                        x = v
                    if y == k:
                        y = v

                if "SRC_" in x:
                    x = x.replace("SRC_", "Src_")

                if "SRC_" in y:
                    y = y.replace("SRC_", "Src_")

                if y == "PKC-delta_pS664":
                    y = "PKC-delta"

                if "RB_" in x:
                    x = x.replace("RB_", "Rb_")

                if "RB_" in y:
                    y = y.replace("RB_", "Rb_")

                try:
                    i = species.index(x)
                except:
                    self.error("Invalid species(%s) found in the file %s " % (x, filename))
                    break
                try:
                    j = species.index(y)
                except:
                    self.error("Invalid species(%s) found in the file %s " % (y, filename))
                    break

                tempdata[i][j] = z
        self.edge_scores[cellLine][ligand] = abs(tempdata)
        M = self.edge_scores[cellLine][ligand].max()
        #if M>1:
        #    print("!!!!!!!!!!!!!!!!!!!!1, %s %s" % (cellLine, ligand))
        #    self.edge_scores[cellLine][ligand] /= float(M)
        
        # max is now computed across all networks
        # https://github.com/dreamtools/dreamtools/issues/16
        # self.edge_scores[cellLine][ligand] /= float(M)


    def compute_all_descendant_matrices(self):
        """Compute all descendancy matrices

        For each cell line and ligand, the matrix is stored
        in the :attr:`edge_scores` dictionary.

        .. seealso:: :meth:`compute_descendant_matrix`

        """
        for c in self.valid_cellLines:
            for l in self.valid_ligands:
                if self.verbose:print("Computing descendancy matrix for (%s, %s)" % (c,l))
                self.compute_descendant_matrix(c,l)

    def compute_descendant_matrix(self, cellLine, ligand):
        """Computes the descendancy matrix for a given cell line and ligand

        :param str cellLine: a valid cell line
        :param str ligand: a valid ligand


        .. note:: we use a cython module to conmpute the matrix. This function
            is the bottle neck of the entire procedure to compute the score.
            This is especially important to estimate te null distribution of
            the AUCs. Using Cython does not improve much the performance (80%)
            but it improves it...

        .. seealso:: :meth:`compute_all_descendant_matrices`
        """
        cython_scoring.compute_descendant_matrix(self, cellLine, ligand)

    def compute_metrics(self, cellLine, ligand):
        scores = self._get_scores(cellLine, ligand)
        classes = self._get_classes(cellLine, ligand)
        classes = [x for x in classes if x!=None]

        sorted_indices = np.argsort(1-scores)
        sorted_scores = [scores[i] for i in sorted_indices]
        sorted_classes = [classes[i] for i in sorted_indices]

        P = float(classes.count(1))
        N = float(classes.count(0))

        roc = {"fpr":[], "tpr":[], "precision":[], "FP":[], "TP":[],
            "recall":[], "accuracy":[], "Fmeasure":[], 'threshold':[]}

        for i in range(0, len(scores)):
            threshold = sorted_scores[i]
            TP = float(sorted_classes[0:i].count(1))
            FP = float(sorted_classes[0:i].count(0))
            TPR = TP/P
            FPR = FP/N
            #print classes[i], sorted_scores[i], threshold, TP, FP, TPR, FPR, TP+FP
            precision = TP / (TP+FP)
            recall = TP / P
            accuracy = (TP+FP)/(P+N)
            if recall >0 and precision >0 :
                Fmeasure = 2./(1./precision+1./recall)
            else:
                Fmeasure = np.nan

            roc["threshold"].append(threshold)
            roc["FP"].append(FP)
            roc["TP"].append(TP)
            roc['tpr'].append(TPR)
            roc['fpr'].append(FPR)
            roc['precision'].append(precision)
            roc['recall'].append(recall)
            roc['accuracy'].append(accuracy)
            roc['Fmeasure'].append(Fmeasure)

        return roc

    def _compute_fpr_tpr(self, FP, TP, N, P):
        roc = {"fpr":[], "tpr":[], "FP":[], "TP":[]}
        roc['fpr'] = FP/float(N)
        roc['tpr'] = TP/float(P)
        roc['TP'] = TP
        roc['FP'] = FP
        return roc

    def compute_roc(self, cellLine, ligand):
        """Compute the ROC curve

        :param scores: list of scores (probabilities)
        :param classes: list of classes (true values)


        .. seealso:: :meth:`compute_roc`
        """
        scores = self.descendancy_matrices[cellLine][ligand][self.mTor_index[cellLine]]
        # remove the None otherwise classes and scores are different
        classes = [x for x in self.true_descendants[cellLine][ligand] if x!=None]

        if self.robustness_testing:
            N = len(scores)
            from random import sample
            indices = sample(range(0,N), int((1-self.masking)*N))
            scores = np.array([s for i,s in enumerate(scores) if i in
                indices])
            classes = [s for i,s in enumerate(classes) if i in indices]

        assert len(scores) ==  len(classes)
        sorted_indices = np.argsort(1-scores)
        sorted_scores = [scores[i] for i in sorted_indices]
        sorted_classes = [classes[i] for i in sorted_indices]
        P = float(classes.count(1))
        N = float(classes.count(0))
        FP = 0
        TP = 0
        #
        roc = {"fpr":[], "tpr":[], "precision":[], "FP":[], "TP":[],
            "recall":[], "accuracy":[], "Fmeasure":[], 'threshold':[]}
        fprev = 1.1 # scores are less than 1

        # an efficient algorithm to compute ROC based on T.Fawcett Pattern
        # Recognition Letters 27, 2006
        i = 0
        while i<len(scores):
            cls = sorted_classes[i]
            score = sorted_scores[i]

            if score != fprev and cls!=None:
                thisroc = self._compute_fpr_tpr(FP, TP, N, P)
                for key in ['fpr', 'tpr', "FP", "TP"]:
                    roc[key].append(thisroc[key])
                roc['threshold'].append(fprev)
                fprev = score

            if cls == 1:
                TP += 1
            elif cls == 0:
                FP += 1
            elif cls == None:
                pass
            else:
                raise ValueError("found a class value different from 0,1 or None")
            i += 1
        thisroc = self._compute_fpr_tpr(FP, TP, N, P)
        for key in ['fpr', 'tpr', "FP", "TP"]:
            roc[key].append(thisroc[key])
        roc['threshold'].append(sorted_scores[-1])

        roc = self.compute_other_metrics(roc)
        return roc

    def compute_other_metrics(self, roc):
        #Be aware that there is alway a first value TP=0,FP=0
        # this should be handled with care the recall/precision computatio
        # This first value is used to compute fpr and tpr but should not be used
        # here
        FP = np.array([float(x) for x in roc['FP']])
        TP = np.array([float(x) for x in roc['TP']])
        N = max(FP) + max(TP)

        # The first value of precision is undefined since FP+TP=0
        # It does not matter since it will be overwritten as explained here
        # below
        precision = TP / (FP+TP)
        recall = TP/float(max(TP))
        # The second value may also be be an issue. There are 2 cases.
        # 1. TP>0
        # 2. TP == 0
        # In the second case,  TP=0 and FP==0 should not happen. FP > 0 instead.
        # In which case, recall = 0 and precision=0. No ambiguity
        # In the first case, if TP>0 then precision >0 and recall > 0.
        # Therefore we end up without a defined value at recall==0
        # So we should set a recall=0 for which precision will be the same as
        # the one where recall >0
        # somehow, precision and recall
        if TP[1]>0:
            precision[0] = precision[1]
        else:
            precision[0] = 0

        roc['precision'] = [float(x) for x in precision]
        roc['recall'] = [float(x) for x in recall]
        return roc

    def compute_auc(self, roc):
        """Compute AUC given a ROC data set

        :param str roc: The roc data structure must be a dictionary with "tpr"
            key. Could be an variable returned by :meth:`compute_roc`.

        """
        import scipy.integrate
        value = scipy.integrate.trapz(roc['tpr'], roc['fpr'])
        return value

    def _get_scores(self, cellLine, ligand):
        """Returns scores of a given descendancy matrix taking care of mTor index"""
        scores = self.descendancy_matrices[cellLine][ligand][self.mTor_index[cellLine]]
        return scores

    def _get_classes(self, cellLine, ligand):
        classes = self.true_descendants[cellLine][ligand]
        return classes

    def compute_all_rocs(self):
        """Computes all ROC curves

        This function can be called once EDA files are loaded and all
        descendant matrices have been computed as well.

        .. seealso:: :meth:`load_all_eda_files_from_zip`,
            :meth:`compute_all_descendant_matrices`
        """
        for c in self.valid_cellLines:
            for l in self.valid_ligands:
                roc = self.compute_roc(c, l )
                self.roc[c][l] = roc.copy()

    def compute_all_aucs(self):
        """Computes all AUC

        This function can be called once EDA files are loaded and all
        descendant matrices have been computed as well.

        In theory, one should compute ROC and then AUC but this function
        recomputes ROC since it is fast to compute.

        .. seealso:: :meth:`load_all_eda_files_from_zip`,
            :meth:`compute_all_descendant_matrices`
        """
        self.validation()

        self.compute_all_descendant_matrices()

        for c in self.valid_cellLines:
            for l in self.valid_ligands:
                roc = self.compute_roc(c, l)
                self.roc[c][l] = roc.copy()
                auc = self.compute_auc(roc)
                self.auc[c][l] = auc

    def compute_all_auprs(self):
        for c in self.valid_cellLines:
            for l in self.valid_ligands:
                roc = self.compute_roc(c, l )
                self.roc[c][l] = roc.copy()
                aupr = self.compute_aupr(roc)
                self.aupr[c][l] = aupr

    def compute_all_metrics(self):
        for c in self.valid_cellLines:
            for l in self.valid_ligands:
                roc = self.compute_metrics(c, l)
                self.roc[c][l] = roc.copy()
                auc = self.compute_aupr(roc)
                self.aupr[c][l] = auc

    def compute_aupr(self, roc):
        import scipy.integrate
        value = scipy.integrate.trapz(roc['precision'], x=roc['recall'])
        return value

    def get_aucs(self):
        """Returns all AUCs"""
        values = [self.auc[k1][k2] for k1 in self.auc.keys() for k2 in self.auc[k1].keys()]
        return values

    def get_average_auc(self):
        """Returns mean of all AUCs"""
        values = self.get_aucs()
        return np.mean(values)

    def plot_roc(self, cellLine, ligand, hold=False):
        """Plots a psecific  ROC curve"""
        from pylab import plot, clf, grid, title

        x = self.roc[cellLine][ligand]['fpr']
        y = self.roc[cellLine][ligand]['tpr']
        auc = self.auc[cellLine][ligand]

        if hold == False:
            clf()
        else:
            from pylab import hold
            hold(True)

        plot(x, y, '-o')
        plot(x,x,'r')
        title("ROC for %s/%s (AUC=%s)" % (cellLine, ligand, auc))
        grid(True)

    def get_null_distribution(self, sample=100, cellLine="BT20", ligand="EGF",
             store_rocs=False, distr="uniform"):
        """Computes the null distribution for a given combinaison

          * Creates a uniformly distribution of a EDA file and stores it in the
            edge_score attribute.
          * recompute the corresponding descendancy matrix
          * Get the corresponding true prediction
          * compute the ROC and AUC

        :param int sample: number of distribution to compute
        :param cellLine:
        :param ligand:
        :param bool store_rocs: if set to True, save the rocs as well
        :return: rocs and aucs (rocs is set to [] for debugging)

        .. plot::
            :include-source:

            from dreamtools.dream8.D8C1 import scoring
            from pylab import clf, plot, hist, grid, pi, exp, sqrt, mean, std
            s = scoring.HPNScoringNetwork()
            rocs, aucs, auprs = s.get_null_distribution(100)
            mu = mean(aucs)
            sigma = std(aucs)
            clf()
            res = hist(aucs,50, normed=True)
            plot(res[1], 1/(sigma * sqrt(2 * pi)) * exp( - (res[1] - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
            grid()

        """
        aucs = []
        #rocs = []
        auprs = []

        N = self.valid_length[cellLine]
        c = cellLine
        l = ligand
        for i in range(0, sample):
            if distr == "inverse":
                x = [float(x)/(N*N) for x in range(1, N*N + 1)]
                np.random.shuffle(x) # in line shuffling
                #reshape and create numpy array
                self.edge_scores[c][l] = np.array(x).reshape(N,N)
            elif distr == "uniform":
                self.edge_scores[c][l] = np.random.uniform(size=N*N).reshape(N,N)
            self.compute_descendant_matrix(c,l)
            roc = self.compute_roc(c, l)
            auc = self.compute_auc(roc)
            aupr = self.compute_aupr(roc)
            if store_rocs:
                rocs.append(roc)
            aucs.append(auc)
            auprs.append(aupr)
        return rocs, aucs, auprs

    def plot_all_rocs(self, cellLines=None):
        """Plots all 32 ROC once scores/rocs have been computed


        .. plot::
            :include-source:
            :width: 80%

            from pylab import clf, plot, hist, grid
            from dreamtools.dream8.D8C1 import scoring
            import os
            s = scoring.HPNScoringNetwork()
            filename = s._path2data + os.sep + 'templates'+os.sep +'alphabeta-Network.zip'
            s.load_submission(filename)
            s.compute_score()
            s.plot_all_rocs()

        """
        if cellLines is None:
            cellLines = self.valid_cellLines
        else:
            cellLines = [cellLines]

        pylab.clf()
        for c in cellLines:
            for l in self.valid_ligands:
                x = self.roc[c][l]['fpr']
                y = self.roc[c][l]['tpr']
                #auc = self.auc[c][l]
                pylab.plot(x, y, '-o', label="%s-%s" % (c,l))
                pylab.hold(True)

        pylab.title("32 ROCs")
        pylab.grid(True)
        pylab.plot(x, x, '--k', linewidth=2)

    def get_mean_zscores(self, aucs=None):
        zscores = self.get_zscores(aucs)
        mu = np.mean([zscores[k1][k2] for k1 in zscores.keys()
            for k2 in zscores[k1].keys()])
        return mu

    def get_zscores(self, aucs=None):
        """

        """
        mu, sigma = self.get_mean_and_sigma_null_parameters()
        zscores = {}
        for c in self.valid_cellLines:
            zscores[c] = {}
            for l in self.valid_ligands:
                if aucs:
                    zscores[c][l] = (aucs[c][l] - mu[c][l])/sigma[c][l]
                else:
                    zscores[c][l] = (self.auc[c][l] - mu[c][l])/sigma[c][l]
        return zscores

    def print_aucs(self):
        # the order here is defined to compare with steven results but could be
        # chnaged later on.
        self.compute_all_aucs()
        for c in self.cellLines_names_steven:
            #["UACC812","BT549","MCF7","BT20"]:
            print(c, "\t"),
            for l in self.ligands_names_steven:
                # ["Serum","PBS", "EGF", "Insulin", "FGF1", "HGF", "NRG1", "IGF1"]:
                roc = self.compute_roc(c, l)
                auc = self.compute_auc(roc)
                print auc,"\t ",
            print

    def get_mean_and_sigma_null_parameters(self):
        """Retrieve mean and sigma for 32 combi from a null AUC distribution"""
        import sc1a_tools
        null = sc1a_tools.AUCnull(self.valid_cellLines, self.valid_ligands, verbose=False)
        #filename = 'sc1a_null_aucs_mean_sigma.dat'
        null.loadaucs()
        mean = null.get_mean_dict()
        sigma = null.get_sigma_dict()
        return mean, sigma


class HPNScoringNetwork_ranking(HPNScoring):
    """This class is used to compute the ranks of the different participants
    based on an average rank over the 32 combinaisons of cell line and ligands.

    ::

        s = HPNScoringNetwork(filename="file1zip")
        s.compute_all_aucs()

        sall = HPNScoringNetwork_all()
        # s.aucs is a list where each element is a dictionary of
        sall.add_auc(s1.auc, "team1")

        # let us build
        aucs2 = copy.deepcopy(s.auc)
        for c in s.valid_cellLines:
            for l in s.valid_ligands:
                auc2[c][l] = numpy.random.uniform(0.5,0.7)

        sall.add_auc(s2.auc, "team2")
        sall.get_ranking()
        {'team1': 1.96875, 'team2': 1.03125}

    This class is independent of HPNSCoringNetwork.
    However, it takes as input the returned values of
    HPNScoringNetwork.compute_all_auc()

    """
    def __init__(self):
        super(HPNScoringNetwork_ranking, self).__init__()
        self.aucs = []
        self.participants = []

        # we remove here the non-robust regime.
        # communication with steven the 4th Nov to inclde
        #  UACC812,IGF1 The 3 to be removed are:
        #  BT549,FGF1   BT549,NRG1   BT20,insulin

        # update from Nov 20th, BT549 FGF1 is now back into business

        self.valid_ligands_final = {
            'UACC812': ['PBS', 'Serum', 'NRG1', 'Insulin', 'HGF', 'EGF', 'FGF1',  'IGF1'],
            'BT20': ['IGF1', 'PBS', 'Serum', 'NRG1', 'HGF', 'EGF', 'FGF1'],
            'BT549': ['IGF1', 'PBS', 'Serum',  'Insulin', 'HGF', 'EGF', 'FGF1'],
            'MCF7': ['IGF1', 'PBS', 'Serum', 'NRG1', 'Insulin', 'HGF', 'EGF', 'FGF1']
            }

    def get_empty_auc(self):
        auc = {}
        for c in self.valid_cellLines:
            auc[c] = {}
            for l in self.valid_ligands_final[c]:
                auc[c][l] = 0
        return auc

    def add_auc(self, auc, participant_id):
        if participant_id in self.participants:
            raise ValueError("participant already added (%s)" % participant_id)
        if auc == None:
            auc = self.get_empty_auc()
        else:
            # copy only the combi for the final leaderboard.
            temp_auc = {}
            for c in self.valid_cellLines:
                temp_auc[c] = {}
                for l in self.valid_ligands_final[c]:
                    temp_auc[c][l] = auc[c][l]
        self.aucs.append(temp_auc)

        self.participants.append(participant_id)
        self._compute_ranks()

    def _rank_index(self, vector):
        sorted_vector = sorted(vector)
        return [sorted_vector.index(x) for x in vector]

    def _compute_ranks(self, invalid=False):
        """If there are some invalid submissions, this may not work anymore """
        N = len(self.aucs)
        ranks = {}
        for c in self.valid_cellLines:
            ranks[c] = {}
            for l in self.valid_ligands_final[c]:
                # for final scores, some combi are removed

                # get this AUC for all participant
                aucs = [x[c][l] for x in self.aucs]
                M = len([x[c][l] for x in self.aucs if x[c][l]==0])
                if M>0:print "what is M: ",M
                # but use a reverse order hence 1-x for the sorting
                if invalid:
                    indices = np.argsort([1-x for x in aucs])
                else:
                    indices = [x+1 for x in self._rank_index([1-x for x in aucs])]

                # need to append all participants that are invalid with same
                # rank that is maxRank
                if invalid:
                    ranks[c][l] = [list(indices).index(i)+1 for i in range(0,len(indices))]
                    # reset all final values to max rank
                    maxRank = N-M+1
                    ranks[c][l] = [x if x<maxRank else maxRank for x in ranks[c][l]]
                else:
                    ranks[c][l] = indices[:]

        self.ranks = copy.deepcopy(ranks)

    def get_ranking(self):
        ranking = {}
        for k in self.participants:
            ranks = self.get_rank_participant(k)
            mu = np.mean([ranks[k1][k2] for k1 in ranks.keys() for k2 in ranks[k1].keys()])
            ranking[k] = mu
        return ranking

    def get_mean_ranks(self):
        return self.get_ranking()

    def get_integer_ranks(self):
        ranking = self.get_ranking()
        integer_ranks = {}

        # get teams and ranks
        teams_ranks = list(ranking.iteritems())
        teams = [x[0] for x in teams_ranks]
        mean_ranks = [x[1] for x in teams_ranks]

        for i, index in enumerate(np.argsort(mean_ranks)):
            integer_ranks[teams[int(index)]] = i+1
        return integer_ranks

    def get_rank_participant(self, participant):
        ranks = {}
        if participant in self.participants:
            index = self.participants.index(participant)
            for c in self.valid_cellLines:
                ranks[c] = {}
                for l in self.valid_ligands_final[c]:
                    ranks[c][l] = self.ranks[c][l][index]
            return ranks
        else:
            raise ValueError("unknown participant")
    # duplicated from HPNScoringNetwork to update leadeboard easily
    def get_mean_zscores(self):
        zscores = {}
        for i,k in enumerate(self.participants):
            zscore = self._get_zscores(self.aucs[i])
            #print zscore
            mu = np.mean([zscore[k1][k2] for k1 in zscore.keys()
                for k2 in zscore[k1].keys()])
            zscores[k] = mu
        return zscores

    # duplicated from HPNScoringNetwork to update leadeboard easily
    def _get_zscores(self, aucs):
        """ """
        mean, sigma = self._get_mean_and_sigma_null_parameters()
        zscores = {}
        for c in self.valid_cellLines:
            zscores[c] = {}
            for l in self.valid_ligands_final[c]:
                zscores[c][l] = (aucs[c][l] - mean[c][l])/sigma[c][l]
        return zscores

    # duplicated from HPNScoringNetwork to update leadeboard easily
    def _get_mean_and_sigma_null_parameters(self):
        """Retrieve mean and sigma for 32 combi from a null AUC distribution"""
        import sc1a_tools
        null = sc1a_tools.AUCnull(self.valid_cellLines, self.valid_ligands, verbose=False)
        filename = 'sc1a_null_aucs_mean_sigma.dat'
        filename = os.sep.join([self._path2data, "data", filename])
        null.loadaucs(filename)
        mean = null.get_mean_dict()
        sigma = null.get_sigma_dict()
        return mean, sigma


class HPNScoringNetworkInsilico(HPNScoringNetworkBase):
    """Scoring class for HPN DREAM8 Network Insilico sub challenge


    This class retrieves the true graph and a test example from synapse.

    ::

        from dreamtools.dream8.D8C1 import HPNScoringNetworkInsilico
        s = HPNScoringNetworkInsilico()
        import os
        filename = s._path2data + os.sep + 'templates' + os.sep + 'alphabeta-Network-Insilico.zip'
        s.read_file(filename)



    .. note:: If you want to test your own local file, provide a filename.

    """
    test_synapse_id = "syn1973430"
    true_synapse_id = "syn1976597"
    def __init__(self, filename=None, verbose=False):
        super(HPNScoringNetworkInsilico, self).__init__(filename,
                verbose=verbose)

        self.read_file(filename)
        self.true_graph = self._load_true_graph_from_zip()

    def read_file(self, filename):
        self.filename = filename
        try:
            self.loadZIPFile(self.filename)
        except Exception, e:
            print e
            # it not read permission loadZIP and get_eda will fail,
            self.error("Could not read the data (invalid ZIP ?)")

        try:
            self.user_graph = self._get_participant_eda()
        except Exception, e:
            print e
            # it not read permission loadZIP and get_eda will fail,
            self.error("Could not compute EDA")

    def _load_true_graph_from_zip(self):
        """Reads true graph  provided by Steven 10 July 2013

        The ZIP file should contain a 20 by 20 matrix

        """
        filename = os.sep.join([self._path2data, "goldstandard", "TrueGraph.csv"])
        reader = csv.reader(open(filename, "r"))
        data = np.array(list(reader), dtype="float")
        return data

    def _get_participant_eda(self):
        """This function retrieves the EDA file from a participant


        :return: a numpy matrix with column and row names stored in :attr:`species`

        """
        filenames = [x for x in self.zip_filenames if x.endswith(".eda") and "__MACOSX" not in x]
        assert len(filenames) == 1
        filename = filenames[0]
        node1, node2, edges, scores = self.get_eda_file(filename)

        N = 20
        species =  ["AB"+str(i) for i in range(1,N+1)]

        tempdata  = np.zeros((N, N))
        for x,y,z in zip(node1, node2, scores):
            i = species.index(x.upper())
            j = species.index(y.upper())
            tempdata[i][j] = z

        tempdata = abs(tempdata)

        M = tempdata.max()
        if M>1:
            tempdata /= float(M)
        #self.species = species[:]

        return tempdata

    def to_eda(self, filename):
        """EXports the user EDA file"""
        fh = open(filename, "w")
        fh.write("EdgeScore\n")
        for i in range(0,20):
            for j in range(0,20):
                fh.write("AB%s (1) AB%s = %s\n" % (i+1, j+1, self.user_graph[i][j]))

        fh.close()

    def get_roc(self):
        """Gets a ROC instance using thegiven the user and true graphs as inputs"""
        roc = ROC()
        roc.scores = self.user_graph.flatten()
        roc.classes = self.true_graph.flatten()
        return roc

    def get_auc(self):
        roc = ROC()
        roc.scores = self.user_graph.flatten()
        roc.classes = self.true_graph.flatten()
        roc_data = roc.get_roc()
        auc = roc.compute_auc(roc_data)
        return auc

    def _get_auc(self):
        return self.get_auc()
    auc = property(_get_auc)

    def get_null_auc_aupr(self, N):
        """Get null distribution of the AUCs and AUPRs

        :param int N: number of samples
        :return: tuple made of 2 lists: the AUCc ad AUPRs

        """

        roc = rocs.ROC()
        roc.scores = self.user_graph.flatten()
        roc.classes = self.true_graph.flatten()

        aucs = []
        auprs = []
        for i in range(0, N):
            if divmod(i, 1000)[1] == 0 and i!=0:
                print("%s completed" % (i/float(N)*100))
            roc.scores = np.random.uniform(0,1,400)
            roc_data = roc.get_roc()
            auc = roc.compute_auc(roc_data)
            aupr = roc.compute_aupr(roc_data)
            aucs.append(auc)
            auprs.append(aupr)
        return aucs, auprs

    def plot_null_distribution(self, aucs=None, auprs=None, N=10000):
        """Plots the null distribution of the AUCs


        .. plot::
            :include-source:
            :width: 80%

            from dreamtools.dream8.D8C1 import HPNScoringNetworkInsilico
            import os

            s = HPNScoringNetworkInsilico()
            filename = s._path2data + os.sep + 'templates' + os.sep + 'alphabeta-Network-Insilico.zip'
            s.read_file(filename)
            aucs, auprs = s.get_null_auc_aupr(1000)
            s.plot_null_distribution(aucs)
            from pylab import xlim
            xlim([0.35,0.65])


        """
        if aucs == None and auprs == None:
            aucs, auprs = self.get_null_auc_aupr(N)

        if aucs:
            pylab.figure(1)
            pylab.clf()
            pylab.hist(aucs, bins=100, normed=True)
            pylab.grid(True)
            pylab.xlim([0,1])
            pylab.title("AUCs null distribution")

            import scipy.stats
            mu, sigma = scipy.stats.norm.fit(aucs)
            X = pylab.linspace(0,1,100)
            pylab.plot(X, scipy.stats.norm.pdf(X, loc=mu, scale=sigma), "r")
            #except Exception:
            #    raise Exception

            pylab.savefig("SC1B_aucs_null_distribution.png")

        if auprs:
            pylab.figure(2)
            pylab.clf()
            auprs2 = [x for x in auprs if np.isnan(x)==False]
            pylab.hist(auprs2, bins=100, normed=True)
            pylab.xlim([0,1])
            pylab.grid(True)
            pylab.title("AUCs null distribution")
            pylab.savefig("SC1B_auprs_null_distribution.png")

    def get_zscore(self):
        """Returns scores for the current submission

        :return: a single value based on the assumption that the distribution of
            the NULL AUC follows a gaussian distribution with parameters that
            are hardcoded as mu=0.497404 and std=0.037436.

            aucs2, auprs2 = s.get_null_auc_aupr(500000)
            scipy.stats.gamma.fit([x for x in auprs if numpy.isnan(x)==False])
            scipy.stats.norm.fit(aucs)

        """
        # based on 1,000,000 simu

        norm_params = {"mu": 0.4974677, "sigma": 0.0373782}
        #gamma_params = {
        #    "a":      7.23283255,
        #    "loc":    0.13995634,
        #    ":scale": 0.00838379}

        roc = self.get_roc()
        roc_data = roc.get_roc()
        auc = roc.compute_auc(roc_data)
        #aupr = roc.compute_aupr(roc_data)
        return (auc-norm_params['mu'])/ norm_params['sigma']

    def compute_score(self):
        """The official score for the SC1B challenge

        :return: zscore

        """
        try:
            zscore = self.get_zscore()
            return zscore
        except:
            pass


class HPNScoringPredictionBase(HPNScoring):
    def __init__(self, filename=None, verbose=False):
        super(HPNScoringPredictionBase, self).__init__(verbose=verbose)
        self.times = [0,5,15,30,60,120,240]
        self.load_species()
        self.filename = filename


class HPNScoringPrediction(HPNScoringPredictionBase):
    test_synapse_id = "syn2000886"
    true_synapse_id = "syn2009136"   # for now it is local in the SC2A file. Could use
                           # theMIDAS as well
    def __init__(self, filename=None, verbose=False):
        super(HPNScoringPrediction, self).__init__(filename)
        self.loadZIPFile(self.filename)

        filename = os.sep.join([self._path2data, "goldstandard", "TruePrediction.zip"])
        self.true_desc_filename = filename

        # same as species_to_ignore + mTOR + target of the inhibitors email
        # steven hill 10/7/2013
        self.phosphos_to_exclude = {
                'MCF7': ['TAZ_pS89', 'FOXO3a_pS318_S321', 'mTOR_pS2448'],
                'UACC812': ['TAZ_pS89','mTOR_pS2448'],
                'BT20': ['TAZ_pS89', 'FOXO3a_pS318_S321', 'mTOR_pS2448'],
                'BT549': ['TAZ_pS89','mTOR_pS2448']
        }

        self.rmse = {}
        self.get_true_prediction()
        self.get_user_prediction()

    def get_user_prediction(self):
        """

        should be MIDAS files as in https://www.synapse.org/#!Synapse:syn1973835
        """
        # look only at inhibitor 3
        self.user_prediction = {}

        filenames = [x for x in self.zip_filenames if x.endswith(".csv") if "TestInhib3" in x and "MACOS" not in x]

        if len(filenames) != 4:
            self.error("Got (%s) files with a correct pattern. Expected 4" % len(filenames))
            print filenames

        if self.verbose:
            print("Loading MIDAS files")

        for filename in filenames:
            tail = os.path.split(filename)[-1]
            team, cell, ligand, other = tail.split("-")
            if cell not in self.valid_cellLines:
                self.error("filename with invalid cellLine %s " % cell)

            zipdata = self.zip_data.open(filename, "rU")  # somehow fneeded for mac users
            data_iter = csv.reader(zipdata, delimiter=",")

            # get the header
            header = data_iter.next()
            # There should be 56 lines exacly with the 8 stimuli times 7 times
            # for all phosphos
            if len(header) == 0:
                self.error("Cannot read the header : %s in %s" % (header, filename ))
                return

            if header[0] != "TR:%s:CellLine" % cell:
                self.error("Error in the header of %s (first row)" % filename )
            stimuli = [x.split(":")[1] for x in header[1:9]]
            if sorted(stimuli) != sorted(self.valid_ligands):
                self.error("Error in the header of %s (invalid stimuli ?)" % filename )
            if header[9] not in ["DA:ALL", "DA::ALL"]:
                self.error("Expected a DA:ALL column in the header at column 10, which was not found")
            phosphos = [x.split(":")[1] for x in header[10:]]
            if len(phosphos) != self.valid_length[cell] and len(phosphos) != self.valid_length_extended[cell]:
                print("WARNING: length don't seem correct")

            if "PKC-delta_pS664" in phosphos:
                index = phosphos.index("PKC-delta_pS664")
                phosphos[index] = "PKC-delta"

            self.user_prediction[cell] = {}
            for phospho in phosphos:
                self.user_prediction[cell][phospho] = {}
                for ligand in self.valid_ligands:
                    self.user_prediction[cell][phospho][ligand] = [0,0,0,0,0,0,0] # 7 times

            # TODO: check that phosphos agree with the true prediction ?
            for iter, row in enumerate(data_iter):
                # get time index
                if len(row)==0:
                    continue
                time = int(row[9])
                itime = self.times.index(time)

                # get the stimuli name for that row
                this_stimuli = [int(x) for x in row[1:9]]
                if sum(this_stimuli) !=1:
                    self.error("Error: found a row with 0 or more than 1 stimuli on row %s (cell %s)" % (iter, cell))
                this_stimulus = self.valid_ligands[this_stimuli.index(1)] # get the unique ligand name

                for ip, phospho in enumerate(phosphos):
                    datum = row[10+ip]
                    #print cell, phospho, this_stimulus, itime
                    if datum == "NA":
                        datum = np.nan
                    else:
                        try:
                            datum = float(datum)
                        except Exception:
                            print row
                            raise Exception
                    self.user_prediction[cell][phospho][this_stimulus][itime] = datum

    def get_true_prediction(self):
        """Reads true predcition from the 4 CSV files that contain the true prediction

        data is stored as follows in the tru_prediction attribute:

        """
        self.true_prediction = {}

        zipdata = zipfile.ZipFile(self.true_desc_filename)

        for cell in self.valid_cellLines:
            self.true_prediction[cell] = {}

            filename = [x for x in zipdata.namelist() if "%s_main_Test.csv" % cell in x][0]
            data = zipdata.open(filename)

            #filename = "SC2A/%s_main_Test.csv" % cell
            #print("Reading true prediction from %s" % filename)
            #fh = open(filename, "r")
            #data = csv.reader(fh)

            slideId = data.next()
            if cell == "UACC812": # skip another line
                slideId = data.next()
            names = data.next()
            hugoId = data.next()
            dummy = data.next()# skip a line

            names = [x.strip() for x in names.split(",")]
            # now the data with col1 = cellline, co2=inhibito, col3=stimulus,
            # col4=timepoints
            indices_to_exclude = [0, 1, 2, 3]
            # create the phospho keys
            for this in self.phosphos_to_exclude[cell]:
                index = names.index(this)
                indices_to_exclude.append(index)

            # create the key to hold this cell line
            self.true_prediction[cell] = {}

            # create the key to hold all phosphos
            for i,name in enumerate(names):
                if i not in indices_to_exclude:
                    self.true_prediction[cell][name] = {}
                    # create the key to hold all ligans
                    for ligand in self.valid_ligands:
                        # build up the 7-length vector to hold the data
                        # each element is a list so that we can append
                        # replicates if any
                        # note a python caveat [[]] * 7 creates 7 references
                        # empty lists. don't use.
                        self.true_prediction[cell][name][ligand] = [[],[],[],[],[],[],[]]
                else:
                    pass

            # now scan the data
            times = ["0min", "5min", "15min", "30min", "60min", "2hr", "4hr"]
            for row in data:
                row = [x.strip() for x in row.split(",")]
                if row[1] == "AZD8055": # this is the inhibitor we are interested in
                    ligand = row[2]
                    if ligand not in self.valid_ligands and ligand!="":
                        raise ValueError("Invalid ligand")

                    # get time and correspoding index in the list of valid times
                    thistime = row[3]
                    time_index = times.index(thistime)

                    # append the data to the relevant phospho index
                    for i, phospho in enumerate(names):
                        # ignore the indices related to FOX, TAX, mTor
                        if i not in indices_to_exclude:
                            datum = row[i]
                            if ligand == "": # happends for time=0min only
                                assert time_index==0
                                for this_ligand in self.valid_ligands:
                                    self.true_prediction[cell][phospho][this_ligand][0].append(float(datum))
                            else:
                                assert time_index!=0
                                self.true_prediction[cell][phospho][ligand][time_index].append(float(datum))

            # Finally, we need to get the average to take care of replicates
            for phospho in self.true_prediction[cell].keys():
                for ligand in self.true_prediction[cell][phospho].keys():
                    for i,time in enumerate(times):
                        vector = self.true_prediction[cell][phospho][ligand][i]

                        if len(vector)==0:
                            m = np.nan
                        else:
                            m = 2**(sum([np.log2(x) for x in vector])/float(len(vector)))
                        self.true_prediction[cell][phospho][ligand][i] = m

        # some sanity checks
        for key in self.valid_length.keys():
            assert self.valid_length_extended[key]-len(self.phosphos_to_exclude[key]) == len(self.true_prediction[key].keys())

    def get_rmse(self, cellLine, phospho):
        """

        .. warning:: x in converted into a log2 scale
        """

        RMSE = 0
        #T = 7.
        #S = 8.

        counter = 0
        for s in self.valid_ligands:
            true  = np.array(self.true_prediction[cellLine][phospho][s])
            user  = np.array(self.user_prediction[cellLine][phospho][s])
            # some values provided may be set to 0
            # so remove the infinite caused by log(0).
            #RMSE += nansum( [x for x in (log2(true)-log2(user))**2 if x!=inf]  )
            data = [x for x in (np.log2(true)-np.log2(user))**2 if x!=np.inf]
            N = len([x for x in data if np.isnan(x)==False])
            RMSE += np.nansum(data)
            counter += N
        # TODO: if nans are include, do we need to change T ?
        if counter != 0:
            RMSE /= float(counter)
            RMSE = np.sqrt(RMSE)
        else:
            RMSE = np.nan
        return RMSE

    def compute_all_rmse(self):
        self.rmse = {}
        for c in self.valid_cellLines:
            self.rmse[c] = {}
            for l in self.species[c]:

                if c == "MCF7" and l in [ 'c-Met_pY1235', "YB-1_PS102"]:
                    continue
                if c == "BT20" and l in ["4EBP1_pS65", '4EBP1_pT37_pT46', "c-Met_pY1235"]:
                    continue
                if c == "UACC812" and l in ["4EBP1_pT37_pT46", "4EBP1_pS65"]:
                    continue

                if l not in self.phosphos_to_exclude[c]:
                    rmse = self.get_rmse(c, l)
                    self.rmse[c][l] = rmse
                else:
                    if self.verbose:print("skip %s/%s" % (c,l))

    def get_training_data(self):
        self.training = {}
        filenames = [
                "MD-BT20_main_for_null.csv",
                "MD-BT549_main_for_null.csv",
                "MD-MCF7_main_for_null.csv",
                "MD-UACC812_main_for_null.csv"]

        for filename in filenames:
            dummy, cell = filename.split("-")
            cell, other = cell.split("_", 1)
            filename = self._path2data + os.sep + 'data' + os.sep +filename
            if self.verbose:print("Scanning %s" % filename)

            data_iter = csv.reader(open(filename, "r"), delimiter=",")

            # get the header
            header = data_iter.next()
            # There should be 56 lines exacly with the 8 stimuli times 7 times
            # for all phosphos
            if header[0] != "TR:%s:CellLine" % cell:
                self.error("Error in the header of %s (first row)" % filename )

            stimuli = [x.split(":")[1] for x in header[1:9]]
            if sorted(stimuli) != sorted(self.valid_ligands):
                self.error("Error in the header of %s (invalid stimuli ?)" % filename )

            N = 3
            if cell == "BT549":
                N = 2

            #inhibitors = []
            if header[8+N+1] != "DA:ALL":
                self.error("Expected a DA:ALL column in the header at column 11 or 12, which was not found")

            phosphos = [x.split(":")[1] for x in header[N+8+2:]]

            if len(phosphos) != self.valid_length[cell] and len(phosphos) != self.valid_length_extended[cell]:
                print("WARNING: length don't seem correct")

            #if "PKC-delta_pS664" in phosphos:
            #    index = phosphos.index("PKC-delta_pS664")
            #    phosphos[index] = "PKC-delta"

            self.training[cell] = {}
            for phospho in phosphos:
                self.training[cell][phospho] = []

            # TODO: check that phosphos agree with the true prediction ?
            for iter, row in enumerate(data_iter):
                # append all data for a given phosphos over all stims,
                # inhibitor+DMSO and times
                for ip, phospho in enumerate(phosphos):
                    datum = row[N+8+2+ip]
                    #print cell, phospho, this_stimulus, itime
                    if datum == "NA":
                        datum = np.nan
                    else:
                        datum = float(datum)

                    self.training[cell][phospho].append(datum)

    def get_null(self, N=100, tag="sc2a"):
        self.get_training_data()

        all_rmses = []
        for i in range(0, N):
            print(tag+" " + str(i))
            self.user_prediction = self.create_random_data()
            self.compute_all_rmse()
            all_rmses.append(copy.deepcopy(self.rmse))
        return all_rmses

    def create_random_data(self):

        """ Here, we don't want the true prediction that contains only what is
        requested (AZD8055) but the orignal training data with 2 or 3 inhibitors such as
        GSK and PD17 so that we can shuffle them.

        We want to select for a given cell line and phosphos a data set to fill
        at a given time. The datum is slected accross the 8 stimuli, inhibitors
        +DMSO, and time points.

        TAZ and FOX were asked to be excluded so this cause some trouble now but
        some user preidction still include them. Should add a if statement to
        ginore them. Does not matter to compute the null distribution
        """
        import random
        data = copy.deepcopy(self.user_prediction)
        self.compute_all_rmse()

        for c in self.rmse.keys():
            for p in self.rmse[c].keys():
                for s in data[c][p].keys():
                    # select 7 random values for 7 time points for each stimuli
                    data[c][p][s] = random.sample(self.training[c][p], 7)[:]
        return data

    def _get_mean_and_sigma_null_parameters(self):
        """Retrieve mean and sigma for 4 celllines and phosphos"""
        filename = 'sc2a_null_mu_sigma_new.dat'
        filename = os.sep.join(["data", filename])
        mu_sigma = pickle.loads(open(filename, "r").read())
        mu = {}
        sigma = {}
        for c in self.valid_cellLines:
            mu[c] = {}
            sigma[c] = {}
            for p in self.valid_phosphos[c]:
                mu[c][p] = mu_sigma[c][p]['mu']
                sigma[c][p] = mu_sigma[c][p]['sigma']
        return mu, sigma

    # not used
    def __get_mean_zscores(self):
        zscores = {}
        for i,k in enumerate(self.participants):
            zscore = self.get_zscores(self.rmse[i])
            mu = np.mean([zscore[k1][k2] for k1 in zscore.keys() for k2 in zscore[k1].keys()])
            zscores[k] = mu
        return zscores

    def get_mean_rmse(self):
        return np.nanmean([self.rmse[k1][k2] for k1 in self.rmse.keys()
            for k2 in self.rmse[k1].keys()])


class HPNScoringPredictionInsilico(HPNScoringPredictionBase):
    """

    dimension1 :inhibitor
    dimenssion2: phosp
    dimensson3 stimulus
    dimnesion4 : time


    """
    test_synapse_id =  "syn2009175"
    true_synapse_id = "syn2143242"

    def __init__(self, filename=None, verbose=False, version='official'):
        """SC2B sub challenge (prediction in silico)

        :param filename: file to score
        :param str version: default to 'official' (see note below). Set to
            anything else to use correct network

        .. note:: This code use the official gold standard used
            in https://www.synapse.org/#!Synapse:syn1720047/wiki/60532 . Note, 
            however, that a corrected version is provided and can be used
        """
        super(HPNScoringPredictionInsilico, self).__init__(filename)
        # WRONG NETWORK as used in the official LB
        if version == 'official':
            fname = os.sep.join([self._path2data, "goldstandard", "TruePredictionInsilico.zip"])
        else:
            # CORRECT NETWORK
            fname = os.sep.join([self._path2data, "goldstandard",  "TruePredictionInsilico2.zip"])
        self.true_desc_filename = fname

        #self.loadZIPFile(self.filename)
        self.valid_cellLines = [""]
        self.times = [0, 1,2,4,6,10,15,30,60,120]
        self.stimuli = ["loLIG1", "hiLIG1", "loLIG2", "hiLIG2",  "loLIG1_loLIG2", "loLIG1_hiLIG2", "hiLIG1_loLIG2", "hiLIG1_hiLIG2"]
        self.inhibitors = ["AB%s"%x for x in range(1,21)]
        self.phosphos = ["AB%s"%x for x in range(1,21)]

        if self.filename is not None:
            self.get_user_prediction()
        #except:
        #    print("could not read user prediction")

        self.get_true_prediction()

    def get_user_prediction(self):
        results = self.read_prediction_insilico(self.filename)
        self.user_prediction = copy.deepcopy(results)

    def get_true_prediction(self):
        #results = self.read_prediction_insilico(self.true_desc_filename)
        results = self.read_true_prediction_michael(self.true_desc_filename)
        self.true_prediction = copy.deepcopy(results)

    def read_true_prediction_michael(self, filename):
        # this is almost the same as in the read_prediction
        results = {}
        zipdata = zipfile.ZipFile(filename)
        for inhib in self.inhibitors: # AB19 is missing from Michael set.
            expected_ending = "-%s-Prediction-Insilico.csv" % inhib
            filename = [x for x in zipdata.namelist() if x.endswith(expected_ending)]
            if len(filename) != 1:
                self.error("Could not find file ending in %s" % expected_ending)
                break
            filename = filename[0]
            # initialise dictionary for the inhibitor
            results[inhib] = {}

            # read data
            data = zipdata.open(filename)

            # get header
            header = data.next()
            header = [x.strip() for x in header.split(",")]

            stimuli = [x.split(":")[1] for x in header if x.endswith("Stimuli")]
            phosphos = [x.split(":")[1] for x in header if x.startswith("DV:")]
            assert len(phosphos)==20

            assert len(stimuli) == 4
            assert stimuli == self.stimuli[0:4], "incorrect stimuli %s " % stimuli

            # create the key to hold all phosphos
            for i,phospho in enumerate(phosphos):
                results[inhib][phospho] = {}
                # create the key to hold all ligans
                for stimulus in self.stimuli:
                    results[inhib][phospho][stimulus] = [[] for i in range(10)]
                else:
                    pass

            # now scan the data
            for row in data:
                row = [x.strip() for x in row.split(",")]

                these_stimuli = row[1:5] #we have only 4 stimuli im Michael file.
                # However, several may be st to 1
                stim_index = [i for  i,stim in enumerate(these_stimuli) if stim == '1' ]

                assert len(stim_index)==1 or len(stim_index)==2
                if len(stim_index) == 1:
                    stim_index = stim_index[0]
                else:
                    # ["loLIG1", "hiLIG1", "loLIG2", "hiLIG2",  "loLIG1_loLIG2", "loLIG1_hiLIG2", "hiLIG1_loLIG2", "hiLIG1_hiLIG2"]
                    if sorted(stim_index) == [0,2]: #loLIG1_loLIG2
                        stim_index = 4
                    elif sorted(stim_index) == [0,3]: #loLIG1_hiLIG2
                        stim_index = 5
                    elif sorted(stim_index) == [1,2]: #hiLIG1_loLIG2
                        stim_index = 6
                    elif sorted(stim_index) == [1,3]: #hiLIG1_hiLIG2
                        stim_index = 7
                    else:
                        raise ValueError

                # get time and correspoding index in the list of valid times
                thistime = float(row[5])
                if thistime == 45:
                    # to skip. THere is an extra time to be ignored since we
                    # asked users not to provide the time 45
                    continue
                time_index = self.times.index(thistime)

                # append the data to the relevant phospho index
                for i, phospho in enumerate(phosphos):
                    # ignore the indices related to FOX, TAX, mTor
                    datum = row[i+1+4+1] # +cell line +1 time + 4 stimuli
                    if datum == "NA":
                        results[inhib][phospho][self.stimuli[stim_index]][time_index]= np.nan
                    else:
                        results[inhib][phospho][self.stimuli[stim_index]][time_index] = float(datum)

        return results

    def read_prediction_insilico(self, filename):
        """Reads true predcition from the 20 CSV files"""
        results = {}
        zipdata = zipfile.ZipFile(filename)

        for inhib in self.inhibitors:
            expected_ending = "-%s-Prediction-Insilico.csv" % inhib
            filename = [x for x in zipdata.namelist() if x.endswith(expected_ending) and "MACOS" not in x]

            if len(filename) != 1:
                self.error("Could not find file ending in %s" % expected_ending)
                break
            filename = filename[0]

            # initialise dictionary for the inhibitor
            results[inhib] = {}

            # read data
            data = zipdata.open(filename, "rU") # universal mode for MAC

            # get header
            header = data.next()
            header = [x.strip() for x in header.split(",")]

            stimuli = [x.split(":")[1] for x in header if x.endswith("Stimuli")]
            stimuli = [x.replace("+", "_") for x in stimuli]  # some users put "+" instead of "_" ...
            phosphos = [x.split(":")[1] for x in header if x.startswith("DV:")]
            if len(phosphos)!=20:
                self.error("Number of expected phosphos (20 )is incorrect (Found %s in %s)  " %(len(phosphos), filename))
                continue

            if len(stimuli) != 8:
                self.error("Number of expected stimuli (8) is incorrect (Found %s in %s)  " %(len(stimuli), filename))
                continue
            for s in stimuli:
                if s not in self.stimuli:
                    self.error("found incorrect stimuli (%s) in %s" % (s, filename))
                    continue

            # create the key to hold all phosphos
            for i,phospho in enumerate(phosphos):
                results[inhib][phospho] = {}
                # create the key to hold all ligans
                for stimulus in self.stimuli:
                    results[inhib][phospho][stimulus] = [[] for i in range(10)]
                else:
                    pass

            # now scan the data
            for i, row in enumerate(data):
                row = [x.strip() for x in row.split(",")]

                these_stimuli = [int(float(x)) for x in row[1:9]]
                stim_index = [i for  i,stim in enumerate(these_stimuli) if stim == 1 ]
                #assert len(stim_index)==0, "no stimuli found on line %s in %s" % (i, filename)
                assert len(stim_index)==1, "more than 1 stimuli on line %s in %s" % (i, filename)
                stim_index = stim_index[0]

                # get time and correspoding index in the list of valid times
                thistime = float(row[9])
                time_index = self.times.index(thistime)

                # append the data to the relevant phospho index
                for i, phospho in enumerate(phosphos):
                    # ignore the indices related to FOX, TAX, mTor
                    datum = row[i+1+8+1] # +cell line +1 time + 8 stimuli
                    if datum == "NA" or datum =='?':
                        results[inhib][phospho][stimuli[stim_index]][time_index]= np.nan
                    else:
                        results[inhib][phospho][stimuli[stim_index]][time_index] = float(datum)

        return results

    def get_rmse(self, inhibitor, phospho):
        """

        .. warning:: x in converted into a log2 scale
        """
        RMSE = 0
        #T = 7.
        #S = 8.

        counter = 0
        for s in self.stimuli:
            true  = np.array(self.true_prediction[inhibitor][phospho][s])
            user  = np.array(self.user_prediction[inhibitor][phospho][s])
            data = [x for x in (np.log2(true)-np.log2(user))**2 if x!=np.inf]
            N = len([x for x in data if np.isnan(x)==False])
            RMSE += np.nansum(data)
            counter += N

        # TODO: if nans are include, do we need to change T ?
        if counter != 0:
            RMSE /= float(counter)
            RMSE = np.sqrt(RMSE)
        else:
            RMSE = np.nan

        return RMSE

    def compute_all_rmse(self):
        self.rmse = {}
        for c in self.inhibitors:
            if c == "AB9":
                continue
            self.rmse[c] = {}
            for l in self.phosphos:
                if l==c:
                    continue
                if l in ["AB3", "AB13", "AB18"] or c in ["AB3", "AB13", "AB18"]:
                    continue

                # those nodes have been ignored in the official leaderboards
                # based on the participants submissions.
                # To get the same results for a new participants, those nodes
                # should be keep the same. Although, we a entirely new set of
                # participants, those should be updated. 
                dummy_nodes = [(2,1), (6,1),(7,1), (6,4),(2,5), (6,5),(16,6),
                        (16,7), (6,8),
                        (16,8),(6,9),(7,9),(16,9),(20,9), (6,10),(6,12),(2,14),(6,14),
                        (7,14), (2,15), (16,15), (5,16), (5,17), (5,19), (16,19)]
                stop = False
                for node in dummy_nodes:
                    n1 = "AB"+str(node[0])
                    n2 = "AB"+str(node[1])
                    if c==n1 and l==n2:
                        stop = True
                if stop:
                    continue
                if l!=c:
                    rmse = self.get_rmse(c, l)
                    self.rmse[c][l] = rmse

    def get_training_data(self):
        self.training = {}
        filenames = [os.sep.join([self._path2data, "data", "MD_insilico.csv"])]

        for filename in filenames:
            if self.verbose:
                print("Scanning %s" % filename)

            data_iter = csv.reader(open(filename, "r"), delimiter=",")

            # get the header
            header = data_iter.next()
            # There should be 56 lines exacly with the 8 stimuli times 7 times
            # for all phosphos
            if header[0] != "TR:inSilico:CellLine":
                self.error("Error in the header of %s (first row)" % filename )

            stimuli = [x.split(":")[1] for x in header[1:8]]
            #inhibitors = []
            if header[8] != "DA:ALL":
                self.error("Expected a DA:ALL column in the header at column 9, which was not found")

            phosphos = [x.split(":")[1] for x in header[9:]]

            self.training = {}
            for phospho in phosphos:
                self.training[phospho] = []

            for iter, row in enumerate(data_iter):
                # append all data for a given phosphos over all stims,
                # inhibitor+DMSO and times
                for ip, phospho in enumerate(phosphos):
                    datum = row[7+2+ip]
                    #print cell, phospho, this_stimulus, itime
                    if datum == "NA":
                        datum = np.nan
                    else:
                        datum = float(datum)
                    self.training[phospho].append(datum)

    def get_null(self, N=100, tag="sc2b"):
        self.get_training_data()

        all_rmses = []
        for i in range(0, N):
            print(tag+" " + str(i))
            self.user_prediction = self.create_random_data()
            self.compute_all_rmse()
            all_rmses.append(copy.deepcopy(self.rmse))
        return all_rmses

    def create_random_data(self):

        """ Here, we don't want the true prediction that contains only what is
        requested (AZD8055) but the orignal training data with 2 or 3 inhibitors such as
        GSK and PD17 so that we can shuffle them.

        We want to select for a given cell line and phosphos a data set to fill
        at a given time. The datum is slected accross the 8 stimuli, inhibitors
        +DMSO, and time points.
        """
        import random
        data = copy.deepcopy(self.true_prediction)

        for c in self.training.keys():
            for p in self.training.keys():
                for s in data[c][p].keys():
                    # select randomly for 10 time points for each inhibitor (8)
                    # (no 45 minute point).
                    data[c][p][s] = random.sample(self.training[c], 10)[:]
        return data

    def _get_mean_and_sigma_null_parameters(self):
        """Retrieve mean and sigma for 32 combi from a null AUC distribution"""
        filename = 'sc2b_null_mu_sigma.dat'
        filename = os.sep.join([self._path2data, "data", filename])
        # a dict contain dict (phospho) of dict (phospho) of dict (mu,sigma)
        mu_sigma = pickle.load(open(filename, "r"))
        mu = {}
        sigma = {}
        for c in self.phosphos:
            mu[c] = {}
            sigma[c] = {}
            for p in self.phosphos:
                if p == c:
                    mu[c][p] = np.nan
                    sigma[c][p] = np.nan
                else:
                    mu[c][p] = mu_sigma[c][p]['mu']
                    sigma[c][p] = mu_sigma[c][p]['sigma']
        return mu, sigma

    def get_mean_zscores(self):
        zscore = self.get_zscores(self.rmse)
        data = [zscore[k1][k2] for k1 in zscore.keys() for k2 in zscore[k1].keys()]
        mu = np.mean([x for x in data if np.isnan(x)==False])
        return mu

    def get_zscores(self, rmses=None):
        mu, sigma = self._get_mean_and_sigma_null_parameters()
        zscores = {}
        for c in self.inhibitors:
            zscores[c] = {}
            for p in self.phosphos:
                if c!=p:
                    if rmses!=None:
                        zscores[c][p] = (rmses[c][p] - mu[c][p])/sigma[c][p]
                    else:
                        zscores[c][p] = (self.rmse[c][p] - mu[c][p])/sigma[c][p]
                else:
                    zscores[c][p] = np.nan
        return zscores

    def get_mean_rmse(self):
        d = self.rmse
        return np.mean([d[k1][k2] for k1 in d.keys() for k2 in d[k1].keys() if
            np.isnan(d[k1][k2])==False])


class HPNScoringPrediction_ranking(HPNScoring):
    """This class is used to compute the ranks of the different participants
    based on an average rank over the 4 cell lines times phosphos

    ::

        s = HPNScoringPrediction(filename="file1zip")
        s.compute_all_rmes()

        r = HPNScoringPrediction_ranking()
        # s.aucs is a list where each element is a dictionary of
        r.add_rme(s1.rmse, "team1")

        rmse1 = r.get_randomised_rmse(r.rmse[0], sigma=1)
        rmse2 = r.get_randomised_rmse(r.rmse[0], sigma=2)
        rmse3 = r.get_randomised_rmse(r.rmse[0], sigma=3)

        r.add_rmse(rmse1, "team2")
        r.add_rmse(rmse2, "team3")
        r.add_rmse(rmse3, "team4")

        sall.add_rmse(s2.rmse, "team2")
        sall.get_ranking()
        {'team1': 1.96875, 'team2': 1.03125}


    This class is independent of HPNSCoringPrediction.
    However, it takes as input the returned values of
    HPNScoringPrediction.compute_all_rmse()

    """
    def __init__(self):
        super(HPNScoringPrediction_ranking, self).__init__()
        self.valid_cellLines = ['UACC812', 'MCF7', 'BT549', 'BT20']
        self.rmse = []
        self.participants = []

    def _get_empty_rmse(self):
        data = {}
        for c in self.valid_cellLines:
            data[c] = {}
            for s in self.species[c]:
                data[c][s] = np.inf
        return data

    def add_rmse(self, data, participant_id):
        if participant_id in self.participants:
            raise ValueError("participant already added")
        if data == None:
            data = self._get_empty_rmse()
        self.rmse.append(copy.deepcopy(data))
        self.participants.append(participant_id)
        self._compute_ranks()

    def _get_species(self):
        if len(self.rmse)>=1:
            species = {}
            for c in self.valid_cellLines:
                species[c] = self.rmse[0][c].keys()
            return species
        else:
            print("you must provide a rmse dict at least to get the species")
    species = property(_get_species)

    def _rank_index(self, vector):
        sorted_vector = sorted(vector)
        return [sorted_vector.index(x) for x in vector]

    def _compute_ranks(self):
        ranks = {}
        for c in self.valid_cellLines:
            ranks[c] = {}
            for l in self.species[c]:
                # get this RMSE for all participant
                data = [x[c][l] for x in self.rmse]
                # but use a reverse order hence 1-x for the sorting
                indices = np.argsort([x for x in data])
                ranks[c][l] = [list(indices).index(i)+1 for i in range(0,len(indices))]
        self.ranks = copy.deepcopy(ranks)

    def get_ranking(self):
        ranking = {}
        for k in self.participants:
            ranks = self.get_rank_participant(k)
            mu = np.mean([ranks[k1][k2] for k1 in ranks.keys() for k2 in ranks[k1].keys()])
            ranking[k] = mu
        return ranking

    def get_mean_ranks(self):
        return self.get_ranking()

    def get_integer_ranks(self):
        ranking = self.get_ranking()
        integer_ranks = {}

        # get teams and ranks
        teams_ranks = list(ranking.iteritems())
        teams = [x[0] for x in teams_ranks]
        mean_ranks = [x[1] for x in teams_ranks]

        for i, index in enumerate(np.argsort(mean_ranks)):
            integer_ranks[teams[int(index)]] = i+1
        return integer_ranks

    def get_rank_participant(self, participant):
        ranks = {}
        if participant in self.participants:
            index = self.participants.index(participant)
            for c in self.valid_cellLines:
                ranks[c] = {}
                for l in self.species[c]:
                    ranks[c][l] = self.ranks[c][l][index]
            return ranks
        else:
            raise ValueError("unknown participant")

    def get_randomised_rmse(self, rmse, sigma=1):
        """THis is useful for testing. See class documentaton"""
        new_rmse = copy.deepcopy(rmse)
        for c in self.valid_cellLines:
            for l in self.species[c]:
                x = new_rmse[c][l]
                new_rmse[c][l] = np.uniform(-1 * x, x*2) + x # new values is between 0 and sigma*x
                #new_rmse[c][l] = x +  sigma + x # new values is between 0 and sigma*x
        return new_rmse

    # Duplicated from HPNScoringPrediction
    def _get_mean_and_sigma_null_parameters(self):
        """Retrieve mean and sigma for 4 celllines and phosphos"""
        filename = 'sc2a_null_mu_sigma_new.dat'
        filename = os.sep.join([self._path2data, "data", filename])
        mu_sigma = pickle.loads(open(filename, "r").read())
        mu = {}
        sigma = {}
        for c in self.valid_cellLines:
            mu[c] = {}
            sigma[c] = {}
            for p in self.valid_phosphos[c]:
                mu[c][p] = mu_sigma[c][p]['mu']
                sigma[c][p] = mu_sigma[c][p]['sigma']
        return mu, sigma

    # Duplicated from HPNScoringPrediction
    def get_mean_zscores(self):
        zscores = {}
        for i,k in enumerate(self.participants):
            zscore = self._get_zscores(self.rmse[i])
            #print zscore
            data = [zscore[k1][k2] for k1 in zscore.keys() for k2 in zscore[k1].keys()]
            data = [x for x in data if np.isnan(x)==False]
            mu = np.mean(data)
            zscores[k] = mu
        return zscores

    # Duplicated from HPNScoringPrediction
    def _get_zscores(self, rmses=None):
        mu, sigma = self._get_mean_and_sigma_null_parameters()
        zscores = {}
        for c in self.valid_cellLines:
            zscores[c] = {}
            for p in self.valid_phosphos[c]:
                if rmses!=None:
                    zscores[c][p] = (rmses[c][p] - mu[c][p])/sigma[c][p]
                else:
                    zscores[c][p] = (self.rmse[c][p] - mu[c][p])/sigma[c][p]
        return zscores

    def _get_valid_phosphos(self):
        rmse = None
        for x in self.rmse:
            if x != None:
                rmse = x
                break
        if rmse == None:
            raise ValueError("No RMSE found. please add one (not None) using add_rmse")
        valid_phosphos = {}
        for c in rmse.keys():
            valid_phosphos[c] = rmse[c].keys()
        return valid_phosphos
    valid_phosphos = property(_get_valid_phosphos)


class HPNScoringPredictionInsilico_ranking(HPNScoring):
    """This class is used to compute the ranks of the different participants
    based on an average rank over the 4 cell lines times phosphos

    ::

        s = HPNScoringPredictionInsilico(filename="file1zip")
        s.compute_all_rmes()

        r = HPNScoringPrediction_ranking()
        # s.aucs is a list where each element is a dictionary of
        r.add_rme(s1.rmse, "team1")

        rmse1 = r.get_randomised_rmse(r.rmse[0], sigma=1)
        rmse2 = r.get_randomised_rmse(r.rmse[0], sigma=2)
        rmse3 = r.get_randomised_rmse(r.rmse[0], sigma=3)

        r.add_rmse(rmse1, "team2")
        r.add_rmse(rmse2, "team3")
        r.add_rmse(rmse3, "team4")

        sall.add_rmse(s2.rmse, "team2")
        sall.get_ranking()
        {'team1': 1.96875, 'team2': 1.03125}


    This class is independent of HPNSCoringPrediction.
    However, it takes as input the returned values of
    HPNScoringPrediction.compute_all_rmse()

    """
    def __init__(self):
        super(HPNScoringPredictionInsilico_ranking, self).__init__()
        self.times = [0, 1,2,4,6,10,15,30,60,120]
        self.inhibitors = ["AB%s"%x for x in range(1,21)]
        self.phosphos = ["AB%s"%x for x in range(1,21)]

        self.ignore = ['AB3', 'AB13', 'AB18']
        for this in self.ignore:
            self.inhibitors.remove(this)
            self.phosphos.remove(this)
        self.inhibitors.remove("AB9")

        self.rmse = []
        self.participants = []

    def _get_empty_rmse(self):
        data = {}
        for c in self.inhibitors:
            data[c] = {}
            for s in self.phosphos:
                data[c][s] = np.inf
        return data

    def add_rmse(self, data, participant_id):
        if participant_id in self.participants:
            raise ValueError("participant already added")
        if data == None:
            data = self._get_empty_rmse()
        self.rmse.append(copy.deepcopy(data))
        self.participants.append(participant_id)
        self._compute_ranks()

    def _rank_index(self, vector):
        sorted_vector = sorted(vector)
        return [sorted_vector.index(x) for x in vector]

    def _compute_ranks(self):
        ranks = {}
        for c in self.inhibitors:
            ranks[c] = {}
            phosphos = self.rmse[0][c].keys()
            for l in phosphos:
                if l!=c:
                    # get this RMSE for all participant

                    data = [x[c][l] for x in self.rmse]

                    # but use a reverse order hence 1-x for the sorting
                    indices = np.argsort([x for x in data])
                    ranks[c][l] = [list(indices).index(i)+1 for i in range(0,len(indices))]


        self.ranks = copy.deepcopy(ranks)

    def get_ranking(self):
        ranking = {}
        for k in self.participants:
            ranks = self.get_rank_participant(k)
            mu = np.mean([ranks[k1][k2] for k1 in ranks.keys() for k2 in ranks[k1].keys()])
            ranking[k] = mu
        return ranking

    def get_mean_ranks(self):
        return self.get_ranking()

    def get_integer_ranks(self):
        ranking = self.get_ranking()
        integer_ranks = {}

        # get teams and ranks
        teams_ranks = list(ranking.iteritems())
        teams = [x[0] for x in teams_ranks]
        mean_ranks = [x[1] for x in teams_ranks]

        for i, index in enumerate(np.argsort(mean_ranks)):
            integer_ranks[teams[int(index)]] = i+1
        return integer_ranks

    def get_rank_participant(self, participant):
        ranks = {}
        if participant in self.participants:
            index = self.participants.index(participant)
            for c in self.inhibitors:
                ranks[c] = {}
                phosphos = self.rmse[0][c].keys()
                for l in phosphos:
                    if c!=l:
                        ranks[c][l] = self.ranks[c][l][index]
            return ranks
        else:
            raise ValueError("unknown participant")

    def get_randomised_rmse(self, rmse, sigma=1):
        """THis is useful for testing. See class documentaton"""
        new_rmse = copy.deepcopy(rmse)
        for c in self.inhibitors:
            phosphos = self.rmse[0][c].keys()
            for l in phosphos:
                if c!=l:
                    x = new_rmse[c][l]
                    new_rmse[c][l] = np.uniform(-1 * x, x*sigma) + x # new values is between 0 and sigma*x
                    #new_rmse[c][l] = x +  sigma + x # new values is between 0 and sigma*x
        return new_rmse

    def get_mean_zscores(self):
        zscores = {}
        for i,k in enumerate(self.participants):
            zscore = self._get_zscores(self.rmse[i])
            #print zscore
            data = [zscore[k1][k2] for k1 in zscore.keys() for k2 in zscore[k1].keys()]
            data = [x for x in data if np.isnan(x)==False]
            mu = np.mean(data)
            zscores[k] = mu
        return zscores

    def _get_mean_and_sigma_null_parameters(self):
        """Retrieve mean and sigma for 32 combi from a null AUC distribution"""
        filename = 'sc2b_null_mu_sigma.dat'
        filename = os.sep.join([self._path2data, "data", filename])
        # a dict contain dict (phospho) of dict (phospho) of dict (mu,sigma)
        mu_sigma = pickle.load(open(filename, "r"))
        mu = {}
        sigma = {}
        for c in self.inhibitors:
            mu[c] = {}
            sigma[c] = {}
            phosphos = self.rmse[0][c].keys()
            for p in phosphos:
                if p == c:
                    mu[c][p] = np.nan
                    sigma[c][p] = np.nan
                else:
                    mu[c][p] = mu_sigma[c][p]['mu']
                    sigma[c][p] = mu_sigma[c][p]['sigma']
        return mu, sigma

    def _get_zscores(self, rmses=None):
        mu, sigma = self._get_mean_and_sigma_null_parameters()
        zscores = {}
        for c in self.inhibitors:
            zscores[c] = {}
            phosphos = self.rmse[0][c].keys()
            for p in phosphos:
                if c!=p:
                    if rmses!=None:
                        zscores[c][p] = (rmses[c][p] - mu[c][p])/sigma[c][p]
                    else:
                        zscores[c][p] = (self.rmse[c][p] - mu[c][p])/sigma[c][p]
                else:
                    zscores[c][p] = np.nan
        return zscores


def sc2a_null(N=100, tag=""):
    s = HPNScoringPrediction()
    res = s.get_null(N, tag=tag)
    return res


def sc2b_null(N=100):
    s = HPNScoringPredictionInsilico()
    res = s.get_null(N)
    return res



