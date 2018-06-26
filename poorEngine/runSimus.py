#!/bin/env python

import os
import shutil

def runSimu(p):
    runfolder='runfolder'+'_nPreSweeps'+str(p)
    os.system('rm -rf %s'%runfolder)
    
    shutil.copytree('pitzDaily',runfolder)
    os.chdir(runfolder)
    os.system("sed -i 's/nPreSweeps.*/nPreSweeps\t%d;/' system/fvSolution"%p)
    os.system("simpleFoam > log.simu%s"%'_nPreSweeps'+str(p))
    os.chdir('..')



def runSimus(npresweepers):
    for p in npresweepers:
        runSimu(p)
    
npresweepers=[4,8]
runSimus(npresweepers)
