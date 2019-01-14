# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 21:08:57 2018

@author: hluo
"""

import numpy as np
import matplotlib.pyplot as plt

def userProbeByLabel_forcing(ax, caseName, path2Data, fieldName, sample, positions, color, cut=0.):
    RelativeDataFile = "./"+"userDefinedLog/history_labelGroup_"+fieldName+".old"
    rawData = np.genfromtxt(path2Data+"/"+caseName+'/'+RelativeDataFile)
#    print rawData.shape
    time = rawData[:,0]
    probeData = rawData[:,1:]
    
    position_in_D = str(positions[sample]/8.0)+"D"
    std = np.std(probeData[:,sample])
    mean = np.mean(probeData[:,sample])
#    print position_in_D + " std : ", std, " mean : ", mean
    ax.plot(time, probeData[:,sample], color=color, linewidth=0.5, label=caseName+"_"+position_in_D+"\nNbSampleEq_"+str(len(time[:])), linestyle='-')   

    RelativeDataFile = "./"+"userDefinedLog/history_labelGroup_"+fieldName
    rawData = np.genfromtxt(path2Data+"/"+caseName+'/'+RelativeDataFile)
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

    return std, mean

def userProbeByLabel(ax, caseName, path2Data, fieldName, sample, positions, color, cut=0.5):
    RelativeDataFile = "./"+"userDefinedLog/history_labelGroup_"+fieldName
    rawData = np.genfromtxt(path2Data+"/"+caseName+'/'+RelativeDataFile)
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
#    fig_rms.savefig('../PICTURE_history_e/'+fieldName+'/RMS_xByD_oneFig.png', bbox_inches='tight',  dpi=300)
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
#    fig_rms.savefig('../PICTURE_history_e/'+fieldName+'/Mean_xByD_oneFig.png', bbox_inches='tight', dpi=300)

def main():
    print "README"
    print "postProcessing data using output from : "
    print "userProbeByLabelVector_noMean ; userProbeByLabelScalar_noMean"
    plt.style.use('seaborn-white') # from defaut
    plt.rcParams.update({'font.size': 20})
    allProbePosition = [0,1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72]
    #       sampling = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    positionSubSet = [0,13,15,17]
    #positionSubSet =  [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    
    path2Data="/store/8simu_tmp/shape_square/2a_3_T/python_postProcessing"
    cases = [
             "BirdCarreau"+"/"+"inlet_0p5",
             "Newtonian"+"/"+"Re4000",
             "BirdCarreau/inlet0p5_impinging",
             "Newtonian/Re4000_impinging",
             "BirdCarreau"+"/"+"inlet_0p3",
             "Newtonian"+"/"+"Re2400",
             "BirdCarreau/inlet_0p3-a_0p5-setT_St_1",  # j=6, involving userProbeByLabel_forcing
		   "BirdCarreau/inlet_0p3-a_0p5-setT_St_5",   # j=7, involving userProbeByLabel_forcing
            ]
    
    # it is possible to only show the first 4 cases
#    cases = [
#             "BirdCarreau"+"/"+"inlet_0p5",
#             "Newtonian"+"/"+"Re4000",
#             "BirdCarreau"+"/"+"inlet_0p3",
#             "Newtonian"+"/"+"Re2400"
#            ]
              
    fieldNames=["U_x", "U_y", "U_z", "T"]

    aliasDict={
        "BirdCarreau/inlet_0p5":r'$NN^{1}_{d}$',
        "Newtonian/Re4000"     :r'$N^{1}_{d}$',
        "BirdCarreau/inlet_0p3":r'$NN^{2}_{d}$',
        "Newtonian/Re2400"     :r'$N^{2}_{d}$',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1":r'$NN^{2}_{d,St=1}$',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5":r'$NN^{2}_{d,St=5}$',
        "BirdCarreau/inlet0p5_impinging"       :r'$NN^{1}_{i}$',
        "Newtonian/Re4000_impinging"           :r'$N^{1}_{i}$'
    }
    
    colorList = [
                  "blue",
                  "red",
                  "green",
                  "black"
                ]
    
    for k, position in enumerate(positionSubSet):
        p=positionSubSet[k]
        print "position : " , allProbePosition[p]
        #figsize should be in inches.
        fig, axses_case = plt.subplots(len(cases), 1, sharex=True, figsize=(20,10))# figsize is an additional parameter for class matplotlib.pyplot.subplots: passed by **fig_kw
        mean = np.zeros((len(allProbePosition),len(cases)))
        std = np.zeros((len(allProbePosition),len(cases)))
        for j, case in enumerate(cases):
            for i, fieldName in enumerate(fieldNames):
        #        mean = np.zeros((len(positionList),4))
        #        std = np.zeros((len(positionList),4))
        #        mean, std = plotField(axarr, fieldName, cases, positionList, colorList, samples, field=i)
        #        plotField(axarr, fieldName, cases, positionList, colorList, samples, field=i)
        #        spatial_mean_rms(arrayName, cases, positionList, mean, std, linestyleList, markerList)
                axses_case[j].set_ylim(-0.5,2)
                axses_case[j].set_yticks([0, 1])
                axses_case[j].tick_params(axis='y', direction='in', length=4, width=1.5)
                axses_case[j].set_xlim(0,0.85)
                
                print "axe number = ", j , fieldName
                if j == 0:
                    if allProbePosition[p] >= 7:
                        std[i,j], mean[i,j] = userProbeByLabel(axses_case[j], case, path2Data, fieldName, p, allProbePosition, colorList[i], cut=0.5)
                    else :
                        std[i,j], mean[i,j] = userProbeByLabel(axses_case[j], case, path2Data, fieldName, p, allProbePosition, colorList[i], cut=0.5)
                elif j == 1:
                    if allProbePosition[p] >= 24:
                        std[i,j], mean[i,j] = userProbeByLabel(axses_case[j], case, path2Data, fieldName, p, allProbePosition, colorList[i], cut=0.5)
                    else :
                        std[i,j], mean[i,j] = userProbeByLabel(axses_case[j], case, path2Data, fieldName, p, allProbePosition, colorList[i], cut=0.5)
                elif j == 2 :
                    std[i,j], mean[i,j] = userProbeByLabel(axses_case[j], case, path2Data, fieldName, p, allProbePosition, colorList[i], cut=0.5)
                elif j == 3 :
                    std[i,j], mean[i,j] = userProbeByLabel(axses_case[j], case, path2Data, fieldName, p, allProbePosition, colorList[i], cut=0.5)
                elif j == 4:
                    if allProbePosition[p] >= 24:
                        std[i,j], mean[i,j] = userProbeByLabel(axses_case[j], case, path2Data, fieldName, p, allProbePosition, colorList[i], cut=0.6)
                    else:
                        std[i,j], mean[i,j] = userProbeByLabel(axses_case[j], case, path2Data, fieldName, p, allProbePosition, colorList[i], cut=0.6)
                elif j == 5 :
                    if allProbePosition[p] >= 24:
                        std[i,j], mean[i,j] = userProbeByLabel(axses_case[j], case, path2Data, fieldName, p, allProbePosition, colorList[i], cut=0.5)
                    else:
                        std[i,j], mean[i,j] = userProbeByLabel(axses_case[j], case, path2Data, fieldName, p, allProbePosition, colorList[i], cut=0.5)
                elif j == 6 :
                        std[i,j], mean[i,j] = userProbeByLabel_forcing(axses_case[j], case, path2Data,  fieldName, p, allProbePosition, colorList[i], cut=0.35)
                elif j == 7 :
                        std[i,j], mean[i,j] = userProbeByLabel_forcing(axses_case[j], case, path2Data, fieldName, p, allProbePosition, colorList[i], cut=0.46)                        
                else :
                    print "There's a big problem"
        
#        spatial_mean_rms(fieldName, cases, allProbePosition, mean, std, linestyleList, markerList)
#        fig.text(0.5, 0.04, r'$t$', ha='center', va='center', fontsize=20)
        axses_case[-1].set_xlabel(r'$t$',fontsize=20)
        x = 0.82
        yStart = 0.84
        for i, case in enumerate(cases):
            y = yStart - i * 0.095
            fig.text(x, y, aliasDict[case])

        fig.suptitle(r'Time history of $Ux,\, Uy,\, Uz,\, T$ @ position '+str(allProbePosition[p]/8.0)+'D')
        fig.savefig(path2Data+"/"+"PICTURE_history_e/"+"4cases/"+str(allProbePosition[p]/8.0)+"D.png", bbox_inches='tight',dpi=300) # bbox_inches = 'tight' is neccessary

main()
