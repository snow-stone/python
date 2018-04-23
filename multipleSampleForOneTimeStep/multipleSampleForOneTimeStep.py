
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def readLines(location,baseName,i):
    data=np.genfromtxt(
                        location
                        +baseName
                        +str(i)
                        +'_U'
                        +'.xy'
                        ,delimiter=' ')
    return data
        
def main():
    Nb_lines=160
    data=[]
    for i in range(Nb_lines):
        #data[i] = readLines('../postProcessing/sets/1/','line',i)  ## list index out of range
        data.append(readLines('../postProcessing/sets/1/','line',i))
    #print data[1].shape
    #print data[0]
    #print type(data),type(data[1])
    
    #print data[0][:2]    
    
    #print data[0][:,0],type(data[0][:,0])
    #print data[0][:,1]
    
    #print data[0],data[0].shape
    #print data[0][:,:2],type(data[0][:,:2]),data[0][:,:2].shape
    
    mean=np.zeros(data[0].shape)
    for i in range(Nb_lines):
        mean+=data[i]
    mean/=Nb_lines
    
    fig,ax = plt.subplots()
    R =0.004
    #Ub=0.6625
    Ub=0.05
    #Ub=1
    x=mean[:,0]/R
    mean[:,1:]=mean[:,1:]/Ub
    for i in range(Nb_lines):
        data[i][:,1:]=data[i][:,1:]/Ub
    
    r=-x+1
    r=r[::-1]
    integral_1D = integrate.simps(mean[:,3],r)
    integral_2D = integrate.simps((2*np.pi)*mean[:,3]*r,r)
    print "integrate the mean profile 1D cartesian : ", integral_1D
    print "average velocity : ", Ub * integral_1D / 1.0
    print "integrate the mean profile 2D polar : ", integral_2D
    print "average velocity : ", Ub * integral_2D / (np.pi * 1.0**2)
    ax.plot(-x+1,mean[:,3],label='mean',color='red')
    for i in range(Nb_lines):
        #ax.plot(x,data[i][:,3],label='0')
        continue
    sizeLabel = 15
    ax.set_xlabel(r'$r$',fontsize=sizeLabel)
    ax.set_ylabel(r'$<U>^+$',fontsize=sizeLabel)
    
    var=np.zeros(data[0].shape)
    for i in range(Nb_lines):
        var+=(data[i]-mean)**2
    var/=Nb_lines
    std=np.sqrt(var)
    #std=var.sqrt()
    
#==============================================================================
#     fig1,ax1 = plt.subplots()
#     ax1.plot(x,var[:,3],label='var',color='red')
#==============================================================================
    
    fig2,ax2 = plt.subplots()
    ax2.plot(x*R*Ub/1.0e-6,std[:,3],label='simu',color='red',marker='^')
    sizeLabel = 15
    ax2.set_xlabel(r'$y^+$',fontsize=sizeLabel)
    ax2.set_ylabel(r'$rmsU_z^+$',fontsize=sizeLabel)
    ax2.set_xscale('log')
    
    string='/home/hluo/Pictures/Niewstadt1995_pipe/rmsProfile_velocity/pipeFlow_UzRMS.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x2 = [iterator[0] for iterator in data]
    y2 = [iterator[1] for iterator in data]
    ax2.plot(x2, y2, label='data to fit Niewstadt1995_pipe', marker='o')
    ax2.legend(bbox_to_anchor=(1, 1.2), ncol=2, fancybox=True, shadow=True)
    
main()