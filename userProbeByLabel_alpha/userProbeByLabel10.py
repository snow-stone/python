# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 21:08:57 2018

@author: hluo
"""

import numpy as np
import matplotlib.pyplot as plt


def userProbeByLabel(ax, caseName, RelativeDataFile, sample, positionSet, cut=400):
    rawData = np.genfromtxt(caseName+RelativeDataFile)
    print rawData.shape
    time = rawData[:,0]
    data = rawData[:,1:]
    
    position_in_D = str(positionSet[sample]/8.0)+"D"
    std = np.std(data[cut:,sample])
    mean = np.mean(data[cut:,sample])
    print position_in_D + " std : ", std, " mean : ", mean
    ax.plot(time[cut:], data[cut:,sample], label=caseName+"_"+position_in_D)
    
#    return std, mean
    
def main():
    positionList = [0,1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72]
    #   sampling = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#    print len(positionList)
    samples = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    dataFile = "/"+"userDefinedLog/fluctuation_labelGroup_U_x"
    plt.style.use('ggplot')
#    print "plt.style.available"
#    print(plt.style.available)
#    mean0 = []
#    mean1 = []
#    mean2 = []
#    mean3 = []
#    
#    std0 = []
#    std1 = []
#    std2 = []
#    std3 = []
#    
#    i=0
    for sample in samples:
        fig = plt.figure()
        ax1 = fig.add_subplot(2,1,1)
        
    #    print "\nFig"
        case1 = "BirdCarreau"+"/"+"inlet_0p5"
#        std0[i], mean0[i] = userProbeByLabel(ax1, case1, dataFile, sample, positionList, cut=400)
        userProbeByLabel(ax1, case1, dataFile, sample, positionList, cut=400)
        case2 = "Newtonian"+"/"+"Re4000"
#        std1[i], mean1[i] = userProbeByLabel(ax1, case2, dataFile, sample, positionList, cut=400)
        userProbeByLabel(ax1, case2, dataFile, sample, positionList, cut=400)
        
        ax1.legend(bbox_to_anchor=(1.7, 1), ncol=1, shadow=True)
        ax1.set_xlabel(r"$t$")
        ax1.set_ylabel(r"$u'$")
        
        ax2 = fig.add_subplot(2,1,2)
        
    #    print "\nFig1"
        case1 = "BirdCarreau"+"/"+"inlet_0p3"    
#        std2[i], mean2[i] = userProbeByLabel(ax2, case1, dataFile, sample, positionList, cut=0)
        userProbeByLabel(ax2, case1, dataFile, sample, positionList, cut=0)
        case2 = "Newtonian"+"/"+"Re2400"
#        std3[i], mean3[i] = userProbeByLabel(ax2, case2, dataFile, sample, positionList, cut=400)
        userProbeByLabel(ax2, case2, dataFile, sample, positionList, cut=400)
        
        ax2.legend(bbox_to_anchor=(1.7, 1), ncol=1, shadow=True)
        ax2.set_xlabel(r"$t$")
        ax2.set_ylabel(r"$u'$")
        
        fig.savefig('PICTURE/x_Eq_'+str(positionList[sample]/8.0)+'D.png', bbox_inches='tight')
#        i=i+1

main()