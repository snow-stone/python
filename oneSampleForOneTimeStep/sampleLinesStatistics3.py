
import numpy as np
import matplotlib.pyplot as plt
#from scipy import integrate

import check_data3 as data_check
import settings

def chart(chunkSizeList):
    N = len(chunkSizeList)
    
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars
    
    fig, ax = plt.subplots()
    
    def autolabel(rects):
        """
        Attach a text label above each bar displaying its height
        """
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.02*height,
                    '%d' % int(height),
                    ha='center', va='bottom')    
    
    
    rects = ax.bar(ind, chunkSizeList, width, color='r')
    autolabel(rects)

    maxHeight=rects.patches[0].get_height()
    print "First/Max rectangle height of all histograms : ", maxHeight
    
    # add some text for labels, title and axes ticks
    ax.set_ylabel('sample Nb in every chunk. C for Chunk',fontsize=settings.sizeLabel)
    ax.set_ylim(0,maxHeight+5)
    ax.set_title('sample Nb by chunk')
    ax.set_xticks(ind + width / 2)
    xlabels = ['C'+str(i+1) for i in range(N)]
    ax.set_xticklabels(tuple(xlabels),fontsize=settings.sizeLabel)

def sampleLinesStatistics1d(validDataList,chunkStep,uTau,ifPlotAllTimes=False):

#==============================================================================
    R =0.004
    nu=1.0e-6    
#==============================================================================
    
    data=[]
    chunkedMean=[]
    chunkedStd=[]
    chunkSizeList=[]
    dataSize=len(validDataList)
    #dataSize=10
    #chunkStep=15
    #uTau=0.0469

    nb_chunk=dataSize/chunkStep
    print "chunk size : ", chunkStep
    print "Number of complete chunks : ", nb_chunk
    
    for validData in validDataList:
        data.append(np.genfromtxt(validData))
    
    mean=np.zeros(data[0].shape)
    print data[0].shape
    for i in range(dataSize):
        mean+=data[i]
    mean/=dataSize
    
    print "#############\n"
    chunckSum=np.zeros(data[0].shape)
    for i in range(0, dataSize, chunkStep):
        print "i = ", i
        k=0
        chunckSum=0
        for j in range(i, i+chunkStep):
            if j < len(data):            
                chunckSum+=data[j]
                k=k+1
        chunkSizeList.append(k)
        chunkedMean.append(chunckSum/k)
    # xcoord
    x=mean[:,0]/R
    for i in range(nb_chunk):
        chunkedMean[i]=chunkedMean[i]/uTau
    print "x min ",min(x),"x max",max(x)
    #print x
    mean[:,1:]=mean[:,1:]/uTau
    for i in range(dataSize):
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
#    ax.plot(x,mean[:,3],label='mean',color='red',linewidth=5)

#    if ifPlotAllTimes:
#        for i in range(nb_chunk):
#            ax.plot(x,chunkedMean[i][:,3],label=str(i+1))
    rPlus=-x+1
    rPlus=rPlus[::-1]*R*uTau/nu
    if ifPlotAllTimes:
        for i in range(nb_chunk):
            ax.plot(rPlus,chunkedMean[i][:,3][::-1],label=str(i+1))
            
    chart(chunkSizeList)
    
    var=np.zeros(data[0].shape)
    for i in range(dataSize):
        var+=(data[i]-mean)**2
    var/=dataSize
    std=np.sqrt(var)

    
    print "#############\n"
    chunkVar=np.zeros(data[0].shape)
    numChunk=0
    for i in range(0, dataSize, chunkStep):
        print "i = ", i
        k=0
        chunkVar=0
        for j in range(i, i+chunkStep):
            if j < len(data):            
                chunkVar+=(data[j]-chunkedMean[numChunk])**2
                k=k+1
        numChunk+=1
        print ' k = ',k
        print '  numChunk = ', numChunk
        chunkSizeList.append(k)
        chunkedStd.append(np.sqrt(chunkVar/numChunk))

    #print chunkedStd[0]

    fig2,ax2 = plt.subplots()

    # rPlus is defined to be zero at wall
    # thus need to reverse the second plotting dimension too !
    # or data will not fit at all
    rPlus=-x+1
    rPlus=rPlus[::-1]*R*uTau/nu
    #ax2.plot(rPlus,std[:,3][::-1],label='simu',color='red',marker='^')
    if ifPlotAllTimes:
        for i in range(nb_chunk):
