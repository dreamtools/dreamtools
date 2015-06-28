
Overview
===========


:Title: Genome-Scale Network Inference
:Nickname: D2C4
:Summary: Reconstruct a genome scale regulatory network from a large collection of microarrays
:SubChallenges: ?
:Synapse page: https://www.synapse.org/#!Synapse:syn3034869


.. contents::


Scoring
---------

::

    from dreamtools import D2C4
    s = D2C4()
    filename = s.download_template() 
    s.score(filename) 


