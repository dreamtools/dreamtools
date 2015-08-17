
Overview
===========


:Title:  DREAM4 Predictive Signaling Network Modeling
:Alias: D4C3
:Summary:  Predict phosphoprotein measurements using an interpretable, predictive network
:Scoring metric: difference between prediction and measuremnts.
    then log-transformed average of the pvalues for the  each protein.
:Synapse page: https://www.synapse.org/#!Synapse:syn2825304


.. contents::


Scoring
---------

::

    from dreamtools import D4C3
    s = D4C3()
    filename = s.download_template() 
    s.score(filename) 


