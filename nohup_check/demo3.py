#!/bin/env python

import subprocess
#import numpy as np

#dataWritingHistory=np.genfromtxt('userDefinedLog/dataWritingHistory',skip_header=0,delimiter=' ')

#with open('userDefinedLog/dataWritingHistory') as f:
#    content = f.readlines()

Nb_procs=4

lines = [line.rstrip('\n') for line in open('userDefinedLog/dataWritingHistory')]

print lines

times = ",".join(lines[:-1]) # omitting the last one

print times


return_code = subprocess.call("./reconstruct3.sh "+times, shell=True)

if not return_code :
    for time in lines:
        print '\n'
        for i in range(Nb_procs):
            rm_command = 'rm -r processor'+str(i)+'/'+str(time)
            return_value = subprocess.call(rm_command, shell=True)
            if not return_value:
                print rm_command
#        if return_value :
#            continue