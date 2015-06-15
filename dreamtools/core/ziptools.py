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
import zipfile


class ZIP(object):
    """Simple utility to load a ZIP file"""

    def __init__(self):
        pass

    def loadZIPFile(self, filename):
        """Loads a ZIP file

        This method uses the zipfile module and stores the data into 
        :attr:`zip_data`. The filenames contained within this archive
        can be found in :attr:`zip_filenames`. To read the data contained 
        in the first filename, type:: 

            self.zip_data.open(self.filenames[0].read()

        :param str filename: the ZIP filename to load

        """
        # USED in D8C1 and D5C2 do not change
        if zipfile.is_zipfile(filename) == False:
            raise ValueError("Input file (%s) is not a valid ZIP file. " % filename)
        else:
            self.zip_data = zipfile.ZipFile(filename)
            self.zip_filenames = self.zip_data.namelist()
            self.filenames = self.zip_filenames # keep zip_filenames for back compat


    def read(self, filename):
        return self.zip_data.read(filename)
