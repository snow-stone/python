import numpy as np
import general_settings as gs
import reference_database as rdb
import matplotlib.pyplot as plt

def main():
    import spatialSeriesReader_returnBothInnerAndOuter as ssR
    import parameters_pipe_Nperiodic_15D_5Dforced as pNp_15D5Df_M0
    import copy

#    sampleNaming='lines_typeUniform_cell'
    sampleNaming='lines_complement0_typeFace_cell'
    
    fig3,ax3 = plt.subplots()
    y_, Uz = rdb.Eggels_thesis.Fig4p5_DNS()
    ax3.plot(y_,Uz,label='DNS_Eggels',linewidth=2)
    y1_, Uz1 = rdb.Eggels_thesis.Fig4p5_HWA()
    ax3.plot(y_[::2],Uz[::2],label='HWA',linewidth=2,marker='s',markerfacecolor='none')
    
    
    l = ssR.pre_check(pNp_15D5Df_M0.parameters,sampleNaming)
    outerCoordData = ssR.process(pNp_15D5Df_M0.parameters,validDataList=l,colonNb=3,innerVar=False)  
    ax3.plot(outerCoordData['rByD'][::2],outerCoordData['mean'][::2],label='run3 t=%.1f M0'%pNp_15D5Df_M0.parameters['dataEntry']['timeStep'],linewidth=gs.lw)
    
    pNp_15D5Df_M0_dict_115=copy.deepcopy(pNp_15D5Df_M0.parameters)
    pNp_15D5Df_M0_dict_115['dataEntry']['timeStep']=115
    l = ssR.pre_check(pNp_15D5Df_M0_dict_115,sampleNaming)
    outerCoordData = ssR.process(pNp_15D5Df_M0_dict_115,validDataList=l,colonNb=3,innerVar=False)  
    ax3.plot(outerCoordData['rByD'][::2],outerCoordData['mean'][::2],label='run3 t=%.1f M0'%pNp_15D5Df_M0_dict_115['dataEntry']['timeStep'],linewidth=gs.lw)

    pNp_15D5Df_M0_dict_120=copy.deepcopy(pNp_15D5Df_M0.parameters)
    pNp_15D5Df_M0_dict_120['dataEntry']['timeStep']=120
    l = ssR.pre_check(pNp_15D5Df_M0_dict_120,sampleNaming)
    outerCoordData = ssR.process(pNp_15D5Df_M0_dict_120,validDataList=l,colonNb=3,innerVar=False)  
    ax3.plot(outerCoordData['rByD'][::2],outerCoordData['mean'][::2],label='run3 t=%.1f M0'%pNp_15D5Df_M0_dict_120['dataEntry']['timeStep'],linewidth=gs.lw)

    ax3.set_xlabel(r'$(R-r)/D$',fontsize=gs.sizeLabel)
    ax3.set_ylabel(r'$\overline{U_z}/\overline{U_z}_{max}$',fontsize=gs.sizeLabel)  
    ax3.set_xlim(0,0.55)
    ax3.set_ylim(0,1.2)
    ax3.legend(bbox_to_anchor=(0.5, 0.6), ncol=1, fancybox=True, shadow=True) 

main()
