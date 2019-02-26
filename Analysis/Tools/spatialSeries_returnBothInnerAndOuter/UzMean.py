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
    import parameters_t_c as pNp_15D5Df_M0
    import copy

    sampleNaming='lines_typeFace_cell'
    
    fig3,ax3 = plt.subplots(figsize=(20,10))
    y_, Uz = rdb.Eggels_thesis.Fig4p5_DNS()
    ax3.plot(y_,Uz,label=r'$DNS_E$',linewidth=1,linestyle='--',marker='s',color='mediumvioletred',markeredgecolor='mediumvioletred', markerfacecolor='none', markersize=16, markeredgewidth=4)
    y1_, Uz1 = rdb.Eggels_thesis.Fig4p5_HWA()
    ax3.plot(y_[::2],Uz[::2],label=r'$HWA$',linewidth=1,linestyle='--',marker='s',color='forestgreen',markeredgecolor='forestgreen', markerfacecolor='none', markersize=16, markeredgewidth=4)
    
    
    l = ssR.pre_check(pNp_15D5Df_M0.parameters,sampleNaming)
    outerCoordData = ssR.process(pNp_15D5Df_M0.parameters,validDataList=l,colonNb=3,innerVar=False)  
    ax3.plot(outerCoordData['rByD'][::2],outerCoordData['mean'][::2],label='simu',linewidth=4,color='darkcyan')
    
    ax3.set_xlabel(r'$(R-r)/D$')
    ax3.set_ylabel(r'$\overline{u_z}/\overline{u_z}_{max}$')
    ax3.set_xlim(0,0.5)
    ax3.set_ylim(0,1.2)
    ax3.legend(bbox_to_anchor=(1, 1), ncol=1, fancybox=True, shadow=True) 

    fig3.savefig('UzMean.png', bbox_inches='tight')

main()
