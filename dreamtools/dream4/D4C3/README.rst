
Overview
===========


:Title:  DREAM4 Predictive Signaling Network Modeling
:Nickname: D4C3
:Summary:  Predict phosphoprotein measurements using an interpretable, predictive network
:SubChallenges: None
:Synapse page: https://www.synapse.org/#!Synapse:syn2825304


.. contents::


Scoring
---------

::

    from dreamtools import D4C3
    s = D4C3()
    filename = s.download_template() 
    s.score(filename) 


