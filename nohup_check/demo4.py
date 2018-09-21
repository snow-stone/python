#!/bin/env python

import subprocess
import time
#import numpy as np

#dataWritingHistory=np.genfromtxt('userDefinedLog/dataWritingHistory',skip_header=0,delimiter=' ')

#with open('userDefinedLog/dataWritingHistory') as f:
#    content = f.readlines()


def getTimes(fileName):

    timeList = [line.rstrip('\n') for line in open(fileName)]
    print timeList
    
    timeString = ",".join(timeList[:-1]) # omitting the last one
    print timeString

    return timeList, timeString

def reconstruct(times2reconstruct):
    return_code = subprocess.call("./reconstruct4.sh "+times2reconstruct, shell=True)

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
    
    timeList, timeString = getTimes('userDefinedLog/dataWritingHistory')
    print "get times"
    
    ifNextStep = reconstruct(timeString)
    print "reconstruct complete"
    time.sleep(10)

    removeTimesInProcessorDirs(ifNextStep, Nb_procs, timeList)    
    print "finish removing times in processor directories"
    
main()