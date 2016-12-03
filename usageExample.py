from strangeness import Strangeness
import argparse

def check_negative_float(value):
    ivalue = float(value)
    if ivalue < 0:
         raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return ivalue

def check_negative_int(value):
    ivalue = int(value)
    if ivalue < 1:
         raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return ivalue

def check_zero_one(value):
    ivalue = float(value)
    if ivalue > 1 or ivalue < 0 :
         raise argparse.ArgumentTypeError("%s is an invalid value. Value should be between 0 and 1" % value)
    return ivalue

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Detects change in unlabeled datasets using martingle property')

    parser.add_argument('filename', help = 'the input csv file, all columns but the first represent the vector values, the first one is the label or ID. Single line header')
    parser.add_argument('threshold', type = check_negative_float, help = 'This value decides the sensitivity of the algorithm. Lesser value causes more detections' )
    parser.add_argument('minQueueLen', type = check_negative_int, help = 'This value decides the minimum number of input values before starting the change detection. Lesser value causes more detections')
    parser.add_argument('epsilon', type = check_zero_one, help = 'This value decides the sensitivity of the algorithm - randomised power martingales')
    parsed = parser.parse_args()

    listTuple = []
    M = 1.0
    L = parsed.threshold
    minInList = parsed.minQueueLen
    epsilon = parsed.epsilon
    #instantiate the class
    strangeness = Strangeness(L,minInList,epsilon)
    print  "label, MartingaleValue"
    header = None 
    with open(parsed.filename,'r') as f:
        for line in f:
            if header != None:
                splitV = line.rstrip().split(',')
                label = splitV[0]
                # this value can be a tuple
                val = [float(x) for x in splitV[1:]]
                #pass the value tuple to get the M value for that tuple
                M = strangeness.getMValue(val)
                print '{},{}'.format(label, str(M))
            else:
                header = True
