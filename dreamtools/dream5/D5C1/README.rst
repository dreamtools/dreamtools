
Overview
===========


:Title: DREAM5 - Epitope-Antibody Recognition (EAR) Specificity Prediction 
:Nickname: D5C1
:Summary: 
:SubChallenges: None
:Synapse page: https://www.synapse.org/#!Synapse:syn2820433


.. contents::


Scoring
---------

::

    from dreamtools import D5C1
    s = D5C1()
    filename = s.download_template() 
    s.score(filename) 


