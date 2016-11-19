
set.seed(345)
numPoints <- 1000
listOfcenters<-c(1,-1,2,3)
dataset<-NULL
for (i in listOfcenters) {
  
  normVals<-cbind(rep(i,numPoints), rnorm(numPoints, i,1))
  rbind(dataset,normVals)->dataset
}

names(dataset)<-c('Label','Value1')
write.csv(dataset, file='martingalesDataWithLabels.csv',row.names = F)
