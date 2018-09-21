#!/bin/env python

import commands, os

cmd = "sbatch 480bN_test-1"
print "submitting job using : %s" % cmd

status, jobnum = commands.getstatusoutput(cmd)

if status == 0:
    print "job is running with jobID : %s" %jobnum
else:
    print "Error when submitting\n"
