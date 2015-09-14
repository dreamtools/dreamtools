
Overview
===========


:Title: DREAM2 - BCL6 Transcriptional Target Prediction
:Alias: D2C1
:Summary: Predict the genes for transcription factor binding.
:SubChallenges: None
:Scoring metric: AUPR and AUC
:Synapse page: https://www.synapse.org/#!Synapse:syn3034857
:Leaderboard: https://www.synapse.org/#!Synapse:syn3034857/wiki/74407

.. contents::


Scoring
---------

::

    from dreamtools import D2C1
    s = D2C1()
    filename = s.download_template() 
    s.score(filename) 


