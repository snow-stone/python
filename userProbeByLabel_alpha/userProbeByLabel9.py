# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 21:08:57 2018

@author: hluo
"""

import numpy as np
import matplotlib.pyplot as plt


def userProbeByLabel(ax, caseName, RelativeDataFile, sample, positionSet, cut=400):
    data = np.genfromtxt(caseName+RelativeDataFile)
    print data.shape
    time = data[:,0]
    
    position_in_D = str(positionSet[sample]/8.0)+"D"
    print position_in_D + " std : ", np.std(data[cut:,sample]), " mean : ", np.mean(data[cut:,sample])
    ax.plot(time[cut:], data[cut:,sample], label=caseName+"_"+position_in_D)
    
def main():
    positionList = [0,1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72]
    #   sampling = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#    print len(positionList)
    samples = [8] #TODO this version works only for a 1-sized list
    dataFile = "/"+"userDefinedLog/fluctuation_labelGroup_U_x"
    plt.style.use('ggplot')
#    print "plt.style.available"
#    print(plt.style.available)

    fig = plt.figure()
    ax1 = fig.add_subplot(2,1,1)
    
#    print "\nFig"
    case1 = "BirdCarreau"+"/"+"inlet_0p5"
    userProbeByLabel(ax1, case1, dataFile, samples[0], positionList, cut=400)
    case2 = "Newtonian"+"/"+"Re4000"
    userProbeByLabel(ax1, case2, dataFile, samples[0], positionList, cut=400)
    
    ax1.legend(bbox_to_anchor=(1.7, 1), ncol=1, shadow=True)
    ax1.set_xlabel(r"$t$")
    ax1.set_ylabel(r"$u'$")
    
    ax2 = fig.add_subplot(2,1,2)
    
#    print "\nFig1"
    case1 = "BirdCarreau"+"/"+"inlet_0p3"    
    userProbeByLabel(ax2, case1, dataFile, samples[0], positionList, cut=0)
    case2 = "Newtonian"+"/"+"Re2400"
    userProbeByLabel(ax2, case2, dataFile, samples[0], positionList, cut=400)
    
    ax2.legend(bbox_to_anchor=(1.7, 1), ncol=1, shadow=True)
    ax2.set_xlabel(r"$t$")
    ax2.set_ylabel(r"$u'$")
    
    fig.savefig('PICTURE/x_Eq_'+str(samples[0]/8.0)+'D.png', bbox_inches='tight')

main()