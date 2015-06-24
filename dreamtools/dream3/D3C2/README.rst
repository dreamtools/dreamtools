
Overview
===========


:Title: DREAM3 Signaling Response Prediction 
:Nickname: D3C2
:Summary: Predict missing protein concentrations from a large corpus of measurements
:SubChallenges: cytokine, phospho 
:Synapse page: https://www.synapse.org/#!Synapse:syn2825325


.. contents::


Scoring
---------

::

    from dreamtools import D3C2
    s = D3C2()
    filename = s.download_template('cytokine') 
    s.score(filename, 'cytokine') 


