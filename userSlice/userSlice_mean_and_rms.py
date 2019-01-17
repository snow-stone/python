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

def plotSlice_old1(ax, sliceNumber, path2Data, dataDir, cut=0.5):
    data = np.genfromtxt(path2Data+"/"+dataDir+"/"+"userDefinedLog/slice"+str(sliceNumber)+"_mean_rms")
    
    time = data[:,0]
    cutSliceIndex = int(cut*len(time))
    
    p = ax.plot(time[cutSliceIndex:],data[cutSliceIndex:,2])
    ax.plot(time[:cutSliceIndex],data[:cutSliceIndex,2],linestyle=':',color=p[0].get_color())
    ax.legend(bbox_to_anchor=(1.3, 1), ncol=1, shadow=True)
    ax.set_title(dataDir)
    
    return np.mean(data[cutSliceIndex:,1]),np.mean(data[cutSliceIndex:,2])

def plotSlice_old(ax, sliceNumber, path2Data, dataDir, cut=0.5, ifPlotInter=True):
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

def plotSlice_Dai(ax, sliceNumber, path2Data, dataDir, cut=0.5):
    data = np.genfromtxt(path2Data+"/"+dataDir+"/"+"userDefinedLog/slice"+str(sliceNumber)+"_mean_rms_Dai")

    time = data[:,0]
    cutSliceIndex = int(cut*len(time))
    
    p = ax.plot(time[cutSliceIndex:],data[cutSliceIndex:,2])
    ax.plot(time[:cutSliceIndex],data[:cutSliceIndex,2],linestyle=':',color=p[0].get_color())
    ax.legend(bbox_to_anchor=(1.3, 1), ncol=1, shadow=True)
    ax.set_title(dataDir)

    print "for slice number : ", sliceNumber
    print "mean : ", np.mean(data[cutSliceIndex:,1])
    
    return np.mean(data[cutSliceIndex:,1]),np.mean(data[cutSliceIndex:,2])

def plotSlice_Dai_0p8(ax, sliceNumber, path2Data, dataDir, cut=0.5):
    data = np.genfromtxt(path2Data+"/"+dataDir+"/"+"userDefinedLog/slice"+str(sliceNumber)+"_mean_rms_Dai_0p8")
    
    time = data[:,0]
    cutSliceIndex = int(cut*len(time))
    
    p = ax.plot(time[cutSliceIndex:],data[cutSliceIndex:,2])
    ax.plot(time[:cutSliceIndex],data[:cutSliceIndex,2],linestyle=':',color=p[0].get_color())
    ax.legend(bbox_to_anchor=(1.3, 1), ncol=1, shadow=True)
    ax.set_title(dataDir)
    
    return np.mean(data[cutSliceIndex:,1]),np.mean(data[cutSliceIndex:,2])

def plotCaseWithSlices_old1(ax_cases, path2Data, dataDir, positionList, marker, aliasDict, cut):
    meanOfMEAN = np.zeros(len(positionList))
    meanOfRMS = np.zeros(len(positionList))
    
    fig, ax_in_case = plt.subplots()
    for i, position in enumerate(positionList):
#        meanOfRMS[i] = plotSlice_old(ax_in_case, position, path2Data, dataDir, cut)
        meanOfMEAN[i], meanOfRMS[i] = plotSlice_old1(ax_in_case, position, path2Data, dataDir, cut)

    print aliasDict[dataDir]+" :"
    print "mean : "
    print meanOfMEAN
    print "rms : "
    print meanOfRMS
    positionList = np.asarray(positionList)
    ax_cases.plot(positionList/8.0, meanOfRMS/meanOfMEAN, label=aliasDict[dataDir], marker=marker)

def plotCaseWithSlices_old_errorbar(ax_cases, path2Data, dataDir, positionList, marker, aliasDict, cut, ifPlotInter):
    meanOfMEAN = np.zeros(len(positionList))
    meanOfRMS = np.zeros(len(positionList))
    
    fig, ax_in_case = plt.subplots()
    for i, position in enumerate(positionList):
        meanOfMEAN[i], meanOfRMS[i] = plotSlice_old(ax_in_case, position, path2Data, dataDir, cut, ifPlotInter)

    print aliasDict[dataDir]+" :"
    print "mean : "
    print meanOfMEAN
    print "rms : "
    print meanOfRMS
    positionList = np.asarray(positionList)
