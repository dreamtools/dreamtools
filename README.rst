DreamTools
==========

:Online documentation: `On pypi website `http://pythonhosted.org/dreamtools/`_,

.. contents::

Overview
----------------

**DreamTools** aims at sharing code used in the scoring of `DREAM <http://dreamchallenges.org>`_ challenges.

The main goals are:

#. provide scoring functions for the Dream challenges for **end-users** via the **dreamtools-scoring** standalone
   application.
#. provide a place to share-reuse code used before/during/after the challenges for **developers** and organisers 
   of the challenges


Code related to aggregation, leaderboards, or more complex analysis are not
guaranteed to be found in dreamtools even though it may be in some challenges
(e.g. D8C1). Some functionalities may be restricted with some access to synapse.


The **dreamtools-scoring** executable
------------------------------------------

For users, **dreamtools** provide one executable called **dreamtools-scoring**, which should be installed automatically
when installing dreamtools. Knowing the name of the challenge (and possibly sub-challenge), it works as  follows::

    dreamtools-scoring --challenge d8c1 --sub-challenge sc1a --submission alphabeta-Network.zip
    
It prints some information and the score of the submision for instance for the example above::

     Solution for alphabeta-Network.zip in challenge d8c1 (sub-challenge sc1a) is :
     AUROC: 0.803628919403
     Rank LB: 1



Not all DREAM challenges are included but here is the current status.


#. DREAM10

#. DREAM9

#. DREAM8.5

#. DREAM8

    * D8C1 (HPN breat cancer)  sub challenges named sc1a, sc1b, sc2a, sc2b. 
      See `Synapse page <https://www.synapse.org/#!Synapse:syn1720047>`_ for details
    * D8C2 (Toxoxicology) sub challenges named sc1, sc2. 
      See `Synapse page <https://www.synapse.org/#!Synapse:syn1761567>`_ for details
    * D8C3 coming soon

#. DREAM7

    * D7C1 (Network Parameter Estimation)

#. DREAM6

    * D6C1 (Network Parameter Estimation) WONT be included (see D7C1 instead)
    
#. DREAM5    

    * D5C2 (transcription factor)  

#. DREAM4

#. DREAM3

#. DREAM2

#. DREAM1

**Format** for the challenges can be found in the README of each subchallenge. For instance, for Dream8 Challenge1, 
please see ./dreamtools/dream8/D8C1/README.rst

Installation
---------------

::

    pip install dreamtools


Issues
-----------

Please fill bug report in https://github.com/dreamtools/dreamtools/issues

For developers
----------------

Not all challenges are yet provided. If you wish to contribute, please let us
know. See doc/source/developers



