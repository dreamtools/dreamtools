
Overview
===========


:Title: DREAM5 - Systems Genetics challenges
:Nickname: D5C3
:Summary: Predict disease phenotypes and infer Gene Networks from Systems Genetics data
:SubChallenges: A100, A300, A999, B 
:Synapse page: https://www.synapse.org/#!Synapse:syn2820440


.. contents::


Scoring
---------

::

    from dreamtools import D5C3
    s = D5C3()
    filename = s.download_template() 
    s.score(filename) 


