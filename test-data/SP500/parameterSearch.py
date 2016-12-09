from subprocess import call
import sys

if __name__ == "__main__":
    inFilename = 'sp500_2007_2016.csv'
    outFilename = 'sp500_2007_2016_mart'
    summary = outFilename + '_summary.csv'
    QueueLen = [ 5, 10, 20, 30 , 50, 100]
    Threshold = [ 3, 5, 10, 15]
    Epsilon  = [ 0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.92, 0.94, 0.95 ]

    with open(summary,"w") as summFile:
        summFile.write('filename,threshold, queueLenght, Epsilon, dataAboveThreshold, totalData\n')
        for q in QueueLen:
            for t in Threshold:
                for e in Epsilon:
                    outF = '{}_{}_{}_{}.csv'.format(outFilename, t,q,e)
                    with open(outF, "w") as outfile:
                        call(["python", "../../usageExample.py",inFilename,str(t),str(q),str(e)], stdout=outfile)
                    call(["Rscript", "plotGraph.R", outF, inFilename, str(t)]) 
                    with open(outF,"r") as inputFile:
                        header = False
                        countAboveThres = 0 
                        lineCount = 0 
                        for line in inputFile:
                            if header == True:
                                values = line.rstrip().split(',')
                                if float(values[1]) >= t:
                                    countAboveThres += 1
                                lineCount += 1
                            else:
                                header = True
                        summFile.write('{},{},{},{},{},{}\n'.format(outF,str(t),str(q),str(e),countAboveThres,lineCount))  

