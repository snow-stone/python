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

def plotSlice(ax, sliceNumber, dataDir, cut=0.5):
    data = np.genfromtxt("../"+dataDir+"/"+"userDefinedLog/slice"+str(sliceNumber)+"_mean_rms")
#    data = np.genfromtxt("Newtonian/Re4000/userDefinedLog/slice"+str(sliceNumber)+"_mean_rms")
    
    #samples = [4,8,13,16]
    
    time = data[:,0]
    cutSliceIndex = int(cut*len(time))
    
    ax.plot(time[cutSliceIndex:],data[cutSliceIndex:,2])
    ax.plot(time[:cutSliceIndex],data[:cutSliceIndex,2],linestyle=':')
    ax.legend(bbox_to_anchor=(1.3, 1), ncol=1, shadow=True)
    
    return np.mean(data[cutSliceIndex:,2])
    
def plotCaseWithSlices(ax_cases, dataDir, positionList, marker, cut):
    meanOfRMS = np.zeros(len(positionList))
    
    fig, ax_in_case = plt.subplots()
    for i, position in enumerate(positionList):
        meanOfRMS[i] = plotSlice(ax_in_case, position, dataDir, cut)

    positionList = np.asarray(positionList)
    ax_cases.plot(positionList/8.0,meanOfRMS, label=dataDir, marker=marker)
    
def main():
    plt.style.use('seaborn-white')
    caseList=["BirdCarreau/inlet_0p5",
              "Newtonian/Re4000",
              "BirdCarreau/inlet_0p3",
              "Newtonian/Re2400"]
    markerList=["s",
                "^",
                "s",
                "^"
                ]
    positionList = [0,1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72,73,74,75]
    
    fig, ax_principle = plt.subplots()

    for i, caseDir in enumerate(caseList):
        plotCaseWithSlices(ax_principle, caseDir, positionList, markerList[i], cut=0.7)
        
    
    ax_principle.set_xlabel(r"$x/D$")
    ax_principle.set_ylabel(r"mixing factor")
    ax_principle.set_ylim(0,1)

    x_XG0, y_XG0 = dai_debitMin('XG')
    ax_principle.plot(x_XG0,y_XG0,label='Dai/inlet_0p3',linestyle='--',marker='s')    
    x_water0, y_water0 = dai_debitMin('EAU')    
    ax_principle.plot(x_water0,y_water0,label='Dai/Re2400',linestyle='--',marker='^')
    
    x_XG1, y_XG1 = dai_debitMoyen('XG')
    ax_principle.plot(x_XG1,y_XG1,label='Dai/inlet_0p5',linestyle='--',marker='s')    
    x_water1, y_water1 = dai_debitMoyen('EAU')    
    ax_principle.plot(x_water1,y_water1,label='Dai/Re4000',linestyle='--',marker='^')


    ax_principle.legend(bbox_to_anchor=(1.4, 1), ncol=1, shadow=True)
    ax_principle.set_xlim(0,40)
    
    fig.savefig('../PICTURE_mixingFactor/mixingFactor.png', bbox_inches='tight', dpi=300)
    
main()