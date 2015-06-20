
Overview
===========


:Title: DREAM 3 Signaling Cascade Identification
:Nickname: D3C1
:Summary: Infer a signaling network from flow cytometry data
:Challenge:
:SubChallenges: None
:Synapse page: https://www.synapse.org/#!Synapse:syn3033068




.. contents::


Scoring
---------

::

    from dreamtools import D3C1
    s = D3C1()
    filename = s.download_templates() 
    s.score(filename) 


