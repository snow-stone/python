# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:50:51 2018

@author: hluo
"""

import numpy as np
#import matplotlib.pyplot as plt
#import time

def getFluxFromPatch(patchName,specificTime=''):
    
    fileToRead='../flux/'+patchName+'_U'+specificTime
    fluxTimeList=[]
    
    with open(fileToRead,'r') as fin:
        print "opening file ", fileToRead
        for line in fin:
            if "Integral of U over area magnitude of patch outlet" in line:
                #print line
                tokens = line.split(' ')
                tokens = [x.replace("(","").replace(")","") for x in tokens]
#                print tokens
#                print tokens[16]
#                time.sleep(10)
                fluxTimeList.append(tokens[16])
    
    # convert str to np.float
    fluxTimeList=np.array(fluxTimeList).astype(np.float64)

    return fluxTimeList
    
def getTimeFromPatch(patchName,specificTime=''):
    
    fileToRead='../flux/'+patchName+'_U'+specificTime
    timeList=[]
    
    with open(fileToRead,'r') as fin:
        print "opening file ", fileToRead
        for line in fin:
            if "Time = " in line:
                #print line
                tokens = line.split(' ')
                timeList.append(tokens[2])
                
    # remove the first element
    #timeList.pop(0)
    # convert str to np.float
    timeList=np.array(timeList).astype(np.float64)

    return timeList

def averagedVelocityPatches(ax, color, specificTime=''):
    time  = getTimeFromPatch('outlet0',specificTime)
    flux0 = getFluxFromPatch('outlet0',specificTime)
    flux1 = getFluxFromPatch('outlet1',specificTime)
    flux2 = getFluxFromPatch('outlet2',specificTime)
    flux3 = getFluxFromPatch('outlet3',specificTime)
    flux4 = getFluxFromPatch('outlet4',specificTime)
    
    print "checking data base compatibility : "
    print "shape of : flux0 flux1 flux2 flux3 flux4"
    print "         ", flux0.shape, flux1.shape, flux2.shape, flux3.shape, flux4.shape
    flux = flux0 + flux1 + flux2 + flux3 + flux4
    
    R=0.004
    if specificTime != '':
        print "Only one time step @ :", specificTime
#    print "time = ", time
#    print "average speed = ", flux/(np.pi*R**2)
    print "###############################\n"
    #fig,ax = plt.subplots()
    ax.plot(time,flux/(np.pi*R**2),linewidth=1.5,label='time=%s'%specificTime,color=color,marker='o')
    #global sizeLabel
    sizeLabel = 15
    ax.set_xlabel(r'$t$',fontsize=sizeLabel)
    ax.set_ylabel(r'$U_z$',fontsize=sizeLabel)
    #ax.legend(loc='upper right')
    #print len(time),len(flux)