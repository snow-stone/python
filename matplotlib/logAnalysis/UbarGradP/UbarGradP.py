# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:50:51 2018

@author: hluo
"""

import matplotlib.pyplot as plt
import sys

sys.path.insert(0,'../..')

import general_settings as gs

def reader(logFile,n):
    #logFile : relative postion of logFile : string
    #n : number of Ubar (GradP) output in logFile : integer
    timeList=[]
    Ubar=[]
    gradP=[]
    
    with open(logFile,'r') as fin:
        print "READING file : "+logFile+"\n"
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
    
    print "len(timeList),len(Ubar),len(gradP)"
    print len(timeList),len(Ubar),len(gradP)
    
    if n*len(timeList) == len(Ubar) and n*len(timeList) == len(gradP) :
        print "Important check!!"
    else:
        sys.exit(str(n)+"*len(timeList) == len(Ubar) and "+str(n)+"*len(timeList) == len(gradP)"+"check didn't pass")
    
    return timeList, Ubar, gradP
    

def Fig1_firstTimeSteps(n, timeStepEnd, timeList, Ubar, gradP):
    fig1,ax1 = plt.subplots()
    timeStepEnd=1000
    ax1.plot(timeList[:timeStepEnd:],Ubar[:timeStepEnd*n:n],linewidth=1.5,label='uncorrected velocity',color='red')
    ax2 = ax1.twinx()
    ax2.plot(timeList[:timeStepEnd:],gradP[:timeStepEnd*n:n],linewidth=1.5,label='gradP',color='blue')
    ax1.set_xlabel(r'$t$',fontsize=gs.sizeLabel)
    ax1.set_ylabel(r'$Ubar$',fontsize=gs.sizeLabel)
    ax1.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    #ax1.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    #ax1.tick_params(colors='r')
    ax2.set_ylabel(r'$gradP$',fontsize=gs.sizeLabel)
    ax2.tick_params(colors='b')
    ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    ax1.set_title('First %d time steps'%(timeStepEnd),y=1.1)
    
def Fig2_lastTimeSteps(n, timeStepStart, timeList, Ubar, gradP):
    fig,ax1 = plt.subplots()
    ax1.plot(timeList[timeStepStart::],Ubar[n*timeStepStart::n],linewidth=1.5,label='uncorrected velocity',color='red')
    ax2 = ax1.twinx()
    ax2.plot(timeList[timeStepStart::],gradP[n*timeStepStart::n],linewidth=1.5,label='gradP',color='blue')
    ax1.set_xlabel(r'$t$',fontsize=gs.sizeLabel)
    ax1.set_ylabel(r'$Ubar$',fontsize=gs.sizeLabel)
#    ax2.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#    ax1.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    #ax1.tick_params(colors='r')
    ax2.set_ylabel(r'$gradP$',fontsize=gs.sizeLabel)
    ax2.tick_params(colors='b')
    ax1.set_title('from time steps %d to the end'%(timeStepStart),y=1.1)

def getUbarGradP(logFile,n):
    timeList, Ubar, gradP = reader(logFile,n)
    Fig1_firstTimeSteps(n, 1000, timeList, Ubar, gradP)
    Fig2_lastTimeSteps(n, 1000, timeList, Ubar, gradP)

getUbarGradP('../../logSimulation2',3)
