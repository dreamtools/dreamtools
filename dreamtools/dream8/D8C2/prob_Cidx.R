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
# Test cases: good prediction should be 1

# ---------------------------
# DEMO: good prediction
# ---------------------------
# E <- runif(200)
# s <- sd(E)
# P <- rank(E)
# pCIdx(E,s,P)
# pCIdx_GS(E,s,P)

# ---------------------------
# DEMO: random prediction
# ---------------------------
# E <- runif(200)
# s <- sd(E)
# P <- rank(E[sample(200)])
# pCIdx(E,s,P)
# pCIdx_GS(E,s,P)

# ---------------------------
# DEMO: inverse prediction
# ---------------------------
# E <- runif(200)
# s <- sd(E)
# P <- rank(-E)
# pCIdx(E,s,P)
# pCIdx_GS(E,s,P)
