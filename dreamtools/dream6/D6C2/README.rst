
Overview
===========


:Title: Estimation of Model Parameters
:Nickname: D6C2
:Summary: Parameter estimation of gene regulatory networks given incomplete structure given perturbed data sets.
:SubChallenges: 
:Synapse page: https://www.synapse.org/#!Synapse:syn2841366


.. contents::


Scoring
---------

::

    from dreamtools import D6C2
    s = D6C2()
    filename = s.download_template() 
    s.score(filename) 


