#!/bin/env python

import commands, os
import sys

slurmFile = sys.argv[1]

cmd = "sbatch %s" % slurmFile
print "submitting job using : %s" % cmd

status, jobnum = commands.getstatusoutput(cmd)

if status == 0:
    print "job is submited with jobID : %s" %jobnum
else:
    print "Error when submitting\n"
