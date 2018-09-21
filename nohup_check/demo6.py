#!/bin/env python

import subprocess
import time
#import numpy as np

#dataWritingHistory=np.genfromtxt('userDefinedLog/dataWritingHistory',skip_header=0,delimiter=' ')

#with open('userDefinedLog/dataWritingHistory') as f:
#    content = f.readlines()


def getTimes(fileName):
    removedList=['0.001']

    list1 = [line.rstrip('\n') for line in open(fileName)]
    list2 = list(set(list1) - set(removedList))
    
    list2_float = [float(x) for x in list2]
    list2 = [str(x) for x in sorted(list2_float, reverse=False)]
    
    print 'timeList to reconstruct :', list2

    list2 =  list2[:-1]
    print 'timeList to reconstruct :', list2
    
    string2 = ",".join(list2)
#    print timeString2Remove

    return list2, string2

def reconstruct(times2reconstruct):
    return_code = subprocess.call("./reconstruct6.sh "+times2reconstruct, shell=True)

    return return_code


def removeTimesInProcessorDirs(flag, Nb_procs, times2remove):
    if not flag :
        for timeI in times2remove:
            print '\n'
            for i in range(Nb_procs):
                rm_command = 'rm -r processor'+str(i)+'/'+str(timeI)
                return_value = subprocess.call(rm_command, shell=True)
                if not return_value:
                    print rm_command
                else:
                    print rm_command+' failed!'
    #        if return_value :
    #            continue
                    
def main():
    Nb_procs=4
#    removedTimeList=[]    
    
    timeList2reconstruct, timeString2reconstruct = getTimes('userDefinedLog/dataWritingHistory')
    print "get times"
    
    ifNextStep = reconstruct(timeString2reconstruct)
    print "reconstruct complete"
    time.sleep(10)

    timeList2Remove = timeList2reconstruct
    removeTimesInProcessorDirs(ifNextStep, Nb_procs, timeList2Remove)    
    print "finish removing times in processor directories"
    
main()