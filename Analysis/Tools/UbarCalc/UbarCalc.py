import numpy as np



# from patchIntegrate utility

def patchIntegrate(paraDict,logFileName):
    
    fileToRead=paraDict['dataEntry']['path']+'/postProcessing/flux/'+logFileName
    timeList=[]
    fluxList=[]
    
    with open(fileToRead,'r') as fin:
        print "opening file ", fileToRead
        flagForArea = True
        for line in fin:
            if "Time =" in line:
#                print line
                tokens = line.split(' ')
                timeList.append(tokens[-1])
            if "Area magnitude of patch" in line and flagForArea:
                area = line.split(' ')[-1]
                flagForArea = False                                
            if "Integral of phi over patch" in line:
#                print line
                tokens = line.split(' ')
                fluxList.append(tokens[-1])
    
    # convert str to np.float
    time=np.array(timeList).astype(np.float64)
    flux=np.array(fluxList).astype(np.float64)
    area=np.float64(area)

    return area,time,flux

def patchesIntegrate(paraDict,logFileNameList):
    for i in range(len(logFileNameList)):
        area, time, flux = patchIntegrate(paraDict,logFileNameList[i])
#        print "area["+str(i)+"]", area
        if i == 0 : 
            fluxTotal=np.zeros(flux.shape)
            
            areaTotal=np.float64(0.0)
        fluxTotal=fluxTotal+flux
        areaTotal=areaTotal+area
    
    return areaTotal,time,fluxTotal



# from cellSetAverage utility (User-defined)

def cellSetAverage(paraDict,FileName):
    
    fileToRead=paraDict['dataEntry']['path']+'/postProcessing/fieldStatistics/sets/'+FileName
    
    data=np.genfromtxt(fileToRead,skip_header=1,delimiter=' ')
    
    time=data[:,0]
    Avg=data[:,1]

    return time,Avg



# from run time library "Foam::fv::pressureGradientExplicitSource"

def RunTimefvOption(paraDict,logFileName):
    
    fileToRead=paraDict['dataEntry']['path']+'/'+logFileName
    timeList=[]
    UbarList=[]
    
    with open(fileToRead,'r') as fin:
        print "opening file ", fileToRead
        for line in fin:
            if line.startswith("Time ="):
#                print line
                tokens = line.split(' ')
                timeList.append(tokens[-1])                     
            if line.startswith("Pressure gradient source: uncorrected Ubar"):
#                print line
                tokens = line.split(' ')
                UbarList.append(tokens[6].strip(','))
    
    timeList=np.array(timeList)
    UbarList=np.array(UbarList)
                
    return timeList, UbarList
