import matplotlib
matplotlib.use('agg')

import matplotlib.pyplot as plt
import reference_database as rdb

from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)    
plt.style.use('seaborn-white') # from defaut
plt.rcParams.update({'font.size': 20})
plt.rcParams['savefig.dpi'] = 200

def main():
    import timeSeriesReader_ReturnOuterVariables as tsR
    import static_parameters_T_RES1b_MethodSynthetic as ps_syn
    import static_parameters_T_RES1d_lR2 as ps_map
    import sys
    
    saveDir = sys.argv[1]

    fig1,ax1 = plt.subplots()
    fig2,ax2 = plt.subplots()

#   get data    
    ps_syn.parameters['sampling']['dataShape']=(104,4)
    l_1b_syn = tsR.pre_check(ps_syn.parameters,"Dai_lines_typeFace_cell-1")
    db_1b_syn = tsR.process(ps_syn.parameters,validDataList=l_1b_syn,colonNb=1)

    ps_map.parameters['sampling']['dataShape']=(195,4)
    l_1d_map = tsR.pre_check(ps_map.parameters,"Dai_lines_typeFace_cell-1")
    db_1d_map = tsR.process(ps_map.parameters,validDataList=l_1d_map,colonNb=1)  

#   No-dimnesionize and plot
    Ux_1p5M_syn=0.25
    Ux_bulk_Dai=0.3

    #ax1.plot(db_1b_syn['rByD'],db_1b_syn['mean']/Ux_1p5M_syn,label='1b-synthetic',linewidth=4, color='orange')
    ax1.plot(db_1d_map['rByD'],db_1d_map['mean']/Ux_bulk_Dai,label='1dlR2-mapped',linewidth=4, color='steelblue')

    #ax2.plot(db_1b_syn['rByD'],db_1b_syn['std']/Ux_1p5M_syn,label='1b-synthetic',linewidth=4, color='orange')  
    ax2.plot(db_1d_map['rByD'],db_1d_map['std']/Ux_bulk_Dai,label='1dlR2-mapped',linewidth=4, color='steelblue')
    
#   reference plot       
    x1,y1 = rdb.Dai_thesis.Fig4p8a('EAU')
    ax1.plot(x1+0.5, y1, label='Dai-1', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='mediumvioletred', color='mediumvioletred', markeredgewidth=2)
    x2,y2 = rdb.Dai_thesis.Fig4p11a('EAU')
    ax2.plot(x2+0.5, y2, label='Dai-1', marker='s', markerfacecolor='none', linewidth=1, linestyle='--', markersize=16, markeredgecolor='mediumvioletred', color='mediumvioletred', markeredgewidth=2)

#   plot settings    
    ax1.set_xlim(0,1)
    ax1.set_ylim(-0.5,4)
    ax1.legend(bbox_to_anchor=(0.6, 1), ncol=1, fancybox=True, shadow=True)
    ax1.set_xlabel(r'$r/D$')
    ax1.set_ylabel(r'$\frac{\overline{\bf{u}_x}}{\bf{u}_{bulk}}$')

    ax2.set_xlim(0,1)
    ax2.set_ylim(0,1)
    ax2.legend(bbox_to_anchor=(0.6, 1), ncol=1, fancybox=True, shadow=True)
    ax2.set_xlabel(r'$r/D$')
    ax2.set_ylabel(r'$\frac{rms(\bf{u}_x)}{\bf{u}_{bulk}}$')
    
    fig1.savefig(saveDir+"cut1_new_1d_lR2_profil1a.png",  bbox_inches='tight')
    fig2.savefig(saveDir+"cut1_new_1d_lR2_profil1b.png",  bbox_inches='tight')

main()
