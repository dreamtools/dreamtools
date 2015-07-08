
Overview
===========


:Title: Genome-Scale network inference
:Nickname: D2C5
:Summary: Reconstruct a genome scale regulatory network from a large collection of microarrays
:SubChallenges: 3 independent type of networks
:Scoring metric: AUPR or AUROc for each sub challenge.
:Synapse page: https://www.synapse.org/#!Synapse:syn3034894


.. contents::


Scoring
---------

::

    from dreamtools import D2C5
    s = D2C5()
    filename = s.download_template() 
    s.score(filename) 


