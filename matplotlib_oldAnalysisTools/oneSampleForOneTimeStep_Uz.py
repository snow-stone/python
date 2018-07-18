import sys
sys.path.insert(0,'oneSampleForOneTimeStep')
import oneSampleForOneTimeStep
sys.path.insert(1,'my_plt_packages')
import general_settings as gs
import reference_database as rdb

def Uz():
    dataShape=(200,4)
    relativePathToData="../../../"
    R=0.004
    nu=1.0e-6
    chunkStep=200
    uTau=0.0473
    colonNb=3
    
    l = \
        oneSampleForOneTimeStep.pre_check(startTime=127.9, endTime=150.4, \
                                          N=501,rightDataShape=dataShape, \
                                          relativePathToData=relativePathToData)
    
    ax1, ax2, ax3 = \
        oneSampleForOneTimeStep.process(R, nu, dataShape, validDataList=l, \
                                        chunkStep=chunkStep, \
                                        uTau=uTau, \
                                        ifPlotAllTimes=True, \
                                        colonNb=colonNb)
    
#==============================================================================
#   additional plot
    def Fig1(ax):
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
        ax.set_xlabel(r'$r^+$'+' from wall to center',fontsize=gs.sizeLabel)
        ax.set_ylabel(r'$<U_z^+>$',fontsize=gs.sizeLabel)
        
    Fig1(ax1)

    def Fig2(ax):
        deg=6
        x_PolyFit, y_PolyFit = rdb.dataFitting_Niewstadt1995_pipe(deg=deg,samplingSize=100)
        ax.plot(x_PolyFit, y_PolyFit, label='polynomial fitting data of degree %d'%(deg), marker='o')
        ax.legend(bbox_to_anchor=(1.5, 1.2), ncol=1, fancybox=True, shadow=True)
        ax.set_xlabel(r'$r^+$'+' from wall to center',fontsize=gs.sizeLabel)
        ax.set_ylabel(r'$rmsU_z^+$',fontsize=gs.sizeLabel)
    
    Fig2(ax2)    
    
    def Fig3(ax):
        deg=6
        x_PolyFit, y_PolyFit = rdb.dataFitting_Niewstadt1995_pipe(deg=deg,samplingSize=100)
        yPlus, UzPlus = rdb.analytic_Uz_meanProfile(True,uTau,samplingSize=100)
        ax.plot(yPlus, y_PolyFit/UzPlus, label='analytic', linewidth=2) 
        x3, y3 = rdb.Niewstadt1995_pipe_Fig9()
        ax.plot(x3, y3, label='Eggels', linewidth=2)
        ax.set_xlim(0,160)
        ax.set_xlabel(r'$r^+$'+' from wall to center',fontsize=gs.sizeLabel)
        ax.set_ylabel(r'$rmsU_z^+/U_z^+$',fontsize=gs.sizeLabel)
        ax.legend(bbox_to_anchor=(1.5, 1.2), ncol=1, fancybox=True, shadow=True)

    Fig3(ax3)   

def main():
    Uz()

main()