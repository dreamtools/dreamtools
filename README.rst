DreamTools
==========

:Online documentation: `On pypi website <http://pythonhosted.org/dreamtools/>`_,
:Issues and bug reports: `On github <https://github.com/dreamtools/dreamtools/issues>`_,

.. contents::

Overview
----------------

**DreamTools** aims at sharing code used in the scoring of `DREAM <http://dreamchallenges.org>`_ challenges.

The main goals are to provide:

#. scoring functions for the Dream challenges for **end-users** via the **dreamtools-scoring** standalone
   application.
#. a place for **developers** involved in the dream challenges to share code


Code related to aggregation, leaderboards, or more complex analysis are not
guaranteed to be found in dreamtools even though it may be in some challenges
(e.g. D8C1). Some functionalities may be restricted with some access to synapse.
Some challenges will require to download public data sets from `Synapse
<www.synapse.org>`_ (in which case you will need to register).


The **dreamtools-scoring** executable
------------------------------------------

For users, **dreamtools** provide one executable called **dreamtools-scoring**, which should be installed automatically
when installing dreamtools. Knowing the name of the challenge (and possibly sub-challenge), it works as  follows::

    dreamtools-scoring --challenge d8c1 --sub-challenge sc1a --submission example.zip
    
It prints some information and the score of the submision for instance for the example above::

     Solution for alphabeta-Network.zip in challenge d8c1 (sub-challenge sc1a) is :
     AUROC: 0.803628919403
     Rank LB: 1


Available challenges
-------------------------

**Dreamtools** software does not include all scoring functions but more will be
implemented in the future. Here is the list of challenges available 

#. DREAM10

#. DREAM9

#. DREAM8.5

#. DREAM8

    * D8C1 (HPN breat cancer)  sub challenges named sc1a, sc1b, sc2a, sc2b. 
      See `Synapse page D8C1 <https://www.synapse.org/#!Synapse:syn1720047>`_ for details
    * D8C2 (Toxoxicology) sub challenges named sc1, sc2. 
      See `Synapse page D8C2 <https://www.synapse.org/#!Synapse:syn1761567>`_ for details
    * D8C3 coming soon

#. DREAM7

    * D7C1 (Network Parameter Estimation)

#. DREAM6

    * D6C1 (Network Parameter Estimation) WONT be included (see D7C1 instead)
    
#. DREAM5    

    * D5C2 (transcription factor)  

#. DREAM4

#. DREAM3

    * D3C1 (Signaling Cascade Challenge)

#. DREAM2

#. DREAM1

**Format** of the template for each challenge should be found in the README of each subchallenge. For instance, for Dream8 Challenge1, 
please see ./dreamtools/dream8/D8C1/README.rst

Installation
---------------

**DreamTools** depends on a few libraries such as Pandas, Numpy, Matplotlib. They should be automatically
installed with **dreamtools** using pip executable::

    pip install dreamtools


Issues
-----------

Please fill bug report in https://github.com/dreamtools/dreamtools/issues


Contributions
---------------

Please join https://github.com/dreamtools/dreamtools


For developers
----------------

Please see doc/source/developers.rst

Credits
-----------

Please see doc/source/credits.rst






