
Overview
===========


:Title: DREAM7 - Sage Bionetworks-DREAM Breast Cancer Prognosis
:Nickname: D7C2
:Summary:  predict breast cancer survival, based on clinical information 
     about the patient's tumor as well as genome-wide molecular profiling 
     data including gene expression and copy number profiles.
:SubChallenges: 
:Synapsei page: https://www.synapse.org/#!Synapse:syn2813426


.. contents::


Scoring
---------

::

    from dreamtools import D7C2
    s = D7C2()
    filename = s.download_template() 
    s.score(filename) 


