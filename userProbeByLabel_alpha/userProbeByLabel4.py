# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 21:08:57 2018

@author: hluo
"""

import numpy as np
import matplotlib.pyplot as plt


def userProbeByLabel(ax, caseName, RelativeDataFile, sampleSet, positionSet, cut=400):
    data = np.genfromtxt(caseName+RelativeDataFile)
    print data.shape
    time = data[:,0]
    
#    fig, ax = plt.subplots()
    
    for sample in sampleSet:
        position_in_D = str(positionSet[sample]/8.0)+"D"
        print position_in_D + " std : ", np.std(data[cut:,sample]), " mean : ", np.mean(data[cut:,sample])
        ax.plot(time[cut:], data[cut:,sample], label=caseName+"_"+position_in_D)
    
#    ax.legend(bbox_to_anchor=(1.3, 1), ncol=1, shadow=True)
    
def main():
    positionList = [0,1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72]
    #   sampling = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    print len(positionList)
    samples = [8]
    dataFile = "/"+"userDefinedLog/fluctuation_labelGroup_U_x"

    fig, ax = plt.subplots()
    
    case1 = "Re2400"    
    userProbeByLabel(ax, case1, dataFile, samples, positionList, cut=400)
    case2 = "Re4000"
    userProbeByLabel(ax, case2, dataFile, samples, positionList, cut=400)
    
    ax.legend(bbox_to_anchor=(1.4, 1), ncol=1, shadow=True)

main()