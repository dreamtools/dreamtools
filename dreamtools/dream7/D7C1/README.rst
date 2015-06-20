Overview
===========


:Title: DREAM7 - Parameter estimation and network topology prediction
:Nickname: D7C1
:Summary: Participants were asked to develop and/or apply optimization methods, including the selection of the most informative experiments, to accurately estimate parameters and predict outcomes of perturbations in Systems Biology models, given the complete and incomplete structure of the model for a gene regulatory network. 
:Challenge:
:SubChallenges: parameter, topology, timecourse            
:Synapse page: https://www.synapse.org/#!Synapse:syn2821735


.. contents::


Scoring
---------

::

    from dreamtools import D7C1
    s = D7C1()
    filename = s.download_template(name='parameter') 
    s.score(filename, 'parameter')

Similarly for the sub-challenges called topology and timecourse.    





