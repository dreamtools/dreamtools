
Overview
===========


:Title: DREAM2 - Synthetic Five-Gene Network Inference
:Nickname: D2C3
:Summary: Infer a gene regulation network from qPCR and microarray measurements
:SubChallenges: 
:Synapse page: https://www.synapse.org/#!Synapse:syn3034869


.. contents::


Scoring
---------

::

    from dreamtools import D2C3
    s = D2C3()
    filename = s.download_template() 
    s.score(filename) 


