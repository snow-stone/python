import numpy as np
import sys
sys.path.append('../reference_database')
import reference_database as rdb
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

def output2Txt(fileName, x, y):
    import os    
    if (os.path.exists('data')):
        print "path data exists\n"
    else:
        os.mkdir('data')
    
    f = open("data/"+fileName, "w+")
    for i in range(len(x)):
        f.write("%.6f %.6f\n" % (x[i], y[i]))
    f.close()


def main():

    plt.style.use('seaborn-white') # from defaut
    plt.rcParams.update({'font.size': 30})
    plt.rcParams['savefig.dpi'] = 100
    
    from matplotlib import rc
    #    rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
    ## for Palatino and other serif fonts use:
    rc('font',**{'family':'serif','serif':['Palatino']})
    rc('text', usetex=True)

    import spatialSeriesReader0_module as reader
    import para_statistic_set4uv as set4uv
    import copy

    fig1,ax1 = plt.subplots(figsize=(16,10))
    l = reader.pre_check(set4uv.parameters,'set4uv','uv_mean')
    outerCoordData = reader.process(set4uv.parameters,validDataList=l,colonNb=1,innerVar=False)
    x=-outerCoordData['rByD']*2+1.0
    y=-outerCoordData['mean']/0.045**2#*max(outerCoordData['mean'])#/0.045    
    #ax1.plot(x,y,label='simu t=%.1f'%set4uv.parameters['dataEntry']['timeStep'],linewidth=2)
    ax1.plot(x,y,label=r'$t_r$',linewidth=4,color='mediumvioletred')
    output2Txt('uv_reynoldsStress',x,y)

    x_DNS, y_DNS = rdb.Gavrilakis1992.Fig9a_DNS_G()
    ax1.plot(x_DNS,y_DNS,label=r'$DNS_G$',color='forestgreen',linewidth=4)

    x_Kim, y_Kim = rdb.Gavrilakis1992.Fig9a_Kim1987()
    ax1.plot(x_Kim,y_Kim,label=r'$DNS_K$',color='orange',linewidth=4)

    x_Niederschulte, y_Niederschulte = rdb.Gavrilakis1992.Fig9a_Niederschulte1989()
    ax1.plot(x_Niederschulte,y_Niederschulte,label=r'$EXP_{Nie}$',linestyle='--',linewidth=1,marker='s',markersize=16,markerfacecolor='none',markerEdgeWidth=4)

    x_Nishino, y_Nishino = rdb.Gavrilakis1992.Fig9a_Nishino1989()
    ax1.plot(x_Nishino,y_Nishino,label=r'$EXP_{Nis}$',marker='^',markersize=16,markerfacecolor='none',markerEdgeWidth=4)

    ax1.set_xlabel(r'$y/h$')
    ax1.set_ylabel(r'$<-u^{\prime}v^{\prime}>/\partial^2*$')
    ax1.set_ylim(0,0.8)
    ax1.set_xlim(0,1)
    ax1.tick_params(axis='both', which='major', direction='out', length=8, width=4)
    ax1.tick_params(axis='x', which='minor', direction='out', length=8, width=2)
    ax1.legend(bbox_to_anchor=(1.0, 1.0), ncol=1, fancybox=True, shadow=True)

    fig1.savefig('uv_reynoldsStress.png')

main()