#    ax_cases.plot(positionList/8.0,meanOfRMS, label=aliasDict[dataDir], marker=marker)
    ax_cases.errorbar(positionList/8.0, meanOfMEAN, yerr=meanOfRMS, label=aliasDict[dataDir], marker=marker)
    
def plotCaseWithSlices_old_rms(ax_cases, path2Data, dataDir, positionList, marker, aliasDict, cut, ifPlotInter):
    meanOfMEAN = np.zeros(len(positionList))
    meanOfRMS = np.zeros(len(positionList))
    
    fig, ax_in_case = plt.subplots()
    for i, position in enumerate(positionList):
        meanOfMEAN[i], meanOfRMS[i] = plotSlice_old(ax_in_case, position, path2Data, dataDir, cut, ifPlotInter)
        
    positionList = np.asarray(positionList)
    ax_cases.plot(positionList/8.0,meanOfRMS, label=aliasDict[dataDir], marker=marker)
    
def plotCaseWithSlices_old_MI(ax_cases, path2Data, dataDir, positionList, marker, aliasDict, cut, ifPlotInter):
    meanOfMEAN = np.zeros(len(positionList))
    meanOfRMS = np.zeros(len(positionList))
    
    fig, ax_in_case = plt.subplots()
    for i, position in enumerate(positionList):
        meanOfMEAN[i], meanOfRMS[i] = plotSlice_old(ax_in_case, position, path2Data, dataDir, cut, ifPlotInter)
        
    positionList = np.asarray(positionList)
    ax_cases.plot(positionList/8.0, meanOfRMS/meanOfRMS[0], label=aliasDict[dataDir], marker=marker)
    
def plotCaseWithSlices_Dai(ax_cases, path2Data, dataDir, positionList, marker, aliasDict, cut):
    meanOfMEAN = np.zeros(len(positionList))
    meanOfRMS = np.zeros(len(positionList))
    
    fig, ax_in_case = plt.subplots()
    for i, position in enumerate(positionList):
        meanOfMEAN[i], meanOfRMS[i] = plotSlice_Dai(ax_in_case, position, path2Data, dataDir, cut)

    print aliasDict[dataDir]+" :"
    print "mean : "
    print meanOfMEAN
    print "rms : "
    print meanOfRMS
    positionList = np.asarray(positionList)
#    ax_cases.plot(positionList/8.0,meanOfRMS, label=aliasDict[dataDir], marker=marker)
    ax_cases.errorbar(positionList/8.0, meanOfMEAN, yerr=meanOfRMS, label=aliasDict[dataDir], marker=marker)
    
def plotCaseWithSlices_Dai_0p8(ax_cases, path2Data, dataDir, positionList, marker, aliasDict, cut):
    meanOfMEAN = np.zeros(len(positionList))
    meanOfRMS = np.zeros(len(positionList))
    
    fig, ax_in_case = plt.subplots()
    for i, position in enumerate(positionList):
        meanOfMEAN[i], meanOfRMS[i] = plotSlice_Dai_0p8(ax_in_case, position, path2Data, dataDir, cut)

    positionList = np.asarray(positionList)
    ax_cases.plot(positionList/8.0,meanOfRMS, label=aliasDict[dataDir], marker=marker)
    
def main():
    plt.style.use('seaborn-white')
    plt.rcParams['font.size'] = 20
    plt.rcParams['legend.fontsize'] = 12 # overwriting fontsize in legend
    plt.rcParams["legend.columnspacing"] = 1 # mesured in fontsize unit : 1 means = legend.fontsize
#    plt.rcParams['figure.titlesize'] = 20
    plt.rcParams['savefig.dpi'] = 100
#    caseList=["BirdCarreau/inlet_0p5",
#              "Newtonian/Re4000",
#              "BirdCarreau/inlet_0p3",
#              "Newtonian/Re2400"]
    #impinging
#    caseList=["BirdCarreau/inlet_0p5",
#              "BirdCarreau/inlet0p5_impinging",
#              "Newtonian/Re4000",
#              "Newtonian/Re4000_impinging"]
    #forcing effect
    caseList=["BirdCarreau/inlet_0p3",
             "BirdCarreau/inlet_0p3-a_0p5-setT_St_1",  
		  "BirdCarreau/inlet_0p3-a_0p5-setT_St_5"
             ]

