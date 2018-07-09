import numpy as np

def pre_check(para,sampleNaming):
    #N : Input number of data files 
    #rightDataShape : 2darray's shape : a tuple like (200,4)
    data=[]
    validDataList=[]
    invalidDataShapeList=[]
    invalidDataList=[]
    N=para['sampling']['raw_sample_size']
    rightDataShape=para['sampling']['dataShape']
    timeStep=para['dataEntry']['timeStep']
    path=para['dataEntry']['path']
#    IFcomplement=para['dataEntry']['IFcomplement']
    
    for i in range(N):
        # load data
        fileName=path+"/"+"postProcessing/sets/"+str(timeStep)+"/"+sampleNaming+"-"+str(i)+"_Ucyl.xy"

        data.append(np.genfromtxt(fileName))
        # check array shapes
        if data[i].shape == rightDataShape:
            validDataList.append(fileName)
        else :
            invalidDataList.append(fileName)
            if len(invalidDataShapeList)==0 : invalidDataShapeList.append(data[i].shape) # for the first invalid shape
            for shape in invalidDataShapeList:                                           # then this loop is then executed     
                if shape != data[i].shape:
                    invalidDataShapeList.append(data[i].shape)
                    break
                else :
                    continue
    
    print "\n"
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
    print "            Report Here on pre_check             \n"
    print "For sampling : " + sampleNaming
    print "Input sampling size : ", N, " Eligable sampling size : ", len(validDataList), "\n"
    print "Non-eligable fileName list :"
    print invalidDataList
    print "\n"
    print "Invalid data shapes are    : ", invalidDataShapeList
    print "Invalid data are in number : ", len(invalidDataList), "/", N
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
    return validDataList

      
def process(para,validDataList,colonNb=3,innerVar=True):
    #rightDataShape : 2darray's shape : a tuple like (200,4)
    #validDataList : list : output from pre_check
    #uTau : float : friction velocity
    #colonNb : integer : colon = 1 or colon = 3 (Ur or Uz)
#==============================================================================
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
#==============================================================================
#   initialization
#   if ifPlotSample == True
    printInfo_coor=False
    dataList=[]
    validDataListSize=len(validDataList)
    R=para['physics']['R']
    nu=para['physics']['nu']
    uTau=para['physics']['uTau']
    rightDataShape=para['sampling']['dataShape']
#==============================================================================
#   preparation
    for validData in validDataList:
        dataList.append(np.genfromtxt(validData))
#   mind that dataList contains also coord information so that mean and std here
#   only have a meaning for colon 1,2,3
    mean = getMean(rightDataShape,dataList)
    std = getStd(rightDataShape,dataList,mean)    
#==============================================================================
#   coordinate system    
    # rbyR
    rByR=mean[:,0]/R
    # rPlus is defined to be zero at wall
    # thus need to reverse the second plotting dimension too !
    # or data will not fit at all
    rPlus=-rByR+1
    rPlus=rPlus[::-1]*R*uTau/nu
    
    if printInfo_coor:
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

    dataCmptList=[]
    for i in range(0, validDataListSize):
        if innerVar :
            dataCmptList.append(dataList[i][:,colonNb][::-1]/uTau)
        else :
            dataCmptList.append(dataList[i][:,colonNb]/max(dataList[i][:,colonNb]))
        
    dataCmptArray=np.array(dataCmptList)

    if innerVar :
        return {'rPlus':rPlus, \
                'mean':mean[:,colonNb][::-1]/uTau, \
                'std':std[:,colonNb][::-1]/uTau, \
                'dataCmptArray':dataCmptArray}
    else :
        return {'rByD':rByR/2.0, \
                'mean':mean[:,colonNb]/max(mean[:,colonNb]), \
                'dataCmptArray':dataCmptArray}