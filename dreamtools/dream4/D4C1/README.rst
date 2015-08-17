
Overview
===========


:Title: Peptide Recognition Domain (PRD) Specificity Prediction
:Alias: D4C1
:Summary: Predict protein-protein interactions at the level of binding domains and peptides
:SubChallenges: There were 3 sub-challenges however the template should contain
    all sub-challenges all together
:Scoring metric: depends on the sub-challenges. Generally log-transformed
     average of the AUROC/AUPR p-values
:Synapse page: https://www.synapse.org/#!Synapse:syn2925957

.. contents::


Scoring
---------

::

    from dreamtools import D4C1
    s = D4C1()
    filename = s.download_template() 
    s.score(filename) 


