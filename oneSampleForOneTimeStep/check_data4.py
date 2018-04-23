#!/usr/bin/env python

# Perform a simple check that the data is loaded, has correct dimensions and
# contains no NaNs

import numpy as np

def convert2TimeDirName(string):
    while string[-1] == '0':
        string = string[:-1] # remove the trailing '0'
    while string[-1] == '.':
        string = string.rstrip('.')
    return string


def check_data_shape(startTime,endTime,N,dataShape):
    #N=101
    data=[]
    validDataList=[]
#    timeArray=np.linspace(28.9, 82.9, N)
    timeArray=np.linspace(startTime, endTime, N)
    timeList=[str(x) for x in timeArray]
    print timeList
#    print "#################\n"
#    print "here is 1st : ", timeList[0], convert2TimeDirName(timeList[0])
    
    for i in range(N):
        # load the data
        fileName="../../postProcessing/sets/"+convert2TimeDirName(timeList[i])+"/central_line" + "_U.xy"
        data.append(np.genfromtxt(fileName))
        # check array shapes 
        if data[i].shape == dataShape: #(200,4):
            validDataList.append(fileName)
        else :
            print "#################################################\n"
            print "data file " + fileName + " has a different dimension to ", (200, 4)
            print "remove it from validDataList"

    return validDataList

#print check_data_shape(101)