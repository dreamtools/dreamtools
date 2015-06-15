# ------------------------------------------------------------------------------------------------
# AUTHOR:      Michael Patrick Menden
# SUPERVISOR:  Julio Saez-Rodriguez
# AFFILIATION: EMBL-EBI
# LIZENS:      GPL
# ------------------------------------------------------------------------------------------------

# Gauss error function
pCIdx_erf <- function(x) {
  2/sqrt(pi) * integrate(f=function(t) {exp(-t^2)}, 0, x)$value
}

# ------------------------------------------------------------------------------------------------
# Cumulative distribution function
pCIdx_CDF <- function(u,v,s) {
  0.5 * (1 + pCIdx_erf(abs(u-v) / (2*s)))
}

# ------------------------------------------------------------------------------------------------
# Probabilistic C-Index 
# E   => 	Vector of continuous experimentally determined values, e.g. EC10.
# s	=>	Scalar representing the pooled standard deviation for E.
# P	=>	Vector containing the predicted rank of E. 
pCIdx <- function(E,s,P) {
  runningSum <- 0
  n <- 0.5 * length(E) * (length(E)-1)
  for (i in 1:(length(E)-1)) {
    for (j in (i+1):length(E)) {
      if ((E[i]>E[j] & P[i]>P[j]) | (E[i]<E[j] & P[i]<P[j])) {
        runningSum <- runningSum + pCIdx_CDF(E[i], E[j], s)
      } else if ((E[i]>E[j] & P[i]<P[j]) | (E[i]<E[j] & P[i]>P[j])) {
        runningSum <- runningSum + 1 - pCIdx_CDF(E[i], E[j], s)
      } else {
        runningSum <- runningSum + 0.5
      }
    }
  }
  runningSum/n
}

# ------------------------------------------------------------------------------------------------
# Cumulative distribution function
pCIdx_CDF_GS <- function(u,v,s) {
  0.5 * (1 + pCIdx_erf((u-v)/(2*s)))
}

# ------------------------------------------------------------------------------------------------
# Probabilistic C-Index (from gustavo's pseudo code)
# E   =>   Vector of continuous experimentally determined values, e.g. EC10.
# s	=>	Scalar representing the pooled standard deviation for E.
# P	=>	Vector containing the predicted rank of E. 
pCIdx_GS <- function(E,s,P) {
  runningSum <- 0
  n <- 0.5 * length(E) * (length(E)-1)
  for (i in 1:(length(E)-1)) {
    for (j in (i+1):length(E)) {
      if (P[i] > P[j]) {
        runningSum <- runningSum + pCIdx_CDF_GS(E[i], E[j], s)
      } else if (P[i] < P[j]) {
        runningSum <- runningSum + pCIdx_CDF_GS(E[j], E[i], s)
      } else if (P[i] == P[j]) {
        runningSum <- runningSum + 0.5
      }
    }
  }
  runningSum/n
}

# ------------------------------------------------------------------------------------------------
# Pooled standard deviation
# R => matrix of replicates. On the columns are the experimental entities, in the rows are the replicates
pooled_sd <- function(R) {
  v <- apply(R, 2, function(x) var(x, na.rm=T))
  n <- apply(R, 2, function(x) sum(!is.na(x)) - 1)
  v <- v[n>0]
  n <- n[n>0]
  sqrt(sum(n * v) / sum(n))
}

# ------------------------------------------------------------------------------------------------
# Test cases: good prediction should be 1

# ---------------------------
# DEMO: good prediction
# ---------------------------

# experimental value
E <- runif(200)

# generated sparse replicates with noise
nRep <- 3
R <- matrix(NA, nrow=nRep, ncol=length(E))
for (i in 1:nRep) {
  R[i,] <- E + runif(length(E), min=-0.1, max=0.1)
  R[i,sample(200, 10)] <- NA
}

# calculated pooled standard deviation
s <- pooled_sd(R)

# good prediction 
P_good <- rank(E)
pCIdx(E,s,P_good)
pCIdx_GS(E,s,P_good)

# random prediction
P_random <- rank(E[sample(200)])
pCIdx(E,s,P_random)
pCIdx_GS(E,s,P_random)

# inverse prediction
P_inverse <- rank(-E)
pCIdx(E,s,P_inverse)
pCIdx_GS(E,s,P_inverse)

# plot predicted versus observed ranking
plot(E, P_good, ylab="P", col='#0000FF55', pch=16, main='probabilistic C-Index (pC)')
points(E, P_random, col='#FF000055', pch=16)
points(E, P_inverse, col='#FFFF0055', pch=16)
label <- paste(c('good', 'random', 'inverse'), ' (pC=',
               formatC(c(pCIdx(E,s,P_good), pCIdx(E,s,P_random), pCIdx(E,s,P_inverse)), digits=2), ")", sep="")
legend("topleft", title="prediction:", label, pch = 16, col=c('#0000FF55', '#FF000055', '#FFFF0055'))

