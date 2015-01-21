# compute ranking of submissions and average performances
# submission: list with one submission per element

computeOverallScores <- function (submissions){
  
  # compute the score for all submission separately for predicted median and interquantile distance
  # and create a matrix with population parameters (i.e. median and interquantile distance) as columns and submissions as rows
  scores<-list()
  metric<-"pearson"
  scores$pearson<-do.call(rbind, lapply(X=submissions, FUN=computeMetric, observed=observed, metric=metric))
  metric<-"spearman"
  scores$spearman<-do.call(rbind, lapply(X=submissions, FUN=computeMetric, observed=observed, metric=metric))
  
  #
  pearson<-list()
  spearman<-list()
  
  # consider also the leaderboard scores for the desired metric in order to compute the overall rank
  # have to invert the sign of just computed scores to compute the rank
  pearson$scoresAll<-rbind(-scores$pearson, -leaderboardScores$pearson)
  spearman$scoresAll<-rbind(-scores$spearman, -leaderboardScores$spearman)
  
  
  # compute rank of teams separately for median and interquantile distance
  pearson$compRanking <- apply(pearson$scoresAll, 2, rank)
  spearman$compRanking <- apply(spearman$scoresAll, 2, rank)
  
  #compute the mean ranking of each team separately for median and interquantile distance
  pearson$meanRanking <- apply(pearson$compRanking, 1, mean)
  spearman$meanRanking <- apply(spearman$compRanking, 1, mean)
  
  #compute the final ranking of each team separately for median and interquantile distance
  pearson$finalRanking <- rank(pearson$meanRanking)
  spearman$finalRanking <- rank(spearman$meanRanking)
  
  N<-length(submissions)
  
  # compute final rank (as average of the rank using the 2 metrics)
  meanRank<-apply(cbind(pearson$finalRanking, spearman$finalRanking),1,mean)
  finalRank<-rank(meanRank)
  
  summaryScores<-data.frame(rankSC=spearman$finalRanking[1:N], SC_m=scores$spearman[,1], SC_q=scores$spearman[,2],
                            rankPC=pearson$finalRanking[1:N], PC_m=scores$pearson[,1], PC_q=scores$pearson[,2],
                            meanRank=meanRank[1:N], finalRank=finalRank[1:N])
    
  print(summaryScores)
  
  res<-summaryScores
  return(res)
  
}


# compute metrics for each submssion for predicted median and interquantile distance
# INPUT:
# submission: prediction matrix (50 rows, 2 columnds)
# observed: test data (50 rows, 2 columnds)
# metric: metric to be used, can be "pearson" or "spearman"
# OUTPUT:
# score computed for predicted population parameter (i.e. median and interquantile distance)
computeMetric <- function (submission, observed, metric){
  
  # convert to lists with one element per compound
  observed.l<-as.list(as.data.frame(as.matrix(observed), stringsAsFactors=F))
  submission.l<-as.list(as.data.frame(as.matrix(submission), stringsAsFactors=F))
  
  # consider metric as a function and compute it for each compound
  metric <- match.fun(metric)
  performance<-mapply(metric, observed=observed.l, predicted=submission.l)
  
  return(performance)
}


# fuction to compute the pearson correlation 
pearson <- function(observed, predicted){
  if (!is.na(predicted) && length(unique(predicted))>1){
    cor(observed, predicted, method="pearson")
  }else{
    0
  }
}

# fuction to compute the pearson correlation 
spearman <- function(observed, predicted){
  if (!is.na(predicted) && length(unique(predicted))>1){
    cor(observed, predicted, method="spearman")
  }else{
    0
  }
}


