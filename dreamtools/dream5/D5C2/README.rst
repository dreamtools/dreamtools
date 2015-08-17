
Overview
===========


:Title: DREAM5 - TF-DNA Motif Recognition Challenge
:Alias: D5C2
:Summary: Predict the specificity of a Transcription Factor binding to a 35-mer probe
:SubChallenges: None
:Scoring Metric: Spearman and Pearson correlation as well as AUROC and AUPR
                 metric
:Synapse page: https://www.synapse.org/#!Synapse:syn2887863


.. contents::


Scoring
---------

::

    from dreamtools import D5C2
    s = D5C2()
    filename = s.download_template() 
    s.score(filename) 


