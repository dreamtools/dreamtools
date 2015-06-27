
Overview
===========


:Title: DREAM2 - Protein-Protein Interaction Network Inference
:Nickname: D2C2
:Summary: Predict a PPI network of 47 proteins
:SubChallenges: 
:Synapse page: https://www.synapse.org/#!Synapse:syn2825374


.. contents::


Scoring
---------

::

    from dreamtools import D2C2
    s = D2C2()
    filename = s.download_template() 
    s.score(filename) 


