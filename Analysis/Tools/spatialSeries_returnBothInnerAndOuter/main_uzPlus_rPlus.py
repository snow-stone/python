import numpy as np
import general_settings as gs
import reference_database as rdb
import matplotlib.pyplot as plt

def main():
    import spatialSeriesReader_returnBothInnerAndOuter as ssR
    import parameters_pipe_periodic_approxEggels as p_appoxEggels
    import copy

#    sampleNaming='lines_typeUniform_cell'
    sampleNaming='lines_typeFace_cell'

    fig1,ax1 = plt.subplots()
    l = ssR.pre_check(p_appoxEggels.parameters,sampleNaming)
    innerCoordData = ssR.process(p_appoxEggels.parameters,validDataList=l,colonNb=3,innerVar=True)
    ax1.plot(innerCoordData['rPlus'],innerCoordData['mean'],label='t=%.1f nu=5e-8'%p_appoxEggels.parameters['dataEntry']['timeStep'],linewidth=gs.lw)
    for i in range(0, len(l), -40):
        ax1.plot(innerCoordData['rPlus'],innerCoordData['dataCmptArray'][i],label=str(i))

    p_appoxEggels_3p6=copy.deepcopy(p_appoxEggels.parameters)
    p_appoxEggels_3p6['dataEntry']['timeStep']=5
    l = ssR.pre_check(p_appoxEggels_3p6,sampleNaming)
    innerCoordData = ssR.process(p_appoxEggels_3p6,validDataList=l,colonNb=3,innerVar=True) 
    ax1.plot(innerCoordData['rPlus'],innerCoordData['mean'],label='t=%.1f nu=1e-6'%p_appoxEggels_3p6['dataEntry']['timeStep'],linewidth=gs.lw)

    p_appoxEggels_3p6=copy.deepcopy(p_appoxEggels.parameters)
    p_appoxEggels_3p6['dataEntry']['timeStep']=3.6
    l = ssR.pre_check(p_appoxEggels_3p6,sampleNaming)
    innerCoordData = ssR.process(p_appoxEggels_3p6,validDataList=l,colonNb=3,innerVar=True) 
    ax1.plot(innerCoordData['rPlus'],innerCoordData['mean'],label='t=%.1f nu=1e-6'%p_appoxEggels_3p6['dataEntry']['timeStep'],linewidth=gs.lw)

    p_appoxEggels_3p5=copy.deepcopy(p_appoxEggels.parameters)
    p_appoxEggels_3p5['dataEntry']['timeStep']=3.5
    l = ssR.pre_check(p_appoxEggels_3p5,sampleNaming)
    innerCoordData = ssR.process(p_appoxEggels_3p5,validDataList=l,colonNb=3,innerVar=True) 
    ax1.plot(innerCoordData['rPlus'],innerCoordData['mean'],label='t=%.1f nu=1e-6'%p_appoxEggels_3p5['dataEntry']['timeStep'],linewidth=gs.lw)



    DNS_x, DNS_y = rdb.Eggels_thesis.Fig4p7_DNS()
    ax1.plot(DNS_x,DNS_y,linewidth=gs.lw,label='DNS_Eggels')    
    x1 = np.arange(1,15,1)
    ax1.plot(x1, x1, linewidth=gs.lw, linestyle='--', color='black')#,label='viscous layer')
    x2 = np.arange(5,200,1)
    ax1.plot(x2, 2.5*np.log(x2)+5.5, linewidth=gs.lw, linestyle='--',color='black')#, label='log layer')

    ax1.legend(bbox_to_anchor=(1.45, 1.0), ncol=1, fancybox=True, shadow=True)
    ax1.set_xscale('log')
    ax1.set_xlim(1,200)
    ax1.set_ylim(1,25)
    ax1.set_xlabel(r'$r^+$',fontsize=gs.sizeLabel)
    ax1.set_ylabel(r'$U_z^+$',fontsize=gs.sizeLabel)
    ax1.set_title('approxEggels spatial stat.')


main()
