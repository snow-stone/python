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
    
    l = multipleSampleForOneTimeStep.pre_check(raw_sample_size,dataShape,150.4,"../")
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
        multipleSampleForOneTimeStep.process(R,nu,dataShape,validDataList=l,uTau=uTau,ifPlotSample=True,colonNb=3)
    
    ax1.set_xlabel(r'$r/D$'+' from center to wall',fontsize=gs.sizeLabel)
    ax1.set_ylabel(r'$<U_z>/<U_z>_0$',fontsize=gs.sizeLabel)
    
    y_, Uz = rdb.Eggels1994_thesis_Fig4p5_DNS()
    ax1.plot(y_,Uz,label='DNS_E',color='blue',linewidth=2)
    y1_, Uz1 = rdb.Eggels1994_thesis_Fig4p5_HWA()
    ax1.plot(y_,Uz,label='HWA',color='purple',linewidth=2,marker='s',markerfacecolor='none')
    ax1.set_xlim(0,0.5)
    ax1.legend(bbox_to_anchor=(1.7, 1.2), ncol=1, fancybox=True, shadow=True)
    

def main():
#    Ur()
    Uz()    
    
main()