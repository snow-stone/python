
import numpy as np
import matplotlib.pyplot as plt
import multipleSampleForOneTimeStep

import sys
sys.path.insert(0,'..')

import general_settings as gs
import reference_database as rdb

def Ur():
    uTau=0.0473
    raw_sample_size=160
    dataShape=(200,4)
    
    l = multipleSampleForOneTimeStep.pre_check(raw_sample_size,dataShape)
    ax, ax2 = \
        multipleSampleForOneTimeStep.process(dataShape,validDataList=l,uTau=uTau,ifPlotAllTimes=True,colonNb=1)
    
    # Ur mean    
    ax.set_xlabel(r'$r$'+' from center to wall',fontsize=gs.sizeLabel)
    ax.set_ylabel(r'$<U_r>^+$',fontsize=gs.sizeLabel)
    
    ax.set_xlim(0,1)
    ax.legend(bbox_to_anchor=(1.5, 1.2), ncol=1, fancybox=True, shadow=True)
    
    # Ur rms
    x2, y2 = rdb.Niewstadt1995_pipe_UrRMS()
    ax2.plot(x2, y2, label='data Niewstadt1995_pipe', marker='o')
    ax2.set_xlabel(r'$r^+$'+' from wall to center',fontsize=gs.sizeLabel)
    ax2.set_ylabel(r'$rmsU_r^+$',fontsize=gs.sizeLabel)
    ax2.set_xscale('log')
    
    deg=4
    x_PolyFit, y_PolyFit = rdb.dataFitting_Niewstadt1995_pipe_UrRMS(deg=deg,samplingSize=60)
    ax2.plot(x_PolyFit, y_PolyFit, label='polynomial fitting data of degree %d'%(deg), marker='o')
    
    ax2.set_ylim(0,1.1)
    ax2.set_xlim(0,300)
    ax2.legend(bbox_to_anchor=(1, 1.4), ncol=1, fancybox=True, shadow=True)
    

def Uz():
    uTau=0.0473
    R=0.004
    raw_sample_size=160
    dataShape=(200,4)
    
    l = multipleSampleForOneTimeStep.pre_check(raw_sample_size,dataShape)
    ax, ax2 = \
        multipleSampleForOneTimeStep.process(dataShape,validDataList=l,uTau=uTau,ifPlotAllTimes=False,colonNb=3)
    
    ax.set_xlabel(r'$r$'+' from center to wall',fontsize=gs.sizeLabel)
    ax.set_ylabel(r'$<U_z>^+$',fontsize=gs.sizeLabel)
    
    y_, UzPlus = rdb.analytic_Uz_meanProfile(False,uTau,100)
    y_=y_/R
    y_=-y_+1
    ax.plot(y_[::-1],UzPlus[::-1],label='mean objectif function',color='blue',linewidth=2)
    ax.set_xlim(0,1)
    ax.legend(bbox_to_anchor=(1.7, 1.2), ncol=1, fancybox=True, shadow=True)
    
    x2, y2 = rdb.data_Niewstadt1995_pipe()
    ax2.plot(x2, y2, label='data Niewstadt1995_pipe', marker='o')
    ax2.set_xlabel(r'$r^+$'+' from wall to center',fontsize=gs.sizeLabel)
    ax2.set_ylabel(r'$rmsU_z^+$',fontsize=gs.sizeLabel)
#    ax2.set_xscale('log')
    
    deg=6
    x_PolyFit, y_PolyFit = rdb.dataFitting_Niewstadt1995_pipe(deg=deg,samplingSize=60)
    ax2.plot(x_PolyFit, y_PolyFit, label='polynomial fitting data of degree %d'%(deg), marker='o')
    ax2.set_ylim(0,4)
    ax2.set_xlim(-50,200)
    ax2.legend(bbox_to_anchor=(1, 1.4), ncol=1, fancybox=True, shadow=True)

def main():
    Ur()
    Uz()    
    
main()