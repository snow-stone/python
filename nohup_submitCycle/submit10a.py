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

def ifJobFoundInSqueue(listJobs,jobID):
    flag = False
    for job in listJobs:
        if jobID == job.split()[0]:
            flag = True
        else:
            continue
    return flag

def getStatus(listJobs,jobID):
    for job in listJobs:
        if jobID == job.split()[0]:
            print 'Job ' + jobID + ' is now ' + job.split()[4] + ' for ' + job.split()[-1]
            return job.split()[4], time.time()
#        else:
#            print "Job %s is no longer in squeue !!" % jobID   
#            # but... in main it looks like... this must have return value
#            # like submitJob? Make a defaut ???

def returnJobStatus(jobID, submittedTime, ifAlwaysPending):
    currentJobList = squeueMonitor()
    
    if ifJobFoundInSqueue(currentJobList, jobID):
        state, timeOfState = getStatus(currentJobList, jobID)
        timeElapsedFromSubmission = timeOfState - submittedTime
        if state == 'RUNNING':
            ifAlwaysPending = False
#            print "job %s states now running, break !!" % jobID
#                    break
            return state, timeElapsedFromSubmission, ifAlwaysPending
        elif state == 'PENDING' :
            ifAlwaysPending = True
            return state, timeElapsedFromSubmission, ifAlwaysPending
        else :
            return "OTHER", timeElapsedFromSubmission, ifAlwaysPending
#        print "elapsed time "+str(time.time() - submittedTime)
    else :
        print "job " + jobID + " is no longer in queue..."
        return "NotInQueue", time.time() - submittedTime, ifAlwaysPending
                
def simu_watchDog(cmd, status, jobID, wallTime, simLogFile):
    import subprocess
    
    if status == 0:
        print "Job is submited with jobID : %s" % jobID
#        watchJob(queue, jobnum, simLogFile, 60*60)        turn off for now
        submittedTime = time.time()
        pendingFlag = True
    
        while time.time() - submittedTime < wallTime:
            interval=10
            print "waiting here for status check every %f seconds", interval
            time.sleep(interval) # 30
            status_of_check, time_of_check, pendingFlag = returnJobStatus(jobID, submittedTime)
            
            print "job " + jobID + status_of_check + " @%s seconds" % time_of_check            
            if status_of_check == "RUNNING":
                #start menage !!
                time.sleep(1)
            elif status_of_check == "PENDING":
                #hold
                time.sleep(1)
            elif status_of_check == "OTHER":
                print "Registering state other than RUNNING and PENDING : " + status_of_check + "@%s seconds" % time_of_check
            elif status_of_check == "NotInQueue":
                print "suspecting job has finished"
                #check simLogFile
                if "Finalising parallel run" in subprocess.check_output(['tail', '-1', simLogFile]):
                    print "simu has finished"
                    return 0
                else :
                    print "simu hasnt finished within setting time. Re-adjust !"
        
        print "Wall time passed..."
        print "*******************"
        if pendingFlag :
            print "Job didnt start RUNNING after %s seconds" + str(wallTime)

    else:
        print "Error happens when submitting : %s" % cmd             
                
def main():

    slurmFile = sys.argv[1]
    simLogFile = sys.argv[2]
#    queue = sys.argv[3] # bdw                              turn off for now 
    
    wallTime=60*60
    
    removeLogFile(simLogFile)
    cmd = "sbatch %s" % slurmFile
    status, jobID = submitJob(cmd, slurmFile)
    
    returnValue = simu_watchDog(cmd, status, jobID, wallTime, simLogFile)

    if returnValue == 0:
        print "last simu successful!"
        #modify the controlDict
        #if endTime not yet enough...
        #Run another simu by return a value as output of function
        #end this python process by return 0
        time.sleep(1)
    else:
        print "Need to debug for simu ..."

main()
