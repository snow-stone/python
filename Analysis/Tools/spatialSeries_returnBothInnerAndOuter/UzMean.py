import numpy as np
import general_settings as gs
import reference_database as rdb
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

def main():

    plt.style.use('seaborn-white') # from defaut
    plt.rcParams.update({'font.size': 30})
    plt.rcParams['savefig.dpi'] = 100
    
    from matplotlib import rc
#    rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
    ## for Palatino and other serif fonts use:
    rc('font',**{'family':'serif','serif':['Palatino']})
    rc('text', usetex=True)

    import spatialSeriesReader_returnBothInnerAndOuter as ssR
    #import parameters_pipe_Nperiodic_15D_5Dforced as pNp_15D5Df_M0
    import parameters_t_c as pNp_15D5Df_M0
    import copy

    sampleNaming='lines_typeFace_cell'
#    sampleNaming='lines_typeUniform_cell'
#    sampleNaming='lines_complement0_typeFace_cell'
    
    fig3,ax3 = plt.subplots(figsize=(20,10))
    y_, Uz = rdb.Eggels_thesis.Fig4p5_DNS()
    ax3.plot(y_,Uz,label=r'$DNS_E$',linewidth=2)
    y1_, Uz1 = rdb.Eggels_thesis.Fig4p5_HWA()
    ax3.plot(y_[::2],Uz[::2],label=r'$HWA$',linewidth=2,marker='s',markerfacecolor='none')
    
    
    l = ssR.pre_check(pNp_15D5Df_M0.parameters,sampleNaming)
    outerCoordData = ssR.process(pNp_15D5Df_M0.parameters,validDataList=l,colonNb=3,innerVar=False)  
    #ax3.plot(outerCoordData['rByD'][::2],outerCoordData['mean'][::2],label='run3 t=%.1f M0'%pNp_15D5Df_M0.parameters['dataEntry']['timeStep'],linewidth=gs.lw)
    ax3.plot(outerCoordData['rByD'][::2],outerCoordData['mean'][::2],label='simu',linewidth=gs.lw)
    
    ax3.set_xlabel(r'$(R-r)/D$')
    ax3.set_ylabel(r'$\overline{u_z}/\overline{u_z}_{max}$')
    ax3.set_xlim(0,0.5)
    ax3.set_ylim(0,1.2)
    ax3.legend(bbox_to_anchor=(1, 1), ncol=1, fancybox=True, shadow=True) 

    fig3.savefig('UzMean.png', bbox_inches='tight')

main()
