
Overview
===========


:Title: DREAM5 - Epitope-Antibody Recognition (EAR) Specificity Prediction 
:Alias: D5C1
:Summary: Predict the binding specificity of peptide-antibody interactions. 
:SubChallenges: None
:Scoring metric: ROC curve is computed with AUC and AUPR metrics and p-values.
    overall score is the mean of those 2 p-values.
:Synapse page: https://www.synapse.org/#!Synapse:syn2820433


.. contents::


Scoring
---------

::

    from dreamtools import D5C1
    s = D5C1()
    filename = s.download_template() 
    s.score(filename) 


