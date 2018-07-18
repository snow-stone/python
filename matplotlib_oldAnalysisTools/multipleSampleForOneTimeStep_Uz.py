import numpy as np
import sys
sys.path.insert(0,'my_plt_packages/')
import general_settings as gs
import reference_database as rdb
sys.path.insert(1,'multipleSampleForOneTimeStep')
import multipleSampleForOneTimeStep

def Ur():
    R=0.004
    nu=1.0e-6
    uTau=0.0473
    raw_sample_size=160
    dataShape=(200,4)
    
    l = multipleSampleForOneTimeStep.pre_check(raw_sample_size,dataShape,150.4,"../../../")
    ax, ax2 = \
        multipleSampleForOneTimeStep.process(R,nu,dataShape,validDataList=l,uTau=uTau,ifPlotSample=False,colonNb=1)
    
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
    R=0.004
    nu=1.0e-6
    uTau=0.0473
    raw_sample_size=160
    dataShape=(200,4)
    
    l = multipleSampleForOneTimeStep.pre_check(raw_sample_size,dataShape,150.4,"../../../")
    ax1, ax2 = \
        multipleSampleForOneTimeStep.process(R,nu,dataShape,validDataList=l,uTau=uTau,ifPlotSample=False,colonNb=3)
    
    def Fig1(ax):    
        ax.set_xlabel(r'$r$'+' from center to wall',fontsize=gs.sizeLabel)
        ax.set_ylabel(r'$<U_z>^+$',fontsize=gs.sizeLabel)
        
        DNS_x, DNS_y = rdb.data_Eggels_pipe_DNS()
        
        ax.plot(DNS_x,DNS_y,linewidth=1.5,label='Eggels')
        ax.set_xscale('log')
        
        a_x1, a_y = rdb.analytic_Uz_meanProfile(True, 0.1, 100)
        #ax.plot(a_x,a_y,linewidth=1.5,label='Analytic')
        
        x1 = np.arange(1,15,1)
        ax.plot(x1, x1, linewidth=1.5,label='viscous layer')
        
        x2 = np.arange(5,200,1)
        ax.plot(x2, 2.5*np.log(x2)+5.5, linewidth=1.5,label='log layer')
        
        print "DNS_x[0],DNS_y[0]",DNS_x[0],DNS_y[0]
        print "DNS_x[1],DNS_y[1]",DNS_x[1],DNS_y[1]
        
        print "(DNS_y[1]-DNS_y[0])/(DNS_x[1]-DNS_x[0])",(DNS_y[1]-DNS_y[0])/(DNS_x[1]-DNS_x[0])
        corr=(DNS_y[1]-DNS_y[0])/(DNS_x[1]-DNS_x[0])
        
        ax.plot(DNS_x,DNS_y/corr,linewidth=1.5,label='Eggels_corr')    
        ax.set_xlim(1,200)
        ax.legend(bbox_to_anchor=(1.7, 1.2), ncol=1, fancybox=True, shadow=True)
    
    Fig1(ax1)
    
    def Fig2(ax):
        x2, y2 = rdb.data_Niewstadt1995_pipe()
        ax.plot(x2, y2, label='data Niewstadt1995_pipe', marker='o')
        ax.set_xlabel(r'$r^+$'+' from wall to center',fontsize=gs.sizeLabel)
        ax.set_ylabel(r'$rmsU_z^+$',fontsize=gs.sizeLabel)
    #    ax.set_xscale('log')
        
        deg=6
        x_PolyFit, y_PolyFit = rdb.dataFitting_Niewstadt1995_pipe(deg=deg,samplingSize=60)
        ax.plot(x_PolyFit, y_PolyFit, label='polynomial fitting data of degree %d'%(deg), marker='o')
        ax.set_ylim(0,4)
        ax.set_xlim(-50,200)
        ax.legend(bbox_to_anchor=(1, 1.4), ncol=1, fancybox=True, shadow=True)
    
    Fig2(ax2)

def main():
#    Ur()
    Uz()    
    
main()