
import numpy as np
import matplotlib.pyplot as plt


import sys
sys.path.insert(0,'..')


import general_settings as gs

def convert2TimeDirName(string):
    if '.' in string:
        while string[-1] == '0':
            string = string[:-1] # remove the trailing '0'
        while string[-1] == '.': # then after that, remove the trailing '.'
            string = string.rstrip('.')
    else:
        print 'Integer timeStep here :', string
    return string

def pre_check(startTime,endTime,N,rightDataShape,relativePathToData):
    data=[]
    validDataList=[]
    invalidDataList=[]
    timeArray=np.linspace(startTime, endTime, N)
    timeList=[str(x) for x in timeArray]
    
    for i in range(N):
        # load the data
        fileName=relativePathToData+"postProcessing/sets/"+convert2TimeDirName(timeList[i])+"/central_line" + "_U.xy"
        data.append(np.genfromtxt(fileName))
        # check array shapes 
        if data[i].shape == rightDataShape: #(200,4):
            validDataList.append(fileName)
        else :
            invalidDataList.append(fileName)
    
    print "\n"
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
    print "            Report Here on pre_check             \n"
    print "Input sampling size    : ", N
    print "Eligable sampling size : ", len(validDataList), "\n"
    print "Non-eligable fileName list :"
    print invalidDataList
    print "\n"
    print "NOTE : Remind that all line-sampled data must begin"
    print "from the center to wall or the coordinates won't fit.\n"    
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
    return validDataList


def chart(chunkSizeList):
    N = len(chunkSizeList)
    
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars

    def autolabel(rects):
        """
        Attach a text label above each bar displaying its height
        """
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.02*height,
                    '%d' % int(height),
                    ha='center', va='bottom')
    
    fig, ax = plt.subplots()
    
    rects = ax.bar(ind, chunkSizeList, width, color='r')
    autolabel(rects)

    maxHeight=rects.patches[0].get_height()
#    print "First/Max rectangle height of all histograms : ", maxHeight
    
    # add some text for labels, title and axes ticks
    ax.set_ylabel('sample Nb in every chunk. C for Chunk',fontsize=gs.sizeLabel)
    ax.set_ylim(0,maxHeight*1.1)
    ax.set_title('sample Nb by chunk')
    
    ax.set_xticks(ind + width / 2)
    xlabels = ['C'+str(i+1) for i in range(N)]
    ax.set_xticklabels(tuple(xlabels),fontsize=gs.sizeLabel)

def getChunkSizeList(rightDataShape,data,chunkStep):
    chunkSizeList=[]
    for i in range(0, len(data), chunkStep):
        k=0
        for j in range(i, i+chunkStep):
            if j < len(data):
                k=k+1
        chunkSizeList.append(k)
    return chunkSizeList

def getChunkedMean(rightDataShape,chunkSizeList,data,chunkStep):
    tmp_Sum=np.zeros(rightDataShape)
    chunkedMean=[]
    for chunkHead in range(0, len(data), chunkStep):
        tmp_Sum=0
        curr_chunk=chunkHead // chunkStep
        for j in range(chunkHead, chunkHead+chunkSizeList[curr_chunk]):
            tmp_Sum+=data[j]
        chunkedMean.append(tmp_Sum/chunkSizeList[curr_chunk])
    return chunkedMean

def getChunkedStd(rightDataShape,chunkSizeList,data,chunkStep,chunkedMean):
    tmp_Sum=np.zeros(rightDataShape)
    chunkedStd=[]
    for chunkHead in range(0, len(data), chunkStep):
        tmp_Sum=0
        curr_chunk=chunkHead // chunkStep
        for j in range(chunkHead, chunkHead+chunkSizeList[curr_chunk]):
            tmp_Sum+=(data[j]-chunkedMean[curr_chunk])**2
        chunkedStd.append(np.sqrt(tmp_Sum/chunkSizeList[curr_chunk]))
    return chunkedStd

def process(rightDataShape,validDataList,chunkStep,uTau,ifPlotAllTimes=False):

#==============================================================================
#   initialization
    R =0.004
    nu=1.0e-6
    
    data=[]
    chunkedMean=[]
    chunkedStd=[]
    chunkSizeList=[]
    validDataListSize=len(validDataList)    
#==============================================================================
#   preparation    
    nb_chunk=validDataListSize // chunkStep
    
    for validData in validDataList:
        data.append(np.genfromtxt(validData))
    
    mean=np.zeros(rightDataShape)
    for i in range(validDataListSize):
        mean+=data[i]
    mean/=validDataListSize
#==============================================================================
#   chunk the time series and chart-plot    
    chunkSizeList = getChunkSizeList(rightDataShape,data,chunkStep)
    chart(chunkSizeList)
#   calculate chunkedMean
    chunkedMean = getChunkedMean(rightDataShape,chunkSizeList,data,chunkStep)

#==============================================================================
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
    print "\t Only non-dimensionize them when plotting.\n"
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
    
    for i in range(nb_chunk):
        chunkedMean[i]=chunkedMean[i]/uTau
    mean[:,1:]=mean[:,1:]/uTau
    for i in range(validDataListSize):
        data[i][:,1:]=data[i][:,1:]/uTau
    
    fig1,ax1 = plt.subplots()
#    ax1.plot(rbyR,mean[:,3],label='mean',color='red',linewidth=5)

#    if ifPlotAllTimes:
#        for i in range(nb_chunk):
#            ax1.plot(rbyR,chunkedMean[i][:,3],label=str(i+1))

    if ifPlotAllTimes:
        for i in range(nb_chunk):
            ax1.plot(rPlus,chunkedMean[i][:,3][::-1],label=str(i+1),linewidth=4)
    
    var=np.zeros(rightDataShape)
    for i in range(validDataListSize):
        var+=(data[i]-mean)**2
    var/=validDataListSize
    std=np.sqrt(var)

    chunkedStd = getChunkedStd(rightDataShape,chunkSizeList,data,chunkStep,chunkedMean)

    fig2,ax2 = plt.subplots()


    ax2.plot(rPlus,std[:,3][::-1],label='simu',color='red',marker='^')
    if ifPlotAllTimes:
        for i in range(nb_chunk):
            ax2.plot(rPlus,chunkedStd[i][:,3][::-1],label=str(i+1),linewidth=1.5)
    

    fig3,ax3 = plt.subplots()
#    ax3.plot(rPlus,std[:,3][::-1],label='division here')
#    ax3.plot(rPlus,mean[:,3][::-1],label='division here')
#    ax3.plot(rPlus,chunkedMean[5][:,3][::-1],label='division here',color='purple')
    ax3.plot(rPlus,std[:,3][::-1]/mean[:,3][::-1],label='simu',color='red')
        
    return ax1, ax2, ax3