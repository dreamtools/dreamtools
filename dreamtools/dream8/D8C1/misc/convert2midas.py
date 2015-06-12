# -*- python -*-
#
#  This file is part of XXX software
#
#  Copyright (c) 2011-2012 - EBI-EMBL
#
#  File author(s): Thomas Cokelaer <cokelaer@ebi.ac.uk>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  website: http://www.ebi.ac.uk/~cokelaer/XXX
#
##############################################################################
"""This file reads a RPPA CSV file and converts it into a MIDAS file.

This has been tested on RPPA dream8 challenge data set. 

Can be extended to incorporate/merge the convert.py file used in the colon
analyais.


"""

import csv



__all__ = ["RPPAReaderDream"]


class RPPAReader(object):
    """a bsse class for the RPPA data set"""
    def __init__(self, filename):
        self.filename = filename
        self.rows = []

    def reset(self):
        self.rows = []

    def read(self, skipnrows=0, skiplastrows=0):
        """read the rows in a CSV file and stores them

        :param int skipnrows:
        :param int skiplastrows:

        """
        self.reset()
        with open(self.filename, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',') # , quotechar='|')
            for i, row in enumerate(spamreader):
                if i>=skipnrows:
                    # data = ', '.join(row)
                    data = []
                    for x in row:
                        try:
                            x = float(x)
                        except:
                            pass
                        data.append(x)
                    self.rows.append(data)
                else:
                    print("ignoring line %s" % i)

    def rppa2midas(self):
        """should return a string containing the MIDAS file"""
        raise NotImplementedError

    def save2midas(self, filename=None):
        if filename == None:
            import os
            tag = os.path.splitext(os.path.split(self.filename)[1])[0]
            filename = "MD-%s.csv" % tag
        txt = self.rppa2midas()
        hf = open(filename, "w")
        hf.write(txt)
        hf.close()


class RPPAReaderColonData(RPPAReader):
    def __init__(self):
        raise NotImplementedError


