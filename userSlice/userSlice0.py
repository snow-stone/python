# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 21:08:57 2018

@author: hluo
"""

import numpy as np
import matplotlib.pyplot as plt

positionList = [0,1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72]

data = np.genfromtxt("BirdCarreau/inlet_0p3/userDefinedLog/slice"+str(0)+"_mean_rms")

#samples = [4,8,13,16]

time = data[:,0]

fig, ax = plt.subplots()

#for i in range(len(positionList)):
#    ax.plot(time, data[:,i+1])

#for sample in samples:
#    ax.plot(time, data[:,sample], label=str(positionList[sample]/8.0)+"D")

ax.plot(time,data[:,2])
ax.legend(bbox_to_anchor=(1.3, 1), ncol=1, shadow=True)