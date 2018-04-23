#!/usr/bin/env python

# Perform a simple check that the data is loaded, has correct dimensions and
# contains no NaNs

import numpy as np

def check_data_shape(N):
    N=160
    data=[]
    validDataList=[]
    
    for i in range(N):
        # load the data
        fileName="../../postProcessing/sets/150.4/line" + str(i) + "_Ucyl.xy"
        data.append(np.genfromtxt(fileName))
        # check array shapes 
        if data[i].shape == (200,4):
            validDataList.append(fileName)
        else :
            print "#################################################\n"
            print "data file " + fileName + " has a different dimension to ", (200, 4)
            print "remove it from validDataList"

    return validDataList

#print validDataList
#print "Everything seems fine!"
#list = check_data_shape(160)
#print list