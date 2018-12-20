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
    
def plotField(arrayName, cases, positionList, samples, field):

    dataFile = "/"+"userDefinedLog/history_labelGroup_"+arrayName

    mean = np.zeros((len(positionList),4))
    std = np.zeros((len(positionList),4))
    
    for i, sample in enumerate(samples):
        fig = plt.figure()
        
        fig, axarr = plt.subplots(4, sharex=True)
        for j, case in enumerate(cases):
            if j == 0:
                if i >= 7:
                    std[i,j], mean[i,j] = userProbeByLabel(axarr[j], case, dataFile, sample, positionList, cut=0.6)
                else :
                    std[i,j], mean[i,j] = userProbeByLabel(axarr[j], case, dataFile, sample, positionList, cut=0.5)
            elif j == 1:
                if i >= 14:
                    std[i,j], mean[i,j] = userProbeByLabel(axarr[j], case, dataFile, sample, positionList, cut=0.5)
                else :
                    std[i,j], mean[i,j] = userProbeByLabel(axarr[j], case, dataFile, sample, positionList, cut=0.5)                
            elif j == 2:
                if i >= 14:
                    std[i,j], mean[i,j] = userProbeByLabel(axarr[j], case, dataFile, sample, positionList, cut=0.8)
                else:
                    std[i,j], mean[i,j] = userProbeByLabel(axarr[j], case, dataFile, sample, positionList, cut=0.5)
            elif j ==3 :
                if i >= 14:
                    std[i,j], mean[i,j] = userProbeByLabel(axarr[j], case, dataFile, sample, positionList, cut=0.8)
                else:
                    std[i,j], mean[i,j] = userProbeByLabel(axarr[j], case, dataFile, sample, positionList, cut=0.5)
            else :
                print "There's a big problem"

        fig.text(0.5, 0.04, r'$t$', ha='center', va='center')
        fig.text(0.06, 0.5, 'Ux Uy Uz T', ha='center', va='center', rotation='vertical')
        fig.savefig("../PICTURE_history_c/"+arrayName+"/x_Eq_"+str(positionList[sample]/8.0).replace('.','p')+"D.png", bbox_inches='tight',dpi=300) # bbox_inches = 'tight' is neccessary

    return mean, std
#==============================================================================
#   RMS 
#==============================================================================    
def spatial_mean_rms(arrayName, cases, positionList, mean , std, linestyleList, markerList):
    fig_rms = plt.figure()
    positionList=[x/8.0 for x in positionList]

    ax1 = fig_rms.add_subplot(1,1,1)

    for i, case in enumerate(cases):
        ax1.plot(positionList,std[:,i],label=cases[i],linestyle=linestyleList[i],marker=markerList[i])
    ax1.legend(bbox_to_anchor=(1., 1), ncol=1, shadow=True)
    ax1.set_xlabel(r"$x/D$")
#    ax1.set_ylabel(latexRMSName)
    
    fig_rms.savefig('../PICTURE_history_c/'+arrayName+'/RMS_xByD_oneFig.png', bbox_inches='tight',  dpi=300)
#==============================================================================
#   Mean
#==============================================================================
    fig_rms = plt.figure()

    ax1 = fig_rms.add_subplot(1,1,1)

    for i, case in enumerate(cases):
        ax1.plot(positionList,mean[:,i],label=cases[i],linestyle=linestyleList[i],marker=markerList[i])
    ax1.legend(bbox_to_anchor=(1., 1), ncol=1, shadow=True)
    ax1.set_xlabel(r"$x/D$")
#    ax1.set_ylabel(latexMEANName)
    
    fig_rms.savefig('../PICTURE_history_c/'+arrayName+'/Mean_xByD_oneFig.png', bbox_inches='tight', dpi=300)

def main():
    plt.style.use('seaborn-white') # from defaut
    positionList = [0,16,32,48]
    samples = [0,1,2,3]
    cases = [
             "BirdCarreau"+"/"+"inlet_0p5",
             "Newtonian"+"/"+"Re4000",
             "BirdCarreau"+"/"+"inlet_0p3",
             "Newtonian"+"/"+"Re2400"]
    
    linestyleList = [
             "-",
             "--",
             "-",
             "--"
              ]
    markerList = [
             "s",
             "^",
             "s",
             "^" 
              ]
    arrayNames=["U_x", "U_y", "U_z", "T"]
    
    for i in range (0,4):
        arrayName =arrayNames[i]
        mean = np.zeros((len(positionList),4))
        std = np.zeros((len(positionList),4))
        mean, std = plotField(arrayName, cases, positionList, samples, field=i)
#        spatial_mean_rms(arrayName, cases, positionList, mean, std, linestyleList, markerList)

main()