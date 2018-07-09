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

    fig2,ax2 = plt.subplots()
    x, y = rdb.Niewstadt_article_1995.dataFitting_Fig7(samplingSize=60)
    ax2.plot(x[::3], y[::3], label='polynomial fitting', linewidth=gs.lw, marker='o')

    l = ssR.pre_check(pNp_15D5Df_M0.parameters,sampleNaming)
    innerCoordData = ssR.process(pNp_15D5Df_M0.parameters,validDataList=l,colonNb=3,innerVar=True)
    ax2.plot(innerCoordData['rPlus'][::2],innerCoordData['std'][::2],label='run3 t=%.1f M0'%pNp_15D5Df_M0.parameters['dataEntry']['timeStep'],marker='v',markerfacecolor='none',linewidth=gs.lw)

    pNp_15D5Df_M0_dict_115=copy.deepcopy(pNp_15D5Df_M0.parameters)
    pNp_15D5Df_M0_dict_115['dataEntry']['timeStep']=115
    l = ssR.pre_check(pNp_15D5Df_M0_dict_115,sampleNaming)
    innerCoordData = ssR.process(pNp_15D5Df_M0_dict_115,validDataList=l,colonNb=3,innerVar=True) 
    ax2.plot(innerCoordData['rPlus'][::2],innerCoordData['std'][::2],label='run3 t=%.1f M0'%pNp_15D5Df_M0_dict_115['dataEntry']['timeStep'],marker='v',markerfacecolor='none',linewidth=gs.lw)

    pNp_15D5Df_M0_dict_120=copy.deepcopy(pNp_15D5Df_M0.parameters)
    pNp_15D5Df_M0_dict_120['dataEntry']['timeStep']=120
    l = ssR.pre_check(pNp_15D5Df_M0_dict_120,sampleNaming)
    innerCoordData = ssR.process(pNp_15D5Df_M0_dict_120,validDataList=l,colonNb=3,innerVar=True) 
    ax2.plot(innerCoordData['rPlus'][::2],innerCoordData['std'][::2],label='run3 t=%.1f M0'%pNp_15D5Df_M0_dict_120['dataEntry']['timeStep'],marker='v',markerfacecolor='none',linewidth=gs.lw)

    ax2.set_ylim(0,4)
    ax2.set_xlim(-50,200)
    ax2.legend(bbox_to_anchor=(1, 1.0), ncol=1, fancybox=True, shadow=True)
    ax2.set_xlabel(r'$r^+$',fontsize=gs.sizeLabel)
    ax2.set_ylabel(r'$(U_z^+)_{rms}$',fontsize=gs.sizeLabel)

 
    
main()