#    positionList = [0,1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72,73,74,75]
    positionList = [1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72,73,74,75]
    path2Data = "/store/8simu_tmp/shape_square/2a_3_T/python_postProcessing"
    
    markerList=["s",
                "^",
                "d",
                "v"
                ]
    
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
    
    aliasDict_Dai={
        'Dai/inlet_0p5' : r'$exp(NN^{1}_{d})$',
        'Dai/Re4000'    : r'$exp(N^{1}_{d})$',
        'Dai/inlet_0p3' : r'$exp(NN^{2}_{d})$',
        'Dai/Re2400'    : r'$exp(N^{2}_{d})$'
    }
    
    fig, ax_principle0 = plt.subplots()

    for i, caseDir in enumerate(caseList):
        print "caseDir : ", caseDir
        plotCaseWithSlices_old_errorbar(ax_principle0, path2Data, caseDir, positionList, markerList[i], aliasDict, cut=0.7, ifPlotInter=False)
#        plotCaseWithSlices_old1(ax_principle, path2Data, caseDir, positionList, markerList[i], aliasDict, cut=0.7)
#        plotCaseWithSlices_Dai(ax_principle, path2Data, caseDir, positionList, markerList[i], aliasDict, cut=0.7)
    
    ax_principle0.set_xlabel(r"$x/D$")
    ax_principle0.set_ylabel(r"$<T>_{slice}$")
    ax_principle0.set_title(r"$statistics \quad on \quad slices$")
    ax_principle0.set_ylim(0,1.)
#    ax_principle.set_xlim(0,40)
    ax_principle0.legend(bbox_to_anchor=(1, 0.8), ncol=2, shadow=True)
    
#    x_XG1, y_XG1 = dai_debitMoyen('XG')
#    ax_principle.plot(x_XG1,y_XG1,label=aliasDict_Dai['Dai/inlet_0p5'],linestyle='-',marker='s',fillstyle='none')    
#    x_water1, y_water1 = dai_debitMoyen('EAU')    
#    ax_principle.plot(x_water1,y_water1,label=aliasDict_Dai['Dai/Re4000'],linestyle='-',marker='^',fillstyle='none')
#
#    x_XG0, y_XG0 = dai_debitMin('XG')
#    ax_principle.plot(x_XG0,y_XG0,label=aliasDict_Dai['Dai/inlet_0p3'],linestyle='-',marker='d',fillstyle='none')    
#    x_water0, y_water0 = dai_debitMin('EAU')    
#    ax_principle.plot(x_water0,y_water0,label=aliasDict_Dai['Dai/Re2400'],linestyle='-',marker='v',fillstyle='none')

    fig.savefig(path2Data+"/"+'PICTURE_mixingFactor/mean_rms.png', bbox_inches='tight')
    
    fig, ax_principle1 = plt.subplots()

    for i, caseDir in enumerate(caseList):
        print "caseDir : ", caseDir
        plotCaseWithSlices_old_rms(ax_principle1, path2Data, caseDir, positionList, markerList[i], aliasDict, cut=0.7, ifPlotInter=False)
        
    ax_principle1.set_xlabel(r"$x/D$")
    ax_principle1.set_ylabel(r"$mixing \quad factor$")
    ax_principle1.legend(bbox_to_anchor=(1, 1), ncol=2, shadow=True)
    ax_principle1.set_ylim(0,0.25)
    fig.savefig(path2Data+"/"+'PICTURE_mixingFactor/rms.png', bbox_inches='tight')

    fig, ax_principle2 = plt.subplots()

    for i, caseDir in enumerate(caseList):
        print "caseDir : ", caseDir
        plotCaseWithSlices_old_MI(ax_principle2, path2Data, caseDir, positionList, markerList[i], aliasDict, cut=0.7, ifPlotInter=False)
        
    ax_principle2.set_xlabel(r"$x/D$")
    ax_principle2.set_ylabel(r"$Mixing \quad Efficiency$")
    ax_principle2.legend(bbox_to_anchor=(1, 1), ncol=2, shadow=True)
#    ax_principle2.set_ylim(0,1.0)
    fig.savefig(path2Data+"/"+'PICTURE_mixingFactor/mixingEfficiencyInpercentage.png', bbox_inches='tight')
    
main()