#!/bin/env python

import os
import shutil

def copyDecomposedCase(np,timeDir):

#    src="/home/lmfa/hluo/LocalSoftware/OpenFOAM/hluo-2.3.x/run/1d_localRefine1"
    src="/home/hluo/Downloads/libraries_tests/python/copyDecompsedCase/pitzDaily"
    processorFolderPrefix="processor"
    decomposedSource=src+"/"+processorFolderPrefix
    
    items=[]
    items.append(timeDir)
    items.append('constant')
    
    for i in range(np):
        processorDirTarget=processorFolderPrefix+str(i)
        if not os.path.isdir(processorDirTarget):
            os.makedirs(processorDirTarget)
            print "makingDir "+processorDirTarget
            for item in items:
                itemSource=decomposedSource+str(i)+"/"+item
                print "copying from ", itemSource
                shutil.copytree(itemSource,processorDirTarget+"/"+item)
        else:
            shutil.rmtree(processorDirTarget)
            print "removing processor dirs in target dir : ", processorDirTarget
            print "Therefore re-run script then the script will do copyDecomposedCase"
    
#    print "\n"
#    print "copying system" 
#    shutil.copytree(src+"/system","./")      # this is wrong... dist must not exist...
#    print "copying constant" 
#    shutil.copytree(src+"/constant","./")
    
    print "\n"
    print "End of script !"

copyDecomposedCase(4,'5')
