DreamTools
==========

Overview
----------------

**DreamTools** aims at sharing code related to `DREAM <http://dreamchallenges.org>`_ challenges.

This repository is meant to contain (small) data sets and codes related to the scoring of the 
`DREAM challenges <http://dreamchallenges.org>`_. 


The main goals are:

#. provide scoring functions for the Dream challenges for end-users
#. provide a place to share-reuse code used before/during/after the challenges for developers

The **dreamtools-scoring** executable
-------------------------------------

For users, **dreamtools** provide one executable called **dreamtools-scoring**, which should be installed automatically
when installing dreamtools. Knowing the name of the challenge (and possibly sub-challenge), it works as  follows::

    dreamtools-scoring --challenge d8c1 --sub-challenge sc1a --submission ~/alphabeta-Network.zip
    
It prints some information and the score of the submision for instance for the example above::

     Solution for alphabeta-Network.zip in challenge d8c1 (sub-challenge sc1a) is :
     AUROC: 0.781937275711

Scoring functions available so far:


* Dream8 HPN (D8C1) sub challenges named sc1a, sc1b, sc2a, sc2b. 
  See `Synapse page <https://www.synapse.org/#!Synapse:syn1720047>`_ for details
* Dream8 Tox (D8C2) sub challenges named sc1, sc2. 
  See `Synapse page <https://www.synapse.org/#!Synapse:syn1761567>`_ for details

**Format** for the challenges can be found in the README of each subchallenge. For instance, for Dream8 Challenge1, 
please see ./dreamtools/dream8/D8C1/READM.rst

Installation
---------------

::

    pip install dreamtools
    
    
Issues
-----------

Please fill bug report in https://github.com/dreamtools/dreamtools/issues
    
For developers
----------------

Not all challenges are yet provided. If you wish to contribute, please let us know. 




