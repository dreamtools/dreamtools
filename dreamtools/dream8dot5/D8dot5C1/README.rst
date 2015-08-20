Overview
===========


:Title: DREAM 8.5 - Rheumatoid Arthritis Responder Challenge
:Nickname: D8dot5C1
:Summary: develop the best possible predictor of anti-TNF response in 
          the context of Rheumatoid Arthritis.
:SubChallenges: sc1, sc2
:Synapse page: https://www.synapse.org/#!Synapse:syn1734172/wiki/

.. contents::
This directory contains tools for scoring of the two sub challenges of Rheumatoid Arthritis Responder DREAM Challenge. 
 

Subchallenge 1
-----------

**Challenge description:** Predict treatment response as measured by the change in disease activity score (DAS28) in response to anti-TNF therapy. 
The template for scoring is provided within this synapse https://www.synapse.org/#!Synapse:syn2355870 page. 


Subchallenge 2
-----------

**Challenge description:** Identify poor responders as defined by EULAR criteria for non-response (~20%% of the study population). 

The template for scoring is provided within this synapse https://www.synapse.org/#!Synapse:syn2355870 page.


For further information on the subchallenge and on the submission format go to https://www.synapse.org/#!Synapse:syn1734172/wiki/62595

For details on the scoring metrics go to https://www.synapse.org/#!Synapse:syn1734172/wiki/62689.

Scoring
---------

From the dreamtools package, you can score a submission from the D8dot5C1 first sub challenge as follows:

::

  from dreamtools import D8dot5C1
  s = D8dot5C1()

  filename = s.download_template('sc1')
  df2 = s.score(filename, 'sc1')
  print(df1)

  filename = s.download_template('sc2')
  df2 = s.score(filename, 'sc2')
  print(df2)

Examples of submission files can be found in the source code (e.g., data/test_sc1.csv)



