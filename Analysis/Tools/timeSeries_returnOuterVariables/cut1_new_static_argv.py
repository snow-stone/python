import matplotlib
matplotlib.use('agg')
import sys
sys.path.append('/home/hluo/work/git/thesis/Thesis_hluo_new/reference_database') # for rdb
import reference_database as rdb
import matplotlib.pyplot as plt

from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)    
plt.style.use('seaborn-white') # from defaut
plt.rcParams.update({'font.size': 20})
plt.rcParams['savefig.dpi'] = 200

def D1_Dai_EAU_mean(ax):
    x1,y1 = rdb.Dai_thesis.Fig4p8a('EAU')
    ax.plot(x1+0.5, y1, label='D1-Dai-EAU', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='mediumvioletred', color='mediumvioletred', markeredgewidth=2)
    x2,y2 = rdb.Dai_thesis.Fig4p8a('XG')
    ax.plot(x2+0.5, y2, label='D1-Dai-XG', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='orange', color='orange', markeredgewidth=2)

def D1_Dai_EAU_rms(ax):
    x2,y2 = rdb.Dai_thesis.Fig4p11a('EAU')
    ax.plot(x2+0.5, y2, label='D1-Dai-EAU', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='mediumvioletred', color='mediumvioletred', markeredgewidth=2)
    x2,y2 = rdb.Dai_thesis.Fig4p11a('XG')
    ax.plot(x2+0.5, y2, label='D1-Dai-XG', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='orange', color='orange', markeredgewidth=2)

def D2_Dai_EAU_mean(ax):
    x1,y1 = rdb.Dai_thesis.Fig4p8b('EAU')
    ax.plot(x1+0.5, y1, label='D2-Dai-EAU', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='mediumvioletred', color='mediumvioletred', markeredgewidth=2)
    x2,y2 = rdb.Dai_thesis.Fig4p8b('XG')
    ax.plot(x2+0.5, y2, label='D2-Dai-XG', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='orange', color='orange', markeredgewidth=2)

def D2_Dai_EAU_rms(ax):
    x1,y1 = rdb.Dai_thesis.Fig4p11b('EAU')
    ax.plot(x1+0.5, y1, label='D2-Dai-EAU', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='mediumvioletred', color='mediumvioletred', markeredgewidth=2)
    x2,y2 = rdb.Dai_thesis.Fig4p11b('XG')
    ax.plot(x2+0.5, y2, label='D2-Dai-XG', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='orange', color='orange', markeredgewidth=2)

def D3_Dai_EAU_mean(ax):
    x1,y1 = rdb.Dai_thesis.Fig4p8c('EAU')
    ax.plot(x1+0.5, y1, label='D3-Dai-EAU', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='mediumvioletred', color='mediumvioletred', markeredgewidth=2)
    x2,y2 = rdb.Dai_thesis.Fig4p8c('XG')
    ax.plot(x2+0.5, y2, label='D3-Dai-XG', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='orange', color='orange', markeredgewidth=2)

def D3_Dai_EAU_rms(ax):
    x1,y1 = rdb.Dai_thesis.Fig4p11c('EAU')
    ax.plot(x1+0.5, y1, label='D3-Dai-EAU', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='mediumvioletred', color='mediumvioletred', markeredgewidth=2)
    x2,y2 = rdb.Dai_thesis.Fig4p11c('XG')
    ax.plot(x2+0.5, y2, label='D3-Dai-XG', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='orange', color='orange', markeredgewidth=2)

def main():
    import timeSeriesReader_ReturnOuterVariables as tsR
    import os

    parameterFileBasename = sys.argv[1]
    saveDir = sys.argv[2]
    ifLocalControl = sys.argv[3]

    simu_module = __import__("parameters_"+parameterFileBasename)
    simu_parameters = simu_module.parameters
    
    fig1,ax1 = plt.subplots()
    fig2,ax2 = plt.subplots()

#   get data    
    simu_parameters['sampling']['dataShape']=simu_parameters['sampling']['dataShape1']
    fileListSimu = tsR.pre_check(simu_parameters,"Dai_lines_typeFace_cell-1")
    dataBase2Plot = tsR.process(simu_parameters,validDataList=fileListSimu,colonNb=1)  

#   reference plot       
    if (parameterFileBasename[0:2] == 'D2'):
        D2_Dai_EAU_mean(ax1)
        D2_Dai_EAU_rms(ax2)
        Ux_bulk_Dai=0.5
    elif (parameterFileBasename[0:2] == 'D1'):
        D1_Dai_EAU_mean(ax1)
        D1_Dai_EAU_rms(ax2)
        Ux_bulk_Dai=0.3
    elif (parameterFileBasename[0:2] == 'D3'):
        D3_Dai_EAU_mean(ax1)
        D3_Dai_EAU_rms(ax2)
        Ux_bulk_Dai=1.3

    if (parameterFileBasename[3:5] == 'NN'):
        simu_color='orange'
    else:
        simu_color='mediumvioletred'

#   No-dimnesionize and plot

    ax1.plot(dataBase2Plot['rByD'],dataBase2Plot['mean']/Ux_bulk_Dai,label=simu_parameters['alias'],linewidth=4, color=simu_color)
    ax2.plot(dataBase2Plot['rByD'],dataBase2Plot['std']/Ux_bulk_Dai,label=simu_parameters['alias'],linewidth=4, color=simu_color)
    
#   plot settings    
    ax1.set_xlim(0,1)
    ax1.set_ylim(-0.5,4)
    if ifLocalControl == "ControlFig_usingParameters":
        print "====================================="
        print "For fig1 :"
        print "In file " + os.path.basename(__file__)
        print "applying ControlFig_usingParameters pre-described in file " + os.path.basename(simu_module.__file__)
        print "====================================="
        ax1.legend(bbox_to_anchor=simu_parameters['plot']['legendPosition1a'], ncol=1, fancybox=True, shadow=True)
    else:
        print "====================================="
        print "For fig1 :"
        print "In file " + os.path.basename(__file__)
        print "applying local constant control on legend positioning"
        print "====================================="
        ax1.legend(bbox_to_anchor=(0.5, 1), ncol=1, fancybox=True, shadow=True)
    ax1.set_xlabel(r'$r/D$')
    ax1.set_ylabel(r'$\frac{\overline{\bf{u}_x}}{\bf{u}_{bulk}}$')

    ax2.set_xlim(0,1)
    ax2.set_ylim(0,1)
    if ifLocalControl == "ControlFig_usingParameters":
        print "====================================="
        print "For fig2 :"
        print "In file " + os.path.basename(__file__)
        print "applying ControlFig_usingParameters pre-described in file " + os.path.basename(simu_module.__file__)
        print "====================================="
        ax2.legend(bbox_to_anchor=simu_parameters['plot']['legendPosition1b'], ncol=1, fancybox=True, shadow=True)
    else:
        print "====================================="
        print "For fig2 :"
        print "In file " + os.path.basename(__file__)
        print "applying local constant control on legend positioning"
        print "====================================="
        ax2.legend(bbox_to_anchor=(0.5, 1), ncol=1, fancybox=True, shadow=True)
    ax2.set_xlabel(r'$r/D$')
    ax2.set_ylabel(r'$\frac{rms(\bf{u}_x)}{\bf{u}_{bulk}}$')
    
    fig1.savefig(saveDir+"cut1a.png",  bbox_inches='tight')
    fig2.savefig(saveDir+"cut1b.png",  bbox_inches='tight')

main()
