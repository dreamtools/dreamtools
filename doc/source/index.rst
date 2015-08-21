


############################################################################
DREAMTools
############################################################################

.. contents::

Overview
---------

**DREAMTools** aims at sharing code used in the scoring of `DREAM <http://dreamchallenges.org>`_ challenges.

The main goals are to provide:

#. scoring functions for the Dream challenges for **end-users** via the **dreamtools** standalone application.
#. a place for **developers** involved in the dream challenges to share code


Code related to aggregation, leaderboards, or more complex analysis are not
guaranteed to be found in DREAMTools even though it may be in some challenges
(e.g. D8C1). Some functionalities may be restricted with some access to synapse.
Some challenges will require to download public data sets from
`Synapse <www.synapse.org>`_ (in which case you will need to register).

The **dreamtools** executable
-------------------------------

For users, **DREAMTools** package provides one executable called **dreamtools**, which should be installed automatically during the installation. Knowing the name of the challenge (and possibly sub-challenge), it works as follows::

    dreamtools --challenge d8c1 --sub-challenge sc1a --submission example.zip

It prints some information and the score of the submision for instance for the example above::

     Solution for alphabeta-Network.zip in challenge d8c1 (sub-challenge sc1a) is :
     AUROC: 0.781937275711

Available challenges
-------------------------

The primary goal of **DREAMTools** is to provide scoring functions used in all DREAM challenges. Currently,
**DREAMTools** includes about 80% of DREAM challenges from DREAM2 to DREAM9.5

Most of them are implemented in pure Python. A couple rely on Perl script and
5-6 call R behind the scene. However, the user interface is identical for all of them.

Installation
---------------

**DREAMTools** depends on a few libraries such as Pandas, Numpy, Matplotlib. They should be automatically
installed with **DREAMTools** using pip executable::

    pip install dreamtools



Issues
-----------

Please fill bug report in https://github.com/dreamtools/dreamtools/issues


Contributions
----------------

Please join https://github.com/dreamtools/dreamtools

Others
--------

Note that in the Github directory, each challenge directory has its own README.rst file, which
contains basic usage and information about the challenge.

.. toctree::
    :maxdepth: 1

    userguide.rst
    developers.rst
    credits.rst
    references.rst
    changelog.rst
