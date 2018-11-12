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
            print "logFile exist, removing with\n"
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

def squeueMonitor():
    import commands
#    cmd = "squeue -u hluo -l"
    cmd = "squeue -u $USER -l"
    
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

def getStateAndTime(listJobs,jobID):
    for job in listJobs:
        if jobID == job.split()[0]:
#            print 'Job ' + jobID + ' is now ' + job.split()[4] + ' for ' + job.split()[-1]
            return job.split()[4], time.time()
#        else:
#            print "Job %s is no longer in squeue !!" % jobID   
#            # but... in main it looks like... this must have return value
#            # like submitJob? Make a defaut ???

def returnJobStatus(jobID, submittedTime, hasBeenRunningOnce):
    currentJobList = squeueMonitor()
    
    if ifJobFoundInSqueue(currentJobList, jobID):
        state, timeOfState = getStateAndTime(currentJobList, jobID)
        timeElapsedFromSubmission = timeOfState - submittedTime
        if state == 'RUNNING':
            hasBeenRunningOnce = True
            return state, timeElapsedFromSubmission, hasBeenRunningOnce
        elif state == 'PENDING' :
            hasBeenRunningOnce = False
            return state, timeElapsedFromSubmission, hasBeenRunningOnce
        else :
            return "OTHER", timeElapsedFromSubmission, hasBeenRunningOnce
    else :
        return "NotInQueue", time.time() - submittedTime, hasBeenRunningOnce
                
def simu_watchDog(cmd, status, jobID, wallTime, simuLogFile):
    import subprocess
    
    if status == 0:
        print "Job is submited with jobID : %s" % jobID
        submittedTime = time.time()
        hasBeenRunningOnce = False
    
        print "via squeue, status check :\n"
        while time.time() - submittedTime < wallTime:
            interval=10
            time.sleep(interval)
            print "status check every %.2f seconds" % interval
            status_of_check, time_of_check, hasBeenRunningOnce = returnJobStatus(jobID, submittedTime, hasBeenRunningOnce)
            
            print "job %s %s @%.2f seconds" % (jobID, status_of_check, time_of_check)           
            if status_of_check == "RUNNING":
                #start menage !!
                time.sleep(1)
            elif status_of_check == "PENDING":
                #hold
                time.sleep(1)
            elif status_of_check == "OTHER":
                print "Registering state other than RUNNING and PENDING : " + status_of_check + " @%.2f seconds" % time_of_check
            elif status_of_check == "NotInQueue":
                if os.path.exists(simuLogFile):          #TODO need to remove simuLogFile before running this script
                    print "%s found" % simuLogFile
                    print "suspecting job has finished"
                    
                    if "Finalising parallel run" in subprocess.check_output(['tail', '-1', simuLogFile]):
                        print "Confirmed : simu has finished"
                        return 0
                    else :
                        print "simu hasnt finished. Rescanning..."
                        print "checking %s" % simuLogFile
                        if "ORTE" in open(simuLogFile).read():
                            print "Confirmed : ORTE error found !\n"
                            print "break here \n"
                            return 2
                        queue = 'bdw'
                        errFile = queue + '_mpi.' + jobID + '.err'
                        if os.path.exists(errFile):
                            print "%s found" % errFile
                            if "mpirun: command not found" in open(errFile).read():
                                print "Confirmed : mpirun: command not found !"
                                print "=>need OpenFOAM env to be charged !\n"
                                return 3
                            elif "DUE TO TIME LIMIT" in open(errFile).read():
                                print "Confirmed : CANCELLED DUE TO TIME LIMIT"
                                print "=>Ask for more time when submitting !\n"
                                return 4
                        else:
                            print "warning : %s not found" % errFile
                else:
                    wait4SimuLogFile=50
                    time.sleep(wait4SimuLogFile)
                    print "warning : %s not found" % simuLogFile
                    print "waiting %s seconds for %s to be created..." % (wait4SimuLogFile+simuLogFile, simuLogFile)
        
        print "Wall time hit......"
        print "*******************"
        if hasBeenRunningOnce :
            print "By checking : Job %s has been in state RUNNING" % jobID
        else:
            print "By checking : Job %s didnt start RUNNING after %.2f seconds" % (jobID, str(wallTime))
            print "              Though this is only a record by checking squeue from time to time"

    else:
        print "Confirmed : Error happens when submitting : %s" % cmd
        print "            Check #SBATCH commands"
        return 1             
                
def tryJob(job_number):

    #import controlDict4Continue6a as cC6a

    #slurmFile = sys.argv[1]
    #simLogFile = sys.argv[2]
#    queue = sys.argv[3] # bdw                              turn off for now
 
