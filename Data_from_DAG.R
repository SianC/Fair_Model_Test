#Import required libraries
library(RGenData)
library(readxl)
library(gendata)
library(mvtnorm)
library(data.table)
library(MASS)
library(fairness)
library(devtools)
library(dagitty)
library(lavaan)
library(lhs)
library(matrixcalc)

#Set Seed
set.seed(0)

#Function Needed Later
################################################################################################################
Factor.Analysis <- function(Data, Corr.Matrix = FALSE, Max.Iter = 50, N.Factors = 0)
{
  Data <- as.matrix(Data)
  k <- dim(Data)[2]
  if (N.Factors == 0) N.Factors <- k
  if (!Corr.Matrix) Cor.Matrix <- cor(Data)
  else Cor.Matrix <- Data
  Criterion <- .001
  Old.H2 <- rep(99, k)
  H2 <- rep(0, k)
  Change <- 1
  Iter <- 0
  Factor.Loadings <- matrix(nrow = k, ncol = N.Factors)
  while ((Change >= Criterion) & (Iter < Max.Iter))
  {
    Iter <- Iter + 1
    Eig <- eigen(Cor.Matrix)
    L <- sqrt(Eig$values[1:N.Factors])
    for (i in 1:N.Factors)
      Factor.Loadings[,i] <- Eig$vectors[,i] * L[i]
    for (i in 1:k)
      H2[i] <- sum(Factor.Loadings[i,] * Factor.Loadings[i,])
    Change <- max(abs(Old.H2 - H2))
    Old.H2 <- H2
    diag(Cor.Matrix) <- H2
  }
  if (N.Factors == k) N.Factors <- sum(Eig$values > 1)
  return(list(loadings = Factor.Loadings[,1:N.Factors], factors = N.Factors))
}
#################################################################################################################
####################### Sampling  ###############################################################
################################################################################################################


combinations <- expand.grid(seq(0.1, 0.3, by = 0.1),
                            seq(0.1, 0.3, by = 0.1),
                            seq(0.1, 0.3, by = 0.1), 
                            seq(0.1, 0.3, by = 0.1),
                            seq(0.1, 0.3, by = 0.1),
                            seq(0.1, 0.3, by = 0.1)) 

A <- as.matrix(combinations)
print(A)
options = sample(1 : 4096, size = 100, replace = F) # I don't want to make loads
################################################################################################################
########################### LOOP ###############################################################################
################################################################################################################



