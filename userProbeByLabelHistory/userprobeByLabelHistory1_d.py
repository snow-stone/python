# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 21:08:57 2018

@author: hluo
"""

import numpy as np
import matplotlib.pyplot as plt

def userProbeByLabel1(ax, caseName, fieldName, sample, positions, color, cut=0.):
    RelativeDataFile = "./"+"userDefinedLog/history_labelGroup_"+fieldName
    rawData = np.genfromtxt("../"+caseName+'/'+RelativeDataFile)
#    print rawData.shape
    time = rawData[:,0]
    probeData = rawData[:,1:]
    cutSliceIndex = int(cut*len(time))
    
    position_in_D = str(positions[sample]/8.0)+"D"
    std = np.std(probeData[cutSliceIndex:,sample])
    mean = np.mean(probeData[cutSliceIndex:,sample])
#    print position_in_D + " std : ", std, " mean : ", mean
    ax.plot(time[cutSliceIndex:], probeData[cutSliceIndex:,sample], color=color, linewidth=0.5, label=caseName+"_"+position_in_D+"\nNbSampleEq_"+str(len(time[cutSliceIndex:])), linestyle='-')
    ax.plot(time[:cutSliceIndex], probeData[:cutSliceIndex,sample], color=color, linewidth=0.5)    

    return std, mean
"""
    RelativeDataFile = "./"+"userDefinedLog/history_labelGroup_"+fieldName+".bak"
    rawData = np.genfromtxt("../"+caseName+'/'+RelativeDataFile)
#    print rawData.shape
    time = rawData[:,0]+0.2
    probeData = rawData[:,1:]
    cutSliceIndex = int(cut*len(time))
    
    position_in_D = str(positions[sample]/8.0)+"D"
    std = np.std(probeData[cutSliceIndex:,sample])
    mean = np.mean(probeData[cutSliceIndex:,sample])
#    print position_in_D + " std : ", std, " mean : ", mean
    ax.plot(time[cutSliceIndex:], probeData[cutSliceIndex:,sample], color=color, linewidth=1.5, label=caseName+"_"+position_in_D+"\nNbSampleEq_"+str(len(time[cutSliceIndex:])), linestyle='-')
    ax.plot(time[:cutSliceIndex], probeData[:cutSliceIndex,sample], color=color, linewidth=0.5)    
