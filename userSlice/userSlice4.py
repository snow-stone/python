# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 21:08:57 2018

@author: hluo
"""

import numpy as np
import matplotlib.pyplot as plt



def plotSlice(ax, sliceNumber, cut=0.5):
    
    data = np.genfromtxt("BirdCarreau/inlet_0p3/userDefinedLog/slice"+str(sliceNumber)+"_mean_rms")
#    data = np.genfromtxt("Newtonian/Re4000/userDefinedLog/slice"+str(sliceNumber)+"_mean_rms")
    
    #samples = [4,8,13,16]
    
    time = data[:,0]
    cutSliceIndex = int(cut*len(time))
    
    ax.plot(time[cutSliceIndex:],data[cutSliceIndex:,2])
    ax.plot(time[:cutSliceIndex],data[:cutSliceIndex,2],linestyle=':')
    ax.legend(bbox_to_anchor=(1.3, 1), ncol=1, shadow=True)
    
    return np.mean(data[cutSliceIndex:,2])
    
def main():
    positionList = [0,1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72]
    meanOfRMS = np.zeros(len(positionList))
    
    fig, ax = plt.subplots()
    for i, position in enumerate(positionList):
        meanOfRMS[i] = plotSlice(ax, position, cut=0.7)
    
    fig1, ax1 = plt.subplots()
    ax1.plot(positionList,meanOfRMS)
    
main()