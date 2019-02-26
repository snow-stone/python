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
    import parameters_t_c as p_appoxEggels
    import copy

    sampleNaming='lines_typeFace_cell'

    fig1,ax1 = plt.subplots(figsize=(20,10))
    l = ssR.pre_check(p_appoxEggels.parameters,sampleNaming)
    innerCoordData = ssR.process(p_appoxEggels.parameters,validDataList=l,colonNb=3,innerVar=True)
    ax1.plot(innerCoordData['rPlus'],innerCoordData['std']/innerCoordData['mean'],label='simu',linewidth=4,color='mediumvioletred')
    for i in range(0, len(l), -40):
        ax1.plot(innerCoordData['rPlus'],innerCoordData['dataCmptArray'][i],label=str(i))

#    print innerCoordData['std']/innerCoordData['mean']

    x2, y2 = rdb.Niewstadt_article_1995.Fig9()
    ax1.plot(x2,y2,label=r'$exp_N$',linewidth=1,linestyle='--',marker='^',color='darkcyan',markeredgecolor='darkcyan', markerfacecolor='none', markersize=16, markeredgewidth=4)
    x1, y1 = rdb.Niewstadt_article_1995.dataFitting_Fig7(samplingSize=200)
#    print x1
#    ax1.plot(x1,y1)
#    x, y = rdb.Niewstadt_article_1995.Fig7()
#    print x
#    ax1.plot(x,y)
    x, y = rdb.analytic_functions.uPlus_yPlus(200,yPlusMax=max(x1),yPlusMin=min(x1))
    ax1.plot(x,y1/y,label='pseudo-analytic', linewidth=1,linestyle='--',marker='s',color='forestgreen',markeredgecolor='forestgreen', markerfacecolor='none', markersize=16, markeredgewidth=4)

    ax1.legend(bbox_to_anchor=(1, 1.0), ncol=1, fancybox=True, shadow=True)
#    ax1.set_xscale('log')
    ax1.set_xlim(1,50)
    ax1.set_ylim(0,0.4)
    ax1.set_xlabel(r'$r^+$')
    ax1.set_ylabel(r'$(u_z)_{rms}/u_z$')
    #ax1.set_title('approxEggels spatial stat.')
    
    fig1.savefig('UzRMS_over_Uz.png', bbox_inches='tight')

main()