"""

def userProbeByLabel(ax, caseName, fieldName, sample, positions, color, cut=0.5):
    RelativeDataFile = "./"+"userDefinedLog/history_labelGroup_"+fieldName
    rawData = np.genfromtxt("../"+caseName+'/'+RelativeDataFile)
#    print rawData.shape
    time = rawData[:,0]
    probeData = rawData[:,1:]
    cutSliceIndex = int(cut*len(time))
    
    position_in_D = str(positions[sample]/8.0)+"D"
    std = np.std(probeData[cutSliceIndex:,sample])
    mean = np.mean(probeData[cutSliceIndex:,sample])
#    print position_in_D + " std : ", std, " mean : ", mean
    ax.plot(time[cutSliceIndex:], probeData[cutSliceIndex:,sample], color=color, linewidth=1.5, label=caseName+"_"+position_in_D+"\nNbSampleEq_"+str(len(time[cutSliceIndex:])), linestyle='-')
    ax.plot(time[:cutSliceIndex], probeData[:cutSliceIndex,sample], color=color, linewidth=0.5)    
    
    return std, mean

##==============================================================================
##   RMS 
##==============================================================================    
#def spatial_mean_rms(fieldName, cases, positions, mean , std, linestyleList, markerList):
#    fig_rms = plt.figure()
#    positions=[x/8.0 for x in positions]
#
#    ax1 = fig_rms.add_subplot(1,1,1)
#
#    for i, case in enumerate(cases):
#        ax1.plot(positions,std[:,i],label=cases[i],linestyle=linestyleList[i],marker=markerList[i])
#    ax1.legend(bbox_to_anchor=(1., 1), ncol=1, shadow=True)
#    ax1.set_xlabel(r"$x/D$")
##    ax1.set_ylabel(latexRMSName)
#    
#    fig_rms.savefig('../PICTURE_history_d/'+fieldName+'/RMS_xByD_oneFig.png', bbox_inches='tight',  dpi=300)
##==============================================================================
##   Mean
##==============================================================================
#    fig_rms = plt.figure()
#
#    ax1 = fig_rms.add_subplot(1,1,1)
#
#    for i, case in enumerate(cases):
#        ax1.plot(positions,mean[:,i],label=cases[i],linestyle=linestyleList[i],marker=markerList[i])
#    ax1.legend(bbox_to_anchor=(1., 1), ncol=1, shadow=True)
#    ax1.set_xlabel(r"$x/D$")
##    ax1.set_ylabel(latexMEANName)
#    
#    fig_rms.savefig('../PICTURE_history_d/'+fieldName+'/Mean_xByD_oneFig.png', bbox_inches='tight', dpi=300)

def main():
    plt.style.use('seaborn-white') # from defaut
    allProbePosition = [0,1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72]
        #   sampling = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    positionSubSet = [0,13,15,17]
#    positionSubSet = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    cases = [
             "BirdCarreau/inlet_0p3-a_0p5-setT_St_1",
			 "BirdCarreau/inlet_0p3-a_0p5-setT_St_5",
             "BirdCarreau"+"/"+"inlet_0p3",
             "Newtonian"+"/"+"Re2400"
            ]
    
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
              
    fieldNames=["U_x", "U_y", "U_z", "T"]
    
    colorList = [
                  "blue",
                  "red",
                  "green",
                  "black"
                ]
    
    for k, position in enumerate(positionSubSet):
        p=positionSubSet[k]
        print "position : " , allProbePosition[p]
        fig, axses_case = plt.subplots(4, 1, sharex=True)
        mean = np.zeros((len(allProbePosition),4))
        std = np.zeros((len(allProbePosition),4))
        for j, case in enumerate(cases):
            for i, fieldName in enumerate(fieldNames):
        #        mean = np.zeros((len(positionList),4))
        #        std = np.zeros((len(positionList),4))
        #        mean, std = plotField(axarr, fieldName, cases, positionList, colorList, samples, field=i)
        #        plotField(axarr, fieldName, cases, positionList, colorList, samples, field=i)
        #        spatial_mean_rms(arrayName, cases, positionList, mean, std, linestyleList, markerList)
                axses_case[j].set_ylim(-0.5,2.5)
                axses_case[j].set_xlim(-0,0.8)
                
                print "axe number = ", j , fieldName
                if j == 0:
                    if allProbePosition[p] >= 7:
                        std[i,j], mean[i,j] = userProbeByLabel1(axses_case[j], case, fieldName, p, allProbePosition, colorList[i])
                    else :
                        std[i,j], mean[i,j] = userProbeByLabel1(axses_case[j], case, fieldName, p, allProbePosition, colorList[i])
                elif j == 1:
                    if allProbePosition[p] >= 24:
                        std[i,j], mean[i,j] = userProbeByLabel1(axses_case[j], case, fieldName, p, allProbePosition, colorList[i])
                    else :
                        std[i,j], mean[i,j] = userProbeByLabel1(axses_case[j], case, fieldName, p, allProbePosition, colorList[i])                
                elif j == 2:
                    if allProbePosition[p] >= 24:
                        std[i,j], mean[i,j] = userProbeByLabel(axses_case[j], case, fieldName, p, allProbePosition, colorList[i], cut=0.8)
                    else:
                        std[i,j], mean[i,j] = userProbeByLabel(axses_case[j], case, fieldName, p, allProbePosition, colorList[i], cut=0.5)
                elif j ==3 :
                    if allProbePosition[p] >= 24:
                        std[i,j], mean[i,j] = userProbeByLabel(axses_case[j], case, fieldName, p, allProbePosition, colorList[i], cut=0.8)
                    else:
                        std[i,j], mean[i,j] = userProbeByLabel(axses_case[j], case, fieldName, p, allProbePosition, colorList[i], cut=0.5)
                else :
                    print "There's a big problem"
        
#        spatial_mean_rms(fieldName, cases, allProbePosition, mean, std, linestyleList, markerList)
        fig.text(0.5, 0.04, r'$t$', ha='center', va='center')
        fig.text(0.87, 0.85, r'$a)$')
        fig.suptitle(r'Time history of $Ux,\, Uy,\, Uz,\, T$ @ position '+str(allProbePosition[p]/8.0)+'D')
        fig.savefig("../PICTURE_history_d/"+"4cases/"+str(allProbePosition[p]/8.0)+"D.png", bbox_inches='tight',dpi=300) # bbox_inches = 'tight' is neccessary

main()
