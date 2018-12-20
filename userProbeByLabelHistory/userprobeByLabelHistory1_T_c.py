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
    
    plt.style.use('seaborn-white') # from defaut

    mean = np.zeros((len(positionList),4))
    std = np.zeros((len(positionList),4))
    
    for i, sample in enumerate(samples):
        fig = plt.figure()
        
        # debit_medium
        ax1 = fig.add_subplot(4,1,1)
        ax2 = fig.add_subplot(4,1,2)
        ax3 = fig.add_subplot(4,1,3)
        ax4 = fig.add_subplot(4,1,4)
        for j, case in enumerate(cases):
            if j == 0:
                if i >= 7:
                    std[i,j], mean[i,j] = userProbeByLabel(ax1, case, dataFile, sample, positionList, cut=0.6)
                else :
                    std[i,j], mean[i,j] = userProbeByLabel(ax1, case, dataFile, sample, positionList, cut=0.5)
            elif j == 1:
                if i >= 14:
                    std[i,j], mean[i,j] = userProbeByLabel(ax2, case, dataFile, sample, positionList, cut=0.5)
                else :
                    std[i,j], mean[i,j] = userProbeByLabel(ax2, case, dataFile, sample, positionList, cut=0.5)                
            elif j == 2:
                if i >= 14:
                    std[i,j], mean[i,j] = userProbeByLabel(ax3, case, dataFile, sample, positionList, cut=0.8)
                else:
                    std[i,j], mean[i,j] = userProbeByLabel(ax3, case, dataFile, sample, positionList, cut=0.5)
            elif j ==3 :
                if i >= 14:
                    std[i,j], mean[i,j] = userProbeByLabel(ax4, case, dataFile, sample, positionList, cut=0.8)
                else:
                    std[i,j], mean[i,j] = userProbeByLabel(ax4, case, dataFile, sample, positionList, cut=0.5)
            else :
                print "There's a big problem"
                        
        ax1.set_xlabel(r"$t$")
        ax1.set_ylabel(latexName)
        ax1.set_ylim(-0.2,1.2)
        ax1.set_xlim(0,0.8)

        ax2.set_xlabel(r"$t$")
        ax2.set_ylabel(latexName)
        ax2.set_ylim(-0.2,1.2)
        ax2.set_xlim(0,0.8)

        ax3.set_xlabel(r"$t$")
        ax3.set_ylabel(latexName)
        ax3.set_ylim(-0.2,1.2)
        ax3.set_xlim(0,0.8)

        ax4.set_xlabel(r"$t$")
        ax4.set_ylabel(latexName)
        ax4.set_ylim(-0.2,1.2)
        ax4.set_xlim(0,0.8)        
        
        fig.savefig("../PICTURE_history_c/"+arrayName+"/x_Eq_"+str(positionList[sample]/8.0).replace('.','p')+"D.png", bbox_inches='tight',dpi=300) # bbox_inches = 'tight' is neccessary
#==============================================================================
#   RMS 
#==============================================================================    
    fig_rms = plt.figure()
    positionList=[x/8.0 for x in positionList]

    ax1 = fig_rms.add_subplot(1,1,1)

    for i, case in enumerate(cases):
        ax1.plot(positionList,std[:,i],label=cases[i],linestyle=linestyleList[i],marker=markerList[i])
    ax1.legend(bbox_to_anchor=(1., 1), ncol=1, shadow=True)
    ax1.set_xlabel(r"$x/D$")
    ax1.set_ylabel(latexRMSName)
    
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
    ax1.set_ylabel(latexMEANName)
    
    fig_rms.savefig('../PICTURE_history_c/'+arrayName+'/Mean_xByD_oneFig.png', bbox_inches='tight', dpi=300)

def main():
    for i in range (0,4):
        plotField(field=i)

main()