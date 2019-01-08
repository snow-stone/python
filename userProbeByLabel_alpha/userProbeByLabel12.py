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
    
    return std, mean
    
def main():
    positionList = [0,1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72]
    #   sampling = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#    print len(positionList)
    samples = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    arrayName="U_z"
    dataFile = "/"+"userDefinedLog/fluctuation_labelGroup_"+arrayName
    plt.style.use('ggplot')
#    print "plt.style.available"
#    print(plt.style.available)
    mean0 = np.zeros(len(positionList))
    mean1 = np.zeros(len(positionList))
    mean2 = np.zeros(len(positionList))
    mean3 = np.zeros(len(positionList))
    
    std0 = np.zeros(len(positionList))
    std1 = np.zeros(len(positionList))
    std2 = np.zeros(len(positionList))
    std3 = np.zeros(len(positionList))
    
    i=0
    for sample in samples:
        print i
        fig = plt.figure()
        ax1 = fig.add_subplot(2,1,1)
        
    #    print "\nFig"
        case1 = "BirdCarreau"+"/"+"inlet_0p5"
        std0[i], mean0[i] = userProbeByLabel(ax1, case1, dataFile, sample, positionList, cut=400)
#        userProbeByLabel(ax1, case1, dataFile, sample, positionList, cut=400)
        case2 = "Newtonian"+"/"+"Re4000"
        std1[i], mean1[i] = userProbeByLabel(ax1, case2, dataFile, sample, positionList, cut=400)
#        userProbeByLabel(ax1, case2, dataFile, sample, positionList, cut=400)
        
        ax1.legend(bbox_to_anchor=(1.7, 1), ncol=1, shadow=True)
        ax1.set_xlabel(r"$t$")
        ax1.set_ylabel(r"$u'$")
        
        ax2 = fig.add_subplot(2,1,2)
        
    #    print "\nFig1"
        case1 = "BirdCarreau"+"/"+"inlet_0p3"    
        std2[i], mean2[i] = userProbeByLabel(ax2, case1, dataFile, sample, positionList, cut=0)
#        userProbeByLabel(ax2, case1, dataFile, sample, positionList, cut=0)
        case2 = "Newtonian"+"/"+"Re2400"
        std3[i], mean3[i] = userProbeByLabel(ax2, case2, dataFile, sample, positionList, cut=400)
#        userProbeByLabel(ax2, case2, dataFile, sample, positionList, cut=400)
        
        ax2.legend(bbox_to_anchor=(1.7, 1), ncol=1, shadow=True)
        ax2.set_xlabel(r"$t$")
        ax2.set_ylabel(r"$u'$")
        
        fig.savefig("PICTURE/"+arrayName+"/x_Eq_"+str(positionList[sample]/8.0)+"D.png", bbox_inches='tight')
        i=i+1
    
    fig1 = plt.figure()
    positionList=[x/8.0 for x in positionList]
#    ax1 = fig1.add_subplot(2,1,1)
#    ax1.plot(positionList,mean0,label="BirdCarreau"+"/"+"inlet_0p5")
#    ax1.plot(positionList,mean1,label="Newtonian"+"/"+"Re4000")
#    ax1.legend(bbox_to_anchor=(1.7, 1), ncol=1, shadow=True)
#    ax1.set_xlabel(r"$x/D$")
#    ax1.set_ylabel(r"$u'$")
#    ax2 = fig1.add_subplot(2,1,2)
#    ax2.plot(positionList,mean2,label="BirdCarreau"+"/"+"inlet_0p3")
#    ax2.plot(positionList,mean3,label="Newtonian"+"/"+"Re2400")
#    ax2.legend(bbox_to_anchor=(1.7, 1), ncol=1, shadow=True)
#    ax2.set_xlabel(r"$x/Dt$")
#    ax2.set_ylabel(r"$u'$")
    ax1 = fig1.add_subplot(2,1,1)
    ax1.plot(positionList,std0,label="BirdCarreau"+"/"+"inlet_0p5")
    ax1.plot(positionList,std1,label="Newtonian"+"/"+"Re4000")
    ax1.legend(bbox_to_anchor=(1.7, 1), ncol=1, shadow=True)
    ax1.set_xlabel(r"$x/D$")
    ax1.set_ylabel(r"$u_{rms}$")
    ax2 = fig1.add_subplot(2,1,2)
    ax2.plot(positionList,std2,label="BirdCarreau"+"/"+"inlet_0p3")
    ax2.plot(positionList,std3,label="Newtonian"+"/"+"Re2400")
    ax2.legend(bbox_to_anchor=(1.7, 1), ncol=1, shadow=True)
    ax2.set_xlabel(r"$x/D$")
    ax2.set_ylabel(r"$u_{rms}$")
    fig1.savefig('PICTURE/'+arrayName+'/RMS_xByD.png', bbox_inches='tight')

main()