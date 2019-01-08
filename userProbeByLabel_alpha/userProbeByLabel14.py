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
    field=0
    arrayNames=["U_x", "U_y", "U_z", "T"]
    arrayName =arrayNames[field]
    dataFile = "/"+"userDefinedLog/fluctuation_labelGroup_"+arrayName
    latexNames = [r"$U'$", r"$V'$", r"$W'$", r"$T'$"]
    latexName  = latexNames[field]
    latexRMSNames = [r"$U_x^{rms}$",r"$U_y^{rms}$",r"$U_z^{rms}$",r"$T^{rms}$"]
    latexRMSName = latexRMSNames[field]
    debit_medium = [
             "BirdCarreau"+"/"+"inlet_0p5",
             "Newtonian"+"/"+"Re4000"
              ]
    debit_min = [
             "BirdCarreau"+"/"+"inlet_0p3",
             "Newtonian"+"/"+"Re2400"]
    cuts_medium = [
            400,
            400
            ]
    cuts_min = [
            0,
            400
            ]
    
    plt.style.use('ggplot')

    mean_medium = np.zeros((len(positionList),2))
    mean_min = np.zeros((len(positionList),2))
    std_medium = np.zeros((len(positionList),2))
    std_min = np.zeros((len(positionList),2))
    
    for i, sample in enumerate(samples):
        fig = plt.figure()

        ax1 = fig.add_subplot(2,1,1)
        for j, case in enumerate(debit_medium):
            std_medium[i,j], mean_medium[i,j] = userProbeByLabel(ax1, case, dataFile, sample, positionList, cuts_medium[j])
        
        ax1.legend(bbox_to_anchor=(1.7, 1), ncol=1, shadow=True)
        ax1.set_xlabel(r"$t$")
        ax1.set_ylabel(latexName)
        
        ax2 = fig.add_subplot(2,1,2)
        for j, case in enumerate(debit_min):
            std_min[i,j], mean_min[i,j] = userProbeByLabel(ax2, case, dataFile, sample, positionList, cuts_min[j])
        
        ax2.legend(bbox_to_anchor=(1.7, 1), ncol=1, shadow=True)
        ax2.set_xlabel(r"$t$")
        ax2.set_ylabel(latexName)
        
        fig.savefig("PICTURE/"+arrayName+"/x_Eq_"+str(positionList[sample]/8.0)+"D.png", bbox_inches='tight')
    
    fig1 = plt.figure()
    positionList=[x/8.0 for x in positionList]

    ax1 = fig1.add_subplot(2,1,1)
    for i, case in enumerate(debit_medium):
        ax1.plot(positionList,std_medium[:,i],label=debit_medium[i])
    ax1.legend(bbox_to_anchor=(1.7, 1), ncol=1, shadow=True)
    ax1.set_xlabel(r"$x/D$")
    ax1.set_ylabel(latexRMSName)
    
    ax2 = fig1.add_subplot(2,1,2)
    for i, case in enumerate(debit_min):
        ax2.plot(positionList,std_min[:,i],label=debit_min[i])
    ax2.legend(bbox_to_anchor=(1.7, 1), ncol=1, shadow=True)
    ax2.set_xlabel(r"$x/D$")
    ax2.set_ylabel(latexRMSName)
    fig1.savefig('PICTURE/'+arrayName+'/RMS_xByD.png', bbox_inches='tight')

main()