class RPPAReaderDream(RPPAReader):
    """a class dedicated to the RPPA data set used in DREAM8 challenge


    r = rppa.RPPAReaderDream(filename="example.csv")
    r.read()
    r.save2midas("test.csv")

    """
    def __init__(self, filename, solvents=["DMSO"], skipnrows=0, skiplastcols=0):
        super(RPPAReaderDream, self).__init__(filename)
        self.qc_test_scores = None
        self.cf_scores = None
        self.solvents = solvents[:]

        self.skipnrows = skipnrows
        self.skiplastcols = skiplastcols
        #self.left_header = ["Cell Line", "Inhibitor", "Stimulus", "Timepoint"]
        if "main" in filename:
            self.mode = "main"
        elif "full" in filename:
            self.mode = "full"
        else:
            raise NotImplementedError("RPPA data for DREAM8 are tagged with main or full word.")
        self.filename = filename
        self.read()

    def read(self, mode="main"):
        # reads the data
        super(RPPAReaderDream, self).read()

        # This is hardcoded. Be aware  that indices should take care of the fact
        # that we are removing rows. From the first 4 rows, we keep only the
        # second one.



        if self.mode == "main":
            # removes names SLIDE_ID
            del self.rows[0]
            if "UACC" in self.filename: # delete extra SLIDE_ID row
                del self.rows[0]
                
            # keep Antibody names
            
            # delete HUGO ID
            del self.rows[1]
            # remove the header (Cell Line, inhibitor,stimulus,timepoint
            #del self.rows[1]
            self.left_header = self.rows[1][0:10]

        elif self.mode == "full":
            # remove slide 
            del self.rows[1] # now index 0 == qc sacore and 1 == antobody names
            if "UACC" in self.filename: # delete extra SLIDE_ID row
                del self.rows[1]
            del self.rows[2] # removes HUGO
            del self.rows[2] # removes phosph


            # save qc score and remove it
            self.qc_test_scores = self.rows[0][:]
            del self.rows[0]

            self.left_header = self.rows[1][0:10][:]

            # let us fet rid of the 5th column (cf scores) qnd 6th column (a
            # tag)
            self.cf_scores = [x[4] for x in self.rows]
            for i, row in enumerate(self.rows):
                del self.rows[i][4]
                del self.rows[i][4]
            

    """data must be

    , , ,,Antibody Name, A, B, C, ...
    CellLine, inhibitor, stimulus, timepoints
    BT20,GSK,'',0min

    """


    def _get_inhibitors(self):
        data = [x[1] for x in self.rows[1:]]
        assert data[0] == self.left_header[1]
        data = data[1:]
        data = sorted([x for x in set(data) if len(x) and x not in self.solvents])
        return data
    inhibitors = property(_get_inhibitors)

    def _get_timepoints(self):
        data = [x[3] for x in self.rows[1:]]
        assert data[0] == self.left_header[3]
        data = data[1:]   # remove the header
        # converts everything in minutes. values contains units (e.g.10min, 2hr)
        data = [int(x[0:len(x)-3]) if x.endswith('min')==True else int(x[0:len(x)-2])*60 for x in data]
        data = sorted(list(set(data)))
        return data
    timepoints = property(_get_timepoints)

    def _get_stimuli(self):
        data = [x[2] for x in self.rows[1:]]
        assert data[0] == self.left_header[2]

        data = data[1:]
        data = sorted([x for x in set(data) if len(x)])
        return data
    stimuli = property(_get_stimuli)


    def _get_cellLine(self):
        data = [x[0] for x in self.rows[2:]]
        assert len(set(data)) == 1
        data = self.rows[2][0]
        return data
    cellLine = property(_get_cellLine)

    def _get_species(self):
        data = self.rows[0][4:]
        return data
    species = property(_get_species)

    def get_header(self):
        header = "TR:%s:CellLine" % self.cellLine
        for x in self.stimuli:
            header += ",TR:%s:Stimuli" % x

        for x in self.inhibitors:
            if x.endswith("i"):
                header += ",TR:%s:Inhibitors" % x.replace(" ", "_")
            else:
                header += ",TR:%s:Inhibitors" % x.replace(" ", "_")

        header += ",DA:ALL"

        for x in self.species:
            header += ",DV:%s" % x.replace(" ", "_")
        return header

    def _get_cues(self):
        cues = self.stimuli + self.inhibitors
        return cues
    cues = property(_get_cues)

    def get_data_at_given_time(self, time):
        # first get the times in minutes
        timepoints = [x[3] for x in self.rows[2:]]
        #del timepoints[0]
        timepoints = [int(x[0:len(x)-3]) if x.endswith('min')==True else int(x[0:len(x)-2])*60 for x in timepoints]

        # get indices of the rows that correspond to the time provided.
        # plus one because header is missing in timepoints list.
        indices = [i+2 for i,x in enumerate(timepoints) if x == time]
        data = []
        for i in indices:
            data.append(self.rows[i])
        return data

    def get_time(self, time):
        txt = ""
        data = self.get_data_at_given_time(time)
        cues = self.cues[:]
        Ncues = len(cues) 
        for row in data:
            this_cues = [0] * Ncues
            this_stim = row[2]
            this_inh = row[1]
            if this_stim != "":
                i1 = self.cues.index(this_stim)
                this_cues[i1] = 1
            if this_inh != "" and this_inh not in self.solvents:
                i2 = self.cues.index(this_inh)
                this_cues[i2] = 1
        
            txt += "1,"    # the cellline should be 1, not its name, which is in the header 
            txt += ",".join([str(x) for x in this_cues])
            txt += ",%s," % time                # the DA:ALL
            #for x in range(0, len(self.species)):
            txt += ",".join([str(x) for x in row[4:]])
            txt+="\n"
        return txt

    def rppa2midas(self):
        txt = self.get_header() + "\n"
        for i in self.timepoints:
            txt += self.get_time(i)
        return txt


def convert(self):
    """This is a dradt that may not work anymore"""
    filenames = ["BT20_full.csv","BT20_main.csv","BT549_full.csv","BT549_main.csv","MCF7_full.csv",
"MCF7_main.csv","UACC812_full.csv", "UACC812_main.csv"]

    for filename in filenames:
        print("Converting %s " % filename)
        import convert2midas
        r = convert2midas.RPPAReaderDream(filename)
        tag = filename.split("_")[0]
        if "_main" in filename:
            md_filename = "MD_%s_main.csv" % tag
        elif "_full" in filename:
            md_filename = "MD_%s_full.csv" % tag
        r.save2midas(md_filename)


