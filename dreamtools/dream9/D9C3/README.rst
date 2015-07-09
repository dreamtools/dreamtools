
Overview
===========


:Title: 
:Nickname: D9C3
:Summary: 
:SubChallenges: 
:Synapse page: https://www.synapse.org/#!Synapse:syn2290704
:Other resource:
https://github.com/Sage-Bionetworks/DREAM_Alzheimers_Challenge_Scoring

.. contents::


Scoring
---------

::

    from dreamtools import D9C3
    s = D9C3()
    filename = s.download_template() 
    s.score(filename) 


