
Overview
===========


:Title: Genome-Scale Network Inference
:Nickname: D2C4
:Summary: Reconstruct a genome scale regulatory network from a large collection of microarrays
:SubChallenges: ?
:Synapse page: https://www.synapse.org/#!Synapse:syn2825394


.. contents::


Scoring
---------

::

    from dreamtools import D2C4
    s = D2C4()
    subname = s.sub_challenges[0]
    filename = s.download_template(subname) 
    s.score(filename, subname) 


