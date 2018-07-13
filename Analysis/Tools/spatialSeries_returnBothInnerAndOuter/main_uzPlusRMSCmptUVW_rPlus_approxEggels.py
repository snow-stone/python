import numpy as np
import general_settings as gs
import reference_database as rdb
import matplotlib.pyplot as plt


def main():
    import spatialSeriesReader_returnBothInnerAndOuter as ssR
    import parameters_pipe_periodic_approxEggels as p_appoxEggels
    import copy

    sampleNaming='lines_typeFace_cell' 

    fig2,ax2 = plt.subplots()
    l = ssR.pre_check(p_appoxEggels.parameters,sampleNaming)
    innerCoordData1 = ssR.process(p_appoxEggels.parameters,validDataList=l,colonNb=1,innerVar=True)
    ax2.plot(innerCoordData1['rByD'][::-1],innerCoordData1['std'],label=('t=%.1f '+r'$r$')%p_appoxEggels.parameters['dataEntry']['timeStep'],linewidth=gs.lw)

    innerCoordData2 = ssR.process(p_appoxEggels.parameters,validDataList=l,colonNb=2,innerVar=True)
    ax2.plot(innerCoordData2['rByD'][::-1],innerCoordData2['std'],label=('t=%.1f '+r'$\theta$')%p_appoxEggels.parameters['dataEntry']['timeStep'],linewidth=gs.lw)

    innerCoordData3 = ssR.process(p_appoxEggels.parameters,validDataList=l,colonNb=3,innerVar=True)
    ax2.plot(innerCoordData3['rByD'][::-1],innerCoordData3['std'],label=('t=%.1f '+r'$z$')%p_appoxEggels.parameters['dataEntry']['timeStep'],linewidth=gs.lw)
    
    x1, y1 = rdb.Eggels_article_1994.Fig8b_DNS_E_cmpt_r()
    x2, y2 = rdb.Eggels_article_1994.Fig8b_DNS_E_cmpt_theta()
    x3, y3 = rdb.Eggels_article_1994.Fig8b_DNS_E_cmpt_z()
    ax2.plot(x1,y1,label='DNS(E)'+r' $r$',marker='s')
    ax2.plot(x2,y2,label='DNS(E)'+r' $\theta$',marker='<')
    ax2.plot(x3,y3,label='DNS(E)'+r' $z$',marker='>')
    
#    ax2.set_ylim(0,4)
    ax2.set_xlim(0,0.5)
    ax2.legend(bbox_to_anchor=(0.3, 1.0), ncol=1, fancybox=True, shadow=True)
    ax2.set_xlabel(r'$r/D$',fontsize=gs.sizeLabel)
    ax2.set_ylabel(r'$(U_z^+)_{rms}$',fontsize=gs.sizeLabel)
    ax2.set_title('Eggels_article_1994 Fig 8(a)') 
    
main()
