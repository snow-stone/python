#!/bin/env python

import commands, os
import sys
import time


def removeLogFile(logFileName):
    # make sure logFile is cleaned before proceed
    # no fatal exception, no return value
    if os.path.exists(logFileName):
        try:
            os.remove(logFileName)
        except OSError as e:
            print "logFile exist with\n"
            print ("Error: %s - %s." % (e.filename, e.strerror))
    else:
        print "logFile doesnt exist\n"
        print "pre-check passes, continue now...\n"

def submitJob(cmd, slurmFile):
    # submit
    if os.path.exists(slurmFile):
        print "submitting job using : %s" % cmd
        status, jobnum = commands.getstatusoutput(cmd)
        return status, jobnum.split()[-1]
    else:
        print "FATAL ERROR!"
        print "file %s doesnt exits" % slurmFile
        return (1, '0000')

def ifScanErrFileExist(errFile):
    if os.path.exists(errFile):
        return True
    else:
        return False

def watchJob(queue, jobnum, simuLogFile, defautWallTime):
    errFile = queue + '_mpi.' + jobnum + '.err'
    scanPeriod = 5

    submittedTime = time.time()
    while time.time() - submittedTime < defautWallTime:
        if ifScanErrFileExist(errFile) :
            print "%s found" % errFile
            if "mpirun: command not found" in open(errFile).read():
                print "mpirun: command not found !"
                print "=>break here"
                print "=>need OpenFOAM env to be charged !\n"
                break
            else:
                time.sleep(5)
                continue
        else:
            time.sleep(scanPeriod)
            print "waiting for %s to be created..." % errFile
        
        """    
        # suspect ORTE error for 1h
        # print "suspectting ORTE error..."    
        if os.path.exists(simuLogFile):
            print "%s found" % simuLogFile
            if "ORTE" in open(simuLogFile).read():
                print "ORTE error found !\n"
                print "break here \n"
                break
            else:
                time.sleep(5)
                continue
        else:
            time.sleep(60)
            print "waiting for %s to be created..." % simuLogFile
            # maybe queued for 1h...
            # maybe ORTE
        """

def squeueMonitor():
    import commands
    cmd = "squeue -u hluo -l"
    
    status, jobs = commands.getstatusoutput(cmd)
    
    """
    ['Mon Sep 24 09:20:57 2018',
     '             JOBID PARTITION     NAME     USER    STATE       TIME TIME_LIMI  NODES NODELIST(REASON)',
     '           5184520      allc 480bN_te     hluo  RUNNING       7:00     15:00     18 n[3574-3591]',
     '           5184518      allc 480bN_te     hluo  RUNNING       7:46     15:00     18 n[3538-3555]',
     '           5184516      allc 480bN_te     hluo  RUNNING       8:17     15:00     18 n[3430-3447]']
    """    
    
    listJobs = jobs.split('\n')
    
    return listJobs[2:]

def getStatus(listJobs,jobID):
    for job in listJobs:
        if jobID == job.split()[0]:
            print 'Job ' + jobID + ' is now ' + job.split()[4] + ' for ' + job.split()[-1]
    return job.split()[4], time.time()

def main():
    slurmFile = sys.argv[1]
    logFile = sys.argv[2]
    queue = sys.argv[3] # bdw
    
    defautWallTime=60*60
    
    removeLogFile(logFile)
    cmd = "sbatch %s" % slurmFile
    status, jobID = submitJob(cmd, slurmFile)
    
    if status == 0:
        print "Job is submited with jobID : %s" % jobID
#        watchJob(queue, jobnum, logFile, 60*60)
        submittedTime = time.time()
        monitorFlag = True
        while time.time() - submittedTime < defautWallTime:
            time.sleep(2)
            currentJobList = squeueMonitor()
            state, timeOfState = getStatus(currentJobList, jobID)
            if state == 'RUNNING':
                monitorFlag = False
                timeOfRunning = timeOfState
                print "job %s states now running, break !!" % jobID
                break
            elif state == 'PENDING' :
                monitorFlag = True
            else :
                print "Registering state other than RUNNING and PENDING : " + state + "@" + timeOfState
            print "elapsed time "+str(time.time() - submittedTime)
            
        if monitorFlag :
            print "Job didnt start RUNNING after " + str(defautWallTime)
        else :
            print "Job start RUNNING atter " + str(timeOfRunning - submittedTime)
    else:
        print "Error when submitting\n"


main()
