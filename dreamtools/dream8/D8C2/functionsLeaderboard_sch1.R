# compute ranking of teams and average performance, based on the selected metric
# submission: list with one submission per element

computeOverallScores <- function (submissions){
  
  keepCompounds<-toxCompoundsID

  # compute the compoud by compound score for all submission
  # and create a matrix with compounds as columns and submissions as rows
  scores<-list()
  metric<-"pearson"
  scores$pearson<-do.call(rbind, lapply(X=submissions, FUN=computeByCompound, observed=observed, metric=metric, keepCompounds=keepCompounds, pooled_std=pooled_std))
  metric<-"probCindex"
  scores$probCindex<-do.call(rbind, lapply(X=submissions, FUN=computeByCompound, observed=observed, metric=metric, keepCompounds=keepCompounds, pooled_std=pooled_std))
  
  #
  pearson<-list()
  probCindex<-list()
  
  # compute average and best score for each submission across compounds
  pearson$scores.average<-apply(scores$pearson, 1, function(x) mean(x, na.rm=T))
  probCindex$scores.average<-apply(scores$probCindex, 1, function(x) mean(x, na.rm=T))
  
  # the best score is the max value 
  pearson$scores.best<-apply(scores$pearson, 1, function(x) max(x, na.rm=T))
  probCindex$scores.best<-apply(scores$probCindex, 1, function(x) max(x, na.rm=T))

  # consider also the leaderboard scores for the desired metric in order to compute the overall rank
  # have to invert the sign of just computed scores to compute the rank
  pearson$scoresAll<-rbind(-scores$pearson, leaderboardScores$pearson)
  probCindex$scoresAll<-rbind(-scores$probCindex, leaderboardScores$probCindex)
  
  # compute rank of teams for each compound
  pearson$compRanking <- apply(pearson$scoresAll, 2, rank)
  probCindex$compRanking <- apply(probCindex$scoresAll, 2, rank)
  
  #compute the mean ranking of each team across compounds
  pearson$meanRanking <- apply(pearson$compRanking, 1, mean)
  probCindex$meanRanking <- apply(probCindex$compRanking, 1, mean)
  
  #compute the final ranking of each team across compounds
  pearson$finalRanking <- rank(pearson$meanRanking)
  probCindex$finalRanking <- rank(probCindex$meanRanking)
  
  N<-length(submissions)
  meanRank<-apply(cbind(pearson$finalRanking, probCindex$finalRanking),1,mean)
  finalRank<-rank(meanRank)
  summaryScores<-data.frame(meanPCI=probCindex$scores.average, maxPCI=probCindex$scores.best, meanRankPCI=probCindex$meanRanking[1:N], rankPCI=probCindex$finalRanking[1:N],
                      meanPC=pearson$scores.average, maxPC=pearson$scores.best, meanRankPC=pearson$meanRanking[1:N], rankPC=pearson$finalRanking[1:N],
                      meanRank=meanRank[1:N], finalRank=finalRank[1:N])
  
  print(summaryScores)
  
  res<-list(byCompoundScores=scores, summaryScores=summaryScores)
  return(res)
  
}


# compute metrics for each compound of each submission
# INPUT:
# submission: prediction matrix (264 rows, 106 columns)
# observed: test data (264 rows, 106 columns)
# metric: metric to be used, can be "pearson" or "probCindex"
# keepCompounds: specify compounds to use, if NA all compounds are considered, use "toxCompoundsID" to include the compounds used in the Leaderboard
# OUTPUT:
# score computed for each compound
computeByCompound <- function (submission, observed, metric, keepCompounds=NA, pooled_std=NA){
  
  if (!is.na(keepCompounds[1])){
    observed <- observed[,keepCompounds]
    submission <- submission[,keepCompounds]
    pooled_std <- pooled_std[keepCompounds]
  }
  
  # convert to lists with one element per compound
  observed.l<-as.list(as.data.frame(as.matrix(observed), stringsAsFactors=F))
  submission.l<-as.list(as.data.frame(as.matrix(submission), stringsAsFactors=F))
  
  # consider metric as a function and compute it for each compound
  if (metric=="probCindex"){
    pooled_std.l<-as.list(pooled_std)
    metric <- match.fun(metric)
    performance_byCompound<-mapply(metric, observed=observed.l, predicted=submission.l, pooled_std=pooled_std.l)
    
  }else{
    metric <- match.fun(metric)
    performance_byCompound<-mapply(metric, observed=observed.l, predicted=submission.l)
  }
  
  return(performance_byCompound)
}


# fuction to compute the pearson correlation 
pearson <- function(observed, predicted){
  if (!is.na(predicted) && length(unique(predicted))>1){
    cor(observed, predicted, method="pearson")
  }else{
    0
  }
}

# fuction to compute the probCindex
# function to compute prob c-Index
#source("prob_Cidx.R")
probCindex <- function(observed, predicted, pooled_std){
  # compute pCIdx
  pCIdx_GS(observed, pooled_std, rank(predicted, ties.method="random"))
}


