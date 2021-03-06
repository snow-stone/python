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

#def D1_Dai_EAU_mean(ax):
#    x1,y1 = rdb.Dai_thesis.Fig4p9a('EAU')
#    ax.plot(-x1+0.5, y1, label='D1-Dai-EAU', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='mediumvioletred', color='mediumvioletred', markeredgewidth=2)
#    x2,y2 = rdb.Dai_thesis.Fig4p9a('XG')
#    ax.plot(-x2+0.5, y2, label='D1-Dai-XG', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='orange', color='orange', markeredgewidth=2)
#
#def D1_Dai_EAU_rms(ax):
#    x2,y2 = rdb.Dai_thesis.Fig4p12a('EAU')
#    ax.plot(-x2+0.5, y2, label='D1-Dai-EAU', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='mediumvioletred', color='mediumvioletred', markeredgewidth=2)
#    x2,y2 = rdb.Dai_thesis.Fig4p12a('XG')
#    ax.plot(-x2+0.5, y2, label='D1-Dai-XG', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='orange', color='orange', markeredgewidth=2)

def D2_Dai_EAU_mean(ax):
    x1,y1 = rdb.Dai_thesis.Fig5p5b('EAU')
    ax.plot(-x1+0.5, y1, label=r'$N^2_{Exp}$', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='mediumvioletred', color='mediumvioletred', markeredgewidth=2)
    x2,y2 = rdb.Dai_thesis.Fig5p5b('XG')
    ax.plot(-x2+0.5, y2, label=r'$NN^2_{Exp}$', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='orange', color='orange', markeredgewidth=2)

def D2_Dai_EAU_rms(ax):
    x2,y2 = rdb.Dai_thesis.Fig5p10b('EAU')
    ax.plot(-x2+0.5, y2, label=r'$N^2_{Exp}$', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='mediumvioletred', color='mediumvioletred', markeredgewidth=2)
    x2,y2 = rdb.Dai_thesis.Fig4p12b('XG')
    ax.plot(-x2+0.5, y2, label=r'$NN^2_{Exp}$', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='orange', color='orange', markeredgewidth=2)

def D3_Dai_EAU_mean(ax):
    x1,y1 = rdb.Dai_thesis.Fig4p9c('EAU')
    ax.plot(-x1+0.5, y1, label='D3-Dai-EAU', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='mediumvioletred', color='mediumvioletred', markeredgewidth=2)
    x2,y2 = rdb.Dai_thesis.Fig4p9c('XG')
    ax.plot(-x2+0.5, y2, label='D3-Dai-XG', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='orange', color='orange', markeredgewidth=2)

def D3_Dai_EAU_rms(ax):
    x1,y1 = rdb.Dai_thesis.Fig4p12c('EAU')
    ax.plot(-x1+0.5, y1, label='D3-Dai-EAU', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='mediumvioletred', color='mediumvioletred', markeredgewidth=2)
    x2,y2 = rdb.Dai_thesis.Fig4p12c('XG')
    ax.plot(-x2+0.5, y2, label='D3-Dai-XG', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='orange', color='orange', markeredgewidth=2)

def main():
    import timeSeriesReader_ReturnOuterVariables_T as tsR
    import os

    parameterFileBasename1 = sys.argv[1]
    parameterFileBasename2 = sys.argv[2]
    saveDir = sys.argv[3]
    ifLocalControl = sys.argv[4]

    simu_module1 = __import__("parameters_"+parameterFileBasename1)
    simu_parameters1 = simu_module1.parameters

    simu_module2 = __import__("parameters_"+parameterFileBasename2)
    simu_parameters2 = simu_module1.parameters

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
    simu_parameters1['sampling']['dataShape']=simu_parameters1['sampling']['dataShape2']
    fileListSimu = tsR.pre_check(simu_parameters1,"Dai_lines_typeFace_cell_T-2")
    dataBase2Plot1 = tsR.process(simu_parameters1,validDataList=fileListSimu,colonNb=1)  

    simu_parameters2['sampling']['dataShape']=simu_parameters2['sampling']['dataShape2']
    fileListSimu = tsR.pre_check(simu_parameters2,"Dai_lines_typeFace_cell_T-2")
    dataBase2Plot2 = tsR.process(simu_parameters2,validDataList=fileListSimu,colonNb=1)  

#   reference plot       
    if (parameterFileBasename1[0:2] == 'D2'):
        D2_Dai_EAU_mean(ax1)
        D2_Dai_EAU_rms(ax2)
        Ux_bulk_Dai=1
    elif (parameterFileBasename1[0:2] == 'D1'):
        D1_Dai_EAU_mean(ax1)
        D1_Dai_EAU_rms(ax2)
        Ux_bulk_Dai=1
    elif (parameterFileBasename1[0:2] == 'D3'):
        D3_Dai_EAU_mean(ax1)
        D3_Dai_EAU_rms(ax2)
        Ux_bulk_Dai=1

    if (parameterFileBasename1[3:5] == 'NN'):
        simu_color='orange'
    else:
        simu_color='mediumvioletred'

#   No-dimnesionize and plot

    #ax1.plot(dataBase2Plot1['rByD'],dataBase2Plot['mean']/Ux_bulk_Dai,label=simu_parameters1['alias'],linewidth=4, color=simu_color)
