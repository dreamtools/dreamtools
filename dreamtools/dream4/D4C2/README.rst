
Overview
===========


:Title: DREAM4 In Silico Network Challenge
:Nickname: D4C2
:Summary: Infer simulated gene regulation networks and predict gene expression measurements
:SubChallenges: 3 called (10,100,100_multifactorial)
:Synapse page: https://www.synapse.org/#!Synapse:syn3049714


.. contents::


Scoring
---------

::

    from dreamtools import D4C2
    s = D4C2()
    filename = s.download_template(10) 
    s.score(filename, 10) 

    filename = s.download_template(100) 
    s.score(filename, 100) 

    filename = s.download_template('100_multifactorial') 
    s.score(filename, '100_multifactorial') 

