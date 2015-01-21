Overview
===========

This directory contains all the data needed for the scoring of the 2 sub challenges of NIEHS-NCATS-UNC DREAM Toxicogenetics Challenge. 


data_sch1.RData
-----------

* observed: gold standard consisting in a data.frame with 264 rows (individuals) and 106 columns (compounds)
* leaderboardScores: precomputed scores for submissions in the final leaderboard
* pooled_std: vector with the pooled standard deviation for each compound (used to compute probabilistic concordance index)
* toxCompoundsID: IDs of the 91 (out of 106) compounds that were used in the final scoring


data_sch2.RData
-----------

* observed: gold standard consisting in a matrix with 50 rows (compounds) and 2 columns (median and interquantile distance)
* leaderboardScores: precomputed scores for submissions in the final leaderboard
