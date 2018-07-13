import matplotlib.pyplot as plt
import general_settings as gs
import reference_database as rdb


def main():
    import timeSeriesReader_ReturnOuterVariables as tsR
    import parameters_T_RES1b_MethodSynthetic as ps_syn
    import parameters_T_RES1d_MethodMapped_subMethod_NearestFace as ps_map
#    import copy
    
    fig1,ax1 = plt.subplots()
    fig2,ax2 = plt.subplots()

#   get data    
    l_1b_syn = tsR.pre_check(ps_syn.parameters,"Dai_lines_typeFace_cell-1")
    db_1b_syn = tsR.process(ps_syn.parameters,validDataList=l_1b_syn,colonNb=1)

    l_1d_map = tsR.pre_check(ps_map.parameters,"Dai_lines_typeFace_cell-1")
    db_1d_map = tsR.process(ps_map.parameters,validDataList=l_1d_map,colonNb=1)  

#   No-dimnesionize and plot
    Ux_1p5M_syn=0.25
    Ux_bulk_Dai=0.3

    ax1.plot(db_1b_syn['rByD'],db_1b_syn['mean']/Ux_1p5M_syn,label='synthetic',linewidth=2)
    ax1.plot(db_1d_map['rByD'],db_1d_map['mean']/Ux_bulk_Dai,label='mapped',linewidth=2)

    ax2.plot(db_1b_syn['rByD'],db_1b_syn['std']/Ux_1p5M_syn,label='synthetic',linewidth=2)  
    ax2.plot(db_1d_map['rByD'],db_1d_map['std']/Ux_bulk_Dai,label='mapped',linewidth=2)
    
#   reference plot       
    x1,y1 = rdb.Dai_thesis.Fig4p8a('EAU')
    ax1.plot(x1+0.5, y1, label='Dai', marker='s', markerfacecolor='none', linewidth=2)
    x2,y2 = rdb.Dai_thesis.Fig4p11a('EAU')
    ax2.plot(x2+0.5, y2, label='Dai', marker='s', markerfacecolor='none', linewidth=2)

#   plot settings    
    ax1.set_xlim(0,1)
    ax1.legend(bbox_to_anchor=(0.6, 0.4), ncol=1, fancybox=True, shadow=True)
    ax1.set_xlabel(r'$r/D$',fontsize=gs.sizeLabel)
    ax1.set_ylabel(r'$<U_x>$',fontsize=gs.sizeLabel)
    ax1.set_title('time stat. @'+r'$-D$'+' cut')

    ax2.set_xlim(0,1)
    ax2.legend(bbox_to_anchor=(0.8, 1), ncol=1, fancybox=True, shadow=True)
    ax2.set_xlabel(r'$r/D$',fontsize=gs.sizeLabel)
    ax2.set_ylabel(r'${U_x}_{rms}$',fontsize=gs.sizeLabel)

main()