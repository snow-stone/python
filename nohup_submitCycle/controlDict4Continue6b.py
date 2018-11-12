#/bin/env python

def getTimesFromControlDict(fileName):
    
    file_controlDict = fileName
    readControlDict = open(file_controlDict,'r')
    
    for line in readControlDict:
    #    print line
        if line.startswith('endTime'):
    #        print line
            lastEndTime = float(line.split()[1].replace(';',''))
        elif line.startswith('startTime'):
    #        print line
            startTime = float(line.split()[1].replace(';',''))
        else :
            continue
    
    readControlDict.close()
    return lastEndTime, startTime

def predict4NextSimu(interval, startTime, lastEndTime, endTimeWall):
    import sys
    
    if startTime >= lastEndTime or startTime >= endTimeWall :
        sys.exit("startTime >= lastEndTime or endTimeWall : openfoam will run without any error message")
    else :
        if lastEndTime < endTimeWall:
            if lastEndTime+interval < endTimeWall:
                endTime=lastEndTime+interval
            else :
                endTime=endTimeWall
        else :
            endTime=endTimeWall

    startTime=lastEndTime
    
    return endTime, startTime

def removeAppendLineInList_startTime(fileName, startTime):
#   only one at a time. Not the 2 at the same time
#   because the "controlDict" is modified when "remove" is executed !!! 

    readControlDict = open(fileName,'r')
    controlDict = readControlDict.readlines()
    for line in controlDict:
        if line.startswith('startTime'):
            print "begins with startTime ! Original line here :"
            print line
            startTimeLine = line.replace(line.split()[1].replace(';',''),str(startTime))
            print "to be replaced by " + startTimeLine
            controlDict.remove(line)
        else:
            continue
    
    readControlDict.close()
    
    controlDict.append(startTimeLine)
    print "startTimeLine appended"
    
#    print controlDict
    
    for line in controlDict:
        print line

    return controlDict

def removeAppendLineInList_endTime(fileName, endTime):
#   only one at a time. Not the 2 at the same time

    readControlDict = open(fileName,'r')
    controlDict = readControlDict.readlines()
    for line in controlDict:
    #    print line
        if line.startswith('endTime'):
            print "begins with endTime ! Original line here :"
            print line
            endTimeLine = line.replace(line.split()[1].replace(';',''),str(endTime))
            print "to be replaced by " + endTimeLine
            controlDict.remove(line)
        else:
            continue
    
    controlDict.append(endTimeLine)
    print "endTimeLine appended"
    
#    print controlDict
    
    for line in controlDict:
        print line

    return controlDict

def writeFromList(controlDict_as_list, file_to_write):

    writeControlDict = open(file_to_write,'w')
    for line in controlDict_as_list:
        writeControlDict.write(line)
    
    writeControlDict.close()
    
    
def updateFile(interval,endTimeWall):
    
    print "controlDict update begins!--------------\n"
    lastEndTime, startTime = getTimesFromControlDict('system/controlDict')
    
    print "1st read controlDict:"
    print "startTime: ", startTime
    print "lastEndTime: ", lastEndTime
    
    
    endTime_new, startTime_new = predict4NextSimu(interval, startTime, lastEndTime, endTimeWall)

    print "startTime_new: ", startTime_new
    print "endTime_new: ", endTime_new

    print "2nd read controlDict:"
    controlDict1 = removeAppendLineInList_startTime('system/controlDict', startTime_new)
    writeFromList(controlDict1, 'system/controlDict')
    print "startTime updated."
    print "3rd read controlDict:"
    controlDict2 = removeAppendLineInList_endTime('system/controlDict', endTime_new)
    writeFromList(controlDict2, 'system/controlDict')
    print "endTime updated."
    print "controlDict update completed!-----------\n"
