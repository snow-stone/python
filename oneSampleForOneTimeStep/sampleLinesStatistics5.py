
import numpy as np
import matplotlib.pyplot as plt
import oneSampleForOneTimeStep
#from scipy import integrate

import sys
sys.path.insert(0,'..')

import general_settings as gs
import reference_database as rdb


def Uz():
    uTau=0.0473
    R=0.004    
    
    l = oneSampleForOneTimeStep.pre_check(startTime=127.9,endTime=150.4,N=501,dataShape=(200,4))
    
    ax, ax2, ax3 = oneSampleForOneTimeStep.process(validDataList=l,chunkStep=200,uTau=uTau,ifPlotAllTimes=True)
    
#    gs.sizeLabel = 15
    ax.set_xlabel(r'$r^+$'+' from wall to center',fontsize=gs.sizeLabel)
    ax.set_ylabel(r'$<U_z^+>$',fontsize=gs.sizeLabel)
    
#    y_, UzPlus = analytic_Uz_meanProfile(uTau,100)
#    y_=y_/R
#    y_=-y_+1
#    ax.plot(y_[::-1],UzPlus[::-1],label='mean objectif function',color='blue',linewidth=2)
#    ax.set_xlim(0.,1)
    yPlus, UzPlus = rdb.analytic_Uz_meanProfile(True,uTau,samplingSize=100)
    ax.plot(yPlus, UzPlus, label='mean objectif function', color='blue', linewidth=2)
    
    x1a, y1a = rdb.data_Eggels_pipe_DNS()
    ax.plot(x1a, y1a, label='DNS_Eggels', linewidth=2)
    
    x1b, y1b = rdb.data_Eggels_pipe_PIV()
#    ax.plot(x1b, y1b, label='EXP_PIV', linewidth=2,marker='o')
    
    x1c, y1c = rdb.data_Eggels_pipe_LDA()
#    ax.plot(x1c, y1c, label='EXP_LDA', linewidth=2,marker='^')
    
    x1d, y1d = rdb.data_Eggels_pipe_HWA()
#    ax.plot(x1d, y1d, label='EXP_HWA', linewidth=2,marker='s')
    
    ax.set_xscale('log')
    ax.set_xlim(1,200)
    ax.legend(bbox_to_anchor=(1.7, 1.5), ncol=1, fancybox=True, shadow=True)
    
    #x2, y2 = data_Niewstadt1995_pipe()
    #ax2.plot(x2, y2, label='data Niewstadt1995_pipe', marker='o')
    ax2.set_xlabel(r'$r^+$'+' from wall to center',fontsize=gs.sizeLabel)
    ax2.set_ylabel(r'$rmsU_z^+$',fontsize=gs.sizeLabel)
    #ax2.set_xscale('log')
    
    deg=6
    x_PolyFit, y_PolyFit = rdb.dataFitting_Niewstadt1995_pipe(deg=deg,samplingSize=100)
    ax2.plot(x_PolyFit, y_PolyFit, label='polynomial fitting data of degree %d'%(deg), marker='o')
#    ax2.set_ylim(0,5)
    #ax2.set_xlim(0,300)
    ax2.legend(bbox_to_anchor=(1.5, 1.2), ncol=1, fancybox=True, shadow=True)
    
    #fig,ax3 = plt.subplots()
#    print "len(yPlus),len(x_PolyFit)"
#    print len(yPlus),len(x_PolyFit)
#    print yPlus
#    print x_PolyFit
#    ax3.plot(yPlus, UzPlus, label='mean objectif function', color='blue', linewidth=2)
#    ax3.plot(x_PolyFit, y_PolyFit, label='polynomial fitting data of degree %d'%(deg), marker='o')
    ax3.plot(yPlus, y_PolyFit/UzPlus, label='analytic', linewidth=2) 
    x3, y3 = rdb.Niewstadt1995_pipe_Fig9()
    ax3.plot(x3, y3, label='Eggels', linewidth=2)    
    
    ax3.set_xlim(0,160)
    ax3.set_xlabel(r'$r^+$'+' from wall to center',fontsize=gs.sizeLabel)
    ax3.set_ylabel(r'$rmsU_z^+/U_z^+$',fontsize=gs.sizeLabel)
    ax3.legend(bbox_to_anchor=(1.5, 1.2), ncol=1, fancybox=True, shadow=True)



def main():
    Uz()

main()