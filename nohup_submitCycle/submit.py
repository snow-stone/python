#!/bin/env python

import commands, os
import sys
import time

slurmFile = sys.argv[1]
logFile = sys.argv[2]

# make sure logFile is cleaned before proceed
try:
    os.remove(logFile)
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror)) 

# submit
cmd = "sbatch %s" % slurmFile
print "submitting job using : %s" % cmd

status, jobnum = commands.getstatusoutput(cmd)

if status == 0:
    print "job is submited with jobID : %s" %jobnum
    # suspect ORTE error for 30min 
    print "suspectting ORTE error..."
    submittedTime = time.time()
    while time.time() - submittedTime < 60*30:
        if os.path.exists(logFile):
            print "%s found" % logFile
            if "ORTE" in open(logFile).read():
                print "ORTE error found !\n"
                print "You may need to re-submit \n"
                # add re-submit here. with some time
                # cmd ??
                break
            else:
                continue
            time.sleep(30)
        else:
            time.sleep(30)
            print "waiting for %s to be created..." % logFile
    # maybe queued for 1h... just after 30min ORTE appears
    print "didnt find ORTE in 30min, should be just fine"

else:
    print "Error when submitting\n"
