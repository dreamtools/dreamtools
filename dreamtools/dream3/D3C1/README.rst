
Overview
===========


:Title: DREAM 3 Signaling Cascade Identification
:Alias: D3C1
:Summary: Infer a signaling network from flow cytometry data
:SubChallenges: None
:Scoring metric: probability of having N correct predictions
:Synapse page: https://www.synapse.org/#!Synapse:syn3033068




.. contents::


Scoring
---------

::

    from dreamtools import D3C1
    s = D3C1()
    filename = s.download_templates() 
    s.score(filename) 


