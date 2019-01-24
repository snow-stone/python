# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 21:08:57 2018

@author: hluo
"""

import numpy as np
import matplotlib.pyplot as plt

def dai_debitMin(fluid):
    switcher={
        'EAU':'water',
        'PAA':'PAA',
        'XG':'XG'
    }
    string = '/home/hluo/Pictures/Dai_T/mixingFactor/debit_min/'+switcher[fluid]+'.csv'
    data=np.genfromtxt(string, skip_header=1, delimiter=',')

    return data[:,0], data[:,1]
    
def dai_debitMoyen(fluid):
    switcher={
        'EAU':'water',
        'PAA':'PAA',
        'XG':'XG'
    }
    string = '/home/hluo/Pictures/Dai_T/mixingFactor/debit_moyen/'+switcher[fluid]+'.csv'
    data=np.genfromtxt(string, skip_header=1, delimiter=',')

    return data[:,0], data[:,1]
#==============================================================================
# 
# impinging plot using 0.8 as reference value
# 
#==============================================================================
def plotSlice_0p8(ax, sliceNumber, path2Data, dataDir, cut=0.5, ifPlotInter=True):
    data = np.genfromtxt(path2Data+"/"+dataDir+"/"+"userDefinedLog/slice"+str(sliceNumber)+"_mean_rms_Dai_0p8")
    
    time = data[:,0]
    cutSliceIndex = int(cut*len(time))
    
    if ifPlotInter :
        p = ax.plot(time[cutSliceIndex:],data[cutSliceIndex:,2])
        ax.plot(time[:cutSliceIndex],data[:cutSliceIndex,2],linestyle=':',color=p[0].get_color())
        ax.legend(bbox_to_anchor=(1.3, 1), ncol=1, shadow=True)
        ax.set_title(dataDir)
    else :
        print "====================="
        print "No intermediate plots"
        print "====================="
    
    return np.mean(data[cutSliceIndex:,1]),np.mean(data[cutSliceIndex:,2])

def plotCaseWithSlices_0p8_mean(ax_cases, path2Data, dataDir, positionList, aliasDict, markerDict, colorDict, cut, ifPlotInter):
    meanOfMEAN = np.zeros(len(positionList))
    meanOfRMS = np.zeros(len(positionList))
    
    fig, ax_in_case = plt.subplots()
    for i, position in enumerate(positionList):
        meanOfMEAN[i], meanOfRMS[i] = plotSlice_0p8(ax_in_case, position, path2Data, dataDir, cut, ifPlotInter)

    print aliasDict[dataDir]+" :"
    print "mean : "
    print meanOfMEAN
    print "rms : "
    print meanOfRMS
    positionList = np.asarray(positionList)
    ax_cases.axhline(y=0.8, linestyle=':', color='black')
    ax_cases.axhline(y=0.5, linestyle=':', color='black')
    ax_cases.plot(positionList/8.0, meanOfMEAN, label=aliasDict[dataDir], marker=markerDict[dataDir], color=colorDict[dataDir], markeredgecolor=colorDict[dataDir], markerfacecolor='none')
#    ax_cases.errorbar(positionList/8.0, meanOfMEAN, yerr=meanOfRMS, label=aliasDict[dataDir], marker=marker)
    
def plotCaseWithSlices_0p8_rms(ax_cases, path2Data, dataDir, positionList, aliasDict, markerDict, colorDict, cut, ifPlotInter):
    meanOfMEAN = np.zeros(len(positionList))
    meanOfRMS = np.zeros(len(positionList))
    
    fig, ax_in_case = plt.subplots()
    for i, position in enumerate(positionList):
        meanOfMEAN[i], meanOfRMS[i] = plotSlice_0p8(ax_in_case, position, path2Data, dataDir, cut, ifPlotInter)
        
    positionList = np.asarray(positionList)
    ax_cases.plot(positionList/8.0,meanOfRMS, label=aliasDict[dataDir], marker=markerDict[dataDir], color=colorDict[dataDir], markeredgecolor=colorDict[dataDir], markerfacecolor='none')
    
def plotCaseWithSlices_0p8_MI(ax_cases, path2Data, dataDir, positionList, aliasDict, markerDict, colorDict, cut, ifPlotInter):
    meanOfMEAN = np.zeros(len(positionList))
    meanOfRMS = np.zeros(len(positionList))
    
    fig, ax_in_case = plt.subplots()
    for i, position in enumerate(positionList):
        meanOfMEAN[i], meanOfRMS[i] = plotSlice_0p8(ax_in_case, position, path2Data, dataDir, cut, ifPlotInter)
        
    positionList = np.asarray(positionList)
    ax_cases.plot(positionList/8.0, meanOfRMS/meanOfRMS[0], label=aliasDict[dataDir], marker=markerDict[dataDir], color=colorDict[dataDir], markeredgecolor=colorDict[dataDir], markerfacecolor='none')

#==============================================================================
# 
# Dai plot using 0.5 as reference value
# 
#==============================================================================
def plotSlice_Dai(ax, sliceNumber, path2Data, dataDir, cut=0.5, ifPlotInter=True):
    data = np.genfromtxt(path2Data+"/"+dataDir+"/"+"userDefinedLog/slice"+str(sliceNumber)+"_mean_rms_Dai")

    time = data[:,0]
    cutSliceIndex = int(cut*len(time))
    
    if ifPlotInter :
        p = ax.plot(time[cutSliceIndex:],data[cutSliceIndex:,2])
        ax.plot(time[:cutSliceIndex],data[:cutSliceIndex,2],linestyle=':',color=p[0].get_color())
        ax.legend(bbox_to_anchor=(1.3, 1), ncol=1, shadow=True)
        ax.set_title(dataDir)
    else :
        print "====================="
        print "No intermediate plots"
        print "====================="
    
    return np.mean(data[cutSliceIndex:,1]),np.mean(data[cutSliceIndex:,2])

def plotCaseWithSlices_Dai_mean(ax_cases, path2Data, dataDir, positionList, aliasDict, markerDict, colorDict, cut, ifPlotInter):
    meanOfMEAN = np.zeros(len(positionList))
    meanOfRMS = np.zeros(len(positionList))
    
    fig, ax_in_case = plt.subplots()
    for i, position in enumerate(positionList):
        meanOfMEAN[i], meanOfRMS[i] = plotSlice_Dai(ax_in_case, position, path2Data, dataDir, cut, ifPlotInter)

    print aliasDict[dataDir]+" :"
    print "mean : "
    print meanOfMEAN
    print "rms : "
    print meanOfRMS
    positionList = np.asarray(positionList)
    ax_cases.axhline(y=0.8, linestyle=':', color='black')
    ax_cases.axhline(y=0.5, linestyle=':', color='black')
    ax_cases.plot(positionList/8.0, meanOfMEAN, label=aliasDict[dataDir], marker=markerDict[dataDir], color=colorDict[dataDir], markeredgecolor=colorDict[dataDir], markerfacecolor='none')

def plotCaseWithSlices_Dai_rms(ax_cases, path2Data, dataDir, positionList, aliasDict, markerDict, colorDict, cut, ifPlotInter):
    meanOfMEAN = np.zeros(len(positionList))
    meanOfRMS = np.zeros(len(positionList))
    
    fig, ax_in_case = plt.subplots()
    for i, position in enumerate(positionList):
        meanOfMEAN[i], meanOfRMS[i] = plotSlice_Dai(ax_in_case, position, path2Data, dataDir, cut, ifPlotInter)
        
    positionList = np.asarray(positionList)
    ax_cases.plot(positionList/8.0,meanOfRMS, label=aliasDict[dataDir], marker=markerDict[dataDir], color=colorDict[dataDir], markeredgecolor=colorDict[dataDir], markerfacecolor='none')
    
def plotCaseWithSlices_Dai_MI(ax_cases, path2Data, dataDir, positionList, aliasDict, markerDict, colorDict, cut, ifPlotInter):
    meanOfMEAN = np.zeros(len(positionList))
    meanOfRMS = np.zeros(len(positionList))
    
    fig, ax_in_case = plt.subplots()
    for i, position in enumerate(positionList):
        meanOfMEAN[i], meanOfRMS[i] = plotSlice_Dai(ax_in_case, position, path2Data, dataDir, cut, ifPlotInter)
        
    positionList = np.asarray(positionList)
    ax_cases.plot(positionList/8.0, meanOfRMS/meanOfRMS[0], label=aliasDict[dataDir], marker=markerDict[dataDir], color=colorDict[dataDir], markeredgecolor=colorDict[dataDir], markerfacecolor='none')

#==============================================================================
#
#   local mean
#
#==============================================================================

def plotSlice_local(ax, sliceNumber, path2Data, dataDir, cut=0.5, ifPlotInter=True):
    data = np.genfromtxt(path2Data+"/"+dataDir+"/"+"userDefinedLog/slice"+str(sliceNumber)+"_mean_rms")
    
    time = data[:,0]
    cutSliceIndex = int(cut*len(time))
    
    if ifPlotInter :
        p = ax.plot(time[cutSliceIndex:],data[cutSliceIndex:,2])
        ax.plot(time[:cutSliceIndex],data[:cutSliceIndex,2],linestyle=':',color=p[0].get_color())
        ax.legend(bbox_to_anchor=(1.3, 1), ncol=1, shadow=True)
        ax.set_title(dataDir)
    else :
        print "====================="
        print "No intermediate plots"
        print "====================="
    
    return np.mean(data[cutSliceIndex:,1]),np.mean(data[cutSliceIndex:,2])

def plotCaseWithSlices_local_mean(ax_cases, path2Data, dataDir, positionList, aliasDict, markerDict, colorDict, cut, ifPlotInter):
    meanOfMEAN = np.zeros(len(positionList))
    meanOfRMS = np.zeros(len(positionList))
    
    fig, ax_in_case = plt.subplots()
    for i, position in enumerate(positionList):
        meanOfMEAN[i], meanOfRMS[i] = plotSlice_local(ax_in_case, position, path2Data, dataDir, cut, ifPlotInter)

    print aliasDict[dataDir]+" :"
    print "mean : "
    print meanOfMEAN
    print "rms : "
    print meanOfRMS
    positionList = np.asarray(positionList)
    ax_cases.axhline(y=0.8, linestyle=':', color='black')
    ax_cases.axhline(y=0.5, linestyle=':', color='black')
    ax_cases.plot(positionList/8.0, meanOfMEAN, label=aliasDict[dataDir], marker=markerDict[dataDir], color=colorDict[dataDir], markeredgecolor=colorDict[dataDir], markerfacecolor='none')
#    ax_cases.errorbar(positionList/8.0, meanOfMEAN, yerr=meanOfRMS, label=aliasDict[dataDir], marker=marker)
    
def plotCaseWithSlices_local_rms(ax_cases, path2Data, dataDir, positionList, aliasDict, markerDict, colorDict, cut, ifPlotInter):
    meanOfMEAN = np.zeros(len(positionList))
    meanOfRMS = np.zeros(len(positionList))
    
    fig, ax_in_case = plt.subplots()
    for i, position in enumerate(positionList):
        meanOfMEAN[i], meanOfRMS[i] = plotSlice_local(ax_in_case, position, path2Data, dataDir, cut, ifPlotInter)
        
    positionList = np.asarray(positionList)
    ax_cases.plot(positionList/8.0,meanOfRMS, label=aliasDict[dataDir], marker=markerDict[dataDir], color=colorDict[dataDir], markeredgecolor=colorDict[dataDir], markerfacecolor='none')
    
def plotCaseWithSlices_local_MI(ax_cases, path2Data, dataDir, positionList, aliasDict, markerDict, colorDict, cut, ifPlotInter):
    meanOfMEAN = np.zeros(len(positionList))
    meanOfRMS = np.zeros(len(positionList))
    
    fig, ax_in_case = plt.subplots()
    for i, position in enumerate(positionList):
        meanOfMEAN[i], meanOfRMS[i] = plotSlice_local(ax_in_case, position, path2Data, dataDir, cut, ifPlotInter)
        
    positionList = np.asarray(positionList)
    ax_cases.plot(positionList/8.0, meanOfRMS/meanOfRMS[0], label=aliasDict[dataDir], marker=markerDict[dataDir], color=colorDict[dataDir], markeredgecolor=colorDict[dataDir], markerfacecolor='none')


def Figure_ref_0p5(caseList, path2Data, saveFigDir):
    print "REAME :"
    print "This is the version using 0.5 as reference value for all cases thus"
    print "letting 2 impinging cases a almost constant rms"
#    positionList = [0,1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72,73,74,75]
    positionList = [1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72,73,74,75]
    
    aliasDict={
        "BirdCarreau/inlet_0p3"                :r'$NN^{1}_{d}$',
        "Newtonian/Re2400"                     :r'$N^{1}_{d}$',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1":r'$NN^{1}_{d,St=1}$',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5":r'$NN^{1}_{d,St=5}$',
        "BirdCarreau/inlet_0p5"                :r'$NN^{2}_{d}$',
        "Newtonian/Re4000"                     :r'$N^{2}_{d}$',
        "BirdCarreau/inlet0p5_impinging"       :r'$NN^{2}_{i}$',
        "Newtonian/Re4000_impinging"           :r'$N^{2}_{i}$'
    }
    
    colorDict={
        "BirdCarreau/inlet_0p3"                : 'red',
        "Newtonian/Re2400"                     : 'blue',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1": 'red',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5": 'red',
        "BirdCarreau/inlet_0p5"                : 'red',
        "Newtonian/Re4000"                     : 'blue',
        "BirdCarreau/inlet0p5_impinging"       : 'red',
        "Newtonian/Re4000_impinging"           : 'blue'
    }
    
    markerDict={
        "BirdCarreau/inlet_0p3"                : 's',
        "Newtonian/Re2400"                     : 's',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1": '^',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5": 'v',
        "BirdCarreau/inlet_0p5"                : 'o',
        "Newtonian/Re4000"                     : 'o',
        "BirdCarreau/inlet0p5_impinging"       : 'x',
        "Newtonian/Re4000_impinging"           : 'x'
    }
    
    aliasDict_Dai={
        'Dai/inlet_0p5' : r'$exp(NN^{1}_{d})$',
        'Dai/Re4000'    : r'$exp(N^{1}_{d})$',
        'Dai/inlet_0p3' : r'$exp(NN^{2}_{d})$',
        'Dai/Re2400'    : r'$exp(N^{2}_{d})$'
    }
    
#    fig, ax_principle0 = plt.subplots()
    fig, axes = plt.subplots(3, 1, sharex=True, figsize=(10,10))

    for i, caseDir in enumerate(caseList):
        print "caseDir : ", caseDir
#        plotCaseWithSlices_local_mean(axes[0], path2Data, caseDir, positionList, aliasDict, markerDict, colorDict, cut=0.7, ifPlotInter=False)
        plotCaseWithSlices_Dai_mean(axes[0], path2Data, caseDir, positionList, aliasDict, markerDict, colorDict, cut=0.7, ifPlotInter=False)
    
    axes[0].set_xlabel(r"$x/D$")
    axes[0].set_ylabel(r"$T_{ref}$")
#    ax_principle0.set_title(r"$statistics \quad on \quad slices$")
    axes[0].set_ylim(0.2,0.9)
#    ax_principle.set_xlim(0,40)
    axes[0].legend(bbox_to_anchor=(1, 1), ncol=2, shadow=True)
    
#    x_XG1, y_XG1 = dai_debitMoyen('XG')
#    ax_principle.plot(x_XG1,y_XG1,label=aliasDict_Dai['Dai/inlet_0p5'],linestyle='-',marker='s',fillstyle='none')    
#    x_water1, y_water1 = dai_debitMoyen('EAU')    
#    ax_principle.plot(x_water1,y_water1,label=aliasDict_Dai['Dai/Re4000'],linestyle='-',marker='^',fillstyle='none')
#
#    x_XG0, y_XG0 = dai_debitMin('XG')
#    ax_principle.plot(x_XG0,y_XG0,label=aliasDict_Dai['Dai/inlet_0p3'],linestyle='-',marker='d',fillstyle='none')    
#    x_water0, y_water0 = dai_debitMin('EAU')    
#    ax_principle.plot(x_water0,y_water0,label=aliasDict_Dai['Dai/Re2400'],linestyle='-',marker='v',fillstyle='none')

#    fig.savefig(path2Data+"/"+saveFigDir+'/mean_rms.png', bbox_inches='tight')
    
#    fig, ax_principle1 = plt.subplots()

    for i, caseDir in enumerate(caseList):
        print "caseDir : ", caseDir
#        plotCaseWithSlices_local_rms(axes[1], path2Data, caseDir, positionList, aliasDict, markerDict, colorDict, cut=0.7, ifPlotInter=False)
        plotCaseWithSlices_Dai_rms(axes[1], path2Data, caseDir, positionList, aliasDict, markerDict, colorDict, cut=0.7, ifPlotInter=False)
        
    axes[1].set_xlabel(r"$x/D$")
    axes[1].set_ylabel(r"$[<T-T_{ref}>_{(y,z)}^2]^{1/2}$")
#    axes[1].legend(bbox_to_anchor=(1, 1), ncol=2, shadow=True)
#    axes[1].set_ylim(0,0.25)
#    fig.savefig(path2Data+"/"+saveFigDir+'/rms.png', bbox_inches='tight')

#    fig, ax_principle2 = plt.subplots()

    for i, caseDir in enumerate(caseList):
        print "caseDir : ", caseDir
#        plotCaseWithSlices_local_MI(axes[2], path2Data, caseDir, positionList, aliasDict, markerDict, colorDict, cut=0.7, ifPlotInter=False)
        plotCaseWithSlices_Dai_MI(axes[2], path2Data, caseDir, positionList, aliasDict, markerDict, colorDict, cut=0.7, ifPlotInter=False)
        
    axes[2].set_xlabel(r"$x/D$")
    axes[2].set_ylabel(r"$\frac{[<T-T_{ref}>_{(y,z)}^2]^{1/2}}{[<T-T_{ref}>_{(y,z)}^2]^{1/2}|_{x=0}}$")
#    axes[2].legend(bbox_to_anchor=(1, 1), ncol=2, shadow=True)
#    ax_principle2.set_ylim(0,1.0)
#    fig.savefig(path2Data+"/"+saveFigDir+'/mixing.png', bbox_inches='tight')
    fig.savefig(path2Data+"/"+saveFigDir+'/mixing_ref_0p5.png', bbox_inches='tight')

def Figure_ref_local(caseList, path2Data, saveFigDir):
    print "README :"
    print "This is the version where we take slice averaged value as reference"
    print "to calculate rms, resulting in a monotone decreasing rms (far from "
    print "junction) for all cases"
#    positionList = [0,1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72,73,74,75]
    positionList = [1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72,73,74,75]
    
    aliasDict={
        "BirdCarreau/inlet_0p3"                :r'$NN^{1}_{d}$',
        "Newtonian/Re2400"                     :r'$N^{1}_{d}$',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1":r'$NN^{1}_{d,St=1}$',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5":r'$NN^{1}_{d,St=5}$',
        "BirdCarreau/inlet_0p5"                :r'$NN^{2}_{d}$',
        "Newtonian/Re4000"                     :r'$N^{2}_{d}$',
        "BirdCarreau/inlet0p5_impinging"       :r'$NN^{2}_{i}$',
        "Newtonian/Re4000_impinging"           :r'$N^{2}_{i}$'
    }
    
    colorDict={
        "BirdCarreau/inlet_0p3"                : 'red',
        "Newtonian/Re2400"                     : 'blue',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1": 'red',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5": 'red',
        "BirdCarreau/inlet_0p5"                : 'red',
        "Newtonian/Re4000"                     : 'blue',
        "BirdCarreau/inlet0p5_impinging"       : 'red',
        "Newtonian/Re4000_impinging"           : 'blue'
    }
    
    markerDict={
        "BirdCarreau/inlet_0p3"                : 's',
        "Newtonian/Re2400"                     : 's',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1": '^',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5": 'v',
        "BirdCarreau/inlet_0p5"                : 'o',
        "Newtonian/Re4000"                     : 'o',
        "BirdCarreau/inlet0p5_impinging"       : 'x',
        "Newtonian/Re4000_impinging"           : 'x'
    }
    
    aliasDict_Dai={
        'Dai/inlet_0p5' : r'$exp(NN^{1}_{d})$',
        'Dai/Re4000'    : r'$exp(N^{1}_{d})$',
        'Dai/inlet_0p3' : r'$exp(NN^{2}_{d})$',
        'Dai/Re2400'    : r'$exp(N^{2}_{d})$'
    }
    
#    fig, ax_principle0 = plt.subplots()
    fig, axes = plt.subplots(3, 1, sharex=True, figsize=(10,10))

    for i, caseDir in enumerate(caseList):
        print "caseDir : ", caseDir
        plotCaseWithSlices_local_mean(axes[0], path2Data, caseDir, positionList, aliasDict, markerDict, colorDict, cut=0.7, ifPlotInter=False)
#        plotCaseWithSlices_Dai_mean(axes[0], path2Data, caseDir, positionList, aliasDict, markerDict, colorDict, cut=0.7, ifPlotInter=False)
    
    axes[0].set_xlabel(r"$x/D$")
    axes[0].set_ylabel(r"$T_{ref}$")
#    ax_principle0.set_title(r"$statistics \quad on \quad slices$")
    axes[0].set_ylim(0.2,0.9)
#    ax_principle.set_xlim(0,40)
    axes[0].legend(bbox_to_anchor=(1, 1), ncol=2, shadow=True)
    
#    x_XG1, y_XG1 = dai_debitMoyen('XG')
#    ax_principle.plot(x_XG1,y_XG1,label=aliasDict_Dai['Dai/inlet_0p5'],linestyle='-',marker='s',fillstyle='none')    
#    x_water1, y_water1 = dai_debitMoyen('EAU')    
#    ax_principle.plot(x_water1,y_water1,label=aliasDict_Dai['Dai/Re4000'],linestyle='-',marker='^',fillstyle='none')
#
#    x_XG0, y_XG0 = dai_debitMin('XG')
#    ax_principle.plot(x_XG0,y_XG0,label=aliasDict_Dai['Dai/inlet_0p3'],linestyle='-',marker='d',fillstyle='none')    
#    x_water0, y_water0 = dai_debitMin('EAU')    
#    ax_principle.plot(x_water0,y_water0,label=aliasDict_Dai['Dai/Re2400'],linestyle='-',marker='v',fillstyle='none')

#    fig.savefig(path2Data+"/"+saveFigDir+'/mean_rms.png', bbox_inches='tight')
    
#    fig, ax_principle1 = plt.subplots()

    for i, caseDir in enumerate(caseList):
        print "caseDir : ", caseDir
        plotCaseWithSlices_local_rms(axes[1], path2Data, caseDir, positionList, aliasDict, markerDict, colorDict, cut=0.7, ifPlotInter=False)
#        plotCaseWithSlices_Dai_rms(axes[1], path2Data, caseDir, positionList, aliasDict, markerDict, colorDict, cut=0.7, ifPlotInter=False)
        
    axes[1].set_xlabel(r"$x/D$")
    axes[1].set_ylabel(r"$[<T-T_{ref}>_{(y,z)}^2]^{1/2}$")
#    axes[1].legend(bbox_to_anchor=(1, 1), ncol=2, shadow=True)
#    axes[1].set_ylim(0,0.25)
#    fig.savefig(path2Data+"/"+saveFigDir+'/rms.png', bbox_inches='tight')

#    fig, ax_principle2 = plt.subplots()

    for i, caseDir in enumerate(caseList):
        print "caseDir : ", caseDir
        plotCaseWithSlices_local_MI(axes[2], path2Data, caseDir, positionList, aliasDict, markerDict, colorDict, cut=0.7, ifPlotInter=False)
#        plotCaseWithSlices_Dai_MI(axes[2], path2Data, caseDir, positionList, aliasDict, markerDict, colorDict, cut=0.7, ifPlotInter=False)
        
    axes[2].set_xlabel(r"$x/D$")
    axes[2].set_ylabel(r"$\frac{[<T-T_{ref}>_{(y,z)}^2]^{1/2}}{[<T-T_{ref}>_{(y,z)}^2]^{1/2}|_{x=0}}$")
#    axes[2].legend(bbox_to_anchor=(1, 1), ncol=2, shadow=True)
#    ax_principle2.set_ylim(0,1.0)
#    fig.savefig(path2Data+"/"+saveFigDir+'/mixing.png', bbox_inches='tight')
    fig.savefig(path2Data+"/"+saveFigDir+'/mixing_ref_local.png', bbox_inches='tight')
    
def plotFor_caseList(caseList, path2Data, saveFigDir):
#    positionList = [0,1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72,73,74,75]
    positionList = [1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72,73,74,75]
    
    aliasDict={
        "BirdCarreau/inlet_0p3"                :r'$NN^{1}_{d}$',
        "Newtonian/Re2400"                     :r'$N^{1}_{d}$',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1":r'$NN^{1}_{d,St=1}$',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5":r'$NN^{1}_{d,St=5}$',
        "BirdCarreau/inlet_0p5"                :r'$NN^{2}_{d}$',
        "Newtonian/Re4000"                     :r'$N^{2}_{d}$',
        "BirdCarreau/inlet0p5_impinging"       :r'$NN^{2}_{i}$',
        "Newtonian/Re4000_impinging"           :r'$N^{2}_{i}$'
    }
    
    colorDict={
        "BirdCarreau/inlet_0p3"                : 'red',
        "Newtonian/Re2400"                     : 'blue',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1": 'red',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5": 'red',
        "BirdCarreau/inlet_0p5"                : 'red',
        "Newtonian/Re4000"                     : 'blue',
        "BirdCarreau/inlet0p5_impinging"       : 'red',
        "Newtonian/Re4000_impinging"           : 'blue'
    }
    
    markerDict={
        "BirdCarreau/inlet_0p3"                : 's',
        "Newtonian/Re2400"                     : 's',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1": '^',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5": 'v',
        "BirdCarreau/inlet_0p5"                : 'o',
        "Newtonian/Re4000"                     : 'o',
        "BirdCarreau/inlet0p5_impinging"       : 'x',
        "Newtonian/Re4000_impinging"           : 'x'
    }
    
    aliasDict_Dai={
        'Dai/inlet_0p5' : r'$exp(NN^{1}_{d})$',
        'Dai/Re4000'    : r'$exp(N^{1}_{d})$',
        'Dai/inlet_0p3' : r'$exp(NN^{2}_{d})$',
        'Dai/Re2400'    : r'$exp(N^{2}_{d})$'
    }
    
#    fig, ax_principle0 = plt.subplots()
    fig, axes = plt.subplots(3, 1, sharex=True, figsize=(10,10))

    for i, caseDir in enumerate(caseList):
        print "caseDir : ", caseDir
#        plotCaseWithSlices_local_mean(axes[0], path2Data, caseDir, positionList, aliasDict, markerDict, colorDict, cut=0.7, ifPlotInter=False)
        plotCaseWithSlices_Dai_mean(axes[0], path2Data, caseDir, positionList, aliasDict, markerDict, colorDict, cut=0.7, ifPlotInter=False)
    
    axes[0].set_xlabel(r"$x/D$")
    axes[0].set_ylabel(r"$T_{ref}$")
#    ax_principle0.set_title(r"$statistics \quad on \quad slices$")
    axes[0].set_ylim(0.2,0.9)
#    ax_principle.set_xlim(0,40)
    axes[0].legend(bbox_to_anchor=(1, 1), ncol=2, shadow=True)
    
#    x_XG1, y_XG1 = dai_debitMoyen('XG')
#    ax_principle.plot(x_XG1,y_XG1,label=aliasDict_Dai['Dai/inlet_0p5'],linestyle='-',marker='s',fillstyle='none')    
#    x_water1, y_water1 = dai_debitMoyen('EAU')    
#    ax_principle.plot(x_water1,y_water1,label=aliasDict_Dai['Dai/Re4000'],linestyle='-',marker='^',fillstyle='none')
#
#    x_XG0, y_XG0 = dai_debitMin('XG')
#    ax_principle.plot(x_XG0,y_XG0,label=aliasDict_Dai['Dai/inlet_0p3'],linestyle='-',marker='d',fillstyle='none')    
#    x_water0, y_water0 = dai_debitMin('EAU')    
#    ax_principle.plot(x_water0,y_water0,label=aliasDict_Dai['Dai/Re2400'],linestyle='-',marker='v',fillstyle='none')

#    fig.savefig(path2Data+"/"+saveFigDir+'/mean_rms.png', bbox_inches='tight')
    
#    fig, ax_principle1 = plt.subplots()

    for i, caseDir in enumerate(caseList):
        print "caseDir : ", caseDir
#        plotCaseWithSlices_local_rms(axes[1], path2Data, caseDir, positionList, aliasDict, markerDict, colorDict, cut=0.7, ifPlotInter=False)
        plotCaseWithSlices_Dai_rms(axes[1], path2Data, caseDir, positionList, aliasDict, markerDict, colorDict, cut=0.7, ifPlotInter=False)
        
    axes[1].set_xlabel(r"$x/D$")
    axes[1].set_ylabel(r"$[<T-T_{ref}>_{(y,z)}^2]^{1/2}$")
#    axes[1].legend(bbox_to_anchor=(1, 1), ncol=2, shadow=True)
#    axes[1].set_ylim(0,0.25)
#    fig.savefig(path2Data+"/"+saveFigDir+'/rms.png', bbox_inches='tight')

#    fig, ax_principle2 = plt.subplots()

    for i, caseDir in enumerate(caseList):
        print "caseDir : ", caseDir
#        plotCaseWithSlices_local_MI(axes[2], path2Data, caseDir, positionList, aliasDict, markerDict, colorDict, cut=0.7, ifPlotInter=False)
        plotCaseWithSlices_Dai_MI(axes[2], path2Data, caseDir, positionList, aliasDict, markerDict, colorDict, cut=0.7, ifPlotInter=False)
        
    axes[2].set_xlabel(r"$x/D$")
    axes[2].set_ylabel(r"$\frac{[<T-T_{ref}>_{(y,z)}^2]^{1/2}}{[<T-T_{ref}>_{(y,z)}^2]^{1/2}|_{x=0}}$")
#    axes[2].legend(bbox_to_anchor=(1, 1), ncol=2, shadow=True)
#    ax_principle2.set_ylim(0,1.0)
#    fig.savefig(path2Data+"/"+saveFigDir+'/mixing.png', bbox_inches='tight')
    fig.savefig(path2Data+"/"+saveFigDir+'/mixing_Dai.png', bbox_inches='tight')
    
def main():
    plt.style.use('seaborn-white')
    plt.rcParams['font.size'] = 20
    plt.rcParams['legend.fontsize'] = 12 # overwriting fontsize in legend
    plt.rcParams["legend.columnspacing"] = 1 # mesured in fontsize unit : 1 means = legend.fontsize
#    plt.rcParams['figure.titlesize'] = 20
    plt.rcParams['savefig.dpi'] = 100

    path2Data = "/store/8simu_tmp/shape_square/2a_3_T/python_postProcessing"
    
#   non-newtonian
    caseList1=[
                "BirdCarreau/inlet_0p3",
                "BirdCarreau/inlet_0p5",
                "Newtonian/Re2400",
                "Newtonian/Re4000"
              ]
#    impinging
    caseList2=["BirdCarreau/inlet_0p5",
              "BirdCarreau/inlet0p5_impinging",
              "Newtonian/Re4000",
              "Newtonian/Re4000_impinging"]
#    forcing
    caseList3=["BirdCarreau/inlet_0p3",
              "BirdCarreau/inlet_0p3-a_0p5-setT_St_1",  
              "BirdCarreau/inlet_0p3-a_0p5-setT_St_5"
             ]
#   all except for forcing
    caseList=[
                "BirdCarreau/inlet_0p3",
                "BirdCarreau/inlet_0p5",
                "BirdCarreau/inlet0p5_impinging",
                "Newtonian/Re2400",
                "Newtonian/Re4000",
                "Newtonian/Re4000_impinging"
              ]
    
    figDir = 'PICTURE_mixingFactor'
#    plotFor_caseList(caseList1, path2Data, figDir+'/'+'non-newtonian')
#    plotFor_caseList(caseList2, path2Data, figDir+'/'+'impinging')
#    plotFor_caseList(caseList3, path2Data, figDir+'/'+'forcing')
    Figure_ref_0p5(caseList, path2Data, figDir+'/')
    Figure_ref_local(caseList, path2Data, figDir+'/')

main()
