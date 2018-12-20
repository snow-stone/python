# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 21:08:57 2018

@author: hluo
"""

import numpy as np
import matplotlib.pyplot as plt


def userProbeByLabel(ax, caseName, RelativeDataFile, sample, positionSet, cut=0.5):
    rawData = np.genfromtxt("../"+caseName+RelativeDataFile)
    print rawData.shape
    time = rawData[:,0]
    data = rawData[:,1:]
    cutSliceIndex = int(cut*len(time))
    
    position_in_D = str(positionSet[sample]/8.0)+"D"
    std = np.std(data[cutSliceIndex:,sample])
    mean = np.mean(data[cutSliceIndex:,sample])
    print position_in_D + " std : ", std, " mean : ", mean
    ax.plot(time[cutSliceIndex:], data[cutSliceIndex:,sample], label=caseName+"_"+position_in_D+"\nNbSampleEq_"+str(len(time[cutSliceIndex:])), linestyle='-')
    ax.plot(time[:cutSliceIndex], data[:cutSliceIndex,sample], linestyle=':')    
    
    return std, mean
    
def plotField(field):
    positionList = [0,16,32,48]
    #   sampling = [0,1 ,2 ,3]
    samples = [0,1,2,3]
    arrayNames=["U_x", "U_y", "U_z", "T"]
    arrayName =arrayNames[field]
    dataFile = "/"+"userDefinedLog/history_labelGroup_"+arrayName
    latexNames = [r"$U_x$", r"$U_y$", r"$U_z$", r"$T$"]
    latexName  = latexNames[field]
    latexRMSNames = [r"$U_x^{rms}$",r"$U_y^{rms}$",r"$U_z^{rms}$",r"$T^{rms}$"]
    latexRMSName = latexRMSNames[field]
    latexMEANNames = [r"$<U_x>$",r"$<U_y>$",r"$<U_z>$",r"$<T>$"]
    latexMEANName = latexMEANNames[field]
    debit_medium = [
             "BirdCarreau"+"/"+"inlet_0p5",
             "Newtonian"+"/"+"Re4000"
              ]
    debit_min = [
             "BirdCarreau"+"/"+"inlet_0p3",
             "Newtonian"+"/"+"Re2400"]
#    color_medium = [
#             "red",
#             "blue"              
#              ]
#    color_min = [
#             "red",
#             "blue"              
#              ]
    linestyle_medium = [
             "-",
             "--"
              ]
    linestyle_min = [
             "-",
             "--"
              ]
    marker_medium = [
             "s",
             "^" 
              ]
    marker_min = [
             "s",
             "^" 
              ]
#    cuts_medium = [
#            0.5,
#            0.5
#            ]
#    cuts_min = [
#            0.5,
#            0.5
#            ]
    
    plt.style.use('seaborn-white') # from defaut

    mean_medium = np.zeros((len(positionList),2))
    mean_min = np.zeros((len(positionList),2))
    std_medium = np.zeros((len(positionList),2))
    std_min = np.zeros((len(positionList),2))
    
    for i, sample in enumerate(samples):
        fig = plt.figure()
        
        # debit_medium
        ax1 = fig.add_subplot(2,1,1)
        for j, case in enumerate(debit_medium):
            if j == 0:
                if i >= 7:
                    std_medium[i,j], mean_medium[i,j] = userProbeByLabel(ax1, case, dataFile, sample, positionList, cut=0.6)
                else :
                    std_medium[i,j], mean_medium[i,j] = userProbeByLabel(ax1, case, dataFile, sample, positionList, cut=0.5)
            else:
                if i >= 14:
                    std_medium[i,j], mean_medium[i,j] = userProbeByLabel(ax1, case, dataFile, sample, positionList, cut=0.5)
                else :
                    std_medium[i,j], mean_medium[i,j] = userProbeByLabel(ax1, case, dataFile, sample, positionList, cut=0.5)                
        
        ax1.legend(bbox_to_anchor=(1.7, 1), ncol=1, shadow=True)
        ax1.set_xlabel(r"$t$")
        ax1.set_ylabel(latexName)
        ax1.set_ylim(-0.2,1.2)
        ax1.set_xlim(0,0.8)
        
        # debit_min
        ax2 = fig.add_subplot(2,1,2)
        for j, case in enumerate(debit_min):
            if j == 0:
                if i >= 14:
                    std_min[i,j], mean_min[i,j] = userProbeByLabel(ax2, case, dataFile, sample, positionList, cut=0.8)
                else:
                    std_min[i,j], mean_min[i,j] = userProbeByLabel(ax2, case, dataFile, sample, positionList, cut=0.5)
            else:
                if i >= 14:
                    std_min[i,j], mean_min[i,j] = userProbeByLabel(ax2, case, dataFile, sample, positionList, cut=0.8)
                else:
                    std_min[i,j], mean_min[i,j] = userProbeByLabel(ax2, case, dataFile, sample, positionList, cut=0.5)
        ax2.legend(bbox_to_anchor=(1.7, 1), ncol=1, shadow=True)
        ax2.set_xlabel(r"$t$")
        ax2.set_ylabel(latexName)
        ax2.set_ylim(-0.2,1.2)
        ax2.set_xlim(0,0.8)
        
        fig.savefig("../PICTURE_history_c/"+arrayName+"/x_Eq_"+str(positionList[sample]/8.0).replace('.','p')+"D.png", bbox_inches='tight',dpi=300) # bbox_inches = 'tight' is neccessary
#==============================================================================
#   RMS 
#==============================================================================    
    fig_rms = plt.figure()
    positionList=[x/8.0 for x in positionList]

    ax1 = fig_rms.add_subplot(1,1,1)
    for i, case in enumerate(debit_medium):
        ax1.plot(positionList,std_medium[:,i],label=debit_medium[i],linestyle=linestyle_medium[i],marker=marker_medium[i])
#    ax1.legend(bbox_to_anchor=(1.7, 1), ncol=1, shadow=True)
#    ax1.set_xlabel(r"$x/D$")
#    ax1.set_ylabel(latexRMSName)
    
#    ax2 = fig_rms.add_subplot(2,1,2)
    for i, case in enumerate(debit_min):
        ax1.plot(positionList,std_min[:,i],label=debit_min[i],linestyle=linestyle_min[i],marker=marker_medium[i])
    ax1.legend(bbox_to_anchor=(1., 1), ncol=1, shadow=True)
    ax1.set_xlabel(r"$x/D$")
    ax1.set_ylabel(latexRMSName)
#    ax1.set_ylim(0,0.4)
    
    fig_rms.savefig('../PICTURE_history_c/'+arrayName+'/RMS_xByD_oneFig.png', bbox_inches='tight',  dpi=300)
#==============================================================================
#   Mean
#==============================================================================
    fig_rms = plt.figure()
#    positionList=[x/8.0 for x in positionList]

    ax1 = fig_rms.add_subplot(1,1,1)
    for i, case in enumerate(debit_medium):
        ax1.plot(positionList,mean_medium[:,i],label=debit_medium[i],linestyle=linestyle_medium[i],marker=marker_min[i])
#    ax1.legend(bbox_to_anchor=(1.7, 1), ncol=1, shadow=True)
#    ax1.set_xlabel(r"$x/D$")
#    ax1.set_ylabel(latexMEANName)
    
#    ax2 = fig_rms.add_subplot(2,1,2)
    for i, case in enumerate(debit_min):
        ax1.plot(positionList,mean_min[:,i],label=debit_min[i],linestyle=linestyle_min[i],marker=marker_min[i])
    ax1.legend(bbox_to_anchor=(1., 1), ncol=1, shadow=True)
    ax1.set_xlabel(r"$x/D$")
    ax1.set_ylabel(latexMEANName)
    
    fig_rms.savefig('../PICTURE_history_c/'+arrayName+'/Mean_xByD_oneFig.png', bbox_inches='tight', dpi=300)

def main():
#    plotField(field=3)
    for i in range (0,4):
        plotField(field=i)

main()