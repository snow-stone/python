
import numpy as np
import matplotlib.pyplot as plt
#from scipy import integrate

import check_data3 as data_check
        
def sampleLinesStatistics2d(validDataList,uTau,ifPlotAllTimes=False):
    
#==============================================================================
    R =0.004
    nu=1.0e-6    
#==============================================================================
    
    data=[]
    sampleSize=len(validDataList)
    for validData in validDataList:
        data.append(np.genfromtxt(validData))
    
    mean=np.zeros(data[0].shape)
    print data[0].shape
    for i in range(sampleSize):
        mean+=data[i]
    mean/=sampleSize
    
    # xcoord
    x=mean[:,0]/R
    mean[:,1:]=mean[:,1:]/uTau
    for i in range(sampleSize):
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
    ax.plot(x,mean[:,3],label='mean',color='red',linewidth=2)
    if ifPlotAllTimes:
        for i in range(sampleSize):
            ax.plot(x,data[i][:,3],label='0')
    
    var=np.zeros(data[0].shape)
    for i in range(sampleSize):
        var+=(data[i]-mean)**2
    var/=sampleSize
    std=np.sqrt(var)
    
    fig2,ax2 = plt.subplots()
    # rPlus is defined to be zero at wall
    # thus need to reverse the second plotting dimension too !
    # or data will not fit at all
    rPlus=-x+1
    rPlus=rPlus[::-1]*R*uTau/nu
    ax2.plot(rPlus,std[:,3][::-1],label='simu',color='red',marker='^')

    return ax, ax2

def data_Niewstadt1995_pipe():
    string='/home/hluo/Pictures/Niewstadt1995_pipe/rmsProfile_velocity/pipeFlow_UzRMS.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y

def dataFitting_Niewstadt1995_pipe(deg,samplingSize):
    string='/home/hluo/Pictures/Niewstadt1995_pipe/rmsProfile_velocity/pipeFlow_UzRMS.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')
    
    x = data[:,0]
    y = data[:,1]
    
    z = np.polyfit(x, y, deg)
    functionPolynome = np.poly1d(z)
    
    x_polyFit = np.linspace(min(x),max(x),samplingSize)
    
    return x_polyFit, functionPolynome(x_polyFit)

def analytic_Uz_meanProfile(uTau,samplingSize):
    nu=1e-6
#    viscousLayer()
#    bufferLayer()
#    logLayer()
    def viscousLayer(yPlus):
        return yPlus
    def bufferLayer(yPlus):
        return 5.0 * np.log(yPlus) - 3.05
    def logLayer(yPlus):
        return 2.5 * np.log(yPlus) + 5.5
        
    yPlus=np.linspace(0,170,samplingSize)
    y=yPlus*nu/uTau
    Uz=np.zeros(len(y))
    for i in range(len(y)):
        if yPlus[i] < 5:
            Uz[i] = uTau * viscousLayer(yPlus[i])
        elif yPlus[i] >= 5 and yPlus[i] < 30:
            Uz[i] = uTau * bufferLayer(yPlus[i])
        else:
            Uz[i] = uTau * logLayer(yPlus[i])
            
#    fig,ax = plt.subplots()
#    ax.set_xscale('log')
#    ax.plot(yPlus,Uz/uTau,label='mean',color='red')
    return y, Uz/uTau

def main():
    
    l = data_check.check_data_shape(160)
    ax, ax2 = sampleLinesStatistics2d(validDataList=l,uTau=0.0469,ifPlotAllTimes=False)
    sizeLabel = 15
    
    ax.set_xlabel(r'$r$'+' from center to wall',fontsize=sizeLabel)
    ax.set_ylabel(r'$<U_z>^+$',fontsize=sizeLabel)
    
    uTau=0.0469
    R=0.004
    y_, UzPlus = analytic_Uz_meanProfile(uTau,100)
    y_=y_/R
    y_=-y_+1
    ax.plot(y_[::-1],UzPlus[::-1],label='mean objectif function',color='blue',linewidth=2)
    ax.set_xlim(0,1)
    ax.legend(bbox_to_anchor=(1, 1.2), ncol=1, fancybox=True, shadow=True)
    
    x2, y2 = data_Niewstadt1995_pipe()
    ax2.plot(x2, y2, label='data Niewstadt1995_pipe', marker='o')
    ax2.set_xlabel(r'$r^+$'+' from wall to center',fontsize=sizeLabel)
    ax2.set_ylabel(r'$rmsU_z^+$',fontsize=sizeLabel)
    ax2.set_xscale('log')
    
    deg=6
    x_PolyFit, y_PolyFit = dataFitting_Niewstadt1995_pipe(deg=deg,samplingSize=60)
    ax2.plot(x_PolyFit, y_PolyFit, label='polynomial fitting data of degree %d'%(deg), marker='o')
    ax2.set_ylim(0,5)
    ax2.set_xlim(0,300)
    ax2.legend(bbox_to_anchor=(1, 1.4), ncol=1, fancybox=True, shadow=True)
    


main()