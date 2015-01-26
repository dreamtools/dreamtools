
# source all functions needed for scoring
source("functionsLeaderboard_sch2.R")

# some test submissions
load("testSubmissions_sch2.RData")

# load all data that I need to compute score (i.e. gold standard and scores precomputed for submissions in the final leaderboard)
load("data/data_sch2.RData")


## function 'computeMetric' can be used to compute metrics for each submssion for predicted median and interquantile distance
# example1, compute pearson correlation for a random submission
scoreByCompound<-computeMetric(submission=randomSubmission1, observed=observed, metric="pearson")
# example2, compute spearman correlation for the best Performer (note: prob C-index computation takes some time)
scoreByCompound<-computeMetric(submission=bestPerformer, observed=observed, metric="spearman")


# function 'computeOverallScores' can be used to compute ranking of submissions and average performances (as in the final lieaderboard)
submissions<-list(bestPerformer=bestPerformer, randomSubmission1=randomSubmission1, greatSubmission=greatSubmission)
res <- computeOverallScores(submissions)





