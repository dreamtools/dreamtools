
Overview
===========


:Title: DREAM 3 In Silico Network Challenge
:Nickname: D3C4
:Summary: Infer simulated gene regulation networks
:SubChallenges: 
:Synapse page: https://www.synapse.org/#!Synapse:syn2853594

.. contents::


Scoring
---------

::

    from dreamtools import D3C4
    s = D3C4()
    filename = s.download_template() 
    s.score(filename) 


