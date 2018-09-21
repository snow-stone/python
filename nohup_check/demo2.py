#!/bin/env python

import subprocess
import numpy as np

dataWritingHistory=np.genfromtxt('userDefinedLog/dataWritingHistory',skip_header=0,delimiter=' ')

print dataWritingHistory

times=''

for time in dataWritingHistory[:-1]: # omitting the last one
    times = times + ',' + str(time)

print times

return_code = subprocess.call("./reconstruct2.sh "+times[1:], shell=True) # use times[1:] for removing the leading ','

print return_code

if not return_code :
    for time in dataWritingHistory[:-1]: # omitting the last one
        print 'rm -r processor*/'+str(time)
        return_value = subprocess.call('rm -r processor*/'+str(time), shell=True)
#        if return_value :
#            continue