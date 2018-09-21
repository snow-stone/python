#!/bin/env python

import subprocess
import numpy as np

dataWritingHistory=np.genfromtxt('userDefinedLog/dataWritingHistory',skip_header=0,delimiter=' ')

print dataWritingHistory

times=''

for time in dataWritingHistory:
    times = times + ',' + str(time)

print times

return_code = subprocess.call("./reconstruct1.sh "+times[1:], shell=True)