
Overview
===========


:Title: DREAM4 In Silico Network Challenge
:Alias: D4C2
:Summary: Infer simulated gene regulation networks and predict gene expression measurements
:SubChallenges: 3 called (10,100,100_multifactorial)
:Scoring metric: same as challenge D3C4 (mean of AUROC and AUPR computed as log-transformed average of several p-values) 
:Synapse page: https://www.synapse.org/#!Synapse:syn3049714


.. contents::


Scoring
---------

The sub challenge must be provided. For instance 10_1 means subchallenge with
size 10, batch 1
::

    from dreamtools import D4C2
    s = D4C2()
    filename = s.download_template("10_1")
    s.score(filename, "10_1")

    filename = s.download_template("100_2")
    s.score(filename, "100_2") 

    filename = s.download_template('100_multifactorial_3') 
    s.score(filename, '100_multifactorial_3') 

You can score one file or the 5 networks as in the challenge itself providing a
list of filenames instead of a single file. 

From dreamtools for a single file::

    dreamtools --challenge D4C2 --sub-challenge 10  --filename ./templates/DREAM

Or a list of files (regular expression accepted)    ::

    dreamtools --challenge D4C2 --sub-challenge 10  --filename ./templates/10/DREAM*

