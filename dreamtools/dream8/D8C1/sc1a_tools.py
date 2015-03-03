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
import pickle
import glob
import os

import pylab

import numpy as np
from scipy.stats import kstest

#from scoring import HPNScoringNetwork
import easydev

__all__ = ["AUCnull"]

class AUCnull(object):
    """Loads all AUCS generated from a ramdom distribution.

    .. warning:: USED by the scoring function.


        >>> import sc1a_tools
        >>> import scoring
        >>> s = scoring.HPNScoringNetwork()
        >>> null = sc1a_tools.AUCnull(s.valid_cellLines, s.valid_ligands, verbose=False)
        >>> #filename = 'sc1a_null_aucs_mean_sigma.dat'
        >>> #filename = easydev.get_share_file("dreamtools", "data/dream8hpn", filename)
        >>> null.loadaucs(filename=None)
        >>> mean = null.get_mean_dict()
        >>> sigma = null.get_sigma_dict()


    """
    def __init__(self, valid_cellLines, valid_ligands, verbose=True):
        self.ligands = valid_ligands[:]
        self.cellLines = valid_cellLines[:]
        self.verbose = verbose

    def loadaucs(self, pickleName=None):
        if pickleName == None:
            pickleName = 'sc1a_null_aucs_mean_sigma.dat'
            pickleName = easydev.get_share_file("dreamtools", "data/dream8hpn",
                    pickleName)
        self.aucs = pickle.load(open(pickleName, "r"))

    def saveaucs(self, pickleName="sc1a_null_aucs.dat"):
        pickle.dump(self.aucs, open(pickleName, "w"))

    def loaddata(self, directory=None, tag="AUC"):
        """Loads bunch of AUCS stored in files

        files should be tagged as tag_cellline_ligand.* and contain a single
        column with all AUCs. This is convenientn if you ran many simulation
        that stores AUC in different files

        """
        self.data = {}
        for c in self.cellLines:
            self.data[c] = {}
            for l in self.ligands:
                self.data[c][l] = []

        for l in self.ligands:
            for c in self.cellLines:
                if self.verbose:print("Combining all data related to %s/%s" % (c,l))
                if directory:
                    filenames = glob.glob(directory +os.sep+"%s_%s_%s*" % (tag, c,l))
                else:
                    filenames = glob.glob("%s_%s_%s*" % (tag, c,l))

                if self.verbose: print("  found %s files\n  reading " % len(filenames))

                for filename in filenames:
                    fh = open(filename, "r")
                    data = fh.read().strip().split()
                    data = [float(x) for x in data]

                    try:
                        self.data[c][l].extend(data)
                    except:
                        self.data[c][l] = data
        self._compute_params()

    def _compute_params(self):
        self.aucs = {}
        for c in self.cellLines:
            self.aucs[c] = {}
            for l in self.ligands:
                self.aucs[c][l] = {"mean":np.mean(self.data[c][l]),
                                    "sigma":np.std(self.data[c][l])}
    def get_mean(self):
        """returns all mean AUCS in a matrix structure"""
        mean = np.array(np.zeros((4,8)))
        for i,c in enumerate(self.cellLines):
            for j,l in enumerate(self.ligands):
                mean[i][j] = self.aucs[c][l]['mean']
        return mean

    def get_sigma(self):
        """returns all std AUCS in a matrix structure"""
        sigma = np.array(np.zeros((4,8)))
        for i,c in enumerate(self.cellLines):
            for j,l in enumerate(self.ligands):
                sigma[i][j] = self.aucs[c][l]['sigma']
        return sigma

    def get_mean_dict(self):
        """returns all mean AUCS in a dictionary structure"""
        mean = {}
        for c in self.cellLines:
            mean[c] = {}
            for l in self.ligands:
                mean[c][l] = self.aucs[c][l]['mean']
        return mean

    def get_sigma_dict(self):
        """returns all std AUCS in a dictionary structure"""
        sigma = {}
        for c in self.cellLines:
            sigma[c] = {}
            for l in self.ligands:
                sigma[c][l] = self.aucs[c][l]['sigma']
        return sigma

    def get_ks(self):
        D = np.array(np.zeros((4,8)))
        pvalue = np.array(np.zeros((4,8)))
        for i,c in enumerate(self.cellLines):
            for j,l in enumerate(self.ligands):
                data = self.data[c][l]
                ks = kstest(data, 'norm', args=([np.mean(data), np.std(data)]))
                D[i][j] = ks[0]
                pvalue[i][j] = ks[1]
        return D, pvalue

    def pcolor(self, mode="mean", vmin=None, vmax=None):
        """

        If you loaded the pickle data sets with only mean and sigma, the D and
        pvalue mode cannot be used.

        """
        from pylab import clf, xticks, yticks, pcolor, colorbar, flipud, log10
        if mode == "mean":
            data = self.get_mean()
        elif mode == "sigma":
            data = self.get_sigma()
        elif mode == "D":
            data = self.get_ks()[0]
        elif mode == "pvalue":
            data = self.get_ks()[1]
        clf();

        if mode == "pvalue":
            pcolor(log10(flipud(data)), vmin=vmin, vmax=vmax);
        else:
            pcolor(flipud(data), vmin=vmin,vmax=vmax);

        colorbar()
        xticks([x+0.5 for x in range(0,8)], self.ligands, rotation=90)
        cellLines = self.cellLines[:]
        cellLines.reverse()
        yticks([x+0.5 for x in range(0,4)], cellLines, rotation=0)

    def plot_auc_histograms(self, directory):
        #from scoring import HPNScoringNetwork
        #s = HPNScoringNetwork()

        self.loaddata(directory=directory, tag="AUC")

        pylab.figure(1)
        pylab.clf()
        for i,c in enumerate(self.cellLines):
            for j,l in enumerate(self.ligands):
                pylab.subplot(4,8,i*8+j+1)
                pylab.hist([x for x in self.data[c][l] if np.isnan(x)==False], 50, normed=True)
                pylab.title("%s/%s" % (c,l))
                pylab.xlim([0.,1])
                pylab.grid(True)

    def plot_aupr_histograms(self, directory):
        #from scoring import HPNScoringNetwork
        #s = HPNScoringNetwork()
        self.loaddata(directory=directory, tag="AUPR")
        pylab.figure(1)
        pylab.clf()
        for i,c in enumerate(self.cellLines):
            for j,l in enumerate(self.ligands):
                pylab.subplot(4,8,i*8+j+1)
                pylab.hist([x for x in self.data[c][l] if np.isnan(x)==False], 50, normed=True)
                pylab.title("%s/%s" % (c,l))
                pylab.xlim([0.,1])
                pylab.grid(True)