import matplotlib.pyplot as plt
import general_settings as gs
import reference_database as rdb


def main():
    import timeSeriesReader_ReturnOuterVariables as tsR
#    import parameters_T_RES1b_MethodSynthetic as ps_syn
    import parameters_T_RES1d_MethodMapped_subMethod_NearestFace as ps_map
#    import copy
    
    fig1,ax1 = plt.subplots()
    fig2,ax2 = plt.subplots()

#   get data    
#    l_1b_syn = tsR.pre_check(ps_syn.parameters,"Dai_lines_typeFace_cell-2")
#    db_1b_syn = tsR.process(ps_syn.parameters,validDataList=l_1b_syn,colonNb=1)

    l_1d_map2 = tsR.pre_check(ps_map.parameters,"Dai_lines_typeFace_cell-2")
    db_1d_map2 = tsR.process(ps_map.parameters,validDataList=l_1d_map2,colonNb=1)

    ps_map.parameters['sampling']['dataShape']=(195,4)
    l_1d_map2a3 = tsR.pre_check(ps_map.parameters,"Dai_lines_typeFace_cell-2a3")
    db_1d_map2a3 = tsR.process(ps_map.parameters,validDataList=l_1d_map2a3,colonNb=1)
    
    ps_map.parameters['sampling']['dataShape']=(192,4)
    l_1d_map2b3 = tsR.pre_check(ps_map.parameters,"Dai_lines_typeFace_cell-2b3")
    db_1d_map2b3 = tsR.process(ps_map.parameters,validDataList=l_1d_map2b3,colonNb=1)

    ps_map.parameters['sampling']['dataShape']=(190,4)
    l_1d_map2c3 = tsR.pre_check(ps_map.parameters,"Dai_lines_typeFace_cell-2c3")
    db_1d_map2c3 = tsR.process(ps_map.parameters,validDataList=l_1d_map2c3,colonNb=1)

    ps_map.parameters['sampling']['dataShape']=(190,4)
    l_1d_map2d3 = tsR.pre_check(ps_map.parameters,"Dai_lines_typeFace_cell-2d3")
    db_1d_map2d3 = tsR.process(ps_map.parameters,validDataList=l_1d_map2d3,colonNb=1)

    ps_map.parameters['sampling']['dataShape']=(188,4)
    l_1d_map2e3 = tsR.pre_check(ps_map.parameters,"Dai_lines_typeFace_cell-2e3")
    db_1d_map2e3 = tsR.process(ps_map.parameters,validDataList=l_1d_map2e3,colonNb=1)
    
    ps_map.parameters['sampling']['dataShape']=(188,4)    
    l_1d_map3 = tsR.pre_check(ps_map.parameters,"Dai_lines_typeFace_cell-3")
    db_1d_map3 = tsR.process(ps_map.parameters,validDataList=l_1d_map3,colonNb=1)

#   No-dimnesionize and plot
#    Ux_1p5M_syn=0.25
    Ux_bulk_Dai=0.3
 
#    ax1.plot(db_1b_syn['rByD'],db_1b_syn['mean']/Ux_1p5M_syn,label='synthetic',linewidth=2)
    ax1.plot(db_1d_map2['rByD'],db_1d_map2['mean']/Ux_bulk_Dai,label='mapped-2',linewidth=2)
    ax1.plot(db_1d_map2a3['rByD'],db_1d_map2a3['mean']/Ux_bulk_Dai,label='mapped-a',linewidth=2)
    ax1.plot(db_1d_map2b3['rByD'],db_1d_map2b3['mean']/Ux_bulk_Dai,label='mapped-b',linewidth=2)
    ax1.plot(db_1d_map2c3['rByD'],db_1d_map2c3['mean']/Ux_bulk_Dai,label='mapped-c',linewidth=2)
    ax1.plot(db_1d_map2d3['rByD'],db_1d_map2d3['mean']/Ux_bulk_Dai,label='mapped-d',linewidth=2)
    ax1.plot(db_1d_map2e3['rByD'],db_1d_map2e3['mean']/Ux_bulk_Dai,label='mapped-e',linewidth=2)
    ax1.plot(db_1d_map3['rByD'],db_1d_map3['mean']/Ux_bulk_Dai,label='mapped-3',linewidth=2)

#    ax2.plot(db_1b_syn['rByD'],db_1b_syn['std']/Ux_1p5M_syn,label='synthetic',linewidth=2)  
    ax2.plot(db_1d_map2['rByD'],db_1d_map2['std']/Ux_bulk_Dai,label='mapped-2',linewidth=2)
    ax2.plot(db_1d_map2a3['rByD'],db_1d_map2a3['std']/Ux_bulk_Dai,label='mapped-a',linewidth=2)
    ax2.plot(db_1d_map2b3['rByD'],db_1d_map2b3['std']/Ux_bulk_Dai,label='mapped-b',linewidth=2)
    ax2.plot(db_1d_map2c3['rByD'],db_1d_map2c3['std']/Ux_bulk_Dai,label='mapped-c',linewidth=2)
    ax2.plot(db_1d_map2d3['rByD'],db_1d_map2d3['std']/Ux_bulk_Dai,label='mapped-d',linewidth=2)
    ax2.plot(db_1d_map2e3['rByD'],db_1d_map2e3['std']/Ux_bulk_Dai,label='mapped-e',linewidth=2)
    ax2.plot(db_1d_map3['rByD'],db_1d_map3['std']/Ux_bulk_Dai,label='mapped-3',linewidth=2)

#   reference plot     
    x1,y1 = rdb.Dai_thesis.Fig4p9a('EAU')
    ax1.plot(-x1+0.5, y1, label='Dai-2', marker='s', markerfacecolor='none', linewidth=2)
    x3,y3 = rdb.Dai_thesis.Fig4p10a('EAU')
    ax1.plot(-x3+0.5, y3, label='Dai-3', marker='s', markerfacecolor='none', linewidth=2)
    x2,y2 = rdb.Dai_thesis.Fig4p12a('EAU')
    ax2.plot(x2+0.5, y2, label='Dai-2', marker='s', markerfacecolor='none', linewidth=2)
    x4,y4 = rdb.Dai_thesis.Fig4p13a('EAU')
    ax2.plot(x4+0.5, y4, label='Dai-3', marker='s', markerfacecolor='none', linewidth=2)
    
#   plot settings    
    ax1.set_xlim(0,1)
    ax1.legend(bbox_to_anchor=(1.4, 1), ncol=1, fancybox=True, shadow=True)
    ax1.set_xlabel(r'$r/D$',fontsize=gs.sizeLabel)
    ax1.set_ylabel(r'$<U_x>$',fontsize=gs.sizeLabel)
    ax1.set_title('time stat. @'+r'$+D,1.5D,2D,2.5D,3D,3.5D,3.625D$'+' cut')

    ax2.set_xlim(0,1)
    ax2.legend(bbox_to_anchor=(1.4, 1), ncol=1, fancybox=True, shadow=True)
    ax2.set_xlabel(r'$r/D$',fontsize=gs.sizeLabel)
    ax2.set_ylabel(r'${U_x}_{rms}$',fontsize=gs.sizeLabel)

main()