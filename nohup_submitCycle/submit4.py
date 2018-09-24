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
        return status, jobnum
    else:
        print "FATAL ERROR!"
        print "file %s doesnt exits" % slurmFile
        return (1, '0000')

def watchJob(status, jobnum, simuLogFile, defautWallTime): 
    if status == 0:
        print "job is submited with jobID : %s" %jobnum
        # suspect ORTE error for 1h
        print "suspectting ORTE error..."
        submittedTime = time.time()
        while time.time() - submittedTime < defautWallTime:
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
    else:
        print "Error when submitting\n"
        # no of231 before ??

def main():
    slurmFile = sys.argv[1]
    logFile = sys.argv[2]
    
    removeLogFile(logFile)
    cmd = "sbatch %s" % slurmFile
    status, jobnum = submitJob(cmd, slurmFile)
    
    watchJob(status, jobnum, logFile, 60*60)

main()
