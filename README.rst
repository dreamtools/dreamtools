DreamTools
==========
Overview
---------

**dreamtools** aims at sharing code related to `DREAM <http://www.the-dream-project.org/>`_ challenges.

This repository is meant to contain (small) data sets and codes related to the scoring of the 
`DREAM challenges <http://dreamchallenges.org>`_. 

It was created at the time of DREAM8-9 and contains only Dream8 HPN challenge code for now. 
Note however that **dreamtools** contains information about DREAM6-7 (parameter estimation). 
More code/scripts about other challenges will be added later. 

The main goals are:

#. provide user a scoring function for the challenges
#. provide developer a place to share-reuse code used before/during/after the challenges

dreamtools-scoring executable
-------------------------------

For users, **dreamtools** provide one executable called **dreamtools-scoring**, which should be installed automatically
when installing dreamtools. Knowing the name of the challenge (and possibly sub-challenge), it works as  follows::

    dreamtools-scoring --challenge d8c1 --sub-challenge sc1a --submission ~/alphabeta-Network.zip
    
It prints some information and the score of the submision.

Installation
---------------

::

    pip install dreamtools
    
    


