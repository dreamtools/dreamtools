
Overview
===========


:Title: Alzheimers Disease Big Data 
:Nickname: D9C3
:Summary:  use the ADNI data to create predictive models of cognitive scores,
    predict discordance between cognitive ability and amyloid load and/or
    predict diagnostic groups based on MR imaging and genetics.
:SubChallenges: 
:Synapse page: https://www.synapse.org/#!Synapse:syn2290704
:Other resource:
https://github.com/Sage-Bionetworks/DREAM_Alzheimers_Challenge_Scoring

.. contents::


Scoring
---------

::

    from dreamtools import D9C3
    s = D9C3()
    filename = s.download_template() 
    s.score(filename) 


