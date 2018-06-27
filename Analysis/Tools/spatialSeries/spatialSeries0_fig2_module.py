import numpy as np
import general_settings as gs
import reference_database as rdb
import matplotlib.pyplot as plt


def addToFig2(ax):
    x2, y2 = rdb.data_Niewstadt1995_pipe()
    ax.plot(x2[::2], y2[::2], label='Niewstadt1995', linewidth=gs.lw, marker='o')
    
    deg=6
    x_PolyFit, y_PolyFit = rdb.dataFitting_Niewstadt1995_pipe(deg=deg,samplingSize=60)
#    ax.plot(x_PolyFit, y_PolyFit, label='polynomial fitting of degree %d'%(deg), marker='o')
    ax.plot(x_PolyFit[::3], y_PolyFit[::3], label='polynomial fitting', linewidth=gs.lw, marker='o')


def main():
    import spatialSeriesReader0_module as ssR
    import parameters_periodic_M1_dict as pM1
    import parameters_Nperiodic_10D_5Dforced_N1_N2_dict as Np_10D5Df_M1
    import parameters_Nperiodic_10D_5Dforced_dict as Np_10D5Df_M0
    import copy
    
    
    fig2,ax2 = plt.subplots()
    addToFig2(ax2)

    l = ssR.pre_check(pM1.parameters,'lines_typeUniform_cell')
    innerCoordData = ssR.process(pM1.parameters,validDataList=l,colonNb=3,innerVar=True)
    ax2.plot(innerCoordData['rPlus'][::5],innerCoordData['std'][::5],label='run0 t=%.1f M1'%pM1.parameters['dataEntry']['timeStep'],marker='v',markerfacecolor='none',linewidth=gs.lw)

    l = ssR.pre_check(Np_10D5Df_M1.parameters,'lines_complement_typeUniform_cell')
    innerCoordData = ssR.process(Np_10D5Df_M1.parameters,validDataList=l,colonNb=3,innerVar=True)
    ax2.plot(innerCoordData['rPlus'][::5],innerCoordData['std'][::5],label='run1 t=%.1f M1'%Np_10D5Df_M1.parameters['dataEntry']['timeStep'],marker='^',markerfacecolor='none',linewidth=gs.lw)
    
    l = ssR.pre_check(Np_10D5Df_M0.parameters,'lines_complement_typeUniform_cell')
    innerCoordData = ssR.process(Np_10D5Df_M0.parameters,validDataList=l,colonNb=3,innerVar=True)
    ax2.plot(innerCoordData['rPlus'][::5],innerCoordData['std'][::5],label='run2 t=%.1f M0'%Np_10D5Df_M0.parameters['dataEntry']['timeStep'],marker='s',markerfacecolor='none',linewidth=gs.lw)

    Np_10D5Df_M0_111=copy.deepcopy(Np_10D5Df_M0.parameters)
    Np_10D5Df_M0_111['dataEntry']['timeStep']=111
    l = ssR.pre_check(Np_10D5Df_M0_111,'lines_complement_typeUniform_cell')
    innerCoordData = ssR.process(Np_10D5Df_M0_111,validDataList=l,colonNb=3,innerVar=True)
    ax2.plot(innerCoordData['rPlus'][::5],innerCoordData['std'][::5],label='run2 t=%.1f M0'%Np_10D5Df_M0_111['dataEntry']['timeStep'],marker='s',markerfacecolor='none',linewidth=gs.lw)

    ax2.set_ylim(0,4)
    ax2.set_xlim(-50,200)
    ax2.legend(bbox_to_anchor=(1, 1.0), ncol=1, fancybox=True, shadow=True)
    ax2.set_xlabel(r'$r^+$',fontsize=gs.sizeLabel)
    ax2.set_ylabel(r'$(U_z^+)_{rms}$',fontsize=gs.sizeLabel)

 
    
main()
