Overview
===========


scoring
-----------

The scoring functions inside **scoring** can be used to obtain the ROC or RMSE
values of a given submissions.

Format of submissions are explained on https://www.synapse.org/#!Synapse:syn1720047/wiki/

ROC and RMSE are absolute values and you may get a **better** score than what
was obtained in the challenges:

- https://www.synapse.org/#!Synapse:syn1720047/wiki/60530
- https://www.synapse.org/#!Synapse:syn1720047/wiki/60532

Note however, the teams were also compared to each other and final ranking could
be different from the pure ROC/RMSE ranking.

Here is the procedure to get the ROC or RMSE::


    from dreamtools.dream8.D8C1 import scoring
    sc1a = scoring.HP

    s = scoring.HPNScoringNetwork(sc1a_submissions.zip)
    s.compute_all_aucs()
    s.get_auc_final_scoring()

    s = scoring.HPNScoringNetworkInsilico(sc1b_submissions.zip)
    s.compute_score()
    s.auc

    s = scoring.HPNScoringPrediction(sc2a_submissions.zip)
    s.compute_all_rmse()
    s.get_mean_rmse()

    s = scoring.HPNScoringPredictionInsilico(sc2b_submissions.zip)
    s.compute_all_rmse()
    s.get_mean_rmse()






downloads.py 
----------------


Download all valid submissions that were used to score and rank the participants
in Dream8-HPN challenge::

    from dreamtools.dream8.D8C1 import downloads
    d = downloads.SubmissionsDownloader()
    d.download_all() # takes some time


    
