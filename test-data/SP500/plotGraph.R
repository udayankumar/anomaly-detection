options(echo=TRUE) # if you want see commands in output file
args <- commandArgs(trailingOnly = TRUE)
print(args)

library(ggplot2)
read.csv(args[1])->orgFile
read.csv(args[2])->martFile

cutoff<-as.numeric(args[3])
cutoff

strsplit(args[1],'_')->nameSplit

paste('graph_',nameSplit[[1]][2],'_',nameSplit[[1]][3],'_',nameSplit[[1]][5],'_',nameSplit[[1]][6],'_',nameSplit[[1]][7],'.pdf',sep="")->graphName

merge(orgFile,martFile)->m
as.Date(m$label,"%m/%d/%y")->m$date
ggplot(m,aes(x=date,y=Open, color =ifelse( m$MartingaleValue >= cutoff,"green","orange"),size=ifelse(m$MartingaleValue >= cutoff,5,1))) + geom_jitter(alpha=1/2 ) + theme(legend.position="none")
ggsave(graphName)
