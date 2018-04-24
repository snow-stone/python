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
        fileName="../../../postProcessing/sets/150.4/line" + str(i) + "_Ucyl.xy"
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
    
    # xcoord
    x=mean[:,0]/R
    mean[:,1:]=mean[:,1:]/uTau
    for i in range(validDataListSize):
        data[i][:,1:]=data[i][:,1:]/uTau
    
#    r=-x+1
#    r=r[::-1]
#    integral_1D = integrate.simps(mean[:,3],r)
#    integral_2D = integrate.simps((2*np.pi)*mean[:,3]*r,r)
#    print "integrate the mean profile 1D cartesian : ", integral_1D
#    print "average velocity : ", uTau * integral_1D / 1.0
#    print "integrate the mean profile 2D polar : ", integral_2D
#    print "average velocity : ", uTau * integral_2D / (np.pi * 1.0**2)
    fig,ax = plt.subplots()
    ax.plot(x,mean[:,colonNb],label='mean',color='red',linewidth=2)
    ax.plot(x,mean[:,colonNb]*uTau/(uTau*0.85),label='mean -15%',linewidth=2)
    ax.plot(x,mean[:,colonNb]*uTau/(uTau*1.15),label='mean +15%',linewidth=2)
    if ifPlotAllTimes:
        for i in range(0, validDataListSize, 20):
            ax.plot(x,data[i][:,colonNb],label=str(i))
    
    var=np.zeros(rightDataShape)
    for i in range(validDataListSize):
        var+=(data[i]-mean)**2
    var/=validDataListSize
    std=np.sqrt(var)
    
    fig2,ax2 = plt.subplots()
    # rPlus is defined to be zero at wall
    # thus need to reverse the second plotting dimension too !
    # or data will not fit at all
    rPlus=-x+1
    rPlus=rPlus[::-1]*R*uTau/nu
    ax2.plot(rPlus,std[:,colonNb][::-1],label='simu',color='red',marker='^')

    return ax, ax2
