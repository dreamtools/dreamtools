
Overview
===========


:Title: Alternative Splicing
:Nickname: D6C1
:Summary: assess the accuracy of the reconstruction of alternatively spliced mRNA
          transcripts from short-read mRNA-seq. 
:SubChallenges: None
:Synapse page: https://www.synapse.org/#!Synapse:syn2817724
:leaderboard: https://www.synapse.org/#!Synapse:syn1688369/wiki/

.. contents::


Scoring
---------

::

    from dreamtools import D6C1
    s = D6C1()
    filename = s.download_template() 
    s.score(filename) 


