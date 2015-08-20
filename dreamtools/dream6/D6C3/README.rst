
Overview
===========


:Title: Gene Expression Prediction
:Nickname: D6C3
:Summary: predict gene expression levels from promoter activity derived by ribosomal protein.
:SubChallenges: None
:Synapse page: https://www.synapse.org/#!Synapse:syn2820426


.. contents::


Scoring
---------

::

    from dreamtools import D6C3
    s = D6C3()
    filename = s.download_template()
    s.score(filename)


