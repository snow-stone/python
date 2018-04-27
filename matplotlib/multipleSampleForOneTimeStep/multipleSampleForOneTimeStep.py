import numpy as np
import matplotlib.pyplot as plt

def pre_check(N,rightDataShape):
    #N : Input number of data files 
    #rightDataShape : 2darray's shape : a tuple like (200,4)
    data=[]
    validDataList=[]
    invalidDataList=[]
    
    for i in range(N):
        # load the data
        fileName="../postProcessing/sets/150.4/line" + str(i) + "_Ucyl.xy"
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
        
def process(rightDataShape,validDataList,uTau,ifPlotAllTimes=False,colonNb=3):
    #rightDataShape : 2darray's shape : a tuple like (200,4)
    #validDataList : list : output from pre_check
    #uTau : float : friction velocity
    #ifPlotAllTimes : bool : if plotting or not the sample, not just the mean
    #colonNb : integer : colon = 1 or colon = 3 (Ur or Uz)
#==============================================================================
    R =0.004
    nu=1.0e-6    
#==============================================================================
    
    data=[]
    validDataListSize=len(validDataList)
    for validData in validDataList:
        data.append(np.genfromtxt(validData))
    
    mean=np.zeros(rightDataShape)
    for i in range(validDataListSize):
        mean+=data[i]
    mean/=validDataListSize
    
    # rbyR : r/R
    rbyR=mean[:,0]/R
    # rPlus is defined to be zero at wall
    # thus need to reverse the second plotting dimension too !
    # or data will not fit at all
    rPlus=-rbyR+1
    rPlus=rPlus[::-1]*R*uTau/nu
#    # data and mean by uTau
#    mean[:,1:]=mean[:,1:]/uTau
#    for i in range(validDataListSize):
#        data[i][:,1:]=data[i][:,1:]/uTau
    
    fig1,ax1 = plt.subplots()
#    ax1.plot(rPlus,mean[:,colonNb][::-1]/uTau,label='mean',color='black',linewidth=1.5)
    ax1.plot(rbyR/2.0,mean[:,colonNb]/max(mean[:,colonNb]),label='mean',color='red',linewidth=2)
    if ifPlotAllTimes:
        for i in range(0, validDataListSize, 20):
            ax1.plot(rbyR,data[i][:,colonNb]/uTau,label=str(i))
    
    var=np.zeros(rightDataShape)
    for i in range(validDataListSize):
        var+=(data[i]-mean)**2
    var/=validDataListSize
    std=np.sqrt(var)
    
    fig2,ax2 = plt.subplots()

    ax2.plot(rPlus,std[:,colonNb][::-1]/uTau,label='simu',color='red',marker='^')

    return ax1, ax2
