import numpy as np
import general_settings as gs
import reference_database as rdb
import matplotlib.pyplot as plt

def addToFig3(ax):        
    y_, Uz = rdb.Eggels1994_thesis_Fig4p5_DNS()
    ax.plot(y_,Uz,label='DNS_Eggels',linewidth=2)
    y1_, Uz1 = rdb.Eggels1994_thesis_Fig4p5_HWA()
    ax.plot(y_[::2],Uz[::2],label='HWA',linewidth=2,marker='s',markerfacecolor='none')    


def main():
    import spatialSeriesReader0_module as ssR
    import parameters_periodic_M1_dict as pM1
    import parameters_Nperiodic_10D_5Dforced_N1_N2_dict as Np_10D5Df_M1
    import parameters_Nperiodic_10D_5Dforced_dict as Np_10D5Df_M0
    import copy
    
    fig3,ax3 = plt.subplots()
    addToFig3(ax3)    
    
    l = ssR.pre_check(pM1.parameters,'lines_typeUniform_cell')
    outerCoordData = ssR.process(pM1.parameters,validDataList=l,colonNb=3,innerVar=False)  
    ax3.plot(outerCoordData['rByD'][::5],outerCoordData['mean'][::5],label='run0 t=%.1f M1'%pM1.parameters['dataEntry']['timeStep'],linewidth=gs.lw)
#    for i in range(0, len(l), -40):
#        ax3.plot(outerCoordData['rByD'],outerCoordData['dataCmptArray'][i],label=str(i))
    
    l = ssR.pre_check(Np_10D5Df_M1.parameters,'lines_complement_typeUniform_cell')
    outerCoordData = ssR.process(Np_10D5Df_M1.parameters,validDataList=l,colonNb=3,innerVar=False) 
    ax3.plot(outerCoordData['rByD'][::5],outerCoordData['mean'][::5],label='run1 t=%.1f M1'%Np_10D5Df_M1.parameters['dataEntry']['timeStep'],linewidth=gs.lw)

    l = ssR.pre_check(Np_10D5Df_M0.parameters,'lines_complement_typeUniform_cell')
    outerCoordData = ssR.process(Np_10D5Df_M0.parameters,validDataList=l,colonNb=3,innerVar=False) 
    ax3.plot(outerCoordData['rByD'][::5],outerCoordData['mean'][::5],label='run1 t=%.1f M1'%Np_10D5Df_M0.parameters['dataEntry']['timeStep'],linewidth=gs.lw)

    Np_10D5Df_M0_111=copy.deepcopy(Np_10D5Df_M0.parameters)
    Np_10D5Df_M0_111['dataEntry']['timeStep']=111
    l = ssR.pre_check(Np_10D5Df_M0_111,'lines_complement_typeUniform_cell')
    outerCoordData = ssR.process(Np_10D5Df_M0.parameters,validDataList=l,colonNb=3,innerVar=False) 
    ax3.plot(outerCoordData['rByD'][::5],outerCoordData['mean'][::5],label='run1 t=%.1f M1'%Np_10D5Df_M0_111['dataEntry']['timeStep'],linewidth=gs.lw)    

    ax3.set_xlabel(r'$(R-r)/D$',fontsize=gs.sizeLabel)
    ax3.set_ylabel(r'$\overline{U_z}/\overline{U_z}_{max}$',fontsize=gs.sizeLabel)  
    ax3.set_xlim(0,0.55)
    ax3.set_ylim(0,1.2)
    ax3.legend(bbox_to_anchor=(0.5, 0.6), ncol=1, fancybox=True, shadow=True) 

main()
