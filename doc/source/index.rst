


#################################################################################
DreamTools
#################################################################################

.. contents::

Overview
---------

**DreamTools** aims at sharing code used in the scoring of `DREAM <http://dreamchallenges.org>`_ challenges.

The main goals are to provide:

#. scoring functions for the Dream challenges for **end-users** via the **dreamtools-scoring** standalone
   application.
#. a place for **developers** involved in the dream challenges to share code


Code related to aggregation, leaderboards, or more complex analysis are not
guaranteed to be found in dreamtools even though it may be in some challenges
(e.g. D8C1). Some functionalities may be restricted with some access to synapse.
Some challenges will require to download public data sets from
`Synapse <www.synapse.org>`_ (in which case you will need to register).

dreamtools-scoring executable
-------------------------------

For users, **dreamtools** provide one executable called **dreamtools-scoring**, which should be installed automatically
when installing dreamtools. Knowing the name of the challenge (and possibly sub-challenge), it works as  follows::

    dreamtools-scoring --challenge d8c1 --sub-challenge sc1a --submission example.zip
    
It prints some information and the score of the submision for instance for the example above::

     Solution for alphabeta-Network.zip in challenge d8c1 (sub-challenge sc1a) is :
     AUROC: 0.781937275711

Available challenges
-------------------------


**Dreamtools** software does not include all scoring functions but more will be
implemented in the future. Here is the list of challenges available


* Dream8 HPN (D8C1) sub challenges named sc1a, sc1b, sc2a, sc2b. 
  See `Synapse page <https://www.synapse.org/#!Synapse:syn1720047>`_ for details
* Dream8 Tox (D8C2) sub challenges named sc1, sc2 
  See `Synapse page <https://www.synapse.org/#!Wiki:syn1761567>`_ for details
* Dream 7 (D7C1) (Network topology and parameter estimation)
* Dream 5 (D5C2) (Transcription factor)


Installation
---------------

**DreamTools** depends on a few libraries such as Pandas, Numpy, Matplotlib. They should be automatically
installed with **dreamtools** using pip executable::

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

    developers.rst
    credits.rst
    references.rst
