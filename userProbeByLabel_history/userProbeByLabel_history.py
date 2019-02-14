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
    time = rawData[:,0]
    probeData = rawData[:,1:]
    
    position_in_D = str(positions[sample]/8.0)+"D"
    std = np.std(probeData[:,sample])
    mean = np.mean(probeData[:,sample])
    cutSliceIndex=int(0.6*len(time))
    ax.plot(time[:cutSliceIndex], probeData[:cutSliceIndex,sample], color=color, linewidth=1, label=caseName+"_"+position_in_D+"\nNbSampleEq_"+str(len(time[:])), linestyle='-')   

    RelativeDataFile = "./"+"userDefinedLog/history_labelGroup_"+fieldName
    rawData = np.genfromtxt(path2Data+"/"+caseName+'/'+RelativeDataFile)
    time = rawData[:,0]+0.2
    probeData = rawData[:,1:]
    cutSliceIndex = int(cut*len(time))
    
    position_in_D = str(positions[sample]/8.0)+"D"
    std = np.std(probeData[cutSliceIndex:,sample])
    mean = np.mean(probeData[cutSliceIndex:,sample])
    ax.plot(time[cutSliceIndex:], probeData[cutSliceIndex:,sample], color=color, linewidth=2, label=caseName+"_"+position_in_D+"\nNbSampleEq_"+str(len(time[cutSliceIndex:])), linestyle='-')
    ax.plot(time[:cutSliceIndex], probeData[:cutSliceIndex,sample], color=color, linewidth=1)    

    return std, mean

def userProbeByLabel(ax, caseName, path2Data, fieldName, sample, positions, color, cut=0.5):
    RelativeDataFile = "./"+"userDefinedLog/history_labelGroup_"+fieldName
    rawData = np.genfromtxt(path2Data+"/"+caseName+'/'+RelativeDataFile)
    time = rawData[:,0]
    probeData = rawData[:,1:]
    cutSliceIndex = int(cut*len(time))
    
    position_in_D = str(positions[sample]/8.0)+"D"
    std = np.std(probeData[cutSliceIndex:,sample])
    mean = np.mean(probeData[cutSliceIndex:,sample])
    ax.plot(time[cutSliceIndex:], probeData[cutSliceIndex:,sample], color=color, linewidth=2, label=caseName+"_"+position_in_D+"\nNbSampleEq_"+str(len(time[cutSliceIndex:])), linestyle='-')
    ax.plot(time[:cutSliceIndex], probeData[:cutSliceIndex,sample], color=color, linewidth=1)    
    
    return std, mean

def main():
    plt.style.use('seaborn-white') # from defaut
    plt.rcParams.update({'font.size': 25})
    plt.rcParams['savefig.dpi'] = 100
    
    from matplotlib import rc
#    rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
    ## for Palatino and other serif fonts use:
    rc('font',**{'family':'serif','serif':['Palatino']})
    rc('text', usetex=True)

    print "README"
    print "postProcessing data using output from : "
    print "userProbeByLabelVector_noMean ; userProbeByLabelScalar_noMean"
    allProbePosition = [0,1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72]
    #       sampling = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    positionSubSet = [0,13,15,17]
    #positionSubSet =  [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    
    path2Data="/store/8simu_tmp/shape_square/2a_3_T/python_postProcessing"
    cases = [
             "BirdCarreau"+"/"+"inlet_0p3",
             "Newtonian"+"/"+"Re2400",
             "BirdCarreau/inlet_0p3-a_0p5-setT_St_1",
		    "BirdCarreau/inlet_0p3-a_0p5-setT_St_5",
             "BirdCarreau"+"/"+"inlet_0p5",
             "Newtonian"+"/"+"Re4000",
             "BirdCarreau/inlet0p5_impinging",
             "Newtonian/Re4000_impinging"
            ]

    fieldNames=["U_y", "T"]
    
    colorDict = {
                  "U_x" : "blue",
                  "U_y" : "red",
                  "U_z" : "green",
                  "T"   : "black"
                }
    
    cutDict = {
        "BirdCarreau/inlet_0p3"                :0.6,
        "Newtonian/Re2400"                     :0.5,
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1":0.35,
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5":0.46,
        "BirdCarreau/inlet_0p5"                :0.5,
        "Newtonian/Re4000"                     :0.5,
        "BirdCarreau/inlet0p5_impinging"       :0.5,
        "Newtonian/Re4000_impinging"           :0.5
    }

    aliasDict={
        "BirdCarreau/inlet_0p3":r'$NN^{1}_{d}$',
        "Newtonian/Re2400"     :r'$N^{1}_{d}$',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1":r'$NN^{1}_{d,St=1}$',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5":r'$NN^{1}_{d,St=5}$',
        "BirdCarreau/inlet_0p5":r'$NN^{2}_{d}$',
        "Newtonian/Re4000"     :r'$N^{2}_{d}$',
        "BirdCarreau/inlet0p5_impinging"       :r'$NN^{2}_{i}$',
        "Newtonian/Re4000_impinging"           :r'$N^{2}_{i}$'
    }
    
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
                
                if case == "BirdCarreau/inlet_0p3-a_0p5-setT_St_1" or case == "BirdCarreau/inlet_0p3-a_0p5-setT_St_5":
                    std[i,j], mean[i,j] = userProbeByLabel_forcing(axses_case[j], case, path2Data,  fieldName, p, allProbePosition, colorDict[fieldName], cutDict[case])
                else:
                    std[i,j], mean[i,j] = userProbeByLabel(axses_case[j], case, path2Data, fieldName, p, allProbePosition, colorDict[fieldName], cutDict[case])
        
        axses_case[-1].set_xlabel(r'$t$')
        x = 0.82
        yStart = 0.82
        for i, case in enumerate(cases):
            y = yStart - i * 0.0975
            fig.text(x, y, aliasDict[case], fontsize=30)

        fig.savefig(path2Data+"/"+"PICTURE_history/"+"8simu/"+str(allProbePosition[p]/8.0)+"D.png", bbox_inches='tight') # bbox_inches = 'tight' is neccessary

main()
