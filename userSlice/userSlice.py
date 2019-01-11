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

def plotSlice(ax, sliceNumber, path2Data, dataDir, cut=0.5):
    data = np.genfromtxt(path2Data+"/"+dataDir+"/"+"userDefinedLog/slice"+str(sliceNumber)+"_mean_rms_Dai")
    
    time = data[:,0]
    cutSliceIndex = int(cut*len(time))
    
    p = ax.plot(time[cutSliceIndex:],data[cutSliceIndex:,2])
    ax.plot(time[:cutSliceIndex],data[:cutSliceIndex,2],linestyle=':',color=p[0].get_color())
    ax.legend(bbox_to_anchor=(1.3, 1), ncol=1, shadow=True)
    ax.set_title(dataDir)
    
    return np.mean(data[cutSliceIndex:,2])
    
def plotCaseWithSlices(ax_cases, path2Data, dataDir, positionList, marker, aliasDict, cut):
    meanOfRMS = np.zeros(len(positionList))
    
    fig, ax_in_case = plt.subplots()
    for i, position in enumerate(positionList):
        meanOfRMS[i] = plotSlice(ax_in_case, position, path2Data, dataDir, cut)

    positionList = np.asarray(positionList)
    ax_cases.plot(positionList/8.0,meanOfRMS, label=aliasDict[dataDir], marker=marker)
    
def main():
    plt.style.use('seaborn-white')
    caseList=["BirdCarreau/inlet_0p5",
              "Newtonian/Re4000",
              "BirdCarreau/inlet_0p3",
              "Newtonian/Re2400"]
    #impinging
#    caseList=["BirdCarreau/inlet_0p5",
#              "BirdCarreau/inlet0p5_impinging",
#              "Newtonian/Re4000",
#              "Newtonian/Re4000_impinging"]
    #forcing effect
#    caseList=["BirdCarreau/inlet_0p3",
#             "BirdCarreau/inlet_0p3-a_0p5-setT_St_1",  
#		  "BirdCarreau/inlet_0p3-a_0p5-setT_St_5"
#             ]

#    positionList = [0,1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72,73,74,75]
    positionList = [1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72,73,74,75]
    path2Data = "/store/8simu_tmp/shape_square/2a_3_T/python_postProcessing"
    
    markerList=["s",
                "^",
                "d",
                "v"
                ]
    
    aliasDict={
        "BirdCarreau/inlet_0p5":"simu1a",
        "Newtonian/Re4000"     :"simu1b",
        "BirdCarreau/inlet_0p3":"simu2a",
        "Newtonian/Re2400"     :"simu2b",
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1":"simu2c",
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5":"simu2d",
        "BirdCarreau/inlet0p5_impinging"       :"simu1ai",
        "Newtonian/Re4000_impinging"           :"simu1bi"
    }
    
    aliasDict_Dai={
        'Dai/inlet_0p5' : "exp1a",
        'Dai/Re4000'    : "exp1b",
        'Dai/inlet_0p3' : "exp2a",
        'Dai/Re2400'    : "exp2b"
    }
    
    fig, ax_principle = plt.subplots()

    for i, caseDir in enumerate(caseList):
        plotCaseWithSlices(ax_principle, path2Data, caseDir, positionList, markerList[i], aliasDict, cut=0.7)
        
    
    ax_principle.set_xlabel(r"$x/D$")
    ax_principle.set_ylabel(r"$mixing \quad factor$")
    ax_principle.set_ylim(0,1)

#    x_XG1, y_XG1 = dai_debitMoyen('XG')
#    ax_principle.plot(x_XG1,y_XG1,label=aliasDict_Dai['Dai/inlet_0p5'],linestyle='-',marker='s',fillstyle='none')    
#    x_water1, y_water1 = dai_debitMoyen('EAU')    
#    ax_principle.plot(x_water1,y_water1,label=aliasDict_Dai['Dai/Re4000'],linestyle='-',marker='^',fillstyle='none')
#
#    x_XG0, y_XG0 = dai_debitMin('XG')
#    ax_principle.plot(x_XG0,y_XG0,label=aliasDict_Dai['Dai/inlet_0p3'],linestyle='-',marker='d',fillstyle='none')    
#    x_water0, y_water0 = dai_debitMin('EAU')    
#    ax_principle.plot(x_water0,y_water0,label=aliasDict_Dai['Dai/Re2400'],linestyle='-',marker='v',fillstyle='none')


    ax_principle.legend(bbox_to_anchor=(1, 1), ncol=2, shadow=True)
#    ax_principle.set_xlim(0,40)
    
    fig.savefig(path2Data+"/"+'PICTURE_mixingFactor/mixingFactor.png', bbox_inches='tight', dpi=300)
    
main()