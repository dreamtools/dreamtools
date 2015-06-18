Overview
===========

:Title: DREAM 9.5 -DREAM Olfaction Prediction Challenge
:Nickname: D9dot5C1
:Summary: This challenge’s focus is to map the chemical properties of odors to predict a give subject’s behavioral responses.
:SubChallenges: SC1A, SC1B, SC2A, SC2B
:Synapse page: https://www.synapse.org/#!Synapse:syn2811262


The DREAM 9.5 challenge implemented here is a translation of the original code from Bruce Hoff, Kelly Norel 
available in another github : https://github.com/Sage-Bionetworks/OlfactionDREAMChallenge

Scoring 
========

Scoring functions retreive gold standard from synapse. Similarly, yuo can get a templates for the sub challenge 1 and 2 as follows. The scores are stored in two dataframes df1 and df2.

::

  from dreamtools import D9dot5C1
  s = D9dot5C1()
  file1, file2 = s.download_templates()

  df1 = s.score_sc1(file1)
  print(df1)
    
  df2 = s.score_sc2(file2)
  print(df2)
