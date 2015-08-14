
Overview
===========


:Title: DREAM2 - Synthetic Five-Gene Network Inference
:Alias: D2C3
:Summary: Infer a gene regulation network from qPCR and microarray measurements
:SubChallenges: DIRECTED-SIGNED_EXCITATORY_chip
        DIRECTED-SIGNED_EXCITATORY_qPCR 
        DIRECTED-SIGNED_INHIBITORY_chip
        DIRECTED-SIGNED_INHIBITORY_qPCR 
        DIRECTED-UNSIGNED_chip
        DIRECTED-UNSIGNED_qPCR 
        UNDIRECTED-SIGNED_EXCITATORY_chip
        UNDIRECTED-SIGNED_EXCITATORY_qPCR 
        UNDIRECTED-SIGNED_INHIBITORY_chip
        UNDIRECTED-SIGNED_INHIBITORY_qPCR 
        UNDIRECTED-UNSIGNED_chip
        UNDIRECTED-UNSIGNED_qPCR
:Scoring metric: AUPR and AUROC metrics
:Synapse page: https://www.synapse.org/#!Synapse:syn3034869


.. contents::


Scoring
---------

::

     from dreamtools import D2C3
     s = D2C3()
     subname = "DIRECTED-UNSIGNED_qPCR"
     filename = s.download_template(subname)
     s.score(filename, subname)



