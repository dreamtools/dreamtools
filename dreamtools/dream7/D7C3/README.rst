
Overview
===========


:Title: The DREAM Phil Bowen ALS Prediction Prize4Life
:Nickname: D7C3
:Summary: to predict the progression of disease in ALS patients based on
    the patient’s current disease status. The data
    available to make this prediction includes demographics, functional
    measures ...
:SubChallenges:
:Synapse page: https://www.synapse.org/#!Synapse:syn2826267


.. contents::


Scoring
---------

::

    from dreamtools import D7C3
    s = D7C3()
    filename = s.download_template() 
    s.score(filename) 


