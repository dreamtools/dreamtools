
# load all data needed to compute score (i.e. gold standard, "toxCompoundsID", "pooled_std" and scores precomputed for submissions in the final leaderboard
load("data/data_sch1.RData")
source("prob_Cidx.R") # could be in functionLeaderboard.R but must be here for the Python script to work
# source all functions needed for scoring
source("functionsLeaderboard_sch1.R")

# some test submissions
load("testSubmissions_sch1.RData")


## function 'computeByCompound' can be used to compute metrics for each submssion for each compound
# example1, compute pearson correlation for a random submission
scoreByCompound<-computeByCompound(submission=randomSubmission1, observed=observed, metric="pearson", keepCompounds=toxCompoundsID)
# example2, compute prob C-index for the best Performer (note: prob C-index computation takes some time)
scoreByCompound<-computeByCompound(submission=bestPerformer, observed=observed, metric="probCindex", keepCompounds=toxCompoundsID, pooled_std=pooled_std)

# function 'computeOverallScores' can be used to compute ranking of submissions and average performances (as in the final lieaderboard)
# takes some time to run because of prob C-index computation
submissions<-list(bestPerformer=bestPerformer, randomSubmission1=randomSubmission1, greatSubmission=greatSubmission)
res <- computeOverallScores(submissions)


