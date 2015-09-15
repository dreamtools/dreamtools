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
# TODO: move everything inside the class
import os
import tarfile

from dreamtools import Challenge
import dreamtools


def get_challenge_list():
    """Returns list of challenge names"""
    registered = sorted([x for x in dir(dreamtools) if x.startswith('D')
        and 'C' in x])
    return registered


def _generic_download(name, mode):
    c = Challenge(name)
    class_inst = c.import_scoring_class()
    if mode == 'template':
        if len(class_inst.sub_challenges) == 0:
            class_inst.download_template()
        else:
            for subname in class_inst.sub_challenges:
                class_inst.download_template(subname)
    elif mode == 'gs':
        if len(class_inst.sub_challenges) == 0:
            class_inst.download_goldstandard()
        else:
            for subname in class_inst.sub_challenges:
                class_inst.download_goldstandard(subname)


def download_gs(name):
    """Download GS file(s) for a given challenge

    :param name: a valid nickname e.g. D2C1"""
    _generic_download(name, 'gs')


def download_template(name):
    """Download template file(s) for a given challenge

    :param name: a valid nickname e.g. D2C1"""
    _generic_download(name, 'template')

class DREAMToolsBundle(object):
    def __init__(self, verbose=True):
        self.verbose = True
        self.download_all()

    def download_all(self):
        """This function downloads all templates and GS stored in Synapse

        This could be used to create a ZIP file will all downlable files and
        use to provide a bundle of those files for those who do not wish to
        have a Synapse access.

        This could be useful for testing as well.

        """
        names = get_challenge_list()
        for name in names:
            print("Downloading template for %s" % name)
            try:
                download_gs(name)
            except NotImplementedError:
                pass
            except Exception as err:
                raise(err)

            print("Downloading GS for %s" % name)
            try:
                download_template(name)
            except NotImplementedError:
                pass
            except Exception as err:
                raise(err)

    def create_bundle(self, output_filename, source_dir=None):
        if source_dir is None:
            from dreamtools import dreampath
            source_dir = dreampath
        with tarfile.open(output_filename, "w:gz") as tar:
            if self.verbose:
                tar.add(source_dir, arcname=os.path.basename(source_dir))
