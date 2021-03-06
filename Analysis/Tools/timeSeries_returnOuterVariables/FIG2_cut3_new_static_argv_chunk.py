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
    x1,y1 = rdb.Dai_thesis.Fig4p10a('EAU')
    ax.plot(-x1+0.5, y1, label='D1-Dai-EAU', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='mediumvioletred', color='mediumvioletred', markeredgewidth=2)
    x2,y2 = rdb.Dai_thesis.Fig4p10a('XG')
    ax.plot(-x2+0.5, y2, label='D1-Dai-XG', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='orange', color='orange', markeredgewidth=2)

def D1_Dai_EAU_rms(ax):
    x2,y2 = rdb.Dai_thesis.Fig4p13a('EAU')
    ax.plot(-x2+0.5, y2, label='D1-Dai-EAU', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='mediumvioletred', color='mediumvioletred', markeredgewidth=2)
    x2,y2 = rdb.Dai_thesis.Fig4p13a('XG')
    ax.plot(-x2+0.5, y2, label='D1-Dai-XG', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='orange', color='orange', markeredgewidth=2)

def D2_Dai_EAU_mean(ax):
    x1,y1 = rdb.Dai_thesis.Fig4p10b('EAU')
    ax.plot(-x1+0.5, y1, label=r'$N^2_{Exp}$', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='mediumvioletred', color='mediumvioletred', markeredgewidth=2)
#    x2,y2 = rdb.Dai_thesis.Fig4p10b('XG')
#    ax.plot(-x2+0.5, y2, label='D2-Dai-XG', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='orange', color='orange', markeredgewidth=2)

def D2_Dai_EAU_rms(ax):
    x2,y2 = rdb.Dai_thesis.Fig4p13b('EAU')
    ax.plot(-x2+0.5, y2, label=r'$N^2_{Exp}$', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='mediumvioletred', color='mediumvioletred', markeredgewidth=2)
#    x2,y2 = rdb.Dai_thesis.Fig4p13b('XG')
#    ax.plot(-x2+0.5, y2, label='D2-Dai-XG', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='orange', color='orange', markeredgewidth=2)

def D3_Dai_EAU_mean(ax):
    x1,y1 = rdb.Dai_thesis.Fig4p10c('EAU')
    ax.plot(-x1+0.5, y1, label='D3-Dai-EAU', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='mediumvioletred', color='mediumvioletred', markeredgewidth=2)
    x2,y2 = rdb.Dai_thesis.Fig4p10c('XG')
    ax.plot(-x2+0.5, y2, label='D3-Dai-XG', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='orange', color='orange', markeredgewidth=2)

def D3_Dai_EAU_rms(ax):
    x1,y1 = rdb.Dai_thesis.Fig4p13c('EAU')
    ax.plot(x1+0.5, y1, label='D3-Dai-EAU', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='mediumvioletred', color='mediumvioletred', markeredgewidth=2)
    x2,y2 = rdb.Dai_thesis.Fig4p13c('XG')
    ax.plot(x2+0.5, y2, label='D3-Dai-XG', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='orange', color='orange', markeredgewidth=2)

def main():
    import timeSeriesReader_ReturnOuterVariables as tsR
    import os

    parameterFileBasename = sys.argv[1]
    saveDir = sys.argv[2]
    ifLocalControl = sys.argv[3]

    simu_module = __import__("parameters_"+parameterFileBasename)
    simu_parameters = simu_module.parameters

    alias_dict={
        "D2-NN-1j_test_from0" : r"$NN^{2,A}_{syn}$",
#        "D2-NN-1j_test_from0p3_forcingStep_St1_A_eq_0p05" : r"$NN^{2,A}_{Step,St=1,A=0.05}$",
        "D2-NN-1j_test_from0p3_forcingSinus_St3p2_A_eq_0p05" : r"$NN^{2,A}_{syn,St=3.2,A=0.05}$",
        "D1-1j_mapped":r"$N^{1,A}_{mapped}$",
        "D2-1j_mapped":r"$N^{2,A}_{mapped}$",
        "D3-1j_mapped":r"$N^{3,A}_{mapped}$",
#        "D2-1j_syn" :  r"$N^{2,A}_{syn-mean}$",
#        "D2-NN-1j_syn":r"$NN^{2,A}_{syn-mean-'}$",
        "D2-NN-1k_syn":r"$NN^{2,B}_{syn}$",
        "D2-NN-1k_syn_forcing":r"$NN^{2,B}_{syn,St=3.2,A=0.025}$"
    }
    
    fig1,ax1 = plt.subplots()
    fig2,ax2 = plt.subplots()