#    for i in range(len(dataBase2Plot1['chunkedMean'])):
#        ax1.plot(dataBase2Plot1['rByD'],dataBase2Plot['chunkedMean'][i]/Ux_bulk_Dai,label=str(i),linewidth=4)
    y1=dataBase2Plot1['chunkedMean'][3]+dataBase2Plot1['chunkedMean'][4]
    y1=y1/2.0
    y1=rdb.smoothFunction.movingAvg(y1,3)
    ax1.plot(dataBase2Plot1['rByD'],y1/Ux_bulk_Dai,label=alias_dict[parameterFileBasename1],linewidth=4)

    y0=dataBase2Plot2['chunkedMean'][3]+dataBase2Plot2['chunkedMean'][4]
    y0=y0/2.0
    ax1.plot(dataBase2Plot2['rByD'],rdb.smoothFunction.movingAvg(y0/Ux_bulk_Dai,3),label=alias_dict[parameterFileBasename2],linewidth=4)

    #ax2.plot(dataBase2Plot1['rByD'],dataBase2Plot['std']/Ux_bulk_Dai,label=simu_parameters1['alias'],linewidth=4, color=simu_color)
#    for i in range(len(dataBase2Plot1['chunkedMean'])):
#        ax2.plot(dataBase2Plot1['rByD'],dataBase2Plot['chunkedStd'][i]/Ux_bulk_Dai,label=str(i),linewidth=4)
    y2=dataBase2Plot1['chunkedStd'][3]+dataBase2Plot1['chunkedStd'][4]
    y2=y2/2.0
    y2=rdb.smoothFunction.movingAvg(y2,3)
    y2=rdb.smoothFunction.movingAvg(y2,3)
    y2=rdb.smoothFunction.movingAvg(y2,3)
    y2=rdb.smoothFunction.movingAvg(y2,3)
    y2=rdb.smoothFunction.movingAvg(y2,3)
    #ax2.plot(dataBase2Plot1['rByD'],dataBase2Plot1['chunkedStd'][3],label=alias_dict[parameterFileBasename1],linewidth=4)
    #ax2.plot(dataBase2Plot1['rByD'],dataBase2Plot1['chunkedStd'][4],label=alias_dict[parameterFileBasename1],linewidth=4)
    ax2.plot(dataBase2Plot1['rByD'],y2/Ux_bulk_Dai,label=alias_dict[parameterFileBasename1],linewidth=4)

    y0=dataBase2Plot2['chunkedStd'][3]+dataBase2Plot2['chunkedStd'][4]
    y0=y0/2.0
    #ax2.plot(dataBase2Plot2['rByD'],dataBase2Plot2['chunkedStd'][3],label=alias_dict[parameterFileBasename1],linewidth=4)
    #ax2.plot(dataBase2Plot2['rByD'],dataBase2Plot2['chunkedStd'][4],label=alias_dict[parameterFileBasename1],linewidth=4)
    ax2.plot(dataBase2Plot2['rByD'],rdb.smoothFunction.movingAvg(y0/Ux_bulk_Dai,10),label=alias_dict[parameterFileBasename2],linewidth=4)
    
#   plot settings    
    ax1.set_xlim(0,1)
    ax1.set_ylim(-0.5,2)
    if ifLocalControl == "ControlFig_usingParameters":
        print "====================================="
        print "For fig1 :"
        print "In file " + os.path.basename(__file__)
        print "applying ControlFig_usingParameters pre-described in file " + os.path.basename(simu_module1.__file__)
        print "====================================="
        ax1.legend(bbox_to_anchor=simu_parameters1['plot']['legendPosition2a'], ncol=1, fancybox=True, shadow=True)
    else:
        print "====================================="
        print "For fig1 :"
        print "In file " + os.path.basename(__file__)
        print "applying local constant control on legend positioning"
        print "====================================="
        ax1.legend(bbox_to_anchor=(0.4, 1), ncol=1, fancybox=True, shadow=True)
    ax1.set_xlabel(r'$r/D$')
    ax1.set_ylabel(r'$\frac{\overline{\bf{U}}_x}{<\bf{U}>_{inlet}}$')
    #ax1.set_title(alias_dict[parameterFileBasename1]) 

    ax2.set_xlim(0,1)
    ax2.set_ylim(0,1)
    if ifLocalControl == "ControlFig_usingParameters":
        print "====================================="
        print "For fig2 :"
        print "In file " + os.path.basename(__file__)
        print "applying ControlFig_usingParameters pre-described in file " + os.path.basename(simu_module1.__file__)
        print "====================================="
        ax2.legend(bbox_to_anchor=simu_parameters1['plot']['legendPosition2b'], ncol=1, fancybox=True, shadow=True)
    else:
        print "====================================="
        print "For fig2 :"
        print "In file " + os.path.basename(__file__)
        print "applying local constant control on legend positioning"
        print "====================================="
        ax2.legend(bbox_to_anchor=(0.5, 1), ncol=1, fancybox=True, shadow=True)
    ax2.set_xlabel(r'$r/D$')
    ax2.set_ylabel(r'$\frac{rms(\bf{U}_x}{\bf{U}_{inlet}}$')
    #ax2.set_title(alias_dict[parameterFileBasename1]) 
    
    fig1.savefig(saveDir+"T_cut2a.png",  bbox_inches='tight')
    fig2.savefig(saveDir+"T_cut2b.png",  bbox_inches='tight')

main()
