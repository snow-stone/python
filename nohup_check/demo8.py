#!/bin/env python

import subprocess
import time

#==============================================================================
# list1 : all time dirs updating in time
# list2 : time dirs which are passed to reconstructPar
# list0 : in main() hold time dirs which were reconstructed then removeds. 
#         Thus global varible
#
# proProcess : if file not created. Let's wait and don't exit !
#==============================================================================

def getTimes(fileName, removedList):

    list1 = [line.rstrip('\n') for line in open(fileName)]
    list2 = list(set(list1) - set(removedList))
    
    list2_float = [float(x) for x in list2]
    list2 = [str(x) for x in sorted(list2_float, reverse=False)]
    
    print "all time dirs : ", list1
    list2 =  list2[:-1]
    print 'timeList to reconstruct avoiding the last time step :', list2
    
    string2 = ",".join(list2)

    return list2, string2

def reconstruct(times2reconstruct):
    return_code = subprocess.call("./reconstruct7.sh "+times2reconstruct, shell=True)

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

def preProcess(dataFile):
    import os.path

    return os.path.exists(dataFile)
                    
def process(dataFile, Nb_procs, removedTimeList):

    list2, string2 = getTimes(dataFile, removedTimeList)
    print "got times"
    
    ifNextStep = reconstruct(string2)
    print "reconstruct complete"
    time.sleep(3)

    timeList2Remove = list2
    removeTimesInProcessorDirs(ifNextStep, Nb_procs, timeList2Remove)    
    print "finished removing times in processor directories"
    
    return timeList2Remove
    
def main():
    startTime = time.time()
    dataFileName='userDefinedLog/dataWritingHistory'    
    Nb_procs = 4
    list0 = []
    
    wait4File=5
    while True and time.time()-startTime < 60 :
        time.sleep(2)
        print '\n'
        print '##########################'
        if preProcess(dataFileName):
            list0 = process(dataFileName, Nb_procs, list0) + list0
        else:
            print "No " + dataFileName + " found ! Waiting ..."
            time.sleep(wait4File)
        
main()