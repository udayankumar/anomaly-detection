import math

class Strangeness(object):
    def __init__(self,threshold, minQueue, epsilon):
        self.M = 1.0
        self.threshold = threshold
        self.minQueue = minQueue
        self.epsilon = epsilon
        self.listTuple = []

    def __clusterMean (self, listTuple, singleTuple):
        if len(listTuple) == 0:
            return singleTuple
        dimensions = len(singleTuple)
        numTuples = len(listTuple) + 1

        sumArray = [0] * dimensions
        #sum of the listTuple
        for aTuple in listTuple:
            #TODO: add a try except for the error case when dimensions do not match
            for i in xrange(0,dimensions):
                sumArray[i] += aTuple[i]

        #adding the singleTuple
        for i in xrange(0,dimensions):
            sumArray[i] += singleTuple[i]

        meanArray = [value/numTuples for value in sumArray]
        return meanArray

    def __euclideanDistance(self,p1,p2):
        return sum((x-y)**2 for (x,y) in zip(p1,p2))**(0.5)

    def __calStrangeness(self, listTuple, singleTuple):
        clusterPoint = self.__clusterMean(listTuple, singleTuple)
        strangeness = [self.__euclideanDistance(point, clusterPoint) for point in listTuple]
        #adding Z_n
        ZnStrangeness = self.__euclideanDistance(singleTuple, clusterPoint)
        return [strangeness, ZnStrangeness]

    def __calPValue(self,listTuple, singleTuple, theta):
        [strangenessTuple, ZnStrangeness] = self.__calStrangeness(listTuple, singleTuple)
        siGreater = sum([int(point > ZnStrangeness) for point in strangenessTuple])
        #adding 1 for the case Zn = Zn
        siEqual = sum([int(point == ZnStrangeness) for point in strangenessTuple]) + 1
        return (float(siGreater) + theta * float(siEqual))/(len(listTuple) + 1)

    def getMValue(self,singleVal):
        if len(self.listTuple) > self.minQueue and self.M < self.threshold:
            p = self.__calPValue(self.listTuple, singleVal, 0.82)
            self.M *= self.epsilon * p**(self.epsilon - 1)
        elif self.M >= self.threshold:
            self.listTuple = []
            self.M = 1.0
        self.listTuple.append(singleVal)
        return self.M