#    slurmFile = '480bB_test-0'
#    simLogFile = 'logSimulation0.core480'

    simuLogFile = "logSimulation_"+str(job_number)
    removeLogFile(simuLogFile)
    
    slurmFile   = "bdw"#-"+str(job_number)
    with open(slurmFile,'w') as sf:
        sf.write("#!/bin/bash\n")
        sf.write("#SBATCH --nodes=18\n")
        sf.write("#SBATCH --ntasks-per-node=28\n")
        sf.write("#SBATCH --ntasks=480\n")
        sf.write("#SBATCH --cpus-per-task=1\n")
        sf.write("#SBATCH --time=00:15:00\n")      # min is the smallest unit here
        sf.write("#SBATCH -C %s\n" % "BDW28")
        sf.write("#SBATCH --mem=50GB\n")
        sf.write("#SBATCH --output=bdw_mpi.%j.out\n")
        sf.write("#SBATCH --error=bdw_mpi.%j.err")
        sf.write("\n")
        sf.write("set -e\n")
        sf.write("ulimit -s unlimited\n")
        sf.write("mpirun -n $SLURM_NTASKS nonNewtonianIcoFoamPS_profiling1 -parallel > %s\n" % simuLogFile)
    sf.close()
#    sys.exit("I'm here")

#    slurmFile = " \
#                  --job-name=TN_bdw \
#                  --nodes=18 \
#                  --ntasks-per-node=28 \
#                  --ntasks=480 \
#                  --cpus-per-task=1 \
#                  --time=00:10:00 \
#                  -C BDW28 \
#                  --mem=50GB \
#                  --output=bdw_mpi.%j.out \
#                  --error=bdw_mpi.%j.err \
#                  \
#                  set -e \
#                  ulimit -s unlimited \
#                  mpirun -n $SLURM_NTASKS nonNewtonianIcoFoamPS_profiling1 -parallel > %s " % simuLogFile
    wallTime=60*60
    
    cmd = "sbatch %s" % slurmFile
    status, jobID = submitJob(cmd, slurmFile)
    
    returnValue = simu_watchDog(cmd, status, jobID, wallTime, simuLogFile)

    return returnValue
"""
    if returnValue == 0:
        print "last simu successful!"
        cC6a.main(interval=0.002)
        #modify the controlDict
        #if endTime not yet enough...
        #Run another simu by return a value as output of function
        #end this python process by return 0
        time.sleep(1)
    else:
        print "Need to debug for simu ..."
"""

def RunJobs(pickUpFromJob, nb_jobs, physical_time_interval, endTimeWall):
    import controlDict4Continue6d as controlDict_editor

    print "Start RunJobs =================\n"
    currentJobNb = pickUpFromJob + 1
    print "Global job number : " + str(currentJobNb)
    
    for i in range(nb_jobs):
        # counting from 1 to nb_jobs
        # other than    0 to nb_jobs-1
        print "Trying job number " + str(i+1) + " of " + str(nb_jobs) + " jobs in this particular submission"
        ifHittingWall, startTime, endTime = controlDict_editor.check(endTimeWall)
        if ifHittingWall == 0 or ifHittingWall == 1:
            if ifHittingWall == 1:
                print "Attention : job endTime == endTimeWall"
            returnFromCurrentJob = tryJob(i+currentJobNb)
            if returnFromCurrentJob == 0:
                if controlDict_editor.update(physical_time_interval, startTime, endTime):
                    continue
                else:
                    print "Error when updating controlDict => break"
                    break
            else :
                print "Failed job number " + str(i+1) + " of " + str(nb_jobs) + " jobs in this particular submission"
                if returnFromCurrentJob == 1:
                    print "Error 1 => break"
                    break
                elif returnFromCurrentJob == 2:
                    print "Error 2. Wait for re-submission..."
                    timeStamp4Resubmission = time.time()
                    while time.time() - timeStamp4Resubmission < 60 * 60 * 3:
                        time.sleep(60*15)
                        returnFromCurrentJob = tryJob(i+currentJobNb)
                        if returnFromCurrentJob == 0:
                            print "re-submission succeed"
                            break
                        else:
                            print "re-submission failed with Error %s" % returnFromCurrentJob
                elif returnFromCurrentJob == 3:
                    print "Error 3 => break" #HINT tested already
                    break
                elif returnFromCurrentJob == 4:
                    print "Error 4 => break" #TOBE tested
                    break
                else :
                    print "Other Error => break" # like exceeded quota. Blocked
                    break
        else :
            print "Hitting endTimeWall : " + str(endTimeWall) + ", thus omitting job nubmer " + str(i+1) + " of " + str(nb_jobs) + " jobs in this particular submission"
                
    print "End RunJobs ===================\n"

RunJobs(pickUpFromJob=1,nb_jobs=300,physical_time_interval=0.001,endTimeWall=0.3) 
#TODO read from file per-job so that this is runtime modifiable
#TODO log seems to be blocked at the beginning then... start to have some contents though contents are complete.