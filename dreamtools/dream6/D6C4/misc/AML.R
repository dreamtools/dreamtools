ScriptPath='../..'
SubmissionDataPath='../../OriginalSubmissions'
##AML
##AlgorithmList=c('2DhistsSVM', 'acgt', 'admire-lvq', 'BAD', 'bcb', 'biolobe', 'cihc', 'daltons', 'EMMIXCYTOM', 'epd', 'fivebyfive', 'flowBin', 'flowPeakssvm', 'flowType', 'flowType-FeaLect', 'giano6', 'GS', 'jkjg', 'PBSC', 'predictor', 'RandomSpheres', 'rnigroup', 'scrph1', 'si', 'sib-vital-it', 'SORT', 'SPADE', 'team21', 'uqs')
##For nature immunology
##AlgorithmList=c('2DhistsSVM', 'admire-lvq', 'bcb', 'biolobe', 'cihc', 'daltons', 'DREAM-A', 'DREAM-B', 'DREAM-C', 'DREAM-D', 'EMMIXCYTOM', 'fivebyfive', 'flowBin', 'flowPeakssvm', 'flowType', 'flowType-FeaLect', 'jkjg', 'PBSC', 'RandomSpheres', 'scrph1', 'SPCA+GLM', 'SPADE', 'team21', 'uqs')
##For nature methods
AlgorithmList=c('2DhistsSVM', 'admire-lvq', 'bcb', 'biolobe', 'cihc', 'daltons', 'DREAM-A', 'DREAM-B', 'DREAM-C', 'DREAM-D', 'EMMIXCYTOM', 'fivebyfive', 'flowBin', 'flowPeakssvm', 'flowType', 'flowType-FeaLect', 'jkjg', 'PBSC', 'RandomSpheres', 'SPCA+GLM', 'SPADE', 'team21', 'uqs')
Dream=c(0,1,1,1,1,1,1,1,0,1,1,0,0,0,0,1,1,1,0,1,0,1,1,1,1,0,1,1)
##AlgorithmList=AlgorithmList[which(Dream==0)]

##parse the metadata
MetaData <- read.csv('../../Data/AML/AMLTraining.csv',stringsAsFactors=FALSE)
##find the testset samples
TestSetMetaData <- which(is.na(MetaData[,'Label']))
TestSet <- unique(MetaData[TestSetMetaData,'SampleNumber'])
##index of the testset samples
TestSetIndex <- unlist(lapply(TestSet,function(x){which(x==MetaData[,'SampleNumber'])[1]}))

##Extract the labels
Labels=matrix('', length(AlgorithmList), length(TestSetIndex));
for (i in 1:length(AlgorithmList)){
  CSV=read.csv(sprintf('%s/%s/%s-AML.csv',SubmissionDataPath,AlgorithmList[i],AlgorithmList[i]),stringsAsFactors=FALSE)
  Labels[i,] <- CSV[TestSetIndex,'Label']  
}

Labels=t(Labels)

##read the complete metadata
CorrectMetaData <- read.csv('../../Data/AML/AML.csv',stringsAsFactors=FALSE)
CorrectLabels=CorrectMetaData[TestSetIndex,'Label']
CorrectLabels[which(CorrectLabels=='aml')]=1
CorrectLabels[which(CorrectLabels=='normal')]=0
CorrectLabels=as.integer(CorrectLabels)

##construct the labels 1:AML 0:normal
Labels[which(Labels=='AML')]=1
Labels[which(Labels=='aml')]=1
Labels[which(Labels=='normal')]=0
Labels=matrix(as.integer(Labels),dim(Labels))

##calculated sensitivity, specificity, and F-measure
sens=vector()
acc=vector()
spec=vector()
fmeasure <- vector()
recall <- vector()
precision<-vector()
##cil=vector()
##cih=vector()
for (i in 1:length(AlgorithmList)){
  neg <- which(CorrectLabels==0)
  TN <- length(which(CorrectLabels[neg]==Labels[neg,i]))
  FP <- length(which(CorrectLabels[neg]!=Labels[neg,i]))
  pos <- which(CorrectLabels!=0)
  TP <- length(which(CorrectLabels[pos]==Labels[pos,i]))
  FN <- length(which(CorrectLabels[pos]!=Labels[pos,i]))
  acc[i] <- (TP+TN)/(TP+TN+FP+FN)
  sens[i] <- TP/(TP+FP)
  spec[i] <- TP/(TP+FN)
  fmeasure[i] <- sens[i]*spec[i]*2/(sens[i]+spec[i])
  recall[i] <- TP / 20
  precision[i] <-TP /20
  ##temp=bootStrap(Labels[,i], CorrectLabels, 1000)
  ##cil[i]=temp[1]
  ##cih[i]=temp[2]
}

##create the latex table
Ndigits=2
mat=cbind(format(sens, digits=Ndigits), format(spec, digits=Ndigits), format(acc, digits=Ndigits), format(fmeasure, digits=Ndigits))
rownames(mat) <- AlgorithmList
##colnames(mat) <- c('Sensitivity', 'Specificity', 'Accuracy', 'Fmeasure', 'Fmeasure CI')
colnames(mat) <- c('Sensitivity', 'Specificity', 'Accuracy', 'Fmeasure')

library(xtable)
print(xtable(mat, label='t2AML', caption='Challenge 1'), caption.placement='top')

##create the Fmeasure barplots
postscript('../../DisplayItems/AMLFmeasures.eps', horizontal=FALSE)
par(mfrow=c(2,1))
index=order(fmeasure,decreasing=TRUE)
index2 <- which(fmeasure[index]==max(fmeasure))
index[index2] <- index[index2][sort(AlgorithmList[index[index2]], index.return=TRUE, decreasing=FALSE)$ix]
bp=barplot(fmeasure[index]-0.4, names.arg=NA, offset=0.4, xlab='Algorithms', ylab='F-measures', xaxt='n', bty='l')
text(bp+0.1, par("usr")[3]+max(fmeasure-0.4)/40, srt = 90, adj = 0, labels = AlgorithmList[index], xpd = TRUE)
axis(1, at=bp, labels=FALSE)
dev.off()

##create the misclassification barplots
MisClassifications <- Labels*0;
for (j in 1:dim(Labels)[2]){
  MisClassifications[,j]=as.integer(Labels[,j]!=CorrectLabels)
}
##MisClassifications=MisClassifications/dim(MisClassifications)[2]
postscript('../../DisplayItems/AMLMisClassifications.eps', horizontal=FALSE)
par(mar=c(6,6,4,2))
par(mfrow=c(3,1))
bp=barplot(rowSums(MisClassifications), col=CorrectLabels+1, xlab='SampleNumber', ylab='Mis-classifications', axes=FALSE,cex.lab=2)
legend(1, max(rowSums(MisClassifications)), legend=c('Normal', 'AML'), col=1:2, lwd=4,box.col=0,cex=2)
axis(2,cex.axis=2)
axis(1, at=bp[c(2,100,which.max(rowSums(MisClassifications)))], labels=c(181,284,340),cex.axis=2)
par(mgp=c(4,1,0))
title(sub='(A) Mis-classifications',cex.sub=2)
dev.off()
