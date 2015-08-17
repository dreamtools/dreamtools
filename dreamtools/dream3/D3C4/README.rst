
Overview
===========


:Title: DREAM 3 In Silico Network Challenge
:Alias: D3C4
:Summary: Infer simulated gene regulation networks
:SubChallenges: different network sizes (10, 50, 100) for 5 datasets
:Scoring metric: mean of AUROC and AUPR computed as log-transformed average 
    of the 5 p-values.
:Synapse page: https://www.synapse.org/#!Synapse:syn2853594

.. contents::


Scoring
---------

::

    from dreamtools import D3C4
    s = D3C4()
    filename = s.download_template() 
    s.score(filename) 


