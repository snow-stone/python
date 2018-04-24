# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:50:51 2018

@author: hluo
"""

import numpy as np
import matplotlib.pyplot as plt
import sys

def getUbarGradP(logFile,n):
    #logFile : relative postion of logFile : string
    #n : number of Ubar (GradP) output in logFile : integer
    timeList=[]
    Ubar=[]
    gradP=[]
    
    with open(logFile,'r') as fin:
        print "READING file : "+logFile+"\n"
        print "..."
        for line in fin:
            if line.startswith("Time = "):
                #print line
                tokens = line.split(' ')
                timeList.append(tokens[2])
            elif line.startswith("Pressure gradient"):
                #print line
                tokens = line.split(' ')
                tokens = [x.replace(",","") for x in tokens]
                Ubar.append(tokens[6])
                gradP.append(tokens[10])
    
    # convert str to np.float
#    timeList=np.array(timeList).astype(np.float64)
#    Ubar=np.array(Ubar).astype(np.float64)
#    gradP=np.array(gradP).astype(np.float64)
    
    print len(timeList),len(Ubar),len(gradP)
    
    if n*len(timeList) == len(Ubar) and n*len(timeList) == len(gradP) :
        print "Important check!!"
    else:
        sys.exit(str(n)+"*len(timeList) == len(Ubar) and "+str(n)+"*len(timeList) == len(gradP)"+"check didn't pass")
    
    ## first figure
    fig1,ax1 = plt.subplots()
    end1=1000
    ax1.plot(timeList[:end1:],Ubar[:end1*3:3],linewidth=1.5,label='uncorrected velocity',color='red')
    ax2 = ax1.twinx()
    ax2.plot(timeList[:end1:],gradP[:end1*3:3],linewidth=1.5,label='gradP',color='blue')
    #global sizeLabel
    sizeLabel = 15
    ax1.set_xlabel(r'$t$',fontsize=sizeLabel)
    ax1.set_ylabel(r'$Ubar$',fontsize=sizeLabel)
    ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    #ax1.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    #ax1.tick_params(colors='r')
    ax2.set_ylabel(r'$gradP$',fontsize=sizeLabel)
    ax2.tick_params(colors='b')
    ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    ax1.set_title('First %d time steps : PID controler'%(end1),y=1.1)
    
    ## second figure
    fig2,ax3 = plt.subplots()
    ax3.plot(timeList[100::],Ubar[300::3],linewidth=1.5,label='uncorrected velocity',color='red')
    ax4 = ax3.twinx()
    ax4.plot(timeList[100::],gradP[300::3],linewidth=1.5,label='gradP',color='blue')
    #global sizeLabel
    sizeLabel = 15
    ax3.set_xlabel(r'$t$',fontsize=sizeLabel)
    ax3.set_ylabel(r'$Ubar$',fontsize=sizeLabel)
    ax3.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    ax3.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    #ax1.tick_params(colors='r')
    ax4.set_ylabel(r'$gradP$',fontsize=sizeLabel)
    ax4.tick_params(colors='b')
    
getUbarGradP('../logSimulation2',3)