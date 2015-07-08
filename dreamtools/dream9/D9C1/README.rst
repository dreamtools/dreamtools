
Overview
===========


:Title: Broad-DREAM Gene Essentiality Prediction 
:Nickname: D9C1
:Summary: Develop predictive models for infer genes that are essential to cancer cell viability using gene expression and/or gene copy number features
:SubChallenges: 3 sub challenges
:Synapse page: https://www.synapse.org/#!Synapse:syn2384331

:Other resources: https://github.com/Sage-Bionetworks/DREAM9_Broad_Challenge_Scoring

.. contents::


Scoring
---------

::

    from dreamtools import D9C1
    s = D9C1()
    filename = s.download_template() 
    s.score(filename) 


