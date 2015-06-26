
Overview
===========


:Title: DREAM3 Gene Expression Prediction
:Nickname: D3C3
:Summary: 
:SubChallenges: Predict missing gene expression measurements
:Synapse page: https://www.synapse.org/#!Synapse:syn3033083

.. contents::


Scoring
---------

::

    from dreamtools import D3C3
    s = D3C3()
    filename = s.download_template() 
    s.score(filename) 


