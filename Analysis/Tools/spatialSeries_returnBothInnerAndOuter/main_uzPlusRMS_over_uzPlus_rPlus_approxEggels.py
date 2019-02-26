import numpy as np
import general_settings as gs
import reference_database as rdb
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

def main():
    import spatialSeriesReader_returnBothInnerAndOuter as ssR
    import parameters_t_c as p_appoxEggels
    import copy

#    sampleNaming='lines_typeUniform_cell'
    sampleNaming='lines_typeFace_cell'

    fig1,ax1 = plt.subplots()
    l = ssR.pre_check(p_appoxEggels.parameters,sampleNaming)
    innerCoordData = ssR.process(p_appoxEggels.parameters,validDataList=l,colonNb=3,innerVar=True)
    ax1.plot(innerCoordData['rPlus'],innerCoordData['std']/innerCoordData['mean'],label='t=%.1f nu=5e-8'%p_appoxEggels.parameters['dataEntry']['timeStep'],linewidth=gs.lw)
    for i in range(0, len(l), -40):
        ax1.plot(innerCoordData['rPlus'],innerCoordData['dataCmptArray'][i],label=str(i))

#    print innerCoordData['std']/innerCoordData['mean']

#    x, y = rdb.Niewstadt_article_1995.Fig9()
    x1, y1 = rdb.Niewstadt_article_1995.dataFitting_Fig7(samplingSize=200)
#    print x1
#    ax1.plot(x1,y1)
#    x, y = rdb.Niewstadt_article_1995.Fig7()
#    print x
#    ax1.plot(x,y)
    x, y = rdb.analytic_functions.uPlus_yPlus(200,yPlusMax=max(x1),yPlusMin=min(x1))
    ax1.plot(x,y1/y)

    ax1.legend(bbox_to_anchor=(1.45, 1.0), ncol=1, fancybox=True, shadow=True)
#    ax1.set_xscale('log')
    ax1.set_xlim(1,50)
    ax1.set_ylim(0,0.4)
    ax1.set_xlabel(r'$r^+$',fontsize=gs.sizeLabel)
    ax1.set_ylabel(r'$u_z(rms)/u_z$',fontsize=gs.sizeLabel)
    ax1.set_title('approxEggels spatial stat.')
    
    fig1.savefig('UzRMS_over_Uz.png', bbox_inches='tight')

main()
