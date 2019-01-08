# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 21:08:57 2018

@author: hluo
"""

import numpy as np
import matplotlib.pyplot as plt


def userProbeByLabel(ax, dataFile, sampleSet, positionSet, cut=400):
    data = np.genfromtxt(dataFile)
    print data.shape
    time = data[:,0]
    
#    fig, ax = plt.subplots()
    
    for sample in sampleSet:
        position_in_D = str(positionSet[sample]/8.0)+"D"
        print position_in_D + " std : ", np.std(data[cut:,sample]), " mean : ", np.mean(data[cut:,sample])
        ax.plot(time[cut:], data[cut:,sample], label=position_in_D)
    
#    ax.legend(bbox_to_anchor=(1.3, 1), ncol=1, shadow=True)
    
def main():
    positionList = [0,1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72]
    #   sampling = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    print len(positionList)
    samples = [4,8,13,16]

    fig, ax = plt.subplots()    
    caseName = "Re2400"
    dataFile = caseName+"/"+"userDefinedLog/fluctuation_labelGroup_U_x"
    
    userProbeByLabel(ax, dataFile, samples, positionList, cut=400)
    ax.legend(bbox_to_anchor=(1.3, 1), ncol=1, shadow=True)
    
#    caseName = "Re4000"
#    dataFile = caseName+"/"+"userDefinedLog/fluctuation_labelGroup_U_x"
#    userProbeByLabel(ax, dataFile, samples, positionList, cut=400)

main()