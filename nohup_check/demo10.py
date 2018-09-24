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

def getTimes(fileName, removedList, log):

    list1 = [line.rstrip('\n') for line in open(fileName)]
    list2 = list(set(list1) - set(removedList))
    
    list2_float = [float(x) for x in list2]
    list2 = [str(x) for x in sorted(list2_float, reverse=False)]

    log.write("all time dirs : \n")
    log.write(str(list1)+"\n")
    list2 =  list2[:-1]

    log.write("timeList to reconstruct avoiding the last time step :\n")
    log.write(str(list2)+"\n")
    
    string2 = ",".join(list2)

    return list2, string2

def reconstruct(times2reconstruct, log):
    cmd = "./reconstruct7.sh "+times2reconstruct
    return_code = subprocess.call(cmd, shell=True)
    
    log.write(cmd+"\n")

    return return_code


def removeTimesInProcessorDirs(flag, Nb_procs, times2remove, log):
    if not flag :
        for timeI in times2remove:
#            print '\n'
            log.write("\n")
            for i in range(Nb_procs):
                rm_command = 'rm -r processor'+str(i)+'/'+str(timeI)
                return_value = subprocess.call(rm_command, shell=True)
                if not return_value:
#                    print rm_command
                    log.write(rm_command + "\n")
                else:
#                    print rm_command+' failed!'
                    log.write(rm_command+" failed!\n")

def preProcess(dataFile):
    import os.path

    return os.path.exists(dataFile)
                    
def process(dataFile, Nb_procs, removedTimeList, log):

    list2, string2 = getTimes(dataFile, removedTimeList, log)
#    print "got times"
    log.write("got times\n")
    
    ifNextStep = reconstruct(string2, log)
#    print "reconstruct complete"
    log.write("reconstruct complete\n")
    time.sleep(3)

    timeList2Remove = list2
    removeTimesInProcessorDirs(ifNextStep, Nb_procs, timeList2Remove, log)    
#    print "finished removing times in processor directories"
    log.write("finished removing times in processor directories\n")
    
    return timeList2Remove
    
def main():
    import os
    startTime = time.time()
    dataFileName='userDefinedLog/dataWritingHistory'    
    Nb_procs = 4
    list0 = []
    pythonLogFile='log.python_demo9'
    removedTimesAsFile='userDefinedLog/removedTimes'    
    
    if os.path.exists(pythonLogFile):
        os.remove(pythonLogFile)
        print "removing " + pythonLogFile
    else:
        print pythonLogFile + " doesnt exist !"
    
    print "creating " + pythonLogFile + " and appending..."
    pythonLog = open(pythonLogFile,'a')
    print "start writing to logFile : " + pythonLogFile
    
    # need removedTimesAsFile to be blank at the beginning
    removedTimes = open(removedTimesAsFile,'r')
    list0 = [line.rstrip('\n') for line in removedTimes]
    removedTimes.close()
    
    addNewRemovedTimes = open(removedTimesAsFile,'a')
    
    wait4File=5
    while True and time.time()-startTime < 60 :
        time.sleep(2)
#        print '\n'
#        print '##########################'
        pythonLog.write("\n")
        pythonLog.write("##########################\n")
        if preProcess(dataFileName):
            deltaList0 = process(dataFileName, Nb_procs, list0, pythonLog)
            list0 = deltaList0 + list0
            for item in deltaList0:
                addNewRemovedTimes.write(item+"\n")
        else:
            print "No " + dataFileName + " found ! Waiting ..."
            time.sleep(wait4File)
            
    addNewRemovedTimes.close()

main()
