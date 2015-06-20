Overview
===========


:Title: DREAM 8 - NIEHS-NCATS-UNC DREAM Toxicogenetics Challenge
:Nickname: D8C2
:Summary: Participants were provided with genetics and transcriptomics information of the 1000 Genomes Project (www.1000genomes.org), as well as cytotoxicity measures derived from compound exposure to over a hundred toxic agents using the 1000 genomes lymphoblastoid cell lines and tasked with solving two related subchallenges.
:SubChallenges: sc1, sc2
:Synapse page: https://www.synapse.org/#!Synapse:syn1761567

.. contents::


This directory contains tools for scoring of the two sub challenges of NIEHS-NCATS-UNC DREAM Toxicogenetics Challenge. 


Subchallenge 1
-----------

**Challenge description:** Predict interindividual variability in in vitro cytotoxicity based on genomic profiles of individual cell lines. For each compound, participants will be challenged to predict the absolute values and relative ranks of cytotoxicity across a set of unknown cell lines for which genomic data is available. 

The template for scoring is provided within this synapse https://www.synapse.org/#!Synapse:syn1917708 page. 

For further information on the subchallenge and on the submission format go to https://www.synapse.org/#!Wiki:syn1761567/ENTITY/55909 

For details on the scoring metrics go to https://www.synapse.org/#!Wiki:syn1761567/ENTITY/60497.


Subchallenge 2
-----------

**Challenge description:** For each compound, predict the concentration at which median cytotoxicity would occur, as well as inter-individual variation in cytotoxicity, described by the 5-95th%ile range, across the population. Each prediction will be scored based on the participant’s ability to predict these two parameters within a set of compounds excluded from the training set. 

For further information on the subchallenge and on the submission format go to https://www.synapse.org/#!Wiki:syn1761567/ENTITY/55911 

For details on the scoring metrics go to https://www.synapse.org/#!Wiki:syn1761567/ENTITY/60498.

Scoring
---------

From the dreamtools package, you can score a submission from the D8C2 first sub challenge as follows:

::

  from dreamtools import D8C2
  s = D8C2()
  filename = s.download_template('sc1')
  df = s.score(filename, 'sc1')


Note that the computation takes a few minutes. The computation for the sub-challenge 2 is much faster and works similalrly::

  from dreamtools import D8C2
  s = D8C2()
  filename = s.download_template('sc2')
  df = s.score(filename, 'sc2')


Examples of submission files can be found in the source code (e.g., data/test_sc1.csv)