for (p in options) {
  
  ###########################################################################################################
  ####################### SET WEIGHTS ##########################################################################
  #############################################################################################################
  weights = A[p,]
  i = 0
  a <- weights[1] 
  b <- weights[2] 
  c <- weights[3] 
  d <- weights[4] 
  e <- weights[5] 
  f <- weights[6]
  #################################################################################################################
  ##########################       DAG    CHANGES        ###########################################################
  #################################################################################################################
  
  ddaagg <- dagitty(sprintf('dag{
               A [pos="0.5,1"]
               B [pos="0,2"]
               C [pos="1,2"]
               D [pos="0.5,3"]
               
               A -> B [beta = %f]
               A -> C [beta = %f]
               A -> D [beta = %f]
               B -> D [beta = %f]
               B -> C [beta = %f]
               C -> D [beta = %f]}', a, b, c, d, e, f)
               
  
               
               )
  plot(ddaagg) 
  
  covg <- impliedCovarianceMatrix(ddaagg)
  covg = round(covg, 10)
  corr <- cov2cor(covg)
  
  if (is.positive.semi.definite(covg, tol=1e-8)){
  #Number of data samples create
    sample_size <- 10000
    semi_pos_def <- rbind(semi_pos_def, A[p,])
    ##################################################################################################################
    ############################# INITIALISE VARIABLES ##############################################################
    #################################################################################################################
    
    N <- sample_size #dim(supplied.data)[1] # Number of cases
    k <- dim(corr)[2] # dim(supplied.data)[2] # Number of variables
    Data <- matrix(0, nrow = N, ncol = k) # Matrix to store the simulated data
    Distributions <- matrix(0, nrow = N, ncol = k) # Matrix to store each variable’s score distribution
    Iteration <- 0 # Iteration counter
    Best.RMSR <- 1 # Lowest RMSR correlation
    Trials.Without.Improvement <- 0 # Trial counter
    
    N.Factors = 0 
    Max.Trials = 5 # If you don't improve after X stop
    Initial.Multiplier = 1 
    
    ################################################################################################################
    ##################### DISTRIBUTIONS ############################################################################
    ################################################################################################################
    
    Distributions[,1] <- sort(rbinorm(N, 5, 0.5)) 
    Distributions[,2] <- sort(rbinom(N, 1, 0.3))
    Distributions[,3] <- sort(rbinorm(N, 3, 0.3)) 
    Distributions[,4] <- sort(rbinom(N, 1, 0.4)) 

    
    ################################################################################################################
    ######################  CREATE DATA ############################################################################
    ################################################################################################################
    
    #Read in correlation matrix
    ################################################################################################################
    #supplied.corr <- read.csv('PhD/Third Year/Survival_Analysis/cor_f_DAG.csv')
    Target.Corr <- corr #Correlation matrix
    Intermediate.Corr <- Target.Corr
    
    
    ###Temp
    #supplied.corr <- corr2
    ################################################################################################################
    
    
    if (N.Factors == 0)
    {
      Eigenvalues.Observed <- eigen(Intermediate.Corr)$values
      Eigenvalues.Random <- matrix(0, nrow = 100, ncol = k)
      Random.Data <- matrix(0, nrow = N, ncol = k)
      for (i in 1:100)
      {
        for (j in 1:k)
          Random.Data[,j] <- sample(Distributions[,j], size = N, replace = TRUE)
        Eigenvalues.Random[i,] <- eigen(cor(Random.Data,use = "complete.obs"))$values #Issues when a column has all 0s
      }
      Eigenvalues.Random <- apply(Eigenvalues.Random, 2, mean) # calculate mean eigenvalue for each factor
      N.Factors <- max(1, sum(Eigenvalues.Observed > Eigenvalues.Random))
    }
    
    
    Shared.Comp <- matrix(rnorm(N * N.Factors, 0, 1), nrow = N, ncol = N.Factors)
    Unique.Comp <- matrix(rnorm(N * k, 0, 1), nrow = N, ncol = k)
    Shared.Load <- matrix(0, nrow = k, ncol = N.Factors)
    Unique.Load <- matrix(0, nrow = k, ncol = 1)
    
    
    
    #Loop
    while (Trials.Without.Improvement < Max.Trials)
    {
      Iteration <- Iteration + 1
      Fact.Anal <- Factor.Analysis(Intermediate.Corr, Corr.Matrix = TRUE, N.Factors = N.Factors)
      if (N.Factors == 1) Shared.Load[,1] <- Fact.Anal$loadings
      else Shared.Load <- Fact.Anal$loadings
      Shared.Load[Shared.Load > 1] <- 1 # Set between 1 and -1
      Shared.Load[Shared.Load < -1] <- -1
      if (Shared.Load[1,1] < 0) Shared.Load <- Shared.Load * -1
      Shared.Load.sq <- Shared.Load * Shared.Load
      for (i in 1:k)
        if (sum(Shared.Load.sq[i,]) < 1) Unique.Load[i,1] <- (1 - sum(Shared.Load.sq[i,]))
      else Unique.Load[i,1] <- 0
      Unique.Load <- sqrt(Unique.Load) #Can't minus a sqr root
      for (i in 1:k)
        Data[,i] <- (Shared.Comp %*% t(Shared.Load))[,i] + Unique.Comp[,i] * Unique.Load[i,1]
      
      
      for (i in 1:k)
      {
        Data <- Data[sort.list(Data[,i]),]
        Data[,i] <- Distributions[,i]
      }
      
      Reproduced.Corr <- cor(Data)
      Residual.Corr <- Target.Corr - Reproduced.Corr
      RMSR <- sqrt(sum(Residual.Corr[lower.tri(Residual.Corr)] * Residual.Corr[lower.tri(Residual.Corr)]) /
                     (.5 * (k * k - k)))
      #break
      #Stat.Par <- stat_par_fn(Data, V1, V2)
      if (RMSR < Best.RMSR) #& (abs(Target.Stat.Par-Stat.Par) < abs(Target.Stat.Par-Best.Stat.Par)))#Update if better
      {
        Best.RMSR <- RMSR
        Best.Corr <- Intermediate.Corr
        Best.Res <- Residual.Corr
        Intermediate.Corr <- Intermediate.Corr + Initial.Multiplier * Residual.Corr
        #Best.Stat.Par <- Stat.Par
        Trials.Without.Improvement <- 0
      }
      else #Continue ifnot better
      {
        Trials.Without.Improvement <- Trials.Without.Improvement + 1
        Current.Multiplier <- Initial.Multiplier * .5 ^ Trials.Without.Improvement
        Intermediate.Corr <- Best.Corr + Current.Multiplier * Best.Res
      }
    }
    
    #Calculate the data set with the lowest RMSR correlation
    Fact.Anal <- Factor.Analysis(Best.Corr, Corr.Matrix = TRUE, N.Factors = N.Factors)
    
    if (N.Factors == 1) {Shared.Load[,1] <- Fact.Anal$loadings
    } else {Shared.Load <- Fact.Anal$loadings}
    
    Shared.Load[Shared.Load > 1] <- 1
    Shared.Load[Shared.Load < -1] <- -1
    if (Shared.Load[1,1] < 0) Shared.Load <- Shared.Load * -1
    Shared.Load.sq <- Shared.Load * Shared.Load
    for (i in 1:k)
      if (sum(Shared.Load.sq[i,]) < 1) {Unique.Load[i,1] <- (1 - sum(Shared.Load.sq[i,]))
      } else {Unique.Load[i,1] <- 0}
    Unique.Load <- sqrt(Unique.Load)
    for (i in 1:k)
      Data[,i] <- (Shared.Comp %*% t(Shared.Load))[,i] + Unique.Comp[,i] * Unique.Load[i,1]
    Data <- apply(Data, 2, scale) # standardizes each variable in the matrix
    for (i in 1:k)
    {
      Data <- Data[sort.list(Data[,i]),]
      Data[,i] <- Distributions[,i]
    }
    
    
    #Report results
    Iteration <- Iteration - Max.Trials
    #cat("\nN =",N,", k =",k,",",Iteration,"Iterations,",N.Factors,"Factors, RMSR r =",round(Best.RMSR,3),"\n")
    
    ##############################################################################################################
    ################################ SAVE DATA ##################################################################
    ##############################################################################################################
    df <- data.frame(Data)
    
    
    filename <- paste0("data_", p, ".csv")
    write.csv(Data, file=sprintf('Path/data_%d.csv', p))
    
  } else{
    print(sprintf("The following run did not create a positive semidefinite covariance matrix - %d", p))
  }
}




