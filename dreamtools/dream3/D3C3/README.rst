
Overview
===========


:Title: DREAM3 Gene Expression Prediction
:Alias: D3C3
:Summary: Predict missing gene expression measurements
:SubChallenges: different network size (10, 50, 100)
:Scoring metric: p-value of a test for association between paired
    samples using the spearman rank correlation.
:Synapse page: https://www.synapse.org/#!Synapse:syn3033083

.. contents::


Scoring
---------

::

    from dreamtools import D3C3
    s = D3C3()
    filename = s.download_template() 
    s.score(filename) 


