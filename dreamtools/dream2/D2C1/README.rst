
Overview
===========


:Title: DREAM2 - BCL6 Transcriptional Target Prediction
:Nickname: D2C1
:Summary: Predict the genes for transcription factor binding.
:SubChallenges: None
:Synapse page: https://www.synapse.org/#!Synapse:syn3034857


.. contents::


Scoring
---------

::

    from dreamtools import D2C1
    s = D2C1()
    filename = s.download_template() 
    s.score(filename) 