#   get data    
    simu_parameters['sampling']['dataShape']=simu_parameters['sampling']['dataShape3']
    fileListSimu = tsR.pre_check(simu_parameters,"Dai_lines_typeFace_cell-3")
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

    #ax1.plot(dataBase2Plot['rByD'],dataBase2Plot['mean']/Ux_bulk_Dai,label=simu_parameters['alias'],linewidth=4, color=simu_color)
#    for i in range(len(dataBase2Plot['chunkedMean'])):
#        ax1.plot(dataBase2Plot['rByD'],dataBase2Plot['chunkedMean'][i]/Ux_bulk_Dai,label=str(i),linewidth=4)
    y1=dataBase2Plot['chunkedMean'][3]+dataBase2Plot['chunkedMean'][4]
    y1=y1/2.0
    ax1.plot(dataBase2Plot['rByD'],y1/Ux_bulk_Dai,label=alias_dict[parameterFileBasename],linewidth=4)
    #ax2.plot(dataBase2Plot['rByD'],dataBase2Plot['std']/Ux_bulk_Dai,label=simu_parameters['alias'],linewidth=4, color=simu_color)
#    for i in range(len(dataBase2Plot['chunkedMean'])):
#        ax2.plot(dataBase2Plot['rByD'],dataBase2Plot['chunkedStd'][i]/Ux_bulk_Dai,label=str(i),linewidth=4)
    y2=dataBase2Plot['chunkedStd'][3]+dataBase2Plot['chunkedStd'][4]
    y2=y2/2.0
    y2=rdb.smoothFunction.movingAvg(y2,3)
    y2=rdb.smoothFunction.movingAvg(y2,3)
    ax2.plot(dataBase2Plot['rByD'],y2/Ux_bulk_Dai,label=alias_dict[parameterFileBasename],linewidth=4)
    
#   plot settings    
    ax1.set_xlim(0,1)
    ax1.set_ylim(-0.5,4)
    if ifLocalControl == "ControlFig_usingParameters":
        print "====================================="
        print "For fig1 :"
        print "In file " + os.path.basename(__file__)
        print "applying ControlFig_usingParameters pre-described in file " + os.path.basename(simu_module.__file__) 
        print "=====================================" 
        ax1.legend(bbox_to_anchor=simu_parameters['plot']['legendPosition3a'], ncol=1, fancybox=True, shadow=True)
    else:
        print "====================================="
        print "For fig1 :"
        print "In file " + os.path.basename(__file__)
        print "applying local constant control on legend positioning"
        print "====================================="
        ax1.legend(bbox_to_anchor=(0.5, 1), ncol=1, fancybox=True, shadow=True)
    ax1.set_xlabel(r'$r/D$')
    ax1.set_ylabel(r'$\frac{\overline{\bf{U}}_x}{<\bf{U}>_{inlet}}$')
    #ax1.set_title(alias_dict[parameterFileBasename])

    ax2.set_xlim(0,1)
    ax2.set_ylim(0,1)
    if ifLocalControl == "ControlFig_usingParameters":
        print "====================================="
        print "For fig2 :"
        print "In file " + os.path.basename(__file__)
        print "applying ControlFig_usingParameters pre-described in file " + os.path.basename(simu_module.__file__)
        print "====================================="
        ax1.legend(bbox_to_anchor=simu_parameters['plot']['legendPosition3b'], ncol=2, fancybox=True, shadow=True)
    else:
        print "====================================="
        print "For fig2 :"
        print "In file " + os.path.basename(__file__)
        print "applying local constant control on legend positioning"
        print "====================================="
        ax2.legend(bbox_to_anchor=(0.5, 1), ncol=1, fancybox=True, shadow=True)
    ax2.set_xlabel(r'$r/D$')
    ax2.set_ylabel(r'$\frac{rms(\bf{U}_x)}{\bf{U}_{inlet}}$')
    #ax2.set_title(alias_dict[parameterFileBasename])
    
    im = plt.imread('cutPositions_cropped_cut3.png')
    rect=[0.1, 0.8, 0.3, 0.3]
    ax1_new = fig1.add_axes(rect, anchor='NE', zorder=-1)
    ax1_new.imshow(im)
    ax1_new.axis('off')
    ax2_new = fig2.add_axes(rect, anchor='NE', zorder=-1)
    ax2_new.imshow(im)
    ax2_new.axis('off')
    ax1.get_legend().remove()
    ax2.get_legend().remove()
    fig1.savefig(saveDir+"cut3a.png",  bbox_inches='tight')
    fig2.savefig(saveDir+"cut3b.png",  bbox_inches='tight')

main()
