import numpy as np
import matplotlib.pyplot as plt

def pre_check(N,rightDataShape,timeStep,relativePathToData):
    #N : Input number of data files 
    #rightDataShape : 2darray's shape : a tuple like (200,4)
    data=[]
    validDataList=[]
    invalidDataList=[]
    
    for i in range(N):
        # load the data
        fileName=relativePathToData+"postProcessing/sets/"+str(timeStep)+"/line" + str(i) + "_Ucyl.xy"
        data.append(np.genfromtxt(fileName))
        # check array shapes 
        if data[i].shape == rightDataShape:
            validDataList.append(fileName)
        else :
            invalidDataList.append(fileName)
    
    print "\n"
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
    print "            Report Here on pre_check             \n"
    print "Input sampling size : ", N, " Eligable sampling size : ", len(validDataList), "\n"
    print "Non-eligable fileName list :"
    print invalidDataList    
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
    return validDataList

def getMean(rightDataShape,data):
    mean=np.zeros(rightDataShape)
    for i in range(len(data)):
        mean+=data[i]
    mean/=len(data)
    return mean
    
def getStd(rightDataShape,data,mean):
    std=np.zeros(rightDataShape)
    for i in range(len(data)):
        std+=(data[i]-mean)**2
    std/=len(data)
    std=np.sqrt(std)
    return std
        
def process(R,nu,rightDataShape,validDataList,uTau,ifPlotSample=False,colonNb=3):
    #rightDataShape : 2darray's shape : a tuple like (200,4)
    #validDataList : list : output from pre_check
    #uTau : float : friction velocity
    #ifPlotSample : bool : if plotting or not the sample, not just the mean
    #colonNb : integer : colon = 1 or colon = 3 (Ur or Uz)
#==============================================================================
#   initialization
#   if ifPlotSample == True
    samplePrintInterval=40    
    dataList=[]
    validDataListSize=len(validDataList)
#==============================================================================
#   preparation
    for validData in validDataList:
        dataList.append(np.genfromtxt(validData))
#   mind that dataList contains also coord information so that mean and std here
#   only have a meaning for colon 1,2,3
    mean = getMean(rightDataShape,dataList)
    std = getStd(rightDataShape,dataList,mean)    
#==============================================================================
#   preparing for plot
#   coordinate system    
    # rbyR
    rbyR=mean[:,0]/R
    # rPlus is defined to be zero at wall
    # thus need to reverse the second plotting dimension too !
    # or data will not fit at all
    rPlus=-rbyR+1
    rPlus=rPlus[::-1]*R*uTau/nu
    
    print "\n"
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
    print "         Resume on coordinate system             \n"
    print "For abssise"
    print "\t External varible :"
    print "\t rbyR - r/R from center to wall\n"
    print "\t Internal/wall varible :"
    print "\t rPlus - from wall to center"
    print "\t       - when plotting reverse the ordinate/second dimension\n"
    print "For ordinate"
    print "\t For flexibility :"
    print "\t Only non-dimensionize them when plotting.\n"
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"

#==============================================================================
    
    fig1,ax1 = plt.subplots()
#    ax1.plot(rbyR/2.0,mean[:,colonNb]/max(mean[:,colonNb]),label='mean',color='red',linewidth=4)
    ax1.plot(rPlus,mean[:,colonNb][::-1]/uTau,label='mean',color='red',linewidth=4)
    if ifPlotSample:
        for i in range(0, validDataListSize, samplePrintInterval):
            ax1.plot(rbyR/2.0,dataList[i][:,colonNb]/max(dataList[i][:,colonNb]),label=str(i))
    
    
    fig2,ax2 = plt.subplots()
    ax2.plot(rPlus,std[:,colonNb][::-1]/uTau,label='simu',color='red',marker='^')

    return ax1, ax2