#            ax2.plot(x,chunkedStd[i][:,3],label=str(i+1))
            ax2.plot(rPlus,chunkedStd[i][:,3][::-1],label=str(i+1),linewidth=1.5)
            
    return ax, ax2

def data_Niewstadt1995_pipe():
    string='/home/hluo/Pictures/Niewstadt1995_pipe/rmsProfile_velocity/pipeFlow_UzRMS.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y
    
def data_Eggels_pipe_DNS():
    string='/home/hluo/Pictures/Thesis.Eggels1994/pipe/Fig4.7/DNS_Eggels.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y
    
def data_Eggels_pipe_LDA():
    string='/home/hluo/Pictures/Thesis.Eggels1994/pipe/Fig4.7/EXP_LDA.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y
    
def data_Eggels_pipe_PIV():
    string='/home/hluo/Pictures/Thesis.Eggels1994/pipe/Fig4.7/EXP_PIV.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y
    
def data_Eggels_pipe_HWA():
    string='/home/hluo/Pictures/Thesis.Eggels1994/pipe/Fig4.7/EXP_HWA.csv'
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
    return yPlus, Uz/uTau

def main():
    uTau=0.0473
    R=0.004    
    
    l = data_check.check_data_shape(startTime=127.9,endTime=150.4,N=501,dataShape=(200,4))
    
    ax, ax2 = sampleLinesStatistics1d(validDataList=l,chunkStep=100,uTau=uTau,ifPlotAllTimes=True)
    
#    settings.sizeLabel = 15
    ax.set_xlabel(r'$r^+$'+' from wall to center',fontsize=settings.sizeLabel)
    ax.set_ylabel(r'$<U_z^+>$',fontsize=settings.sizeLabel)
    
#    y_, UzPlus = analytic_Uz_meanProfile(uTau,100)
#    y_=y_/R
#    y_=-y_+1
#    ax.plot(y_[::-1],UzPlus[::-1],label='mean objectif function',color='blue',linewidth=2)
#    ax.set_xlim(0.,1)
    yPlus, UzPlus = analytic_Uz_meanProfile(uTau,100)
    ax.plot(yPlus, UzPlus, label='mean objectif function', color='blue', linewidth=2)
    
    x1a, y1a = data_Eggels_pipe_DNS()
    ax.plot(x1a, y1a, label='DNS_Eggels', linewidth=2)
    
    x1b, y1b = data_Eggels_pipe_PIV()
#    ax.plot(x1b, y1b, label='EXP_PIV', linewidth=2,marker='o')
    
    x1c, y1c = data_Eggels_pipe_LDA()
#    ax.plot(x1c, y1c, label='EXP_LDA', linewidth=2,marker='^')
    
    x1d, y1d = data_Eggels_pipe_HWA()
#    ax.plot(x1d, y1d, label='EXP_HWA', linewidth=2,marker='s')
    
    ax.set_xscale('log')
    ax.set_xlim(1,200)
    ax.legend(bbox_to_anchor=(1.7, 1.5), ncol=1, fancybox=True, shadow=True)
    
    #x2, y2 = data_Niewstadt1995_pipe()
    #ax2.plot(x2, y2, label='data Niewstadt1995_pipe', marker='o')
    ax2.set_xlabel(r'$r^+$'+' from wall to center',fontsize=settings.sizeLabel)
    ax2.set_ylabel(r'$rmsU_z^+$',fontsize=settings.sizeLabel)
    #ax2.set_xscale('log')
    
    deg=6
    x_PolyFit, y_PolyFit = dataFitting_Niewstadt1995_pipe(deg=deg,samplingSize=60)
    ax2.plot(x_PolyFit, y_PolyFit, label='polynomial fitting data of degree %d'%(deg), marker='o')
#    ax2.set_ylim(0,5)
    #ax2.set_xlim(0,300)
    ax2.legend(bbox_to_anchor=(1.5, 1.2), ncol=1, fancybox=True, shadow=True)
    


main()