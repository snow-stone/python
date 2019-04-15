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

def main():
    import timeSeriesReader_ReturnOuterVariables as tsR

    parameterFileBasename = sys.argv[1]
    saveDir = sys.argv[2]

    simu_case = getattr(__import__("parameters_"+parameterFileBasename),"parameters")
    
    fig1,ax1 = plt.subplots()
    fig2,ax2 = plt.subplots()

#   get data    
    simu_case['sampling']['dataShape']=simu_case['sampling']['dataShape1']
    fileListSimu = tsR.pre_check(simu_case,"Dai_lines_typeFace_cell-1")
    dataBase2Plot = tsR.process(simu_case,validDataList=fileListSimu,colonNb=1)  

#   reference plot       
    if (parameterFileBasename[0:2] == 'D2'):
        D2_Dai_EAU_mean(ax1)
        D2_Dai_EAU_rms(ax2)
        Ux_bulk_Dai=0.5
    elif (parameterFileBasename[0:2] == 'D1'):
        D1_Dai_EAU_mean(ax1)
        D1_Dai_EAU_rms(ax2)
        Ux_bulk_Dai=0.3

    if (parameterFileBasename[3:5] == 'NN'):
        simu_color='orange'
    else:
        simu_color='mediumvioletred'

#   No-dimnesionize and plot

    ax1.plot(dataBase2Plot['rByD'],dataBase2Plot['mean']/Ux_bulk_Dai,label=simu_case['alias'],linewidth=4, color=simu_color)
    ax2.plot(dataBase2Plot['rByD'],dataBase2Plot['std']/Ux_bulk_Dai,label=simu_case['alias'],linewidth=4, color=simu_color)
    
#   plot settings    
    ax1.set_xlim(0,1)
    ax1.set_ylim(-0.5,4)
    ax1.legend(bbox_to_anchor=(0.5, 1), ncol=1, fancybox=True, shadow=True)
    ax1.set_xlabel(r'$r/D$')
    ax1.set_ylabel(r'$\frac{\overline{\bf{u}_x}}{\bf{u}_{bulk}}$')

    ax2.set_xlim(0,1)
    ax2.set_ylim(0,1)
    ax2.legend(bbox_to_anchor=(0.5, 1), ncol=1, fancybox=True, shadow=True)
    ax2.set_xlabel(r'$r/D$')
    ax2.set_ylabel(r'$\frac{rms(\bf{u}_x)}{\bf{u}_{bulk}}$')
    
    fig1.savefig(saveDir+"cut1a.png",  bbox_inches='tight')
    fig2.savefig(saveDir+"cut1b.png",  bbox_inches='tight')

main()
